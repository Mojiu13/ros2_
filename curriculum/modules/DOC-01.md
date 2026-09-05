# DOC-01｜软件设计、架构与测试文档

> Phase 3 · P0 · 工作量 M

## 为什么学习

整理真实发生的需求、设计、测试和故障证据，不在项目尾声虚构前置决策。

## Prerequisites

TEST-01

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定宿主安装 ROS。

## 开始时检查

APP-01A 原始需求/接口、TEST-01 追踪矩阵和 Project A/B 真实产物存在。

## 核心实践任务

整理而非重写 REQUIREMENTS；补软件设计、节点/接口架构、Docker 环境、执行时序、配置、调试指南、TEST_PLAN/REPORT 与变更记录；检查需求→设计→测试链接。

## 最小理论

可追踪性、受众、设计决策记录、证据与结论分离、文档漂移。

## 故障注入

文档与接口/Compose/命令不一致、把未实现功能写成成果、测试报告只报成功。

## 输出文件 / Deliverables

Project A/B README、SOFTWARE_DESIGN、架构图、调试指南、测试文档与证据索引。

## Exit Criteria

陌生读者三分钟理解项目；按 Docker README 可复现；需求→设计→测试可追踪且无虚构。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。临时 container 修改未回写环境定义时也不得完成。

## 模块面试范围

如何证明设计取舍；文档如何防漂移；测试报告如何基于证据。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、本文件、prerequisite 报告、Docker 架构/环境记录以及相关项目文档；不得依赖其他聊天记忆。
