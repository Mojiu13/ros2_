# SYS-01｜参观 6/7 DOF 完整机械臂系统

> CORE TO APPLY · 工作量 S

## 为什么在 CORE

先看终点，建立完整链路地图，不在此处钻内部实现。

## Prerequisites

ROS-03

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

依据 Jazzy 当前维护状态选择成熟 6/7 DOF 模型；启动参考系统；识别 move_group、controller_manager、joint_states、TF、FollowJointTrajectory、RViz、Gazebo/simulated hardware；观察一次 Plan/Execute；画目标→MoveIt→Controller→Robot→State Feedback。

## 最小理论

各组件只讲名称、角色和上下游；不讲 planning pipeline、controller lifecycle 或内部 manager 实现。

## 故障注入

只做一个关键 node/action 不存在的观察案例。

## Deliverables

A2 型号与版本记录、完整链路图 v1、接口清单。

## Exit Criteria

能三分钟说明目标、规划、执行与反馈；能指出组件位置，不要求深入原理。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-MOVEIT；DLC_REF: DLC-CONTROL-LOWLEVEL

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

完整链路和组件角色，不考内部源码。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
