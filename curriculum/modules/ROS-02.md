# ROS-02｜Python 与 C++ ROS 包最小工程

> Phase 0 · P0 · 工作量 M

## 为什么学习

岗位同时要求 C++ 与 Python，rclcpp 必须早期进入而不是放到路线末尾。

## Prerequisites

ROS-01

## 环境要求

ament_python 与 ament_cmake 可用

## 开始时检查

读取 ROS-01 产物；确认两种构建类型可用。

## 核心实践任务

各建一个最小包；实现同一 pub/sub 小闭环；维护 package.xml、CMakeLists.txt/setup.py；构建、运行并对照差异。

## 最小理论

包、可执行文件、依赖声明、编译型与解释型包的边界。

## 故障注入

缺依赖、头文件找不到、entry point 错、未安装 launch/config、旧构建缓存。

## 输出文件 / Deliverables

cpp_basics 包；py_basics 包；构建故障记录；双语言对照笔记。

## Exit Criteria

能独立补依赖并修复常见构建错误；能解释两种包结构；两端通信可观察。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

## 模块面试范围

package.xml 与构建文件各负责什么；为什么 build 成功却 ros2 run 找不到。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

新对话先读取：`README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、本文件、所有 Prerequisites 的模块报告，以及本模块涉及项目的 README/设计/错误记录。不得假设记得上一聊天。
