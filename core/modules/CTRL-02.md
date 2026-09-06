# CTRL-02｜Direct FollowJointTrajectory 与 A2 控制基线

> CORE TO APPLY · 工作量 L

## Core Skill

先用 A1 理解轨迹契约，再在成熟 A2 上证明 MoveIt 之前的控制链独立正常。

## Prerequisites

CTRL-01

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- `trajectory_msgs/JointTrajectory` 的 joint order、positions 与严格递增 `time_from_start`。
- `FollowJointTrajectory` 的 goal / feedback / result 与 action server 可用性。
- 直接调用 controller 能把 MoveIt 排除在外，从而建立独立控制基线。
- 闭环中命令下发与 joint state 反馈需分别验证，看到 goal accepted 不等于真实运动成功。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

Stage A：A1 上直接发送安全 JointTrajectory，观察 joint_names、time_from_start、feedback/result。Stage B：在 SYS-01 的成熟 6/7 DOF A2 上读取现成 config，验证 simulated hardware、joint_state_broadcaster、joint_trajectory_controller、FollowJointTrajectory、joint order，并绕过 MoveIt 直接运动。

## Minimum Theory

讲清轨迹契约和 action 生命周期；不读 JTC 源码，不研究实时调度或高级 tolerances。

## Fault / Debug

joint mismatch、时间不递增、controller inactive 或 action missing 中一到两个代表案例。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

A1 direct 示例、A2 controller baseline、反馈证据和故障记录。

另须创建或更新 `docs/modules/CTRL-02/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

A1 原理能解释；A2 明确证明 simulated robot→ros2_control→JTC→FJT→motion 正常，方可进入 MoveIt。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/CTRL-02/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-CONTROL`：高级 trajectory/controller 工程；`DLC-CONTROL-LOWLEVEL`：JTC 源码与实时内部。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

FJT、time_from_start、为何 MoveIt 前先验证 controller。；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/CTRL-02/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
