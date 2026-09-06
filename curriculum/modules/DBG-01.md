# DBG-01｜Docker-to-Application 跨层故障注入与诊断

> Phase 3 · P0 · 工作量 L

## 为什么学习

建立覆盖容器环境到应用层的统一排障树，直接匹配机械臂应用岗位。

## Prerequisites

APP-02A

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

APP-02A 可控失败、Project A2/B 正常基线存在；一次只注入一个故障。

## 核心实践任务

保留 Host→Docker/container/user/mount→ROS environment→workspace→ROS graph→TF/model→Gazebo→ros2_control/controller→MoveIt→application 分层。复用 ENV-01 的一个 Docker 故障案例理解边界；新增故障训练主要覆盖未 source、package/build/launch、topic/action、TF/URDF/joint mismatch、inactive controller、planning/start state/execution/timeout 等 ROS 与机器人软件问题。

## 最小理论

分层诊断、控制变量、最小复现、证据链；Docker user/ownership、graphics 与 ROS 问题边界。

## 故障注入

不主动制造大量 Docker 故障。Docker 层最多复查一个已有案例；其余注入集中在 ROS graph、TF/model、Gazebo、ros2_control/controller、MoveIt 和 application，且一次只注入一个未知故障。

## 输出文件 / Deliverables

DEBUGGING_PLAYBOOK、ERROR_LOG、分层决策树、Application Gate 核心案例集。

## Exit Criteria

每个代表案例有正常基线、现象、观察、层级、假设验证、根因、修复和回归；主要案例来自 ROS 与机器人软件层，Docker 不喧宾夺主。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

完整排障层级；Docker 问题为何会伪装成 ROS；Plan vs Execute；joint mismatch 跨哪些层。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
