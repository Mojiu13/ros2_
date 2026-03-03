import time

import rclpy
from rclpy.node import Node

from moveit.planning import MoveItPy
from moveit.core.robot_state import RobotState


class PandaMoveItPyDemo(Node):
    def __init__(self):
        super().__init__("panda_moveitpy_demo")

        # Connect to MoveIt (move_group etc.)
        self.moveit = MoveItPy(node_name="moveitpy_client")
        self.arm = self.moveit.get_planning_component("panda_arm")

    def run_once(self):
        # 让 state monitor 稍微热身，避免刚启动时拿不到 joint_states
        time.sleep(0.5)

        # start state = current
        self.arm.set_start_state_to_current_state()

        # 取当前 RobotState，并基于它做一个很小的关节偏移
        model = self.moveit.get_robot_model()
        goal_state = RobotState(model)
        goal_state.update()

        # 关节名通常是 panda_joint1..7
        jname = "panda_joint1"
        try:
            v = goal_state.get_variable_position(jname)
            goal_state.set_variable_position(jname, v + 0.3)
        except Exception as e:
            self.get_logger().error(f"Cannot access {jname}: {e}")
            self.get_logger().error("If joint name differs, run introspection snippet to print joint names.")
            raise

        # set goal + plan
        self.arm.set_goal_state(robot_state=goal_state)

        self.get_logger().info("Planning (MoveItPy)...")
        plan_result = self.arm.plan()
        if not plan_result:
            raise RuntimeError("Planning failed")

        self.get_logger().info("Executing...")
        self.moveit.execute(plan_result.trajectory, controllers=[])

        self.get_logger().info("Done ✅")


def main(args=None):
    rclpy.init(args=args)
    node = PandaMoveItPyDemo()
    try:
        node.run_once()
    except Exception as e:
        node.get_logger().error(str(e))
    finally:
        node.destroy_node()
        rclpy.shutdown()
