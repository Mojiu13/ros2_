# MOVEIT-03｜PlanningScene、约束与轨迹质量

> Phase 2 · P1 · 工作量 L

## 为什么学习

覆盖应用开发常见的环境障碍、约束和速度调整，不陷入规划算法研究。

## Prerequisites

INT-01

## 环境要求

编程规划执行可用

## 开始时检查

保存无障碍基线轨迹与时间。

## 核心实践任务

增删碰撞物；观察 current scene/state；调整 scaling、规划时间和尝试次数；检查 trajectory positions/velocities/accelerations/time；做简单路径约束。

## 最小理论

PlanningScene、碰撞检查、路径与时间参数化的区别、规划失败分类。

## 故障注入

scene 未同步、start state collision、不可达或过约束目标、空/异常轨迹。

## 输出文件 / Deliverables

场景操作示例；轨迹检查报告；规划失败矩阵。

## Exit Criteria

能解释并复现至少三类 planning failure；能用指标比较轨迹变化。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

PlanningScene 从哪里来；路径规划与时间参数化；如何区分碰撞和不可达。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
