#!/usr/bin/env python3
import rclpy
from rclpy.logging import get_logger

from moveit.planning import MoveItPy


def main():
    rclpy.init()
    logger = get_logger("moveitpy_closed_loop")

    # 1) MoveItPy 实例（内部就是 moveit_cpp + state_monitor）
    robot = MoveItPy(node_name="moveitpy_closed_loop")

    # 2) 取 planning group（你刚确认是 panda_arm）
    arm = robot.get_planning_component("panda_arm")

    # 3) 起点 / 终点：用 SRDF 里的命名姿态（不引入 IK / FK）
    arm.set_start_state(configuration_name="ready")
    arm.set_goal_state(configuration_name="extended")

    logger.info("Planning panda_arm: ready -> extended")
    plan_result = arm.plan()
    if not plan_result:
        logger.error("Planning failed")
        rclpy.shutdown()
        return

    # 4) 关键连接点：execute()
    # 这一行 === Action Client → /panda_arm_controller/follow_joint_trajectory
    logger.info("Executing trajectory via MoveItPy")
    robot.execute(plan_result.trajectory, controllers=[])

    # 5) 给执行一点时间（execute 是异步的）
    executor = rclpy.executors.SingleThreadedExecutor()
    executor.add_node(robot._node)
    for _ in range(200):
        executor.spin_once(timeout_sec=0.05)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
