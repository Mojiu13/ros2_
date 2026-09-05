# APP-02B｜Retry、Replan 与有限恢复

> Phase 3 · P1 · 工作量 L

## 为什么学习

Standard Track 增加有限、可解释的恢复，而不是让恢复逻辑掩盖根因。

## Prerequisites

APP-02A, DBG-01

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定宿主安装 ROS。

## 开始时检查

APP-02A 错误语义稳定；DBG-01 已有根因分类；列出 retryable/non-retryable 表。

## 核心实践任务

实现 readiness check、有限 retry、replan、recovery policy/budget 和 safe termination；为每类策略绑定明确前置条件、次数、退避与最终结果。

## 最小理论

幂等、恢复预算、retryable 分类、replan 与重复执行差异、安全终止；不宣称真实硬件安全认证。

## 故障注入

可暂态恢复的 server readiness、不可达目标、持续 controller failure、重复失败；验证预算耗尽。

## 输出文件 / Deliverables

Project B v2、recovery policy、预算/时序图、测试与需求追踪更新。

## Exit Criteria

无无限 retry；非 retryable 不重试；预算耗尽明确终止；恢复日志保留原始 root cause。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。临时 container 修改未回写环境定义时也不得完成。

## 模块面试范围

哪些错误能 retry/replan；恢复预算；如何避免掩盖根因；safe termination 的项目边界。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、本文件、prerequisite 报告、Docker 架构/环境记录以及相关项目文档；不得依赖其他聊天记忆。
