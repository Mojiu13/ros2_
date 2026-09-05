# SIM-01｜Xacro、碰撞/惯性与 Docker 中的 Gazebo Sim

> Phase 1 · P0 · 工作量 L

## 为什么学习

把 A1 从可视模型变成 Docker 中可稳定仿真的模型，并验证 GUI/GPU 链路。

## Prerequisites

MODEL-01

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定宿主安装 ROS。

## 开始时检查

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

除非证据、复述和模块面试全部完成，否则不得标记 Completed。临时 container 修改未回写环境定义时也不得完成。

## 模块面试范围

RViz/Gazebo 边界；collision/inertial；如何区分 graphics 与 ROS/Gazebo 故障。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、本文件、prerequisite 报告、Docker 架构/环境记录以及相关项目文档；不得依赖其他聊天记忆。
