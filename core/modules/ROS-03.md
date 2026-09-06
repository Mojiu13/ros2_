# ROS-03｜Launch、Parameter、YAML、Namespace 与 Remap

> CORE TO APPLY · 工作量 M

## Core Skill

掌握真实 ROS 工作中高频的启动与配置能力。

## Prerequisites

ROS-02

## Starting Environment

使用 ENV-01 已验收的稳定 `ros2-dev`。环境定义通常不再演化；出现证据明确的环境阻塞时才回看 ENV-01 或记录相应 DLC_REF。

## Required Supporting Knowledge

- node name、topic name、namespace，以及 relative/absolute name 的最低直觉。
- remap 改变连接名称；parameter 配置节点行为；YAML 是配置载体；launch 负责启动和组合系统。
- launch directory install 与 config directory install：在首次创建这些目录时理解 `install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})` 和 `install(DIRECTORY config DESTINATION share/${PROJECT_NAME})`。
- ROS 从 install space 查找已安装的 launch/config；修改后必须重新构建并 source 正确 overlay，才能验证新文件。
- 用 CLI 验证最终名称与参数值，不能以“文件写了”代替生效证据。

这些内容属于 CORE Supporting Knowledge：首次出现时必须解释、实践并检查理解，不能因为它们不是 ROS/机器人主技能就跳到 DLC。

## Core Practice

用 launch 启动多个节点；从 YAML 加载参数；为 launch/config 添加真实的 directory install rules；重新构建并 source overlay；修改 namespace/remap；用 CLI 证明最终节点、接口和参数；修复一次配置错误。

## Minimum Theory

讲到能预测并验证最终 node/topic/parameter 名称，并理解 launch/config 为何必须安装到 install space；不推演名称解析内部规则或提前扩展高级 CMake。

## Fault / Debug

YAML 层级、参数未加载、namespace/remap 或 launch 安装错误。

使用 baseline → symptom → observation → layer → hypothesis → verification → root cause → fix → regression 记录证据；一次只改一个变量。

## Deliverables

launch/config 示例、配置观察表、故障记录。

另须创建或更新 `docs/modules/ROS-03/MODULE_REPORT.md`，内容来自真实实践，不得预造证据。

## Exit Criteria

不改业务代码即可调整参数和连接；能证明配置实际生效。

还必须能无提示解释本模块的 Required Supporting Knowledge，并满足下方完成记录与模块面试要求。

## Completion Record（强制）

标记 `Completed` 前必须同时满足：

1. 完成 Core Practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 写入 `docs/modules/ROS-03/MODULE_REPORT.md`；
4. 完成 CORE 模块面试；
5. 更新 `LEARNING_STATUS.md`，并为本模块形成一次范围合理、可解释的 Git commit。

缺少任一项只能保持 `In Progress`。

## DLC Extensions

`DLC-TOOLS`：高级 CMake/配置工程；`DLC-ROS-RUNTIME`：大型 launch、composition、lifecycle/QoS。

DLC 只保存不影响当前 CORE 继续的深化内容。Required Supporting Knowledge 即使属于工具、数学、测试或文档，也不得锁进 DLC。只有学习者明确说“进入 <DLC_ID>”才展开对应 DLC。

## Interview Scope

参数加载、namespace/remap、launch 成功但行为错误的排查；并检查 Required Supporting Knowledge 是否能用于解释现象和排错。不得追问本模块列出的 DLC 内部原理。

## New Chat Resume

读取 `README.md`、`LEARNING_STATUS.md`、`core/CORE_INDEX.md`、`core/EMBEDDED_SKILLS.md`、本文件、所有 prerequisite reports、当前 `docs/modules/ROS-03/MODULE_REPORT.md`（若已存在）、`projects/PROJECTS.md`、相关项目真实 README/evidence、`prompts/TEACHING_PROTOCOL.md` 和 `prompts/MODULE_INTERVIEW_RULES.md`；不得依赖上一聊天记忆。
