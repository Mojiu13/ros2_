# SIM-01｜MiniArm Gazebo Sim 基础

> CORE TO APPLY · 工作量 M

## Core Skill

让 A1 从可视模型变成稳定可仿真的模型。

## Prerequisites

MODEL-01

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- visual、collision、inertial 的职责；mass 与 inertia 的基本意义，inertial 不是装饰字段。
- damping、friction、gravity 对模型稳定性与运动现象的最低影响。
- RViz 主要显示模型/数据，Gazebo Sim 计算碰撞与物理；因此 RViz 正常而 Gazebo 仍可能掉落、抖动或穿透。
- 通过单变量前后对照解释参数与现象，不推导惯性矩阵。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

加入基础 collision/inertial，spawn 到 Gazebo；让模型稳定；做 2–3 个代表实验：damping、collision、mass/inertial；解释 RViz 与 Gazebo 的区别。

## Minimum Theory

讲到能从物理字段推断掉落/抖动/穿透的常见层级；不推惯性矩阵，不展开高级 physics 或 renderer。

## Fault / Debug

从模型坠落/抖动、collision 或 inertial 错误中选择一个代表案例；真实 graphics 问题只按需处理。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

A1 Gazebo launch/model、2–3 个参数实验和一个故障记录。

另须创建或更新 `docs/modules/SIM-01/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

模型稳定加载；代表参数实验有前后对照；能区分显示与物理问题。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/SIM-01/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-SIM`：world/sensor/physics tuning；真实图形异常触发 `DLC-SIM-GRAPHICS`。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

RViz/Gazebo、collision/inertial、参数如何影响现象。；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/SIM-01/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
