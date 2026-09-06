# CTRL-01｜ros2_control 与 Controller 最小闭环

> CORE TO APPLY · 工作量 L

## 为什么在 CORE

让模型从可仿真升级为可控制，保留机械臂主线必需的控制接口。

## Prerequisites

SIM-01

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

为 A1 接入 ros2_control；配置 state/command interface、controller_manager、joint_state_broadcaster、joint_trajectory_controller；观察最小 lifecycle：load/configure/activate。

## 最小理论

state/command interface、controller_manager、broadcaster/controller 与 simulated hardware 的角色；不深入 ResourceManager、实时 update 或源码。

## 故障注入

controller inactive、interface 或 joint name mismatch 中一个案例。

## Deliverables

A1 ros2_control/config、接口图、controller 状态证据和故障记录。

## Exit Criteria

controllers active；joint states 可观察；能解释 interfaces 和最小 lifecycle。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-CONTROL；DLC_REF: DLC-CONTROL-LOWLEVEL

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

interfaces、manager、broadcaster、active 状态。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
