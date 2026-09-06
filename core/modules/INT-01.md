# INT-01｜6/7 DOF 完整系统集成

> CORE TO APPLY · 工作量 M

## 为什么在 CORE

从干净启动证明 A2 的模型、仿真、控制、规划和代码形成可重复系统。

## Prerequisites

MOVEIT-02

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

启动稳定 ros2-dev；从干净 workspace 运行 A2；执行 named/joint/pose；采集 node/TF/controller/action/trajectory/state feedback 证据；只做集成，不增加新理论。

## 最小理论

无新增理论；只复述端到端数据流和边界。

## 故障注入

随机选择一个已学层的单一故障并用已有方法定位。

## Deliverables

Project A2 v1、系统图 v2、集成验收报告和最小 README。

## Exit Criteria

6/7 DOF robot→simulated hardware→ros2_control→controller→MoveIt→C++/Python 可从干净启动完整运行。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

复杂多层故障 DLC_REF: DLC-DEBUG

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

完整数据流、Plan/Execute、反馈与分层定位。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
