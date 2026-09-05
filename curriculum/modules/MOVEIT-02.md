# MOVEIT-02｜C++/Python 编程规划与执行

> Phase 1 · P0 · 工作量 L

## 为什么学习

把 GUI 成功转换为可维护应用代码，同时证明 C++ 主力与 Python 工具能力。

## Prerequisites

MOVEIT-01

## 环境要求

优先使用 Jazzy 官方稳定 API；记录实际 API 选择

## 开始时检查

RViz 闭环成功；读取 MoveIt 配置映射。

## 核心实践任务

C++ 实现 named/joint/pose target 的 plan→inspect→execute；Python 实现任务调用、数据检查或等价接口；输出成功/失败、耗时和错误语义。

## 最小理论

start state、goal constraints、RobotTrajectory、规划与执行 API 边界。

## 故障注入

current state 超时、不可达 pose、空轨迹、执行 server 缺失、API/发行版差异。

## 输出文件 / Deliverables

C++ 规划节点；Python 辅助/客户端；API 决策记录；结果日志。

## Exit Criteria

至少两类目标可编程执行；失败不会被误报成功；能解释选择的 Jazzy API。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

如何设置 start/goal；plan 与 execute 返回值如何处理；Python 与 C++ 各放哪层。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
