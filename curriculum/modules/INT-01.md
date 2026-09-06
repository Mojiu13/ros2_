# INT-01｜6/7 DOF 全链路集成验收

> Phase 1 · P0 · 工作量 M

## 为什么学习

把 A2 的成熟 6/7 DOF 模型、Docker、Gazebo、ros2_control、MoveIt 与代码组合成最低工程基线。

## Prerequisites

MOVEIT-02

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

A1 学习证据完整；A2 的版本、模型、controller、MoveIt 配置与 Docker 环境均有基线。

## 核心实践任务

从新建 container/干净 workspace 构建并启动 A2；执行 named/joint/pose；采集 container/mount/network、计算图、TF、controller、action、规划/执行/反馈证据；完成一次分层故障定位。

## 最小理论

Host→container→ROS→model→planning→trajectory→controller→simulated robot→feedback 的端到端边界。

## 故障注入

从 Docker network/mount、TF、MoveIt、controller、application 中选择一个单一故障。

## 输出文件 / Deliverables

Project A2 v1、系统地图 v2、集成验收报告、最小可复现 README、阶段面试。

## Exit Criteria

删除/重建 container 后 A2 仍可重复；6/7 DOF 全链路运行；能定位单故障。最终求职集成证据明确来自 A2。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

从目标到 6/7 DOF 运动的数据流；Docker 对链路的影响；Plan/Execute 和反馈边界。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
