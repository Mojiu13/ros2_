# APP-01B｜MoveIt TaskNode 与基本状态机

> CORE TO APPLY · 工作量 L

## 为什么在 CORE

形成可展示的机械臂应用层项目，而不是停留在官方 demo。

## Prerequisites

APP-01A

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

接入 MoveIt；支持 named/joint/pose；完成 planning、execution、feedback、result 和 RECEIVED/VALIDATING/PLANNING/EXECUTING/终态的基本状态机；分离 planning/execution error。

## 最小理论

任务层与 MoveIt/controller 边界、状态机与错误映射最低直觉。

## 故障注入

非法目标、规划失败、执行失败或 controller unavailable 中代表案例。

## Deliverables

Project B v1、状态图、执行流和需求实现对照。

## Exit Criteria

三类目标可用或有明确失败；反馈/结果/状态一致；不实现复杂 recovery。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-APP-RECOVERY

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

TaskNode 边界、状态机、错误分层。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
