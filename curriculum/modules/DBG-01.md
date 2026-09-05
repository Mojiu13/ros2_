# DBG-01｜跨层故障注入与诊断手册

> Phase 3 · P0 · 工作量 L

## 为什么学习

故障排查是独立主线，也是应用岗位最能拉开差距的能力。

## Prerequisites

INT-01

## 环境要求

可工作的全栈作为对照组

## 开始时检查

确认一次只注入一个故障，并记录正常基线。

## 核心实践任务

覆盖未 source、包/build/launch、topic、TF、URDF、joint mismatch、inactive controller、action missing、planning/start state/execution/timeout/mismatch；逐项形成证据链。

## 最小理论

分层诊断、控制变量、最小复现、相关性与因果性。

## 故障注入

本模块本身即系统化故障注入；禁止同时叠加多个未知故障。

## 输出文件 / Deliverables

DEBUGGING_PLAYBOOK；ERROR_LOG；故障定位决策树；复现材料。

## Exit Criteria

至少完成规定故障族的代表案例；每例包含现象、观察、层级、根因、修复和回归。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

机械臂不动的排查树；Plan failed 与 Execute failed；joint mismatch 会跨哪些文件。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
