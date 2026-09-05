# MOVEIT-01｜6/7 DOF 机械臂 SRDF、MoveIt 配置与 RViz 规划执行

> Phase 1 · P0 · 工作量 L

## 为什么学习

把 Project A 从简单学习模型迁移到成熟 6/7 DOF 复杂度，掌握语义模型、规划组、末端和 controller 映射。

## Prerequisites

CTRL-02

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定宿主安装 ROS。

## 开始时检查

A1 控制闭环完成；教学时确认 A2 机械臂及 MoveIt 配置在 Jazzy 当前维护状态，不从零手搓工业 7DOF 模型。

## 核心实践任务

读取并有目的地修改成熟机械臂的 URDF/SRDF/kinematics/joint_limits/controllers；识别 planning group 与 end effector；在 RViz 比较 joint-space target 与 Cartesian pose target；观察 FK/IK solution、joint limit、workspace、unreachable pose 与接近 singularity 的工程现象。

## 最小理论

URDF/SRDF；joint-space/Cartesian target；FK/IK 与 IK solution；workspace、joint limit、singularity 工程直觉；不做 DH/Jacobian 推导。

## 故障注入

group/end effector/kinematics/controller mapping 错；无 IK、不可达、超 joint limit、近奇异或碰撞目标。

## 输出文件 / Deliverables

A2 MoveIt 配置审计与修改、目标实验、失败分类、Plan/Execute 证据。

## Exit Criteria

6/7 DOF A2 在 RViz 规划执行；能用现实含义解释各运动学术语并区分配置/IK/规划/执行失败。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。临时 container 修改未回写环境定义时也不得完成。

## 模块面试范围

planning group/end effector；joint 与 pose target；FK/IK；不可达、limit、workspace、singularity；MoveIt 如何选 controller。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、本文件、prerequisite 报告、Docker 架构/环境记录以及相关项目文档；不得依赖其他聊天记忆。
