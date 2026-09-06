# APP-01B｜MoveIt TaskNode 与基本状态机

> CORE TO APPLY · 工作量 L

## Core Skill

形成可展示的机械臂应用层项目，而不是停留在官方 demo。

## Prerequisites

APP-01A

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- 任务层、MoveIt 与 controller 的职责边界；TaskNode 不直接冒充规划器或 controller。
- state machine、state transition、terminal state 与状态/feedback/result 一致性。
- planning failure、execution failure、downstream unavailable 的分层和 error propagation。
- 接口实现必须可追溯到 requirement 与 acceptance criteria。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

接入 MoveIt；支持 named/joint/pose；完成 planning、execution、feedback、result 和 RECEIVED/VALIDATING/PLANNING/EXECUTING/终态的基本状态机；分离 planning/execution error。

## Minimum Theory

讲到基本状态机和分层错误可实现、可验证；复杂状态机架构与自动恢复进入 DLC。

## Fault / Debug

非法目标、规划失败、执行失败或 controller unavailable 中代表案例。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

Project B v1、状态图、执行流和需求实现对照。

另须创建或更新 `docs/modules/APP-01B/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

三类目标可用或有明确失败；反馈/结果/状态一致；不实现复杂 recovery。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/APP-01B/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-APP-RECOVERY`：retry、replan、recovery policy/budget 与高级状态机。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

TaskNode 边界、状态机、错误分层；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/APP-01B/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
