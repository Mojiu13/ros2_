# ROS-03｜Launch、Parameter、YAML、Namespace 与 Remap

> CORE TO APPLY · 工作量 M

## 为什么在 CORE

掌握真实 ROS 工作中高频的启动与配置能力。

## Prerequisites

ROS-02

## 环境要求

使用 ENV-01 验收后的稳定 `ros2-dev`；正常情况下直接进入 ROS/机械臂任务。Docker、Linux、Git、CMake 只在当前步骤需要时解释最小部分。

## 开始时检查

读取 CORE_INDEX、本模块、prerequisite reports、LEARNING_STATUS、环境清单和当前项目真实证据；确认所需 node/package/配置基线。

## 核心实践

用 launch 启动多个节点；从 YAML 加载参数；修改 namespace/remap；用 CLI 证明最终节点、接口和参数；修复一次配置错误。

## 最小理论

launch、参数作用域和名称解析只讲写、改、查、排错所需直觉。

## 故障注入

YAML 层级、参数未加载、namespace/remap 或 launch 安装错误。

## Deliverables

launch/config 示例、配置观察表、故障记录。

## Exit Criteria

不改业务代码即可调整参数和连接；能证明配置实际生效。

## Anti-Rabbit-Hole

至少 80–90% 注意力留给当前任务。辅助知识只给继续实践所需的最小解释；值得深入时记录下列 DLC_REF 并立即返回主线：

DLC_REF: DLC-TOOLS；DLC_REF: DLC-ROS-RUNTIME

除非主题确实阻塞 CORE，或学习者明确说“进入 <DLC_ID>”，否则不得展开 DLC。

## 模块面试范围

参数加载、namespace/remap、launch 成功但行为错误的排查。

CORE 面试不得追问对应 DLC 的内部原理。

## 新对话恢复

读取 README、LEARNING_STATUS、core/CORE_INDEX.md、本文件、prerequisite reports、projects/PROJECTS.md、相关项目 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md；不得依赖上一聊天记忆。
