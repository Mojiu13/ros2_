# ROS-01｜ROS 2 计算图、接口与 CLI

> CORE TO APPLY · 工作量 M

## 为什么在 CORE

先会观察 ROS 系统并为 topic/service/action 选择正确接口。

## Prerequisites

ENV-01

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

运行并观察 node、topic、service、action；查询接口类型、publisher/subscriber/server/client；用 CLI 发布、调用和发送最小 goal；画计算图。

## 最小理论

ROS graph、node、interface type、topic/service/action；只知道 ROS_DOMAIN_ID、localhost/container 边界和 DDS discovery 可能影响发现。

## 故障注入

接口不存在、类型错误、server 缺失、ROS_DOMAIN_ID 不一致中的一个最小案例。

## Deliverables

计算图、接口选择表、CLI 速查和故障记录。

## Exit Criteria

能按需求选接口；能找到通信两端；能用 CLI 证明接口是否存在和工作。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-ROS-NETWORK；DLC_REF: DLC-ROS-MIDDLEWARE

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

topic/service/action 边界、ROS graph、发现失败的最低判断。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
