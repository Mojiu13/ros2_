# APP-02A｜Cancel、Timeout 与错误传播

> Phase 3 · P0 · 工作量 L

## 为什么学习

Fast Track 的 TaskNode 必须能正确结束失败任务，而不是只处理成功路径。

## Prerequisites

APP-01B

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定宿主安装 ROS。

## 开始时检查

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

除非证据、复述和模块面试全部完成，否则不得标记 Completed。临时 container 修改未回写环境定义时也不得完成。

## 模块面试范围

cancel acceptance/rejection；timeout 放哪层；client interruption；错误如何逐层保真。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、本文件、prerequisite 报告、Docker 架构/环境记录以及相关项目文档；不得依赖其他聊天记忆。
