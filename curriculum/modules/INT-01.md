# INT-01｜6/7 DOF 全链路集成验收

> Phase 1 · P0 · 工作量 M

## 为什么学习

把 A2 的成熟 6/7 DOF 模型、Docker、Gazebo、ros2_control、MoveIt 与代码组合成最低工程基线。

## Prerequisites

MOVEIT-02

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定宿主安装 ROS。

## 开始时检查

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

除非证据、复述和模块面试全部完成，否则不得标记 Completed。临时 container 修改未回写环境定义时也不得完成。

## 模块面试范围

从目标到 6/7 DOF 运动的数据流；Docker 对链路的影响；Plan/Execute 和反馈边界。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、本文件、prerequisite 报告、Docker 架构/环境记录以及相关项目文档；不得依赖其他聊天记忆。
