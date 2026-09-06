# CTRL-02｜A1/A2 Direct Trajectory 与控制基线迁移

> Phase 1 · P0 · 工作量 L

## 为什么学习

先在 A1 理解 direct trajectory 原理，再把同一验证迁移到成熟 6/7 DOF A2，消除 MoveIt 前缺少 controller baseline 的断层。

## Prerequisites

CTRL-01

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

读取 CTRL-01 的 A1 controller 证据和 SYS-01 已选定的 A2 模型、版本与参考基线；Stage B 开始前确认 A2 Gazebo/simulated hardware 入口可用。

## 核心实践任务

Stage A｜A1 Direct Trajectory：在 2–3 DOF MiniArm 上验证 controller active、FollowJointTrajectory、JointTrajectory、joint names/order、time_from_start、feedback/result，并注入轨迹错误。Stage B｜A2 Control Baseline Migration：在 SYS-01 选定的成熟 6/7 DOF 模型上读取并验证现成 Gazebo/simulated hardware、ros2_control/controller 配置；确认 joint_state_broadcaster 与 joint_trajectory_controller active、FollowJointTrajectory 存在、joint names/order 正确；不经过 MoveIt 发送一条安全合法轨迹，让 A2 真实运动并得到正确 feedback/result。优先理解/验证/修改成熟配置，不重复发明。

## 最小理论

JointTrajectory、FollowJointTrajectory、时间与关节顺序；A1 原理学习与 A2 集成验证的边界；MoveIt 并非 direct trajectory 所必需。

## 故障注入

A1/A2 joint mismatch、顺序错误、时间不递增、controller inactive、action missing、容差 abort、A2 配置与仿真入口不一致。

## 输出文件 / Deliverables

A1 direct trajectory 示例与字段注释；A2 controller/config 审计；A2 直接轨迹与运动证据；两阶段故障矩阵。

## Exit Criteria

A1 能解释 direct trajectory 原理。A2 必须明确证明 `Gazebo/simulated hardware → ros2_control → joint_trajectory_controller → FollowJointTrajectory → 6/7 DOF robot motion` 正常，且 feedback/result 正确。未通过 A2 baseline 不得进入 MOVEIT-01。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

A1 与 A2 各证明什么；FollowJointTrajectory/time_from_start；为何 MoveIt 前先测 A2 controller；成熟配置应如何验证而非重写。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
