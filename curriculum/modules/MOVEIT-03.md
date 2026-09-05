# MOVEIT-03｜PlanningScene、约束与轨迹质量

> Phase 2 · P1 · 工作量 L

## 为什么学习

覆盖应用开发常见的环境障碍、约束和速度调整，不陷入规划算法研究。

## Prerequisites

INT-01

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。

如果本模块新增依赖，必须更新版本化环境定义、重建 image/container、验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。

编程规划执行可用## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。

保存无障碍基线轨迹与时间。## 核心实践任务

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

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

PlanningScene 从哪里来；路径规划与时间参数化；如何区分碰撞和不可达。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
