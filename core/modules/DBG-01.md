# DBG-01｜五类高频故障核心包

> CORE TO APPLY · 工作量 M

## Core Skill

用最小案例覆盖第一份机械臂岗位最常见的排错场景。

## Prerequisites

APP-02A

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- 统一排错链：baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression。
- 控制变量；一次只改一个东西；不能凭感觉猜原因。
- CLI、log、ROS graph、TF、controller state、action/result 与 joint state 是证据来源。
- 先区分 environment/build、model/TF、control、planning、execution/application 层，再验证一个主要假设。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

每类至少一个代表案例：① build/source/package/launch；② TF/frame/URDF/joint name；③ controller inactive/action missing；④ MoveIt planning/start state/unreachable；⑤ execution/timeout/application error。每例遵循现象→观察→层级→假设→验证→根因→修复→回归。

## Minimum Theory

掌握可复用的证据驱动方法；race condition、性能 profiling、DDS 深度诊断与复杂复合故障进入 DLC。

## Fault / Debug

本模块即五类代表故障；不制造几十个案例或多层复合故障。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

五个 ERROR_LOG 条目、核心决策树、2–3 个可讲述的 debugging 故事候选。

另须创建或更新 `docs/modules/DBG-01/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

五类各至少一例且证据完整；能区分 planning/execution/controller/model/application。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/DBG-01/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-ENV-ADV`、`DLC-ROS-NETWORK`、`DLC-SIM-GRAPHICS` 仅由对应真实阻塞触发；`DLC-DEBUG` 保存复合故障、race 与性能分析。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

五类排查顺序和真实证据，不考深层内部；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/DBG-01/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
