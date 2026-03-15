import time


class MoveItClient:
    """
    MoveItClient 是 TaskNode 的下游能力适配层。

    职责：
    - 封装 MoveIt 的规划调用
    - 封装 MoveIt 的执行调用
    - 隔离 TaskNode 与 MoveIt 的直接依赖
    """

    def __init__(self, node):
        self._node = node

    def is_ready(self) -> bool:
        """
        检查 MoveIt 是否可用。

        真实实现可能检查：
        - move_group action server
        - planning scene
        - controller
        """
        return True

    def plan_pose(self, group_name, target_pose, planning_time, vel_scale, acc_scale):
        """
        Pose 目标规划。

        输入：
        - group_name
        - target_pose

        返回：
        plan_ok
        moveit_error
        message
        plan_result
        """

        self._node.get_logger().info(
            f'[MoveItClient] plan_pose() called: group={group_name}, frame={target_pose.header.frame_id}'
        )

        # 模拟规划耗时
        time.sleep(0.25)

        if group_name.strip() == '':
            self._node.get_logger().error(
                '[MoveItClient] empty group_name -> plan fail'
            )
            return False, 100, 'Plan failed: empty group_name', None

        return True, 0, 'Plan OK (stub)', {'trajectory': 'fake'}

    def execute(self, plan_result):
        """
        执行规划结果。

        输入：
        plan_result

        返回：
        exec_ok
        moveit_error
        message
        """

        self._node.get_logger().info('[MoveItClient] execute() called')

        time.sleep(0.5)

        if plan_result is None:
            return False, 200, 'Execute failed: empty plan_result'

        return True, 0, 'Execute OK (stub)'