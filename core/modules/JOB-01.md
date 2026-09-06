# JOB-01｜投递期项目表达与面试闭环

> CORE AFTER APPLY · 工作量 M

## Core Skill

边投递边把现有真实证据转成简洁表达，并用真实面试反馈回补。

## Prerequisites

DELIVERY-01；Application Gate 已通过并已开始投递

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- 项目表达需对应 requirement、架构、接口、验证、限制和真实证据。
- 30 秒摘要、3 分钟项目介绍、系统链路图与 debugging 故事面向不同追问深度。
- 未知或未实现内容要明确边界；不得用 DLC 术语掩盖主线理解不足。
- 真实面试反馈应映射到现有 CORE 缺口或一个有触发证据的 DLC。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

准备 30 秒和 3 分钟项目介绍；两个项目真实 bullet；白板画完整 ROS 链；整理 5–10 个 CORE 技术问答和 2–3 个真实 debugging 故事；根据真实反馈迭代。

## Minimum Theory

只把已有证据压缩为可信表达，并用反馈回补；大型题库、压力面试课程和高级系统设计进入 DLC。

## Fault / Debug

发现夸大、证据链接缺失或跨层回答混乱并修正。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

PROJECT_PITCH、CORE_QA、DEBUG_STORIES、简历迭代记录。

另须创建或更新 `docs/modules/JOB-01/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

表达与仓库一致；能讲项目、链路和故障；所有未实现内容明确标注。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/JOB-01/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-JOB`：由真实面试反馈触发的大型题库、压力排障与系统设计强化。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

本模块本身就是精简 CORE 面试，只考主线。；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/JOB-01/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
