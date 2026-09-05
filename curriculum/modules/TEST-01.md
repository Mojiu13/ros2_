# TEST-01｜需求可追踪的功能、异常与 ROS 集成测试

> Phase 3 · P0 · 工作量 L

## 为什么学习

把 APP-01A 的需求变成可追踪测试，满足功能测试和测试报告岗位职责。

## Prerequisites

APP-02A

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定宿主安装 ROS。

## 开始时检查

REQUIREMENTS、TaskNode v1、APP-02A 错误语义存在；冻结被测版本和 Docker image 标识。

## 核心实践任务

为每个 FR/NFR 建 Requirement→Test Case 矩阵，例如 FR-01→TC-01；覆盖正常、边界、非法、cancel、timeout、planning/execution/controller/action failure、回归；Python pytest、C++ gtest 与基础 ROS launch/integration test；记录 expected/actual/result。

## 最小理论

需求追踪、测试层级、oracle、fixture、超时、隔离、回归。

## 故障注入

测试竞态、资源未清理、container 状态泄漏、假阳性、依赖版本漂移。

## 输出文件 / Deliverables

TEST_PLAN、traceability matrix、自动化测试、TEST_REPORT、缺陷列表。

## Exit Criteria

所有 P0 requirement 至少一个测试；关键 FR 有正反例；环境可重建、测试可重复；失败可定位且报告真实。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。临时 container 修改未回写环境定义时也不得完成。

## 模块面试范围

Requirement→Test Case；单元/集成；如何测 cancel/timeout；expected/actual。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、本文件、prerequisite 报告、Docker 架构/环境记录以及相关项目文档；不得依赖其他聊天记忆。
