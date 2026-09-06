# APP-01B｜MoveIt TaskNode 与最小状态机

> Phase 3 · P0 · 工作量 L

## 为什么学习

在已冻结接口上接入 MoveIt，形成可展示但边界清晰的 TaskNode v1。

## Prerequisites

APP-01A

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

APP-01A 的 REQUIREMENTS、接口和骨架已评审；A2 编程规划执行回归通过。

## 核心实践任务

C++ TaskNode 支持 named/joint/pose target；调用 MoveIt planning/execution；明确 planning 与 execution error；发布真实 feedback/result；实现 RECEIVED/VALIDATING/PLANNING/EXECUTING/SUCCEEDED/FAILED 最小状态机。Python client 覆盖三类请求。

## 最小理论

任务层与运动层边界、最小状态机、下游错误映射；本模块暂不实现 timeout/cancel/retry。

## 故障注入

非法目标、无 IK/规划失败、执行失败、controller unavailable；检查状态和结果是否一致。

## 输出文件 / Deliverables

TaskNode v1、state diagram、execution flow、Project B v1、需求实现追踪更新。

## Exit Criteria

三类目标按需求工作或给出正确失败；planning/execution 不混淆；feedback/result 与状态一致；单模块规模可在一个对话完成。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

TaskNode 为什么不直接控制 controller；状态机；错误分层；相比 MoveIt demo 增加了什么。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
