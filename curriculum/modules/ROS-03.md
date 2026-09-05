# ROS-03｜Launch、Parameter、YAML、Namespace 与 Remap

> Phase 0 · P0 · 工作量 M

## 为什么学习

真实 ROS 工作大量发生在启动与配置层，必须尽早形成配置驱动能力。

## Prerequisites

ROS-02

## 环境要求

默认使用 ENV-01 验收通过的 Dockerized ROS2 Jazzy 环境；不假定 Host 安装 ROS。

如果本模块新增依赖，必须更新版本化环境定义、重建 image/container、验证并记录到 `docs/ENVIRONMENT_MANIFEST.md`。

两个基础包可运行## 开始时检查

先确认 Docker Engine、目标 image/container、宿主 source bind mount、ROS underlay、workspace overlay，以及 prerequisite 报告/项目证据。

读取双语言包结构和当前接口名。## 核心实践任务

统一 launch 多节点；从 YAML 加载参数；实验 namespace/remap；检查最终节点名、接口名和参数值。

## 最小理论

launch description、参数作用域、名称解析、配置与代码分离。

## 故障注入

YAML 层级错、参数未加载、namespace 重复、remap 指向错误、launch 文件未安装。

## 输出文件 / Deliverables

launch/config 示例；名称解析表；配置层排障卡。

## Exit Criteria

不改业务代码即可改变参数和连接关系；能证明配置是否真正生效。

除非上述证据、复述和模块面试都完成，否则不得标记 Completed。

如果为了本模块在 running container 中临时安装或修改依赖，但没有回写 Dockerfile/Compose/entrypoint 等版本化环境定义并重建验证，则模块不得 Completed。

## 模块面试范围

参数加载链；namespace 与 remap 的区别；launch 成功但节点行为不对怎么查。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

读取 `README.md`、`LEARNING_STATUS.md`、`curriculum/CURRICULUM_INDEX.md`、当前 module、prerequisite reports、`curriculum/DOCKER_FIRST_ARCHITECTURE.md`、`docs/ENVIRONMENT_MANIFEST.md`，以及当前项目真实 README/evidence。不得依赖上一聊天记忆。
