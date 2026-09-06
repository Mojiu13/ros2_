# ROS-01｜ROS 2 计算图、接口与 CLI

> CORE TO APPLY · 工作量 M

## Core Skill

先会观察 ROS 系统并为 topic/service/action 选择正确接口。

## Prerequisites

ENV-01

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- ROS graph 中 node 与 topic/service/action 两端的关系，以及用 CLI 观察而不是猜测。
- topic 适合持续数据流、service 适合短请求响应、action 适合可反馈/可取消的长任务。
- ROS 2 通信依赖 middleware/DDS；discovery 负责让端点彼此发现。
- `ROS_DOMAIN_ID`、localhost 与 container 网络边界可能影响发现；两个节点都运行不等于一定能发现彼此。
- `ps`、`pgrep`、`kill`、日志查看与 ROS CLI 的最低进程/证据检查方法。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

运行并观察 node、topic、service、action；查询接口类型、publisher/subscriber/server/client；用 CLI 发布、调用和发送最小 goal；画计算图。

## Minimum Theory

讲到能解释端点、接口选择与最低 discovery 失败；不进入 participant internals、RTPS、discovery protocol、vendor 实现或 QoS policy matrix。

## Fault / Debug

接口不存在、类型错误、server 缺失、ROS_DOMAIN_ID 不一致中的一个最小案例。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

计算图、接口选择表、CLI 速查和故障记录。

另须创建或更新 `docs/modules/ROS-01/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

能按需求选接口；能找到通信两端；能用 CLI 证明接口是否存在和工作。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/ROS-01/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-ROS-NETWORK`：跨主机/复杂容器网络与深入 discovery 排障；`DLC-ROS-MIDDLEWARE`：DDS/RTPS/vendor/executor 内部。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

topic/service/action 边界、ROS graph、发现失败的最低判断。；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/ROS-01/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
