# DELIVERY-01｜最低测试、文档与项目交付

> CORE TO APPLY · 工作量 L

## 为什么在 CORE

用最少但可信的测试和文档把项目变成可投递证据。

## Prerequisites

DBG-01

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

设计 6–10 个有意义 case，覆盖正常、非法、unreachable、cancel、timeout、controller/action unavailable、planning/execution failure；只选真正合适的 pytest/gtest/launch_testing 中一种或少量组合实现 1–3 个自动化 smoke test。完成 Project A/B README、简短 requirements、简短 software design、一张 architecture diagram、interface 说明、TEST_REPORT、known limitations/debug notes 和 MINIMUM_RESUME_EVIDENCE。

## 最小理论

expected/actual/result、smoke/regression、文档可复现性和诚实边界；不学完整测试工程或企业文档体系。

## 故障注入

一个测试假阳性、环境未清理或 README 复现失败案例。

## Deliverables

6–10 cases、1–3 automated smoke tests、TEST_REPORT、最小文档包、两个项目真实简历 bullet。

## Exit Criteria

陌生人能按 README 复现；测试结果真实；两个项目均有最低证据；Application Gate checklist 全部满足。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-TEST；DLC_REF: DLC-DOC；DLC_REF: DLC-JOB

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

测试为何可信、文档如何复现、已知限制和真实项目证据。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
