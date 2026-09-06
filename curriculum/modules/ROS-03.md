# ROS-03｜Launch、Parameter、YAML、Namespace 与 Remap

> Phase 0 · P0 · 工作量 M

## 为什么学习

真实 ROS 工作大量发生在启动与配置层，必须尽早形成配置驱动能力。

## Prerequisites

ROS-02

## 环境要求

默认使用 ENV-01 已构建并验收的完整 `ros2-dev` image；不假定 Host 安装 ROS。正常情况下只启动主 development container、进入容器并确认本模块所需 package 可用，然后直接开始 ROS/机器人软件学习。只有实际缺包、版本冲突或新增项目特定依赖时才修改环境定义、重建并更新 `docs/ENVIRONMENT_MANIFEST.md`。

## 开始时检查

[HOST] 如主环境未运行，启动既有 Compose 项目。[CONTAINER] 确认 workspace/source mount、ROS underlay、workspace overlay和本模块 prerequisite evidence；检查本模块所需 package 可用。环境正常时不重新审计 Docker。

读取双语言包结构和当前接口名。

## 核心实践任务

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

如果实际修改了运行环境，或为诊断在 running container 中临时安装了依赖，必须回写 Dockerfile/Compose/entrypoint、重建验证并更新 `docs/ENVIRONMENT_MANIFEST.md`；否则模块不得 Completed。

## 模块面试范围

参数加载链；namespace 与 remap 的区别；launch 成功但节点行为不对怎么查。

面试必须遵守 `prompts/MODULE_INTERVIEW_RULES.md`：先提问，后评价，再复述，最后才整理标准答案。

## 新对话上下文恢复

读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、Docker architecture、ENVIRONMENT_MANIFEST 和当前项目真实 README/evidence。ENV-01 完成后默认环境稳定；除非出现容器、权限、GUI、缺包、污染或版本冲突，不重新展开 Docker 教学。
