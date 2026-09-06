# CORE_TEACHING_PROMPT_TEMPLATE

~~~text
请连接并读取 GitHub 仓库 Mojiu13/ros2_。

我要学习的 CORE 模块是：<MODULE_ID>。

请读取 README.md、LEARNING_STATUS.md、core/CORE_INDEX.md、core/modules/<MODULE_ID>.md、prerequisite reports、projects/PROJECTS.md、相关项目真实 README/evidence、prompts/TEACHING_PROTOCOL.md 和 prompts/MODULE_INTERVIEW_RULES.md。

严格遵守 Anti-Rabbit-Hole Rule 和 DLC LOCK：辅助知识只给继续当前任务所需的最小解释；值得深入则标记 DLC_REF；立即返回 CORE。除非它确实阻塞当前模块，或我明确说“进入 DLC-XXX”，否则不要展开 DLC。

至少 80–90% 注意力用于当前 ROS/机械臂实践。Docker、Linux、Git、CMake、网络、GPU、测试理论和文档理论不得抢走主线。

每次只给一个可验证目标和少量命令/代码，说明观察点，等我贴真实输出。错误先归层、收集证据、验证一个主要假设。

模块面试只考 CORE，不考 DLC。先报告目标、边界、Exit Criteria 和 DLC_REF，然后只给第一小步。
~~~
