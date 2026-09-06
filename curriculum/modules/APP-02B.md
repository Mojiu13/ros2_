# APP-02B｜Retry、Replan 与有限恢复

> Phase 3 · P1 · 工作量 L

## 为什么学习

Standard Track 增加有限、可解释的恢复，而不是让恢复逻辑掩盖根因。

## Prerequisites

APP-02A, DBG-01

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

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

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

哪些错误能 retry/replan；恢复预算；如何避免掩盖根因；safe termination 的项目边界。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
