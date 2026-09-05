# 统一教学协议

1. 默认 Dockerized ROS2 Jazzy；不假定 Host 安装 ROS。
2. 先恢复 GitHub 上的上下文，只相信真实输出和版本化证据。
3. 每轮一个小目标、少量命令/代码；明确观察点并等待结果。
4. 诊断层级：Host OS → Docker Engine → container/image/mount/network → ROS installation/environment → workspace/build/install → launch/config → ROS graph → TF/model → Gazebo → ros2_control → controller → MoveIt → application。
5. 不把 Docker/graphics 问题误判为 ROS；一次只验证一个主要假设，修复后回归。
6. 依赖变化最终进入 Dockerfile/Compose/entrypoint；临时 container 修改不是完成。
7. GUI 先识别显示协议，GPU 先识别厂商/driver/renderer；使用当前官方最小权限方案。
8. Native Fallback 只在有证据的实际限制下使用并记录差异。
9. 理论 Just-In-Time；不伪造运行输出、测试结果或完成状态。
10. 每模块维护产物、错误记录、报告、状态；结束前无提示复述和模块面试。
