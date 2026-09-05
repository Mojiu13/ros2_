# SIM-01｜Xacro、碰撞/惯性与 Docker 中的 Gazebo Sim

> Phase 1 · P0 · 工作量 L

## 为什么学习

把 A1 从可视模型变成 Docker 中可稳定仿真的模型，并验证 GUI/GPU 链路。

## Prerequisites

MODEL-01

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。

如果本模块新增依赖，必须更新版本化环境定义、重建 image/container、验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。

默认使用 ENV-01 的 Dockerized Jazzy 环境；不假定 Host 安装 ROS。到 SIM-01 才正式按官方文档加入 Gazebo Sim、ros_gz 和 GUI/GPU simulation requirements，更新环境定义、重建并记录 Gazebo release、renderer 与 GPU vendor 配置。## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。

MODEL-01 的 TF/pose 基线正确；复查 Host display、GPU vendor/driver、container renderer 和 Gazebo Jazzy 对应集成版本。## 核心实践任务

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

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

RViz/Gazebo 边界；collision/inertial；如何区分 graphics 与 ROS/Gazebo 故障。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
