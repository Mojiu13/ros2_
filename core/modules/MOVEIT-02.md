# MOVEIT-02｜A2 C++ / Python 编程规划执行

> CORE TO APPLY · 工作量 L

## 为什么在 CORE

把 GUI 成功转换为能形成项目证据的应用代码。

## Prerequisites

MOVEIT-01

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

C++ 实现 named/joint/pose 的 plan→inspect→execute；Python 作为 client/tool；记录成功/失败、耗时和错误层；检查 start state、frame、joint limits 与空轨迹。

## 最小理论

MoveIt API、goal constraints、RobotTrajectory 只讲调用和错误处理所需内容。

## 故障注入

current state 超时、frame_id、unreachable、空轨迹或 execution server 缺失中的代表案例。

## Deliverables

C++ 规划节点、Python tool/client、运行证据和错误记录。

## Exit Criteria

至少两类目标稳定，第三类有明确失败语义；规划/执行不混淆。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-MOVEIT；DLC_REF: DLC-MOVEIT-INTERNALS

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

编程 plan/execute、start/goal、返回值和 C++/Python 分工。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
