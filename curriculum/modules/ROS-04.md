# ROS-04｜QoS、Lifecycle 与 ROS 工程边界

> Phase 2 · P1 · 工作量 M

## 为什么学习

补齐常见工程机制，但保持在应用岗位所需深度。

## Prerequisites

INT-01

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

选择一个真实接口作为实验对象。

## 核心实践任务

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

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

QoS 不匹配的现象；普通节点与 lifecycle 节点的差别。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
