# SYS-01｜6/7 DOF 参考机械臂完整链路观察

> Phase 1 · P0 · 工作量 S

## 为什么学习

先在真实复杂度的成熟 6/7 DOF 机械臂上观察完整终点，为 Project A2 建立基线。

## Prerequisites

ROS-03

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

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

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

MoveIt 与 ros2_control 关系；两个 controller manager；6/7 DOF 系统不动时如何先分层。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
