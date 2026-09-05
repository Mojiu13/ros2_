# ADV-01｜joint_trajectory_controller 源码主线

> Advanced Optional · P2 · 工作量 L

## 为什么学习

为偏底层岗位加分，不作为首份应用开发工作的入场门槛。

## Prerequisites

CTRL-03

## 环境要求

锁定与 Jazzy 对应源码版本

## 开始时检查

先提出明确问题：轨迹如何从 goal 变成周期 command。

## 核心实践任务

沿 goal validation→realtime buffer→update→sample→tolerance→interface write 阅读并做注释/实验。

## 最小理论

实时边界、插值、容差；只补回答主线所需内容。

## 故障注入

源码版本错位、把实现细节误当稳定 API、失去主线。

## 输出文件 / Deliverables

源码导航图；版本链接；行为实验。

## Exit Criteria

能用代码位置与实验解释主线，不要求逐行记忆。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

action goal 如何进入 update；tolerance abort；command write 的边界。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
