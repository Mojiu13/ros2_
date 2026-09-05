# APP-02A｜Cancel、Timeout 与错误传播

> Phase 3 · P0 · 工作量 L

## 为什么学习

Fast Track 的 TaskNode 必须能正确结束失败任务，而不是只处理成功路径。

## Prerequisites

APP-01B

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。

如果本模块新增依赖，必须更新版本化环境定义、重建 image/container、验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。

APP-01B v1 和需求追踪存在；明确每个等待阶段的边界和最终 result。## 核心实践任务

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

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

cancel acceptance/rejection；timeout 放哪层；client interruption；错误如何逐层保真。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
