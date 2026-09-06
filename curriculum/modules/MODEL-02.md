# MODEL-02｜机器人模型工程化与参数验证

> Phase 2 · P1 · 工作量 L

## 为什么学习

从“能显示”升级为可维护、可验证、适合仿真与规划的模型工程。

## Prerequisites

INT-01

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

固定可工作的模型版本作为对照。

## 核心实践任务

模块化 Xacro；mesh/坐标约定；limit/mimic；collision 简化；inertial 合理性；模型静态检查与参数回归。

## 最小理论

碰撞几何权衡、惯性矩阵基本约束、坐标约定和配置一致性。

## 故障注入

自碰撞、错误惯性、极限不一致、资源安装缺失。

## 输出文件 / Deliverables

工程化 description 包；模型检查清单；参数变更报告。

## Exit Criteria

模型变更有验证流程；RViz/Gazebo/MoveIt 使用同一描述源；关键参数可追踪。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

如何权衡 visual/collision；joint limit 在哪些层重复出现。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
