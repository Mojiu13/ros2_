# CTRL-03｜Controller 配置、容差与夹爪协同

> Phase 2 · P1 · 工作量 L

## 为什么学习

掌握工作中常见的 controller YAML、限制、容差和多 controller 协同。

## Prerequisites

INT-01

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。

如果本模块新增依赖，必须更新版本化环境定义、重建 image/container、验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。

机械臂 controller 可稳定运行## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。

保留 CTRL-02 的合法轨迹作为回归。## 核心实践任务

调整 update/publish rate、constraints、goal_time；加入 gripper controller 或第二执行器；验证切换与资源占用；顺序动作。

## 最小理论

控制循环/发布频率边界、path/goal tolerance、多 controller 资源声明。

## 故障注入

容差 abort、controller 冲突、错误关节集合、夹爪失败后的状态不一致。

## 输出文件 / Deliverables

参数实验报告；arm+gripper 顺序演示；controller 调试卡。

## Exit Criteria

能用实验解释关键参数影响；两 controller 协同有失败策略。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

path 与 goal tolerance；多个 controller 何时冲突。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
