# MODULE_TEACHING_PROMPT_TEMPLATE

把下面的 `<MODULE_ID>` 替换为课程编号，在全新的 ChatGPT 对话中使用。

~~~text
请连接并读取 GitHub 仓库 Mojiu13/ros2_。

我要学习的模块是：<MODULE_ID>。

开始教学前必须依次读取：
1. README.md；
2. LEARNING_STATUS.md；
3. curriculum/CURRICULUM_INDEX.md；
4. curriculum/modules/<MODULE_ID>.md；
5. 该模块 Prerequisites 对应的模块报告和明确列出的项目文档；
6. prompts/TEACHING_PROTOCOL.md；
7. prompts/MODULE_INTERVIEW_RULES.md。

如果仓库证据与我口述冲突，以真实文件、命令输出和日志为准，并指出冲突。不要依赖其他聊天窗口的记忆。

严格以模块文件为边界：不要提前教学后续模块，不要扩展为百科课程，不要使用 ROS 1、Gazebo Classic 或与 Jazzy 不兼容的旧做法。版本不确定时先查 Jazzy 官方文档。

教学采用小步交互：每次只给一个可验证目标和少量命令/代码，说明预期观察点，然后等我贴真实输出；不得假定成功。发生错误时先归层、收集最小证据、提出一个最可能假设并验证，不要同时罗列十几种修复。

本模块必须完成运行、观察、修改、单一故障注入、定位、修复、回归、文档、复述和模块面试。先不要给标准面试答案。

现在先报告：读取了哪些文件、当前模块的目标/边界/Exit Criteria、开始前还缺哪些可验证前提。随后只给第一小步。
~~~
