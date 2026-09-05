# MOVEIT-01｜SRDF、MoveIt 配置与 RViz 规划执行

> Phase 1 · P0 · 工作量 L

## 为什么学习

建立自己模型的规划组、运动学、限制和 controller 映射。

## Prerequisites

CTRL-02

## 环境要求

MoveIt 2 Jazzy

## 开始时检查

确认直接轨迹闭环可用，避免把控制层故障误判为 MoveIt。

## 核心实践任务

生成/维护 SRDF 与 MoveIt config；定义 planning group/named state/end effector；在 RViz Plan/Execute；核对 kinematics、joint limits、controllers。

## 最小理论

URDF 与 SRDF；RobotModel、planning group、MoveIt controller mapping；IK 只讲使用边界。

## 故障注入

planning group 空、kinematics 缺失、controller mapping 错、不可达目标、碰撞目标。

## 输出文件 / Deliverables

moveit_config 包；配置映射表；Plan/Execute 证据。

## Exit Criteria

自建机械臂可在 RViz 规划执行；能区分配置、规划和执行失败。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

SRDF 解决什么；MoveIt 如何选 controller；Plan 成功 Execute 失败怎么查。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
