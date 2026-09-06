# MOVEIT-02｜C++/Python 编程规划与执行及运动学直觉

> Phase 1 · P0 · 工作量 L

## 为什么学习

在 A2 上把 GUI 闭环转换为 C++/Python 应用代码，并巩固规划失败所对应的机器人学含义。

## Prerequisites

MOVEIT-01

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

A2 RViz 闭环成功；确认 Jazzy 当前稳定 API，记录 C++/Python API 选择和版本。

## 核心实践任务

C++ 实现 named/joint/pose target 的 plan→inspect→execute；Python 实现任务调用或等价验证工具。记录 FK/IK 输入输出、可能的多 IK solution、unreachable/limit/workspace/near-singularity 现象；输出规划/执行耗时与错误。

## 最小理论

start state、goal constraints、RobotTrajectory；FK/IK 工程边界；规划与执行 API；singularity 只讲诊断直觉。

## 故障注入

current state 超时、frame_id 错、无 IK、超限、空轨迹、execution server 缺失、API 版本差异。

## 输出文件 / Deliverables

A2 C++ 节点、Python 客户端/工具、API 决策、运动学失败记录、结果日志。

## Exit Criteria

6/7 DOF 上至少两类目标稳定执行，第三类有明确错误；不误报失败；能解释目标如何变成轨迹。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

start/goal；joint/pose target；IK solution；unreachable vs planning failure；Python/C++ 分工。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
