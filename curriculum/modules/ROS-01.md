# ROS-01｜ROS 2 计算图、CLI、通信选择与容器网络

> Phase 0 · P0 · 工作量 M

## 为什么学习

在容器化环境中建立可观察 ROS 计算图，并理解网络命名空间如何影响 DDS discovery，而不提前深入 DDS 协议。

## Prerequisites

ENV-01

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

读取 ENV-01 重建报告、Compose 网络配置与 ROS_DOMAIN_ID；确认 container 内基础节点可运行。

## 核心实践任务

观察 node/topic/service/action；完成最小通信和接口选择。理解 container network namespace、localhost 边界、ROS_DOMAIN_ID 与 DDS discovery 会受网络影响；如有助于理解，可临时启动第二个 container 或 tool container 做一次最小发现演示，但不把多容器网络实验作为核心验收，也不深入 Docker networking。

## 最小理论

节点与 topic/service/action；bridge/host network、localhost 作用域、DDS discovery 和 ROS_DOMAIN_ID 的最低限度。

## 故障注入

以 ROS graph/interface 错误为主要故障；网络部分只观察一个最小 discovery/ROS_DOMAIN_ID 现象，不展开 bridge/host network 故障矩阵。

## 输出文件 / Deliverables

通信地图、接口选择表、CLI 观察记录；可选的最小 discovery 笔记。

## Exit Criteria

能选择 topic/service/action；能用 CLI 找到接口两端；知道 localhost、ROS_DOMAIN_ID 和容器网络可能影响 discovery，但无需完成深入多容器网络实验。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

topic/service/action 边界；localhost 在两个 container 中是否相同；ROS_DOMAIN_ID 的作用；发现失败怎么分层。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
