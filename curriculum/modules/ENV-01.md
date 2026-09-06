# ENV-01｜完整 Dockerized ROS2 Jazzy 机械臂开发环境与可重建工作区

> Phase 0 · P0 · 工作量 L

## 为什么学习

一次搭建完整、稳定、可重建的机械臂 ROS 开发基础设施。ENV-01 后 Docker 退居后台，课程注意力转向 ROS2 与机器人软件。

## Prerequisites

基本 Linux 使用；C++ / Python 基础；不要求 ROS 或 Docker 深入知识

## 环境要求

Ubuntu 24.04 Host + 一个主 `ros2-dev` container。实际执行时根据 ROS2 Jazzy、Gazebo、MoveIt、ros2_control 与 Docker 官方当前文档确认镜像、包名和版本，不照搬 ROS1、Foxy 或 Humble 教程。

## 开始时检查

[HOST] 记录 Ubuntu、CPU 架构、GPU vendor/driver、Docker/Compose 版本、Git/编辑器和 Docker 用户权限；确认宿主源码目录。无需 Host 安装 ROS。

## 核心实践任务

亲手建立 Dockerfile、compose.yaml、entrypoint.sh 和 non-root development user，处理 Host UID/GID 与 bind-mounted 源码 ownership。Image 一次包含 ROS2 Jazzy、RViz2、与 Jazzy 匹配的 Gazebo Sim、ros_gz、ros2_control、ros2_controllers、gz_ros2_control 或当前等价方案、MoveIt2、colcon、rosdep、ament、build-essential、cmake、git 及基础 C++/Python ROS 开发依赖。建立 `/workspace/src/build/install/log` 与 underlay/overlay；掌握 compose up/down、进入 container 和 rebuild。完成基础 GUI passthrough，并按实际 Intel/AMD/NVIDIA 验证 GUI/3D 基础可用。只验证软件存在、ROS CLI/最小节点和 GUI 基础启动，不教学 Gazebo、controller、MoveIt、TF 或 motion planning 原理。删除 container 后重建并再次运行。

## 最小理论

image、container、Dockerfile、Compose、bind mount、entrypoint、non-root user、UID/GID、Host/Container 边界；named volume 只知道用途；workspace/source/underlay/overlay。明确不学 cgroup、namespace 内部、多阶段优化、缓存细节、微服务、Kubernetes 或 CI 镜像优化。

## 故障注入

只做一个受控 Docker 故障：优先选择 UID/GID/ownership、mount 或 entrypoint/source 中的一项，完成现象→证据→修复→重建回归。不扩展为 Docker 故障训练集。

## 输出文件 / Deliverables

`docker/Dockerfile`、`compose.yaml`、`entrypoint.sh`、`README.md`；完整 ros2-dev image；最小 workspace/package；`docs/ENVIRONMENT_MANIFEST.md`；GUI 基础验证；删除重建报告。

## Exit Criteria

Docker 环境能启动；完整主线软件栈已安装并记录；workspace 可构建；宿主源码持久化且无大量 root-owned 文件；container 使用合理 non-root user；RViz/Gazebo GUI 至少具备基础启动条件；删除 development container 后源码仍在，重新 build/start、workspace build、source 后最小 ROS2 node 再次成功。无需理解或操作 Gazebo physics、controller lifecycle、MoveIt planning、DDS 深层或 GPU 内部机制。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

Host 与 container 边界；image/container/mount/entrypoint；UID/GID；怎样重建；为什么软件可提前安装而知识仍按模块学习。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
