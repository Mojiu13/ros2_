# TEST-01｜功能、边界、异常与 ROS 集成测试

> Phase 3 · P0 · 工作量 L

## 为什么学习

岗位要求软件功能测试与优化，测试必须是独立工程能力。

## Prerequisites

APP-01

## 环境要求

TaskNode v1 与可重复仿真

## 开始时检查

冻结需求和可测接口；确认正常基线。

## 核心实践任务

设计正常/边界/异常/failure injection/regression；Python 用 pytest，C++ 用 gtest；加入基础 launch/integration test；记录 expected/actual/result。

## 最小理论

测试层级、可重复性、oracle、fixture、回归与覆盖边界。

## 故障注入

测试超时、资源未清理、依赖启动竞态、假阳性。

## 输出文件 / Deliverables

TEST_PLAN；测试用例；自动化测试；TEST_REPORT；缺陷列表。

## Exit Criteria

核心需求均有正反测试；测试可重复；失败能定位到层；报告不伪造结果。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

单元与集成测试边界；如何测试 timeout/cancel；expected 与 actual 怎么记录。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
