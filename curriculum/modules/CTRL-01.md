# CTRL-01｜ros2_control 接入与 Controller 生命周期

> Phase 1 · P0 · 工作量 L

## 为什么学习

让模型从可看变为可控，并理解接口、硬件与 controller 的边界。

## Prerequisites

SIM-01

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

模型在 Gazebo 稳定；关节名与 limit 已冻结为基线。

## 核心实践任务

添加 ros2_control 描述；配置 state/command interface；启动 controller_manager、joint_state_broadcaster、joint_trajectory_controller；观察 lifecycle 和 interfaces。

## 最小理论

ResourceManager、hardware interface、controller_manager、broadcaster/controller；configure/activate。

## 故障注入

controller 加载失败、inactive、接口 claim 冲突、关节名或接口名不匹配。

## 输出文件 / Deliverables

ros2_control Xacro/YAML；controller 状态表；接口地图。

## Exit Criteria

controller 可加载并 active；joint_states 来自控制链；能按证据解释 activation failure。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

state/command interface；controller_manager 做什么；为什么 active 才能接收目标。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
