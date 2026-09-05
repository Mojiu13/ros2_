# Docker 环境目录（由 ENV-01 实作）

本目录当前只声明边界，不预先生成未经本机验证的 Dockerfile/Compose。

ENV-01 将根据当时官方 Jazzy/Gazebo/MoveIt/Docker 文档和本机 CPU、桌面会话、GPU 类型创建并验证：`Dockerfile`、`compose.yaml`、`entrypoint.sh`。

验收必须包括源码 bind mount、underlay/overlay、GUI、GPU renderer、ROS discovery、依赖回写和删除 container 后重建。Native Fallback 必须有实际限制、理由和差异记录。
