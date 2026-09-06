# 统一教学协议

1. Docker 只在 ENV-01 集中学习并一次构建完整 `ros2-dev` image；不假定 Host 安装 ROS。
2. ENV-01 后默认环境稳定。正常模块只启动 Compose、进入 container、确认 package 可用，随后直接学习 ROS/机器人软件。
3. Just-In-Time 只针对知识：软件可以预装，但 Gazebo、controller、MoveIt、TF、DDS 与规划理论只在对应模块教学。
4. 只有 container 启动、mount/UID/GID、GUI、缺包、污染、版本冲突或项目特定依赖时才回到 Docker。
5. 真实环境变更必须写回 Dockerfile/Compose/entrypoint、重建并更新 ENVIRONMENT_MANIFEST；临时安装不是永久状态。
6. 命令位置可能混淆时标注 `[HOST]` 或 `[CONTAINER]`。
7. 排障仍保留 Host→Docker→ROS environment→workspace→ROS graph→TF/model→Gazebo→ros2_control/controller→MoveIt→application，但故障训练重点在 ROS/机器人软件。
8. 默认一个主 development container，不强制微服务拆分。
9. 每轮一个可验证目标和少量命令/代码，等待真实输出；一次验证一个主要假设，修复后回归。
10. 不伪造输出、测试或完成状态；模块结束前完成文档、复述和面试。
