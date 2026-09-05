# INT-01｜第一遍全链路集成验收

> Phase 1 · P0 · 工作量 M

## 为什么学习

把零散成功合成可重复系统，并在深入前确认每层边界。

## Prerequisites

MOVEIT-02

## 环境要求

自建模型、仿真、控制、MoveIt 全部可启动

## 开始时检查

逐项读取 Phase 1 产物；列出已知未解决问题。

## 核心实践任务

从干净终端启动全栈；执行 named/joint/pose 目标；采集计算图、TF、controller 和 action 证据；做一次分层故障定位。

## 最小理论

需求→节点→接口→配置→执行→反馈的端到端视角。

## 故障注入

从环境、launch、TF、MoveIt、controller 中随机选择一层注入单一故障。

## 输出文件 / Deliverables

Project A v1；系统地图 v2；集成验收报告；阶段面试记录。

## Exit Criteria

可重复启动和运行；能在限定排查树内定位单故障；全部 P0 证据齐全。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

从目标到关节运动的数据流；反馈如何回到应用；完整排查顺序。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
