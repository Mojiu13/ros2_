from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    panda_share = get_package_share_directory("moveit_resources_panda_moveit_config")
    demo_launch = os.path.join(panda_share, "launch", "demo.launch.py")

    # 关键：生成完整 moveit_config（包含 robot_description / robot_description_semantic / pipelines 等）
    moveit_config = (
        MoveItConfigsBuilder(robot_name="panda",
                             package_name="moveit_resources_panda_moveit_config")
        .to_moveit_configs()
    )

    return LaunchDescription([
        # 启动官方 demo（RViz + move_group + controllers）
        IncludeLaunchDescription(PythonLaunchDescriptionSource(demo_launch)),

        # 启动你的 MoveItPy 节点，并注入完整参数
        Node(
            package="my_py_pkg",
            executable="moveitpy_closed_loop",
            name="moveitpy_closed_loop",
            output="screen",
            parameters=[moveit_config.to_dict()],
        ),
    ])
