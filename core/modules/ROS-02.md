# ROS-02｜C++ / Python ROS 包与最小通信编程

> CORE TO APPLY · 工作量 L

## Core Skill

建立真实 ROS 编程能力，并在 TaskNode 前掌握最小 Action。

## Prerequisites

ROS-01

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- `package.xml` 与 `CMakeLists.txt`/Python package metadata 的职责边界。
- 当前代码实际使用的 `find_package`、`add_executable`、dependency declaration 与 `ament_target_dependencies`。
- executable install：通过当前真实 target 理解 `install(TARGETS ...)`，以及可执行文件为何需要进入 install space。
- `rosidl` interface generation：定义文件、生成、依赖与消费接口。
- build → source overlay → run：理解重新构建后为何必须加载正确 overlay，再验证节点和接口。
- Action 最低事件流：goal → accept/reject → execute → feedback → result，并理解 goal handle 与 cancel。
- 若当前实现涉及 callback、线程或 executor，只解释为何当前代码这样组织；不展开内部调度架构。
- 构建/运行前后使用 Git `status`/`diff`，完成模块后形成一次合理 commit。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

创建 ament_cmake、ament_python 和 custom interface package；用合理跨语言组合完成最小 pub/sub、service server/client、action server/client；Action 覆盖 goal response、feedback、result、cancel 与 goal handle，不重复刷两套完整 demo。

## Minimum Theory

讲清当前包和代码涉及的 ament/rosidl/Action 事件流；不系统讲 executor internals、callback groups 或多线程架构。

## Fault / Debug

依赖/接口未生成、未 source、类型不一致、goal 拒绝或 cancel 未结束。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

三个最小包、custom interfaces、跨语言运行证据和构建故障记录。

另须创建或更新 `docs/modules/ROS-02/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

能独立建包和接口；C++/Python 通过同一接口通信；最小 Action 生命周期可运行和解释。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/ROS-02/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-TOOLS`：高级 CMake/Git/Linux；`DLC-ROS-RUNTIME`：callback group、composition、lifecycle/QoS 使用深化；`DLC-ROS-MIDDLEWARE`：executor 内部。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

跨语言通信、接口生成、Action 生命周期、CMake/ament 最小职责；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/ROS-02/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
