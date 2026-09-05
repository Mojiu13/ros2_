# MODEL-02｜机器人模型工程化与参数验证

> Phase 2 · P1 · 工作量 L

## 为什么学习

从“能显示”升级为可维护、可验证、适合仿真与规划的模型工程。

## Prerequisites

INT-01

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。

如果本模块新增依赖，必须更新版本化环境定义、重建 image/container、验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。

Project A v1## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。

固定可工作的模型版本作为对照。## 核心实践任务

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

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

如何权衡 visual/collision；joint limit 在哪些层重复出现。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
