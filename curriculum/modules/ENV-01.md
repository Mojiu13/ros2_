# ENV-01｜ROS 工程环境与可复现工作区

> Phase 0 · P0 · 工作量 S

## 为什么学习

先建立可复现、可诊断的 ROS 工程工作方式，避免后续问题被环境污染。

## Prerequisites

C++/Python 基础

## 环境要求

Ubuntu 24.04；ROS 2 Jazzy；Git；编辑器

## 开始时检查

确认系统版本、ROS_DISTRO、shell 环境及仓库状态；不默认任何组件已安装。

## 核心实践任务

建立 workspace；理解 src/build/install/log；完成依赖声明、rosdep、colcon、source、Git 提交流程；使用常见 Linux 进程/文件/日志工具。

## 最小理论

overlay/underlay、环境变量、包依赖和构建产物的最小心智模型。

## 故障注入

未 source、包找不到、依赖缺失、旧 overlay 污染、构建失败。

## 输出文件 / Deliverables

环境基线记录；工作区说明；命令速查表；首条错误记录。

## Exit Criteria

能从干净终端解释并复现环境；能用证据区分安装、依赖、构建和 source 问题；产物已记录。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

source 的作用；四个工作区目录；rosdep 与 apt 的边界；如何定位 package not found。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
