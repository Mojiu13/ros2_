# SYS-01｜参考机械臂完整链路观察

> Phase 1 · P0 · 工作量 S

## 为什么学习

在自建系统前先看到完整终点，建立 RobotModel→MoveIt→Controller→RobotState 的全局地图。

## Prerequisites

ROS-03

## 环境要求

Jazzy 兼容的参考 MoveIt 配置可用

## 开始时检查

读取前四模块产物；确认参考 demo 的版本与来源。

## 核心实践任务

在 RViz 中完成一次规划执行；观察关键节点、TF、joint_states、MoveIt action 与 controller action；画出执行和反馈链。

## 最小理论

URDF/SRDF、move_group、planning pipeline、controller manager、hardware 的角色边界。

## 故障注入

隐藏一个关键节点或 action server，按层定位但不深入修复细节。

## 输出文件 / Deliverables

完整系统地图 v1；接口清单；观察证据。

## Exit Criteria

能用 3 分钟讲清规划、执行、反馈三条链；能指出 Plan 与 Execute 的边界。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

MoveIt 与 ros2_control 的关系；两个 controller manager 的区别；机械臂不动先分哪几层。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
