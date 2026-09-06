# MOVEIT-01｜6/7 DOF 机械臂 SRDF、MoveIt 配置与 RViz 规划执行

> Phase 1 · P0 · 工作量 L

## 为什么学习

把 Project A 从简单学习模型迁移到成熟 6/7 DOF 复杂度，掌握语义模型、规划组、末端和 controller 映射。

## Prerequisites

CTRL-02

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。到 MOVEIT-01 才正式加入本项目所需 MoveIt2 development dependencies；如果本模块新增依赖，必须更新 Dockerfile/Compose/entrypoint 等版本化环境定义，重建 image/container，验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。SYS-01 已有的 runtime 依赖不替代本次开发环境验收。

## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。读取 CTRL-02 的 A2 Stage B 报告；必须先证明成熟 6/7 DOF A2 的 Gazebo/simulated hardware、joint_state_broadcaster、joint_trajectory_controller、FollowJointTrajectory 和 direct trajectory 均正常，否则不得开始 MoveIt。实际型号仍在 SYS-01 根据 Jazzy/Gazebo/ros2_control/MoveIt/Docker 支持状态选择，不提前写死。

## 核心实践任务

读取并有目的地修改成熟机械臂的 URDF/SRDF/kinematics/joint_limits/controllers；识别 planning group 与 end effector；在 RViz 比较 joint-space target 与 Cartesian pose target；观察 FK/IK solution、joint limit、workspace、unreachable pose 与接近 singularity 的工程现象。

## 最小理论

URDF/SRDF；joint-space/Cartesian target；FK/IK 与 IK solution；workspace、joint limit、singularity 工程直觉；不做 DH/Jacobian 推导。

## 故障注入

group/end effector/kinematics/controller mapping 错；无 IK、不可达、超 joint limit、近奇异或碰撞目标。

## 输出文件 / Deliverables

A2 MoveIt 配置审计与修改、目标实验、失败分类、Plan/Execute 证据。

## Exit Criteria

未通过 CTRL-02 Stage B 的 A2 controller/direct trajectory baseline，不得开始或完成 MOVEIT-01。通过后，6/7 DOF A2 必须能在 RViz 规划执行，并能区分配置、IK、规划与执行失败。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

planning group/end effector；joint 与 pose target；FK/IK；不可达、limit、workspace、singularity；MoveIt 如何选 controller。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
