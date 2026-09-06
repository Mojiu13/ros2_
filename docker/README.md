# ros2-dev 开发环境

ENV-01 将一次建立完整、稳定、可重建的机械臂 ROS2 Jazzy image，而不是让 Dockerfile 随每个学习模块频繁演化。

预计包含 ROS2 Jazzy、RViz2、Gazebo Sim/ros_gz、ros2_control/ros2_controllers、Gazebo control integration、MoveIt2、colcon/rosdep/ament、C++/Python ROS 开发工具。实际包名和版本在 ENV-01 按当前官方文档验证。

本目录最终维护 `Dockerfile`、`compose.yaml`、`entrypoint.sh` 和复现说明。默认一个 non-root `ros2-dev` container，宿主源码 bind mount，UID/GID 合理映射。

ENV-01 后只有容器启动、权限、GUI、缺包、污染、版本冲突或项目特定依赖时才重新处理 Docker；正常模块直接启动环境并学习 ROS。
