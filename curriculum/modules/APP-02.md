# APP-02｜超时、取消、重试与基本恢复

> Phase 3 · P1 · 工作量 XL

## 为什么学习

把“能跑”升级为工程上可控失败，体现机械臂调试与应用开发能力。

## Prerequisites

APP-01,DBG-01

## 环境要求

TaskNode v1

## 开始时检查

定义哪些错误可恢复、哪些必须终止；保存正常回归。

## 核心实践任务

实现 timeout/cancel；有限 retry/replan；controller/action readiness 检查；safe stop/最终错误上报；避免无限重试。

## 最小理论

错误分类、幂等、恢复预算、安全边界；不宣称真实硬件安全认证。

## 故障注入

action server missing、controller inactive、不可达目标、执行超时、用户取消。

## 输出文件 / Deliverables

Project B v2；恢复策略表；时序图；故障演示。

## Exit Criteria

每类故障有确定状态和上报；cancel 可验证；恢复次数受限；回归无破坏。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

哪些错误适合 retry；cancel 与 stop 的区别；如何避免恢复逻辑掩盖根因。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
