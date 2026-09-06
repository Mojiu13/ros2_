# MOVEIT-01｜6/7 DOF 机械臂 SRDF、MoveIt 配置与 RViz 规划执行

> Phase 1 · P0 · 工作量 L

## 为什么学习

把 Project A 从简单学习模型迁移到成熟 6/7 DOF 复杂度，掌握语义模型、规划组、末端和 controller 映射。

## Prerequisites

CTRL-02

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

读取 CTRL-02 的 A2 Stage B 报告。必须先证明成熟 6/7 DOF A2 的 simulated hardware、joint_state_broadcaster、joint_trajectory_controller、FollowJointTrajectory 和 direct trajectory 正常；否则不得开始 MoveIt。实际型号仍由 SYS-01 根据当前支持状态选择。

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

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

planning group/end effector；joint 与 pose target；FK/IK；不可达、limit、workspace、singularity；MoveIt 如何选 controller。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
