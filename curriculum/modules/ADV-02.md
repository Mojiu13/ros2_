# ADV-02｜最小自定义 ros2_control Controller

> Advanced Optional · P2 · 工作量 XL

## 为什么学习

展示框架接入理解，适合偏控制框架岗位。

## Prerequisites

ADV-01

## 环境要求

mock/fake hardware

## 开始时检查

确认目标岗位确实受益；不加入复杂控制算法。

## 核心实践任务

实现 ControllerInterface 生命周期、接口声明、pluginlib 导出、加载激活与 mock 测试。

## 最小理论

插件发现、接口 claim、实时 update 最小约束。

## 故障注入

插件找不到、接口不匹配、activate 失败、非实时操作进入 update。

## 输出文件 / Deliverables

custom_controller 包；测试；设计说明。

## Exit Criteria

可构建、加载、激活、读 state/写 command；异常路径可验证。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

controller_manager 如何发现插件；生命周期回调职责。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
