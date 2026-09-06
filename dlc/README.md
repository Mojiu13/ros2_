# DLC｜非阻塞深化扩展

DLC 只保存“当前不需要掌握”的深化知识。它们完全跳过也不会阻塞 CORE completion、Application Gate 或投递，不是以后必须全部补完的第二套课程。

**Required Supporting Knowledge 不属于 DLC，即使它不是 ROS / 机器人主技能。**

边界示例：

- CMake basics = CORE Supporting Knowledge；advanced CMake = DLC。
- quaternion usage = CORE Supporting Knowledge；quaternion algebra = DLC。
- controller lifecycle = CORE Supporting Knowledge；controller realtime internals = DLC。
- expected/actual test case = CORE Supporting Knowledge；full automated test architecture = DLC。

## DLC LOCK

当前学习 CORE 时，Assistant 应先完成模块列出的 Required Supporting Knowledge。遇到真正非阻塞的深化内容，只记录 `DLC_REF: <DLC_ID>` 并返回主线。只有学习者明确说“进入 <DLC_ID>”才正式开始。

每个 DLC 还必须满足自己的 Trigger Conditions。没有真实问题、岗位需求或明确兴趣时，保持锁定。

## 等级

- DLC-A：CORE 完成后优先考虑的高价值扩展。
- DLC-B：按岗位、项目或真实问题选择。
- DLC-C：源码、数学或框架深度；通常只对特定岗位有价值。

DLC 有独立 deliverables 与面试，不得把其深度问题加入 CORE 面试或 Gate。
