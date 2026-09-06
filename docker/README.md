# ros2-dev

ENV-01 一次搭建完整 Jazzy 机械臂开发 image；后续 Docker 退居后台。包含 RViz2、Gazebo Sim/ros_gz、ros2_control/ros2_controllers、Gazebo control integration、MoveIt2、colcon/rosdep 与 C++/Python 工具。

默认单一 non-root development container，宿主源码 bind mount。具体包名/版本在 ENV-01 按当前官方文档验证并记录。

高级 Docker/network/device/GPU：`DLC_REF: DLC-ENV-ADV`、`DLC-ROS-NETWORK`、`DLC-SIM-GRAPHICS`。
