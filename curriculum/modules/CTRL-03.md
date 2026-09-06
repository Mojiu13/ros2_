# CTRL-03｜Controller 配置、容差与夹爪协同

> Phase 2 · P1 · 工作量 L

## 为什么学习

掌握工作中常见的 controller YAML、限制、容差和多 controller 协同。

## Prerequisites

INT-01

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

保留 CTRL-02 的合法轨迹作为回归。

## 核心实践任务

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

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

path 与 goal tolerance；多个 controller 何时冲突。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
