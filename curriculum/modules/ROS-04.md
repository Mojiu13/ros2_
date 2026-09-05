# ROS-04｜QoS、Lifecycle 与 ROS 工程边界

> Phase 2 · P1 · 工作量 M

## 为什么学习

补齐常见工程机制，但保持在应用岗位所需深度。

## Prerequisites

INT-01

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。

如果本模块新增依赖，必须更新版本化环境定义、重建 image/container、验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。

Project A v1## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。

选择一个真实接口作为实验对象。## 核心实践任务

对可靠性/持久性做最小 QoS 实验；使用 lifecycle 节点或现有 lifecycle 组件；观察启动顺序和状态依赖；规划包边界。

## 最小理论

QoS 兼容、lifecycle 状态机、组件化只讲取舍。

## 故障注入

QoS 不兼容无数据、节点未 active、启动竞态。

## 输出文件 / Deliverables

QoS 实验表；生命周期图；包边界说明。

## Exit Criteria

能诊断“双方都在但没数据”；能说明何时值得用 lifecycle。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

QoS 不匹配的现象；普通节点与 lifecycle 节点的差别。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
