# CTRL-01｜ros2_control 接入与 Controller 生命周期

> Phase 1 · P0 · 工作量 L

## 为什么学习

让模型从可看变为可控，并理解接口、硬件与 controller 的边界。

## Prerequisites

SIM-01

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。

如果本模块新增依赖，必须更新版本化环境定义、重建 image/container、验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。

默认使用 ENV-01 的 Dockerized Jazzy 环境；不假定 Host 安装 ROS。到 CTRL-01 才正式加入 ros2_control、ros2_controllers、gz_ros2_control 或 Jazzy 当前等价集成，更新环境定义、重建并记录版本。## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。

模型在 Gazebo 稳定；关节名与 limit 已冻结为基线。## 核心实践任务

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

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

state/command interface；controller_manager 做什么；为什么 active 才能接收目标。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
