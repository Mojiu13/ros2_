# CTRL-02｜Direct FollowJointTrajectory 与 A2 控制基线

> CORE TO APPLY · 工作量 L

## 为什么在 CORE

先用 A1 理解轨迹契约，再在成熟 A2 上证明 MoveIt 之前的控制链独立正常。

## Prerequisites

CTRL-01

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

Stage A：A1 上直接发送安全 JointTrajectory，观察 joint_names、time_from_start、feedback/result。Stage B：在 SYS-01 的成熟 6/7 DOF A2 上读取现成 config，验证 simulated hardware、joint_state_broadcaster、joint_trajectory_controller、FollowJointTrajectory、joint order，并绕过 MoveIt 直接运动。

## 最小理论

JointTrajectory 与 FollowJointTrajectory 时间/顺序语义；不读 controller source 或 realtime internals。

## 故障注入

joint mismatch、时间不递增、controller inactive 或 action missing 中一到两个代表案例。

## Deliverables

A1 direct 示例、A2 controller baseline、反馈证据和故障记录。

## Exit Criteria

A1 原理能解释；A2 明确证明 simulated robot→ros2_control→JTC→FJT→motion 正常，方可进入 MoveIt。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-CONTROL；DLC_REF: DLC-CONTROL-LOWLEVEL

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

FJT、time_from_start、为何 MoveIt 前先验证 controller。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
