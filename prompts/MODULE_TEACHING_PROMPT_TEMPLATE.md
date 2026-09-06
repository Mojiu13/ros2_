# MODULE_TEACHING_PROMPT_TEMPLATE

把 `<MODULE_ID>` 替换为课程编号，在全新 ChatGPT 对话中使用。

~~~text
请连接并读取 GitHub 仓库 Mojiu13/ros2_。

我要学习的模块是：<MODULE_ID>。

开始前读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、DOCKER_FIRST_ARCHITECTURE、ENVIRONMENT_MANIFEST、当前项目真实 README/evidence、TEACHING_PROTOCOL 和 MODULE_INTERVIEW_RULES。不要依赖上一聊天记忆。

默认 ENV-01 已经一次构建完整、稳定的 ros2-dev image，包含课程主线软件。除 ENV-01 外，不要把 Docker 当作当前模块的学习对象。

正常情况下只需要：在 [HOST] 启动既有 Compose 环境；进入 [CONTAINER]；确认 source mount、ROS/workspace overlay 和本模块 package；然后直接开始 ROS/机器人内容。

只有 container 无法启动、mount/UID/GID、GUI、缺包、环境污染、版本冲突或新增项目特定依赖时才讨论 Docker。实际改变环境时，必须更新版本化定义、重建并更新 ENVIRONMENT_MANIFEST。

Just-In-Time 只针对知识：即使软件已安装，也不要提前讲 Gazebo、ros2_control、MoveIt、TF、DDS 或规划原理。版本敏感步骤查询当前官方文档。

命令位置容易混淆时标明 [HOST] / [CONTAINER]。每轮只给一个可验证目标和少量命令/代码，说明观察点，等我贴真实输出；错误先归层并验证一个主要假设。

完成运行、观察、修改、单一故障注入、修复、回归、文档、复述和模块面试；先不提供标准面试答案。

现在先报告读取文件、模块目标/边界/Exit Criteria和缺少的前提，然后只给第一小步。
~~~
