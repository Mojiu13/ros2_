# APP-02A｜Cancel、Timeout 与错误传播

> Phase 3 · P0 · 工作量 L

## 为什么学习

Fast Track 的 TaskNode 必须能正确结束失败任务，而不是只处理成功路径。

## Prerequisites

APP-01B

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

APP-01B v1 和需求追踪存在；明确每个等待阶段的边界和最终 result。

## 核心实践任务

实现 cancel request 与 acceptance/rejection；planning/execution timeout；client interruption；planning failure、execution failure、controller unavailable、action server unavailable 的错误传播；统一 final result，确保资源清理和状态终止。本模块不做 retry/replan。

## 最小理论

取消语义、deadline/timeout、错误传播、terminal state、cancel 与停止的边界。

## 故障注入

在 VALIDATING/PLANNING/EXECUTING 分别取消；让下游 server/controller 消失；制造 planning/execution timeout 和客户端断开。

## 输出文件 / Deliverables

Project B v1.1、cancel/timeout 时序图、错误码矩阵、故障证据、需求追踪更新。

## Exit Criteria

每个测试任务都有唯一 terminal state；cancel 接受/拒绝合理；timeout 不无限等待；下游错误不被误报为通用失败。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

cancel acceptance/rejection；timeout 放哪层；client interruption；错误如何逐层保真。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
