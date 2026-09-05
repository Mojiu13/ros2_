# CTRL-02｜绕过 MoveIt 直接执行 JointTrajectory

> Phase 1 · P0 · 工作量 M

## 为什么学习

亲手证明 trajectory 是 MoveIt 与控制层的契约，避免把 MoveIt 误认为直接驱动硬件。

## Prerequisites

CTRL-01

## 环境要求

轨迹 controller active

## 开始时检查

读取接口地图；核对关节顺序、限制和 action 名。

## 核心实践任务

检查 FollowJointTrajectory；直接发送合法多点轨迹；观察 goal/feedback/result 与 joint_states；比较 time_from_start 和关节顺序。

## 最小理论

JointTrajectory 数据结构、action 生命周期、容差和时间语义。

## 故障注入

joint name mismatch、时间不递增、超限目标、action server missing、容差 abort。

## 输出文件 / Deliverables

直接控制示例；轨迹字段注释；执行故障矩阵。

## Exit Criteria

不经过 MoveIt 可驱动仿真机械臂；能从 result 区分拒绝、取消、超时和 abort。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

FollowJointTrajectory 是什么；time_from_start 的意义；MoveIt 是否必需。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
