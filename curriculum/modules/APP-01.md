# APP-01｜TaskNode 任务接口与状态机

> Phase 3 · P0 · 工作量 XL

## 为什么学习

形成可写进简历的应用层成果，而不是停留在官方 demo。

## Prerequisites

INT-01

## 环境要求

Project A v1 稳定

## 开始时检查

确认底层全栈回归通过；定义任务需求和接口契约。

## 核心实践任务

以 C++ 为核心实现任务 action server；支持 named/joint/pose goal、feedback/result、输入校验和串行状态；Python 客户端用于调用/测试。

## 最小理论

任务层与运动层边界；状态机；action 并发与取消的最小语义。

## 故障注入

非法目标、并发 goal、规划失败、执行失败、客户端中断。

## 输出文件 / Deliverables

Project B v1；接口文档；状态机图；演示记录。

## Exit Criteria

三类目标至少两类稳定、第三类有明确失败语义；feedback/result 真实；代码与配置分层。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

为什么封装 TaskNode；它是否直接控制 controller；接口如何避免误用。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
