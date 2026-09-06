# MODEL-01｜MiniArm URDF、Xacro、TF 与 RViz

> CORE TO APPLY · 工作量 L

## 为什么在 CORE

用简单 A1 模型亲手理解机器人模型、坐标与最低运动学直觉。

## Prerequisites

SYS-01

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

从零创建 2–3 DOF MiniArm；完成 link/joint/origin/axis/limit、基础 Xacro、robot_state_publisher、TF、RViz；通过实验理解 DOF、joint/task space、pose/frame/transform、RPY/quaternion、PoseStamped/frame_id 和 FK 直觉。

## 最小理论

只讲会用、会看、会解释所需直觉；不推导矩阵、DH、Jacobian、SO(3)/SE(3) 或动力学。

## 故障注入

URDF 解析、TF 断链、axis/origin、fixed frame 或 frame_id 错误。

## Deliverables

A1 description 包、显示 launch、TF 图、模型实验和故障记录。

## Exit Criteria

模型可显示和运动；能解释 pose/frame/transform 与关节变化到末端变化。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-MODEL-ENGINEERING；DLC_REF: DLC-ROBOT-MATH

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

URDF/TF、DOF、joint/task space、pose、FK 直觉。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
