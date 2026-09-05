# SYS-01｜6/7 DOF 参考机械臂完整链路观察

> Phase 1 · P0 · 工作量 S

## 为什么学习

先在真实复杂度的成熟 6/7 DOF 机械臂上观察完整终点，为 Project A2 建立基线。

## Prerequisites

ROS-03

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。

如果本模块新增依赖，必须更新版本化环境定义、重建 image/container、验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。

默认使用 ENV-01 的最小 Dockerized Jazzy 环境；不假定 Host 安装 ROS。若参考系统首次需要 RViz/MoveIt runtime，在 SYS-01 按当前官方文档 Just-In-Time 加入、重建并记录版本；这里只加入观察参考系统所需依赖，不提前加入全部 MoveIt development 工具。

## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。

先确认 Docker Engine、目标 image/container、source mount、ROS underlay、workspace overlay、ROS-03 证据。教学时依据 Jazzy 当前维护状态选择 A2 型号；如果第一次正式运行 RViz，在本模块配置并验证必要的 Host→Container GUI 通道。

## 核心实践任务

在 RViz/Gazebo（若参考包支持）完成规划执行；观察节点、TF、joint_states、MoveIt 与 controller action；画规划、执行、反馈链并记录参考模型来源/版本。

## 最小理论

成熟模型、URDF/SRDF、move_group、planning pipeline、MoveIt controller manager、ros2_control controller_manager 与 simulated hardware 的边界。

## 故障注入

隐藏一个 action server 或破坏一个容器网络/显示入口，先归层再恢复。

## 输出文件 / Deliverables

Project A2 参考基线；完整系统地图 v1；版本与支持状态记录。

## Exit Criteria

能讲清 6/7 DOF 规划/执行/反馈；Docker 中可重复启动；知道 Plan/Execute 与两个 manager 的边界。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

MoveIt 与 ros2_control 关系；两个 controller manager；6/7 DOF 系统不动时如何先分层。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
