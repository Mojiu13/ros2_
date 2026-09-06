# CORE_TEACHING_PROMPT_TEMPLATE

~~~text
请连接并读取 GitHub 仓库 Mojiu13/ros2_。

我要学习的 CORE 模块是：<MODULE_ID>。

请读取 README.md、LEARNING_STATUS.md、core/CORE_INDEX.md、core/EMBEDDED_SKILLS.md、core/modules/<MODULE_ID>.md、所有 prerequisite 的 docs/modules/<ID>/MODULE_REPORT.md、当前 docs/modules/<MODULE_ID>/MODULE_REPORT.md（若存在）、projects/PROJECTS.md、相关项目真实 README/evidence、prompts/TEACHING_PROTOCOL.md、docs/templates/MODULE_REPORT.md 和 prompts/MODULE_INTERVIEW_RULES.md。

先明确本模块的 Core Skill、Required Supporting Knowledge、Minimum Theory、Exit Criteria 和 DLC Extensions。Required Supporting Knowledge 属于 CORE：如果缺少它会导致复制粘贴、无法排错、阻塞未来 1–2 个模块、遗漏第一份岗位高频问题或无法解释系统链路，就必须在当前实践中教到 Minimum Sufficient Depth。

严格遵守 Anti-Rabbit-Hole Rule 和 DLC LOCK。只有完全跳过也不影响 CORE 的深化内容才标记 DLC_REF 并返回主线；除非我明确说“进入 DLC-XXX”，不要展开 DLC。DLC LOCK 不得阻止当前模块必需的辅助知识。

每次只给一个可验证目标和少量命令/代码，说明观察点，等我贴真实输出。错误按 baseline→symptom→observation→layer→hypothesis→verification→root cause→fix→regression 处理，一次只改变一个变量。

首次出现的 Linux、Git、CMake/ament、YAML、CLI/log 或基础调试能力必须结合当前任务解释和使用。实践占主导，但不得机械套用 80–90%/10–20% 配额删掉必要基础。

结束前执行模块面试，并使用 docs/templates/MODULE_REPORT.md 创建/更新 docs/modules/<MODULE_ID>/MODULE_REPORT.md。只有 practice + real evidence + report + interview 全部完成，才更新 LEARNING_STATUS.md 为 Completed，并形成一次合理 Git commit。

现在不要一次给出整个模块，也不要宣称任何未验证结果。先报告目标、边界、完成条件和可能的 DLC_REF，然后只给第一小步。
~~~
