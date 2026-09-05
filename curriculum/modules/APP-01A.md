# APP-01A｜任务需求、接口设计与 Action Server 骨架

> Phase 3 · P0 · 工作量 M

## 为什么学习

需求分析必须在编码前发生；先定义应用场景、可验收行为和接口契约，再写 TaskNode。

## Prerequisites

INT-01

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定宿主安装 ROS。

## 开始时检查

Project A2/INT-01 稳定；选择一个具体但不过大的任务场景；检查已有项目证据。

## 核心实践任务

编写 REQUIREMENTS.md：FR-01...、NFR-01... 与 acceptance criteria；至少覆盖 named target、joint target、feedback、明确 result、非法目标拒绝、planning/execution 分离、有限等待、可诊断日志、配置分离。设计 INTERFACE_DESIGN 和 Task.action 的 goal/feedback/result/error 字段；实现 C++ Action Server skeleton 与 Python client，只验证接口生命周期和输入校验，不接入 MoveIt。

## 最小理论

functional/non-functional requirement、acceptance criteria、接口契约、action goal/feedback/result、输入校验、需求可测试性。

## 故障注入

非法 goal、缺字段/歧义错误码、client 中断、server 不可用；验证骨架能确定结束。

## 输出文件 / Deliverables

REQUIREMENTS.md、INTERFACE_DESIGN.md、Task.action、C++ Action Server Skeleton、Python Client。

## Exit Criteria

需求编号稳定且可测试；接口字段可追踪到需求；非法输入不进入执行；server/client 在 Docker 中可构建运行。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。临时 container 修改未回写环境定义时也不得完成。

## 模块面试范围

为什么需求在编码前；FR/NFR；acceptance criteria；为什么选 action；错误语义如何设计。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、本文件、prerequisite 报告、Docker 架构/环境记录以及相关项目文档；不得依赖其他聊天记忆。
