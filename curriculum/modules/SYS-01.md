# SYS-01｜6/7 DOF 参考机械臂完整链路观察

> Phase 1 · P0 · 工作量 S

## 为什么学习

先在真实复杂度的成熟 6/7 DOF 机械臂上观察完整终点，为 Project A2 建立基线。

## Prerequisites

ROS-03

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定宿主安装 ROS。

## 开始时检查

确认 Docker GUI/GPU 与 ROS discovery 已通过；教学时依据 Jazzy 官方支持现状选择维护良好的 6/7 DOF 参考机械臂，不凭旧教程固定型号。

## 核心实践任务

在 RViz/Gazebo（若参考包支持）完成规划执行；观察节点、TF、joint_states、MoveIt 与 controller action；画规划、执行、反馈链并记录参考模型来源/版本。

## 最小理论

成熟模型、URDF/SRDF、move_group、planning pipeline、MoveIt controller manager、ros2_control controller_manager 与 simulated hardware 的边界。

## 故障注入

隐藏一个 action server 或破坏一个容器网络/显示入口，先归层再恢复。

## 输出文件 / Deliverables

Project A2 参考基线；完整系统地图 v1；版本与支持状态记录。

## Exit Criteria

能讲清 6/7 DOF 规划/执行/反馈；Docker 中可重复启动；知道 Plan/Execute 与两个 manager 的边界。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。临时 container 修改未回写环境定义时也不得完成。

## 模块面试范围

MoveIt 与 ros2_control 关系；两个 controller manager；6/7 DOF 系统不动时如何先分层。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、本文件、prerequisite 报告、Docker 架构/环境记录以及相关项目文档；不得依赖其他聊天记忆。
