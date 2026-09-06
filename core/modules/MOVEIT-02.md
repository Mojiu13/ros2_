# MOVEIT-02｜A2 C++ / Python 编程规划执行

> CORE TO APPLY · 工作量 L

## Core Skill

把 GUI 成功转换为能形成项目证据的应用代码。

## Prerequisites

MOVEIT-01

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- MoveIt 编程接口中的 start state、goal constraints、plan result、RobotTrajectory 与 execute result。
- pose target 的 frame、current state 时效、joint limits 与空轨迹检查。
- C++ 主节点与 Python client/tool 的职责边界，以及错误如何保真返回。
- 程序必须分别记录 planning 与 execution 的结果、耗时和证据。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

C++ 实现 named/joint/pose 的 plan→inspect→execute；Python 作为 client/tool；记录成功/失败、耗时和错误层；检查 start state、frame、joint limits 与空轨迹。

## Minimum Theory

只讲 API 调用、结果检查、frame/current state/trajectory 错误处理；不进入 MoveIt 源码或规划器内部。

## Fault / Debug

current state 超时、frame_id、unreachable、空轨迹或 execution server 缺失中的代表案例。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

C++ 规划节点、Python tool/client、运行证据和错误记录。

另须创建或更新 `docs/modules/MOVEIT-02/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

至少两类目标稳定，第三类有明确失败语义；规划/执行不混淆。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/MOVEIT-02/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-MOVEIT`：复杂应用 API 与轨迹检查；`DLC-MOVEIT-INTERNALS`：规划器与执行内部。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

编程 plan/execute、start/goal、返回值和 C++/Python 分工；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/MOVEIT-02/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
