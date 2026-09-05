# ENV-01｜Docker 化 ROS2 Jazzy 工程环境与可复现工作区

> Phase 0 · P0 · 工作量 L

## 为什么学习

建立项目自己定义、可重建的 ROS 开发环境，而不是让宿主机或某个手工改过的 container “碰巧能跑”。Docker 只学 ROS 工程当前需要的部分。

## Prerequisites

基本 Linux 使用；C++ / Python 基础；不要求 ROS 或 Docker 深入知识

## 环境要求

从普通 Ubuntu 24.04 Host 开始。教学时先按 Docker、ROS2 Jazzy、Gazebo、MoveIt 和 GPU vendor 当前官方文档确认镜像、软件源、GUI 与 runtime 方案。

## 开始时检查

检查 Ubuntu 版本、CPU 架构、桌面会话（X11/XWayland/Wayland）、GPU 型号与 Host driver；检查 Docker Engine/Compose 与用户权限。不得先假定 NVIDIA，也不得假定 Host 已安装 ROS。

## 核心实践任务

Host 明确只承担 Docker/Compose、Git、编辑器、桌面/GPU driver、硬件访问基础和源码持久化。亲手创建 docker/Dockerfile、compose.yaml、entrypoint.sh、README；在 image 中安装 Jazzy、colcon、rosdep、ament、MoveIt2、ros2_control、Gazebo ROS 集成及编译依赖。建立 /workspace/src/build/install/log；宿主源码 bind mount，区分 named volume。验证 underlay/overlay。识别显示协议后让 RViz2 GUI 工作；识别 Intel/AMD/NVIDIA 后检查 container 图形设备与 OpenGL renderer，确认不是意外软件渲染。完成 bridge/host networking 基线与 ROS_DOMAIN_ID 记录。

## 最小理论

image、container、Dockerfile、Compose、bind mount、named volume；Host/container 边界；ROS workspace、source、underlay/overlay；GUI/GPU 和容器网络只讲当前实验所需。

## 故障注入

Docker 权限失败、mount 路径错误、源码只存在 container、entrypoint 未 source、GUI 无显示、GPU 不可见或软件渲染、端口/网络命名空间误解。每次只注入一个。

## 输出文件 / Deliverables

docker/Dockerfile、docker/compose.yaml、docker/entrypoint.sh、docker/README；环境基线；GUI/GPU/renderer 记录；mount/network 图；重建验收报告。

## Exit Criteria

能够删除 ROS 开发 container，从 Dockerfile/Compose 重建；宿主源码仍存在；重新 build 后 ROS 环境和示例节点再次成功。能解释 image/container/bind/named volume/workspace/source/underlay/overlay。GUI 可用，GPU 路径有证据，所有依赖可由版本化环境定义恢复。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。临时 container 修改未回写环境定义时也不得完成。

## 模块面试范围

Host 与 container 各负责什么；为什么临时 apt install 不可复现；源码为什么用 bind mount；如何证明硬件加速；删除 container 后如何恢复。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、本文件、prerequisite 报告、Docker 架构/环境记录以及相关项目文档；不得依赖其他聊天记忆。
