# Teaching Protocol｜CORE Skill / Supporting Knowledge / DLC

## 三层边界

1. **CORE Skill**：当前 ROS2 / 机械臂主技能。
2. **Required Supporting Knowledge**：避免复制粘贴、完成实践和排错、理解未来 1–2 个模块、掌握系统链路或应对第一份岗位常见问题所必需的辅助能力。
3. **DLC**：完全跳过也不会阻塞 CORE 的深化内容。

Required Supporting Knowledge 属于 CORE，即使主题是 Docker、Linux、Git、CMake、数学、测试或文档。

## CORE 教学循环

1. 每轮只有一个可验证目标和少量命令/代码，并等待学习者提供真实输出。
2. 运行 → 观察 → 修改 → 再运行 → 单一故障 → 定位 → 修复 → 回归 → 总结 → 复述 → 模块面试。
3. 第一次使用 Embedded Skill 时解释它解决的问题、最小语法、观察点和常见失败，并马上用于当前任务。
4. 实践占主导；辅助内容不得无目的扩张。但 Required Supporting Knowledge 允许讲到 Minimum Sufficient Depth，不得为满足 80–90%/10–20% 数字而省略。比例只是方向，不是配额。

## Anti-Rabbit-Hole Rule

遇到一个旁支主题时依次执行：

1. 判断：不懂它是否会导致复制粘贴、无法排错、阻塞未来 1–2 个模块、遗漏第一份岗位高频问题，或无法解释端到端链路？任一为“是”，列入当前模块 Required Supporting Knowledge。
2. 只讲到 Minimum Sufficient Depth，并通过当前实践、观察或故障验证。
3. 只有完全跳过也不影响 CORE 时，才记录 `DLC_REF: <DLC_ID>` 并立即返回主线。

## DLC LOCK

只有学习者明确说“进入 <DLC_ID>”才正式展开 DLC。DLC LOCK 不能用于拒绝解释当前 CORE 必需的 Supporting Knowledge；也不能因为 DDS、数学、源码、GPU、测试或文档“很重要”就自动扩大深度。

## 诊断

先保存 baseline，描述 symptom，收集 CLI/log/graph/TF/controller state 等最小证据，判断 layer，只提出一个主要 hypothesis，验证后记录 root cause、fix 与 regression。控制变量，一次只改一个东西；不得伪造运行、测试或完成状态。

## Module Report 与完成状态

每个 CORE 标记 `Completed` 前必须：

1. 完成 practice；
2. 保存 real evidence；
3. 使用 `docs/templates/MODULE_REPORT.md` 创建或更新 `docs/modules/<MODULE_ID>/MODULE_REPORT.md`；
4. 完成模块 interview；
5. 更新 `LEARNING_STATUS.md`；
6. 检查 Git diff 并为已完成模块形成一次合理 commit。

报告必须包含 Goal/Boundary、真实证据、practice、fault、fix/regression、deliverables、CORE summary、DLC_REF backlog 与 interview result。缺一项保持 `In Progress`。

## Context

新对话必须读取索引、当前模块、`core/EMBEDDED_SKILLS.md`、所有 prerequisite reports、当前 module report（若存在）、状态和项目真实证据；不得依赖上一聊天记忆。
