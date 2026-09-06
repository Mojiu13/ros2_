# TEST-01｜需求可追踪的功能、异常与 ROS 集成测试

> Phase 3 · P0 · 工作量 L

## 为什么学习

把 APP-01A 的需求变成可追踪测试，满足功能测试和测试报告岗位职责。

## Prerequisites

APP-02A

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

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

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

Requirement→Test Case；单元/集成；如何测 cancel/timeout；expected/actual。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
