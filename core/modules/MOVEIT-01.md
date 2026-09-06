# MOVEIT-01｜A2 MoveIt2 配置与 RViz Plan/Execute

> CORE TO APPLY · 工作量 L

## Core Skill

在已知控制链正常的 A2 上建立最小规划执行能力。

## Prerequisites

CTRL-02

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- planning group、end effector、start state、goal、joint target 与 pose target。
- FK、IK、IK solution、unreachable、workspace、joint limits 的工程直觉。
- collision 与 PlanningScene 的最低直觉；场景变化为何可能改变或阻止路径。
- planning 产生 trajectory，execution 将 trajectory 交给控制链，两类成功/失败必须分开。
- 奇异性最低工程直觉：某些姿态附近运动能力退化，IK、规划或控制可能更困难；不推 Jacobian。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

读取/修改 SRDF、planning group、end effector、kinematics config、joint limits、controller mapping；在 RViz 完成 named/joint/pose target 的 Plan/Execute；加入一个简单 collision object 并观察路径变化。

## Minimum Theory

讲清 FK/IK、可达性、限制、碰撞、奇异性最低直觉和 Plan/Execute 边界；数学推导、OMPL 与 pipeline 内部进入 DLC。

## Fault / Debug

无 IK/不可达、start state、controller mapping 或 execution failure 中代表案例。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

A2 MoveIt config 审计、三类目标、简单障碍物实验和失败分类。

另须创建或更新 `docs/modules/MOVEIT-01/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

RViz 可规划执行；能区分 IK/规划/执行问题；不要求 OMPL、约束或高级场景研究。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/MOVEIT-01/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-MOVEIT`：复杂 PlanningScene/约束/调参；`DLC-ROBOT-MATH`：运动学数学；`DLC-MOVEIT-INTERNALS`：pipeline、OMPL 与源码。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

SRDF/group/end effector、FK/IK、Plan vs Execute、简单 PlanningScene。；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/MOVEIT-01/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
