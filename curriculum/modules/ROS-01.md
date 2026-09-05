# ROS-01｜ROS 2 计算图、CLI 与通信选择

> Phase 0 · P0 · 工作量 M

## 为什么学习

机械臂系统首先是一组可观察的节点与接口，必须先会看图、选接口、定位连接问题。

## Prerequisites

ENV-01

## 环境要求

Jazzy 基础示例可运行

## 开始时检查

读取 ENV-01 报告与环境基线；确认当前 workspace。

## 核心实践任务

观察 node/topic/service/action；用 CLI 检查类型、发布者、订阅者与 action server；完成最小 topic/service/action 交互。

## 最小理论

节点、消息、请求响应、长任务反馈/取消；机械臂轨迹为何适合 action；QoS 只讲当前实验所需。

## 故障注入

topic 不存在、类型不匹配、action server 缺失、命名错误。

## 输出文件 / Deliverables

通信地图；接口选择表；CLI 观察记录；错误条目。

## Exit Criteria

能根据需求选择 topic/service/action；能沿计算图找到接口两端；模块面试通过。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

三类通信边界；action 五个角色；接口不存在时的证据链。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
