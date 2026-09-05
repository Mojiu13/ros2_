# ROS-01｜ROS 2 计算图、CLI、通信选择与容器网络

> Phase 0 · P0 · 工作量 M

## 为什么学习

在容器化环境中建立可观察 ROS 计算图，并理解网络命名空间如何影响 DDS discovery，而不提前深入 DDS 协议。

## Prerequisites

ENV-01

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定宿主安装 ROS。

## 开始时检查

读取 ENV-01 重建报告、Compose 网络配置与 ROS_DOMAIN_ID；确认 container 内基础节点可运行。

## 核心实践任务

观察 node/topic/service/action；完成最小通信与接口选择。至少做一次 Container A↔Container B 或 Host↔ROS Container 的 discovery/topic 实验，对比 bridge 与 host networking 的实际现象；检查 localhost、container namespace、ROS_DOMAIN_ID 和相同/不同 domain 的影响。

## 最小理论

节点与 topic/service/action；bridge/host network、localhost 作用域、DDS discovery 和 ROS_DOMAIN_ID 的最低限度。

## 故障注入

节点运行但彼此发现不了、ROS_DOMAIN_ID 不一致、只监听本地、错误把网络问题当节点代码问题。

## 输出文件 / Deliverables

通信地图、接口选择表、容器网络实验表、discovery 排障记录。

## Exit Criteria

能根据任务选择通信方式；能用证据区分节点、ROS graph 与 container network 问题；A/B 或 Host/container discovery 实验可重复。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。临时 container 修改未回写环境定义时也不得完成。

## 模块面试范围

topic/service/action 边界；localhost 在两个 container 中是否相同；ROS_DOMAIN_ID 的作用；发现失败怎么分层。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、本文件、prerequisite 报告、Docker 架构/环境记录以及相关项目文档；不得依赖其他聊天记忆。
