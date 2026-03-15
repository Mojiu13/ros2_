import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, GoalResponse, CancelResponse

from task_node_mp_a.moveit_client import MoveItClient
from task_node_mp_a_interfaces.action import ExecutePose


# TaskNode 层错误码
# 这一层表示“任务编排层”的状态，不等同于 MoveIt 自己的错误码
TASK_OK = 0
TASK_NOT_READY = 1
TASK_TIMEOUT = 2
TASK_CANCELED = 3
TASK_INTERNAL = 4


class TaskNode(Node):
    """
    TaskNode 是任务级编排节点。

    职责：
    1. 对外暴露 /task/execute_pose Action
    2. 管理 goal / feedback / cancel / result 生命周期
    3. 调用 MoveItClient 完成规划与执行
    4. 将下游结果整理成统一的 Action Result

    不负责：
    - controller 细节
    - 具体规划算法实现
    - 硬件控制细节
    """

    def __init__(self):
        super().__init__('task_node')

        # 下游能力适配层
        self._moveit = MoveItClient(self)

        # Action Server：对外提供 execute_pose 接口
        self._server = ActionServer(
            self,
            ExecutePose,
            'task/execute_pose',
            execute_callback=self.execute_cb,
            goal_callback=self.goal_cb,
            cancel_callback=self.cancel_cb,
        )

        self.get_logger().info('TaskNode ready: /task/execute_pose')

    def goal_cb(self, goal: ExecutePose.Goal):
        """
        Goal 接收阶段的最小校验。

        当前只检查 target_pose 的 frame_id 是否为空。
        更复杂的参数检查后续可以继续扩展。
        """
        if goal.target_pose.header.frame_id.strip() == '':
            self.get_logger().warn(
                'Rejected goal: target_pose.header.frame_id is empty'
            )
            return GoalResponse.REJECT

        return GoalResponse.ACCEPT

    def cancel_cb(self, goal_handle):
        """
        Cancel 请求处理。

        当前 stub 版本：
        - 直接接受 cancel
        - 后续接入真实 MoveIt 时，可以在这里转发 stop/cancel
        """
        self.get_logger().warn('Cancel requested by client')
        return CancelResponse.ACCEPT

    def _make_result(
        self,
        success: bool,
        task_error: int,
        moveit_error: int,
        message: str,
    ):
        """
        统一构造 ExecutePose.Result。

        目的：
        - 避免 execute_cb() 里重复写样板代码
        - 让主流程更清晰
        """
        result = ExecutePose.Result()
        result.success = success
        result.task_error = task_error
        result.moveit_error = moveit_error
        result.message = message
        return result

    async def _finish_canceled(self, goal_handle, msg: str):
        """
        统一处理 canceled 路径。
        """
        result = self._make_result(
            success=False,
            task_error=TASK_CANCELED,
            moveit_error=0,
            message=msg,
        )
        goal_handle.canceled()
        return result

    async def execute_cb(self, goal_handle):
        """
        Action 主执行逻辑。

        流程：
        1. 检查 MoveIt 是否可用
        2. 发布 PLANNING feedback
        3. 调用 MoveItClient.plan_pose()
        4. 发布 EXECUTING feedback
        5. 调用 MoveItClient.execute()
        6. 返回最终结果
        """
        goal = goal_handle.request
        fb = ExecutePose.Feedback()

        # ---------- 0) MoveIt readiness 检查 ----------
        if not self._moveit.is_ready():
            result = self._make_result(
                success=False,
                task_error=TASK_NOT_READY,
                moveit_error=0,
                message='MoveIt is not ready',
            )
            goal_handle.abort()
            return result

        # ---------- 1) PLANNING ----------
        fb.stage = 'PLANNING'
        fb.progress = 0.1
        fb.message = f'Planning for group={goal.group_name}'
        goal_handle.publish_feedback(fb)

        # 在规划前检查 cancel
        if goal_handle.is_cancel_requested:
            return await self._finish_canceled(
                goal_handle,
                'Canceled before planning',
            )

        # 调用下游能力层：Pose 规划
        plan_ok, moveit_error, plan_msg, plan_result = self._moveit.plan_pose(
            goal.group_name,
            goal.target_pose,
            goal.planning_time,
            goal.vel_scale,
            goal.acc_scale,
        )

        # 规划失败
        if not plan_ok:
            result = self._make_result(
                success=False,
                task_error=TASK_INTERNAL,
                moveit_error=moveit_error,
                message=plan_msg,
            )
            goal_handle.abort()
            return result

        # ---------- 2) EXECUTING ----------
        fb.stage = 'EXECUTING'
        fb.progress = 0.6
        fb.message = 'Executing trajectory'
        goal_handle.publish_feedback(fb)

        # 在执行前检查 cancel
        if goal_handle.is_cancel_requested:
            return await self._finish_canceled(
                goal_handle,
                'Canceled before execution',
            )

        exec_ok, moveit_error, exec_msg = self._moveit.execute(plan_result)

        # 执行失败
        if not exec_ok:
            result = self._make_result(
                success=False,
                task_error=TASK_INTERNAL,
                moveit_error=moveit_error,
                message=exec_msg,
            )
            goal_handle.abort()
            return result

        # ---------- 3) DONE ----------
        result = self._make_result(
            success=True,
            task_error=TASK_OK,
            moveit_error=0,
            message='OK',
        )
        goal_handle.succeed()
        return result


def main():
    """
    ROS2 节点入口。
    """
    rclpy.init()
    node = TaskNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()