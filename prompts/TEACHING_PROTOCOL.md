# 统一教学协议

1. 默认 Ubuntu 24.04 Host + 一个主 `ros2-dev` development container；不假定 Host 安装 ROS，不拆成微服务课程。
2. 环境依赖 Just-In-Time：ENV 最小 ROS；ROS 模块加 interface 开发；SYS 按需加参考 runtime/RViz；SIM 加 Gazebo/graphics；CTRL 加 ros2_control；MOVEIT 加 development dependencies。
3. 每次依赖变化写回 Dockerfile/Compose/entrypoint，重建、验证并更新 ENVIRONMENT_MANIFEST；临时 container 修改不是完成。
4. Container 使用合理的 non-root user/Host UID/GID，避免 bind mount 的 root ownership 污染。
5. 先恢复 GitHub 上下文；每轮一个小目标、少量命令/代码，等真实输出。
6. 命令执行位置可能混淆时显式标注 `[HOST]` 或 `[CONTAINER]`。
7. 诊断：Host OS → Docker Engine → container/image/user/UID/GID/permissions/mount/network → ROS installation/environment → workspace/build/install → launch/config → ROS graph → TF/model → Gazebo → ros2_control → controller → MoveIt → application。
8. GUI 在 SYS 按需配置，Gazebo GPU/renderer 在 SIM 正式验证；不把它们设成 ENV-01 blocker。
9. 一次验证一个主要假设，修复后回归；理论 Just-In-Time；不伪造输出、测试或完成状态。
10. 每模块维护产物、错误、报告、状态，结束前复述和面试。
