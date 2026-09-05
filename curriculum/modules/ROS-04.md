# ROS-04｜QoS、Lifecycle 与 ROS 工程边界

> Phase 2 · P1 · 工作量 M

## 为什么学习

补齐常见工程机制，但保持在应用岗位所需深度。

## Prerequisites

INT-01

## 环境要求

Project A v1

## 开始时检查

选择一个真实接口作为实验对象。

## 核心实践任务

对可靠性/持久性做最小 QoS 实验；使用 lifecycle 节点或现有 lifecycle 组件；观察启动顺序和状态依赖；规划包边界。

## 最小理论

QoS 兼容、lifecycle 状态机、组件化只讲取舍。

## 故障注入

QoS 不兼容无数据、节点未 active、启动竞态。

## 输出文件 / Deliverables

QoS 实验表；生命周期图；包边界说明。

## Exit Criteria

能诊断“双方都在但没数据”；能说明何时值得用 lifecycle。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

QoS 不匹配的现象；普通节点与 lifecycle 节点的差别。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
