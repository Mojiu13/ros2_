# CTRL-02｜A1/A2 Direct Trajectory 与控制基线迁移

> Phase 1 · P0 · 工作量 L

## 为什么学习

先在 A1 理解 direct trajectory 原理，再把同一验证迁移到成熟 6/7 DOF A2，消除 MoveIt 前缺少 controller baseline 的断层。

## Prerequisites

CTRL-01

## 环境要求

使用 Dockerized Jazzy 环境。CTRL-01 时已经 Just-In-Time 加入 ros2_control 栈；Stage B 若 A2 模型需要额外 runtime/config，必须更新环境定义、重建、验证并记录版本。

## 开始时检查

确认 Docker/image/container、mount、underlay/overlay、CTRL-01 的 A1 controller 证据；读取 SYS-01 已选定的 A2 模型、版本和参考基线。Stage B 开始前确认 A2 Gazebo/simulated hardware 入口可获得。

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

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

A1 与 A2 各证明什么；FollowJointTrajectory/time_from_start；为何 MoveIt 前先测 A2 controller；成熟配置应如何验证而非重写。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
