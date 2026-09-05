# TEST-01｜需求可追踪的功能、异常与 ROS 集成测试

> Phase 3 · P0 · 工作量 L

## 为什么学习

把 APP-01A 的需求变成可追踪测试，满足功能测试和测试报告岗位职责。

## Prerequisites

APP-02A

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。

如果本模块新增依赖，必须更新版本化环境定义、重建 image/container、验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。

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

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

Requirement→Test Case；单元/集成；如何测 cancel/timeout；expected/actual。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
