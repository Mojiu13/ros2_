# SIM-01｜MiniArm Gazebo Sim 基础

> CORE TO APPLY · 工作量 M

## 为什么在 CORE

让 A1 从可视模型变成稳定可仿真的模型。

## Prerequisites

MODEL-01

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

加入基础 collision/inertial，spawn 到 Gazebo；让模型稳定；做 2–3 个代表实验：damping、collision、mass/inertial；解释 RViz 与 Gazebo 的区别。

## 最小理论

visual/collision/inertial 和物理稳定性的最低直觉。GPU 正常时不研究 renderer。

## 故障注入

从模型坠落/抖动、collision 或 inertial 错误中选择一个代表案例；真实 graphics 问题只按需处理。

## Deliverables

A1 Gazebo launch/model、2–3 个参数实验和一个故障记录。

## Exit Criteria

模型稳定加载；代表参数实验有前后对照；能区分显示与物理问题。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-SIM；真实黑屏/软件渲染/GUI 卡死时 DLC_REF: DLC-SIM-GRAPHICS

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

RViz/Gazebo、collision/inertial、参数如何影响现象。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
