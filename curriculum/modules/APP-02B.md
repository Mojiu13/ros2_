# APP-02B｜Retry、Replan 与有限恢复

> Phase 3 · P1 · 工作量 L

## 为什么学习

Standard Track 增加有限、可解释的恢复，而不是让恢复逻辑掩盖根因。

## Prerequisites

APP-02A, DBG-01

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。

如果本模块新增依赖，必须更新版本化环境定义、重建 image/container、验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。

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

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

哪些错误能 retry/replan；恢复预算；如何避免掩盖根因；safe termination 的项目边界。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
