# MODEL-02｜机器人模型工程化与参数验证

> Phase 2 · P1 · 工作量 L

## 为什么学习

从“能显示”升级为可维护、可验证、适合仿真与规划的模型工程。

## Prerequisites

INT-01

## 环境要求

Project A v1

## 开始时检查

固定可工作的模型版本作为对照。

## 核心实践任务

模块化 Xacro；mesh/坐标约定；limit/mimic；collision 简化；inertial 合理性；模型静态检查与参数回归。

## 最小理论

碰撞几何权衡、惯性矩阵基本约束、坐标约定和配置一致性。

## 故障注入

自碰撞、错误惯性、极限不一致、资源安装缺失。

## 输出文件 / Deliverables

工程化 description 包；模型检查清单；参数变更报告。

## Exit Criteria

模型变更有验证流程；RViz/Gazebo/MoveIt 使用同一描述源；关键参数可追踪。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

如何权衡 visual/collision；joint limit 在哪些层重复出现。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
