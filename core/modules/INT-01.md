# INT-01｜6/7 DOF 完整系统集成

> CORE TO APPLY · 工作量 M

## Core Skill

从干净启动证明 A2 的模型、仿真、控制、规划和代码形成可重复系统。

## Prerequisites

MOVEIT-02

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- 从干净启动验证依赖顺序、配置加载、接口 readiness 与 state feedback，而不是依赖残留进程。
- 用 node/graph、TF、controller state、action、trajectory、joint state 和日志构成端到端证据链。
- 接口契约跨包保持一致：frame、joint names/order、controller mapping 与 action name。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

启动稳定 ros2-dev；从干净 workspace 运行 A2；执行 named/joint/pose；采集 node/TF/controller/action/trajectory/state feedback 证据；只做集成，不增加新理论。

## Minimum Theory

无新理论；要求把既有必要知识用于端到端取证和接口一致性检查。

## Fault / Debug

随机选择一个已学层的单一故障并用已有方法定位。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

Project A2 v1、系统图 v2、集成验收报告和最小 README。

另须创建或更新 `docs/modules/INT-01/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

6/7 DOF robot→simulated hardware→ros2_control→controller→MoveIt→C++/Python 可从干净启动完整运行。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/INT-01/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

仅真实复杂多层故障触发 `DLC-DEBUG`；不得把 DLC 当作集成 prerequisite。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

完整数据流、Plan/Execute、反馈与分层定位。；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/INT-01/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
