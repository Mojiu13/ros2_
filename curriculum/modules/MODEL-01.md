# MODEL-01｜最小机械臂 URDF、TF 与 RViz

> Phase 1 · P0 · 工作量 M

## 为什么学习

岗位要求能创建、修改和调试模型，而不是只会使用现成 URDF。

## Prerequisites

SYS-01

## 环境要求

RViz2、robot_state_publisher

## 开始时检查

读取系统地图；明确本模块只做模型显示链。

## 核心实践任务

从零建立 2–3 自由度模型；配置 link/joint/origin/axis/limit/visual；发布 joint state 与 TF；在 RViz 检查。

## 最小理论

树结构、坐标变换、固定/旋转关节、模型描述与运行时状态的区别。

## 故障注入

断 TF、错误 parent/child、axis/origin 错、fixed frame 错、URDF 解析失败。

## 输出文件 / Deliverables

最小 URDF；显示 launch；TF 图；模型故障记录。

## Exit Criteria

能预测修改 origin/axis 后的现象；TF 树完整；无意外断链；面试通过。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

URDF 与 TF 的关系；robot_state_publisher 与 joint_state_publisher 的区别。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
