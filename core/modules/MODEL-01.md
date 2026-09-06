# MODEL-01｜MiniArm URDF、Xacro、TF 与 RViz

> CORE TO APPLY · 工作量 L

## Core Skill

用简单 A1 模型亲手理解机器人模型、坐标与最低运动学直觉。

## Prerequisites

SYS-01

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- link、joint、DOF、joint space 与 Cartesian/task space。
- position、orientation、pose；pose 必须连同表达它的 frame 一起理解。
- frame、transform、parent/child、base frame、tool/end-effector frame。
- RPY 与 quaternion 的用途直觉；`PoseStamped` 与 `frame_id` 表达“哪个 frame 下的什么 pose”。
- FK 的工程直觉：给定 joint state，沿父子变换得到末端 pose。
- Xacro 只用于当前模型所需的复用与参数化，不展开宏工程。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

从零创建 2–3 DOF MiniArm；完成 link/joint/origin/axis/limit、基础 Xacro、robot_state_publisher、TF、RViz；通过实验理解 DOF、joint/task space、pose/frame/transform、RPY/quaternion、PoseStamped/frame_id 和 FK 直觉。

## Minimum Theory

讲到能看懂“什么 frame 下表达什么 pose”并解释 FK；rotation matrix/quaternion 推导、齐次变换数学、DH、Jacobian、动力学进入 DLC。

## Fault / Debug

URDF 解析、TF 断链、axis/origin、fixed frame 或 frame_id 错误。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

A1 description 包、显示 launch、TF 图、模型实验和故障记录。

另须创建或更新 `docs/modules/MODEL-01/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

模型可显示和运动；能解释 pose/frame/transform 与关节变化到末端变化。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/MODEL-01/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-MODEL-ENGINEERING`：复杂 mesh/mimic/碰撞与惯性工程；`DLC-ROBOT-MATH`：矩阵、四元数代数、DH、Jacobian、动力学。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

URDF/TF、DOF、joint/task space、pose、FK 直觉；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/MODEL-01/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
