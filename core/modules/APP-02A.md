# APP-02A｜Cancel、Timeout 与明确错误传播

> CORE TO APPLY · 工作量 M

## Core Skill

让 TaskNode 在失败路径上也能正确结束，这是 Action 应用最低可靠性。

## Prerequisites

APP-01B

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- cancel acceptance/rejection、cancel 与 stop 的边界，以及客户端中断后的服务端责任。
- timeout 与 deadline 的最低语义；所有路径最终进入唯一 terminal state。
- invalid input、planning failure、execution failure、downstream unavailable 的错误保真传播。
- 本模块只保证正确失败，不自动引入 retry、replan 或 recovery policy。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

实现 cancel acceptance/rejection、timeout、invalid input、planning failure、execution failure、controller/action unavailable 和明确 final result；处理 client interruption。

## Minimum Theory

讲到 cancel/timeout/deadline/terminal state 正确闭环；retry、replan、recovery budget 与高级恢复策略进入 DLC。

## Fault / Debug

分别选择 cancel、timeout 和下游不可用做代表验证。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

Project B v1.1、错误矩阵、取消/超时时序与运行证据。

另须创建或更新 `docs/modules/APP-02A/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

每个任务唯一终态；不无限等待；错误来源可判断；无 retry/recovery 依赖。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/APP-02A/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-APP-RECOVERY`：自动重试、重规划和有限恢复策略。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

cancel、timeout、下游错误传播和终态；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/APP-02A/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
