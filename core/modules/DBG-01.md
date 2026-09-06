# DBG-01｜五类高频故障核心包

> CORE TO APPLY · 工作量 M

## 为什么在 CORE

用最小案例覆盖第一份机械臂岗位最常见的排错场景。

## Prerequisites

APP-02A

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

每类至少一个代表案例：① build/source/package/launch；② TF/frame/URDF/joint name；③ controller inactive/action missing；④ MoveIt planning/start state/unreachable；⑤ execution/timeout/application error。每例遵循现象→观察→层级→假设→验证→根因→修复→回归。

## 最小理论

分层诊断、控制变量和最小证据链。Docker/network/GUI 只需判断可能属于环境层。

## 故障注入

本模块即五类代表故障；不制造几十个案例或多层复合故障。

## Deliverables

五个 ERROR_LOG 条目、核心决策树、2–3 个可讲述的 debugging 故事候选。

## Exit Criteria

五类各至少一例且证据完整；能区分 planning/execution/controller/model/application。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

环境/网络/graphics/复合/性能问题分别 DLC_REF: DLC-ENV-ADV、DLC-ROS-NETWORK、DLC-SIM-GRAPHICS、DLC-DEBUG

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

五类排查顺序和真实证据，不考深层内部。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
