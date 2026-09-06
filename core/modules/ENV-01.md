# ENV-01｜完整 Dockerized ROS2 Jazzy 开发环境

> CORE TO APPLY · 工作量 L

## 为什么在 CORE

一次搭建完整、稳定、可重建的 ros2-dev 环境，之后让 Docker 退居后台。

## Prerequisites

C++ / Python 基础；基本 Ubuntu 使用

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

建立 Dockerfile、Compose、entrypoint、non-root UID/GID、宿主源码 bind mount 和 workspace；一次安装 Jazzy、RViz2、Gazebo Sim/ros_gz、ros2_control/ros2_controllers、Gazebo control integration、MoveIt2 与 C++/Python 开发工具；验证 CLI、基础 GUI、最小节点和删除 container 后重建。

## 最小理论

image/container、bind mount、Host/container、compose up/down、进入容器、rebuild、underlay/overlay；只讲完成环境所需内容。

## 故障注入

只做一个 ownership、mount 或 entrypoint/source 的代表故障。

## Deliverables

docker/ 环境定义；ENVIRONMENT_MANIFEST；最小 workspace；重建证据。

## Exit Criteria

完整 image 可重建；源码不丢；non-root 权限正常；workspace 重编译；最小节点再次运行。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-ENV-ADV；DLC_REF: DLC-SIM-GRAPHICS；DLC_REF: DLC-TOOLS

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

Host/container 边界、UID/GID、持久化与可重建性。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
