# CTRL-01｜ros2_control 与 Controller 最小闭环

> CORE TO APPLY · 工作量 L

## Core Skill

让模型从可仿真升级为可控制，保留机械臂主线必需的控制接口。

## Prerequisites

SIM-01

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- state interface、command interface、hardware/simulated hardware、controller_manager、controller 与 broadcaster。
- 最低 lifecycle：load → configure → activate；已加载、已配置、已激活不是同一状态。
- 闭环直觉：目标 → controller → command interface → robot/simulation → state interface → joint state。
- joint state feedback 是观察与后续规划当前状态的依据；接口名称和 joint name 必须一致。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

为 A1 接入 ros2_control；配置 state/command interface、controller_manager、joint_state_broadcaster、joint_trajectory_controller；观察最小 lifecycle：load/configure/activate。

## Minimum Theory

讲清接口、组件、最低 lifecycle 与闭环；PID、实时内部、update loop、ResourceManager 和 controller 源码进入 DLC。

## Fault / Debug

controller inactive、interface 或 joint name mismatch 中一个案例。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

A1 ros2_control/config、接口图、controller 状态证据和故障记录。

另须创建或更新 `docs/modules/CTRL-01/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

controllers active；joint states 可观察；能解释 interfaces 和最小 lifecycle。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/CTRL-01/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-CONTROL`：多 controller、切换、容差与调参；`DLC-CONTROL-LOWLEVEL`：实时内部、ResourceManager、源码和自定义接口。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

interfaces、manager、broadcaster、active 状态。；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/CTRL-01/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
