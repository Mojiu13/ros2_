# APP-01A｜最小需求、Task.action 与 Server 骨架

> CORE TO APPLY · 工作量 M

## Core Skill

用小规模需求证明会先定义问题再编码。

## Prerequisites

INT-01

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- requirement、functional/non-functional requirement、acceptance criteria、validation 与 interface contract。
- Action 的 goal/feedback/result/error 字段必须能支持验收和错误传播。
- server unavailable、invalid input 与执行期失败属于不同边界。
- Git diff 与一次合理 commit 用于把接口决策和证据固定下来。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

写 5–10 个 FR、2–4 个 NFR 和 acceptance criteria；设计 Task.action goal/feedback/result/error；实现 C++ Action Server skeleton 和 Python client；验证输入拒绝、feedback/result 与 cancel 骨架。

## Minimum Theory

讲到需求可验证、接口可实现且错误语义明确；正式需求管理、追踪工具和企业文档流程进入 DLC。

## Fault / Debug

非法输入、server 不可用或含糊错误码中的一个案例。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

简短 REQUIREMENTS、INTERFACE_DESIGN、Task.action、C++ skeleton、Python client。

另须创建或更新 `docs/modules/APP-01A/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

规模受控；需求可测试；接口生命周期正确；不建立企业级需求体系。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/APP-01A/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-DOC`：正式文档/追踪体系；`DLC-TEST`：完整测试架构。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

为何先定义需求、Action 字段和输入校验。；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/APP-01A/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
