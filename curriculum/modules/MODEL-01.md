# MODEL-01｜MiniArm URDF、TF、RViz 与机器人空间基础

> Phase 1 · P0 · 工作量 L

## 为什么学习

用简单 2–3 DOF MiniArm 亲手理解模型、坐标和运动空间，为复杂机械臂集成建立不黑盒的机器人学直觉。

## Prerequisites

SYS-01

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

确认 Project A2 参考链路已观察；新建 Project A1 学习模型，避免把成熟模型配置直接复制为答案。

## 核心实践任务

从零建立 2–3 DOF URDF；配置 link/joint/origin/axis/limit/visual；发布 joint state/TF 并在 RViz 操作。通过改 joint 值和 frame 实验比较 joint space 与 Cartesian/task space；观察 base/tool/end-effector frame；构造 position/orientation/pose、RPY、quaternion、PoseStamped/frame_id 示例；用关节变化到末端位姿变化形成 FK 直觉。

## 最小理论

DOF、joint space、Cartesian/task space；position/orientation/pose；frame/transform；base/tool/end-effector frame；RPY/quaternion；PoseStamped/frame_id；forward kinematics 直觉，不做复杂矩阵推导。

## 故障注入

TF 断链、parent/child、axis/origin/fixed frame/frame_id 错；四元数无效；混淆点的坐标与参考 frame。

## 输出文件 / Deliverables

Project A1 URDF、显示 launch、TF 图、空间/姿态实验表、模型故障记录。

## Exit Criteria

能预测 origin/axis/关节变化对末端 pose 的影响；能解释 pose 必须带 frame；TF 树完整；基本概念可口述。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

DOF 与 joint space；pose/frame/transform；RPY 与 quaternion；FK 做什么；robot_state_publisher 角色。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
