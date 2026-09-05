# ENV-01｜Docker 化 ROS2 Jazzy 最小开发环境与可重建工作区

> Phase 0 · P0 · 工作量 M

## 为什么学习

只建立可重建的 ROS2 Jazzy 基础开发环境，不提前安装或调通 Gazebo、MoveIt、ros2_control、完整 RViz/GPU 或复杂 DDS 网络。后续依赖按模块 Just-In-Time 加入。

## Prerequisites

基本 Linux 使用；C++ / Python 基础；不要求 ROS 或 Docker 深入知识

## 环境要求

从普通 Ubuntu 24.04 Host 开始。Host 只需 Docker Engine/Compose、Git、编辑器、Docker 用户权限、CPU 架构和基本 GPU 厂商信息。Container 只安装 ROS2 Jazzy 基础开发环境、colcon、rosdep、ament 及 C++/Python ROS 编译基础。

## 开始时检查

[HOST] 确认 Ubuntu 版本、CPU 架构、GPU vendor、Docker/Compose 版本、Git/编辑器和 Docker 用户权限；不要求 Host 安装 ROS。确认仓库状态和将被 bind mount 的源码路径。

## 核心实践任务

亲手创建最小 `docker/Dockerfile`、`compose.yaml`、`entrypoint.sh`；建立 non-root development user，并用 Host UID/GID 映射避免 bind-mounted 文件变成 root-owned。建立 `/workspace/src/build/install/log`，区分 image/container/bind mount/named volume/entrypoint；理解 `/opt/ros/jazzy` underlay 与 workspace overlay；编译运行最小 ROS2 示例。记录环境清单。删除 container 后从版本化定义重建、重新编译并再次运行。

## 最小理论

image、container、Dockerfile、Compose、bind mount、named volume、entrypoint；UID/GID 与文件 ownership 的开发所需直觉；workspace、source、underlay、overlay。不深入 namespace 或 Docker 系统原理。

## 故障注入

Docker 权限失败、Host/Container UID/GID 不匹配、root-owned 文件、mount 路径错误、源码只存在 container、entrypoint/source 错、overlay 未生效。一次只注入一个。

## 输出文件 / Deliverables

`docker/Dockerfile`、`docker/compose.yaml`、`docker/entrypoint.sh`、`docker/README.md`、最小 workspace/package、`docs/ENVIRONMENT_MANIFEST.md`、删除重建验收记录。

## Exit Criteria

Container 使用合理的 non-root development user；Host 可正常编辑/删除/Git 操作 bind-mounted 文件且没有大量 root-owned 文件；删除 container 后源码仍在；重建 image/container 和 workspace 后最小节点再次成功。ENV-01 不以 Gazebo、MoveIt、ros2_control、复杂网络或 Gazebo GPU 为完成条件。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

Host/Container 边界；UID/GID 与 ownership；image/container/mount/volume；underlay/overlay；为何临时 apt install 不是可复现环境。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
