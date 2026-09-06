# APP-01A｜最小需求、Task.action 与 Server 骨架

> CORE TO APPLY · 工作量 M

## 为什么在 CORE

用小规模需求证明会先定义问题再编码。

## Prerequisites

INT-01

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

写 5–10 个 FR、2–4 个 NFR 和 acceptance criteria；设计 Task.action goal/feedback/result/error；实现 C++ Action Server skeleton 和 Python client；验证输入拒绝、feedback/result 与 cancel 骨架。

## 最小理论

functional/non-functional requirement、acceptance criteria 和接口契约的最小用法。

## 故障注入

非法输入、server 不可用或含糊错误码中的一个案例。

## Deliverables

简短 REQUIREMENTS、INTERFACE_DESIGN、Task.action、C++ skeleton、Python client。

## Exit Criteria

规模受控；需求可测试；接口生命周期正确；不建立企业级需求体系。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-DOC；DLC_REF: DLC-TEST

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

为何先定义需求、Action 字段和输入校验。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
