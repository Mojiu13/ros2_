# SIM-01｜Xacro、碰撞/惯性与 Docker 中的 Gazebo Sim

> Phase 1 · P0 · 工作量 L

## 为什么学习

把 A1 从可视模型变成 Docker 中可稳定仿真的模型，并验证 GUI/GPU 链路。

## Prerequisites

MODEL-01

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

MODEL-01 的 TF/pose 基线正确；复查 Host display、GPU vendor/driver、container renderer 和 Gazebo Jazzy 对应集成版本。

## 核心实践任务

重构 Xacro，补 collision/inertial，spawn 到 Gazebo Sim；修改质量、惯性、damping、friction、collision。对 RViz2/Gazebo 做 GUI smoke test，记录显示协议与 renderer；比较硬件加速和意外软件渲染现象。

## 最小理论

visual/collision/inertial、基础物理稳定性、Xacro；Host display/GPU device/container userspace 的职责边界。

## 故障注入

无窗口/权限、renderer 软件退化、模型坠落/抖动/穿透、资源路径或 spawn 失败；先区分 graphics、Gazebo、model。

## 输出文件 / Deliverables

A1 Xacro/Gazebo launch、参数实验、GUI/GPU 验证、仿真故障记录。

## Exit Criteria

Docker 中 RViz/Gazebo 可靠；renderer 有证据；模型稳定；至少四类参数实验完成；能解释 RViz 正常而 Gazebo 异常。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

RViz/Gazebo 边界；collision/inertial；如何区分 graphics 与 ROS/Gazebo 故障。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
