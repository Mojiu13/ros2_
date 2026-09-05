# SIM-01｜Xacro、碰撞/惯性与 Gazebo Sim 入门

> Phase 1 · P0 · 工作量 L

## 为什么学习

岗位明确要求搭建仿真并按环境调整模型参数。

## Prerequisites

MODEL-01

## 环境要求

Jazzy 对应 Gazebo Sim 与 ros_gz 集成

## 开始时检查

验证模型在 RViz 正确；确认采用现代 Gazebo Sim，不混用 Gazebo Classic 教程。

## 核心实践任务

把 URDF 重构为 Xacro；补 collision/inertial；spawn 到 Gazebo Sim；逐项修改质量、惯性、damping、friction、collision 并记录现象。

## 最小理论

visual/collision/inertial 的职责；基础物理稳定性；Xacro 参数与宏。

## 故障注入

模型坠落/抖动/穿透、惯性无效、资源路径错误、桥接或 spawn 失败。

## 输出文件 / Deliverables

Xacro 模型；Gazebo launch；参数实验表；仿真问题记录。

## Exit Criteria

模型可稳定加载；至少四类参数实验有预期/实际对照；能解释 RViz 正常但仿真异常。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

为什么 collision/inertial 缺失会影响仿真；Gazebo 与 RViz 的职责边界。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
