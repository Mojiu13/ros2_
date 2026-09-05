# MODULE_TEACHING_PROMPT_TEMPLATE

把 `<MODULE_ID>` 替换为课程编号，在全新 ChatGPT 对话中使用。

~~~text
请连接并读取 GitHub 仓库 Mojiu13/ros2_。

我要学习的模块是：<MODULE_ID>。

开始前读取 README、LEARNING_STATUS、CURRICULUM_INDEX、当前 module、prerequisite reports、DOCKER_FIRST_ARCHITECTURE、ENVIRONMENT_MANIFEST、当前项目真实 README/evidence、TEACHING_PROTOCOL 和 MODULE_INTERVIEW_RULES。不要依赖上一聊天记忆。

默认是 Ubuntu 24.04 Host + 单个主 ros2-dev container，不假定 Host 安装 ROS。先检查 Docker Engine、目标 image/container、non-root user/UID/GID、source mount、ROS underlay、workspace overlay 和 prerequisite evidence；只检查本模块真正需要的额外层。

依赖 Just-In-Time 加入：ENV 只建 ROS base；ROS 模块加基础/interface 开发；SYS 按需加参考 runtime/RViz；SIM 加 Gazebo/ros_gz/graphics；CTRL 加 ros2_control；MOVEIT 加 MoveIt development dependencies。任何临时 container 安装最终必须回写环境定义、重建并更新 ENVIRONMENT_MANIFEST。

GUI/GPU 只在对应模块处理。Native Fallback 必须有已验证限制、理由和环境差异。版本敏感步骤查当前官方文档。

命令执行位置容易混淆时，用 `[HOST]` 或 `[CONTAINER]` 标明。不要把 Docker/user/permissions/graphics 问题误判为 ROS 问题。

每轮只给一个可验证目标和少量命令/代码，说明观察点，等我贴真实输出；错误先归层、收集证据、验证一个主要假设。

完成运行、观察、修改、单一故障注入、修复、回归、文档、复述和模块面试；先不提供标准面试答案。

现在先报告读取文件、模块目标/边界/Exit Criteria和缺少的前提，然后只给第一小步。
~~~
