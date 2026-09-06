# MOVEIT-01｜A2 MoveIt2 配置与 RViz Plan/Execute

> CORE TO APPLY · 工作量 L

## 为什么在 CORE

在已知控制链正常的 A2 上建立最小规划执行能力。

## Prerequisites

CTRL-02

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

读取/修改 SRDF、planning group、end effector、kinematics config、joint limits、controller mapping；在 RViz 完成 named/joint/pose target 的 Plan/Execute；加入一个简单 collision object 并观察路径变化。

## 最小理论

FK/IK 工程直觉、IK solution、workspace、unreachable、start state、joint limit、planning vs execution；PlanningScene 只建立最低直觉。

## 故障注入

无 IK/不可达、start state、controller mapping 或 execution failure 中代表案例。

## Deliverables

A2 MoveIt config 审计、三类目标、简单障碍物实验和失败分类。

## Exit Criteria

RViz 可规划执行；能区分 IK/规划/执行问题；不要求 OMPL、约束或高级场景研究。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-MOVEIT；DLC_REF: DLC-ROBOT-MATH；DLC_REF: DLC-MOVEIT-INTERNALS

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

SRDF/group/end effector、FK/IK、Plan vs Execute、简单 PlanningScene。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
