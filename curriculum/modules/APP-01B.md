# APP-01B｜MoveIt TaskNode 与最小状态机

> Phase 3 · P0 · 工作量 L

## 为什么学习

在已冻结接口上接入 MoveIt，形成可展示但边界清晰的 TaskNode v1。

## Prerequisites

APP-01A

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。

如果本模块新增依赖，必须更新版本化环境定义、重建 image/container、验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。

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

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

TaskNode 为什么不直接控制 controller；状态机；错误分层；相比 MoveIt demo 增加了什么。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
