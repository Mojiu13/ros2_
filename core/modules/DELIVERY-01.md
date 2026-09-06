# DELIVERY-01｜最低测试、文档与项目交付

> CORE TO APPLY · 工作量 L

## Core Skill

用最少但可信的测试和文档把项目变成可投递证据。

## Prerequisites

DBG-01

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- test case、precondition、input、expected、actual、pass/fail。
- normal、boundary、failure、regression 与 smoke test 的最低用途。
- README 的目标和受众；architecture diagram、interface description、requirement summary、test report、known limitations、reproduction steps。
- 文档结论必须来自真实运行证据，且学习者能解释为何这样组织，不能只让 AI 代写。
- 6–10 个手工/可执行 test cases 与 1–3 个自动化 smoke tests 是 CORE 必交证据。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

设计 6–10 个有意义 case，覆盖正常、非法、unreachable、cancel、timeout、controller/action unavailable、planning/execution failure；只选真正合适的 pytest/gtest/launch_testing 中一种或少量组合实现 1–3 个自动化 smoke test。完成 Project A/B README、简短 requirements、简短 software design、一张 architecture diagram、interface 说明、TEST_REPORT、known limitations/debug notes 和 MINIMUM_RESUME_EVIDENCE。

## Minimum Theory

讲到能亲手设计可信 case、少量 smoke tests 和可复现文档；fixture/mocking/full gtest/pytest/launch_testing/CI/test architecture 与企业文档体系进入 DLC。

## Fault / Debug

一个测试假阳性、环境未清理或 README 复现失败案例。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

6–10 cases、1–3 automated smoke tests、TEST_REPORT、最小文档包、两个项目真实简历 bullet。

另须创建或更新 `docs/modules/DELIVERY-01/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

陌生人能按 README 复现；测试结果真实；两个项目均有最低证据；Application Gate checklist 全部满足。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/DELIVERY-01/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-TEST`：fixture、mocking、完整框架、CI 与测试架构；`DLC-DOC`：企业文档体系；`DLC-JOB`：求职强化。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

测试为何可信、文档如何复现、已知限制和真实项目证据。；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/DELIVERY-01/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
