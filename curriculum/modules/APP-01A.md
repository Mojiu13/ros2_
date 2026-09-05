# APP-01A｜任务需求、接口设计与 Action Server 骨架

> Phase 3 · P0 · 工作量 M

## 为什么学习

需求分析必须在编码前发生；先定义应用场景、可验收行为和接口契约，再写 TaskNode。

## Prerequisites

INT-01

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。

如果本模块新增依赖，必须更新版本化环境定义、重建 image/container、验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。

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

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

为什么需求在编码前；FR/NFR；acceptance criteria；为什么选 action；错误语义如何设计。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
