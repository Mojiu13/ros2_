# MOVEIT-03｜PlanningScene、约束与轨迹质量

> Phase 2 · P1 · 工作量 L

## 为什么学习

覆盖应用开发常见的环境障碍、约束和速度调整，不陷入规划算法研究。

## Prerequisites

INT-01

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

保存无障碍基线轨迹与时间。

## 核心实践任务

增删碰撞物；观察 current scene/state；调整 scaling、规划时间和尝试次数；检查 trajectory positions/velocities/accelerations/time；做简单路径约束。

## 最小理论

PlanningScene、碰撞检查、路径与时间参数化的区别、规划失败分类。

## 故障注入

scene 未同步、start state collision、不可达或过约束目标、空/异常轨迹。

## 输出文件 / Deliverables

场景操作示例；轨迹检查报告；规划失败矩阵。

## Exit Criteria

能解释并复现至少三类 planning failure；能用指标比较轨迹变化。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

PlanningScene 从哪里来；路径规划与时间参数化；如何区分碰撞和不可达。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
