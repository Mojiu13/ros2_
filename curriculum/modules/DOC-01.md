# DOC-01｜软件设计、架构与测试文档

> Phase 3 · P0 · 工作量 M

## 为什么学习

整理真实发生的需求、设计、测试和故障证据，不在项目尾声虚构前置决策。

## Prerequisites

TEST-01

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

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

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

如何证明设计取舍；文档如何防漂移；测试报告如何基于证据。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
