# APP-02A｜Cancel、Timeout 与明确错误传播

> CORE TO APPLY · 工作量 M

## 为什么在 CORE

让 TaskNode 在失败路径上也能正确结束，这是 Action 应用最低可靠性。

## Prerequisites

APP-01B

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

实现 cancel acceptance/rejection、timeout、invalid input、planning failure、execution failure、controller/action unavailable 和明确 final result；处理 client interruption。

## 最小理论

terminal state、deadline/timeout、cancel 与 stop、错误保真；不做 retry/replan/recovery。

## 故障注入

分别选择 cancel、timeout 和下游不可用做代表验证。

## Deliverables

Project B v1.1、错误矩阵、取消/超时时序与运行证据。

## Exit Criteria

每个任务唯一终态；不无限等待；错误来源可判断；无 retry/recovery 依赖。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-APP-RECOVERY

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

cancel、timeout、下游错误传播和终态。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
