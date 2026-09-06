# ENV-01｜完整 Dockerized ROS2 Jazzy 开发环境

> CORE TO APPLY · 工作量 L

## Core Skill

一次搭建完整、稳定、可重建的 ros2-dev 环境，之后让 Docker 退居后台。

## Prerequisites

C++ / Python 基础；基本 Ubuntu 使用

## Starting Environment

Ubuntu 24.04 Host + Docker Engine / Compose + Git/editor。起点不要求已有 ROS container；本模块负责建立并验收它。

## Required Supporting Knowledge

- Host 与 container 的边界；image 是可重建模板，container 是其运行实例。
- Dockerfile、Compose、bind mount、workspace 和源码持久化各自解决什么问题。
- non-root、UID/GID、`ls -l`、`chmod`、`chown` 与宿主/容器文件 ownership 的最低关系。
- ROS underlay/overlay、`source`、重新构建后为何必须加载正确环境。
- 本模块实际需要的路径与文件观察：`pwd`、`ls`、`cd`、`mkdir`、`ls -l`。
- 本模块实际需要的环境与命令定位：`env`、`export`、`which`。
- 本模块实际需要的权限与安装：`chmod`、`chown`、`apt`。
- `cat`、`grep`、`find` 仅在检查当前环境文件、定位配置或验证安装时真实用到才教学和验收。
- 本模块需要的 Git 基础：`status`、`diff`、`add`、`commit`、`.gitignore`；完成时形成一次合理 commit。

这些内容属于当前 ENV-01 的 CORE Supporting Knowledge：真实使用时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

`core/EMBEDDED_SKILLS.md` 中未在本模块真实使用的 Must Learn Along CORE 内容，不作为 ENV-01 Exit Criteria；它们在后续 CORE 首次需要时 Just-In-Time 教学。

## Core Practice

建立 Dockerfile、Compose、entrypoint、non-root UID/GID、宿主源码 bind mount 和 workspace；一次安装 Jazzy、RViz2、Gazebo Sim/ros_gz、ros2_control/ros2_controllers、Gazebo control integration、MoveIt2 与 C++/Python 开发工具；验证 CLI、基础 GUI、最小节点和删除 container 后重建。

## Minimum Theory

讲到能独立判断文件在哪一侧、源码为何持久化、source/rebuild 为何必要、权限为何异常并能修复。Docker layer/cache、daemon、复杂网络、多阶段构建进入 DLC。

## Fault / Debug

只做一个 ownership、mount 或 entrypoint/source 的代表故障。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

docker/ 环境定义；ENVIRONMENT_MANIFEST；最小 workspace；重建证据。

另须创建或更新 `docs/modules/ENV-01/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

完整 image 可重建；源码不丢；non-root 权限正常；workspace 重编译；最小节点再次运行。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/ENV-01/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-ENV-ADV`：Docker internals、多阶段构建、复杂 device/GPU/network；`DLC-SIM-GRAPHICS`：真实渲染异常；`DLC-TOOLS`：高级 Linux/Git/CMake。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

Host/container 边界、UID/GID、持久化与可重建性；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/ENV-01/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
