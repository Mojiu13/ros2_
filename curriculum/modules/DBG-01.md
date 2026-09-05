# DBG-01｜Docker-to-Application 跨层故障注入与诊断

> Phase 3 · P0 · 工作量 L

## 为什么学习

建立覆盖容器环境到应用层的统一排障树，直接匹配机械臂应用岗位。

## Prerequisites

APP-02A

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定宿主安装 ROS。

## 开始时检查

APP-02A 可控失败、Project A2/B 正常基线存在；一次只注入一个故障。

## 核心实践任务

按 Host OS→Docker Engine→container/image/mount/network→ROS installation/environment→workspace/build/install→launch/config→ROS graph→TF/model→Gazebo→ros2_control→controller→MoveIt→application 分层。覆盖未 source、包/build/launch、discovery、GUI/GPU、TF/URDF/joint mismatch、inactive controller、action missing、planning/start state/execution/timeout/mismatch。

## 最小理论

分层诊断、控制变量、最小复现、证据链；Docker/graphics 与 ROS 问题边界。

## 故障注入

本模块即系统化注入；禁止同时叠加未知故障。

## 输出文件 / Deliverables

DEBUGGING_PLAYBOOK、ERROR_LOG、分层决策树、Application Gate 核心案例集。

## Exit Criteria

每个代表案例有正常基线、现象、观察、层级、假设验证、根因、修复和回归；至少覆盖 Gate 要求的五个故障族。

除非证据、复述和模块面试全部完成，否则不得标记 Completed。临时 container 修改未回写环境定义时也不得完成。

## 模块面试范围

完整排障层级；Docker 问题为何会伪装成 ROS；Plan vs Execute；joint mismatch 跨哪些层。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、本文件、prerequisite 报告、Docker 架构/环境记录以及相关项目文档；不得依赖其他聊天记忆。
