# ROS2 机械臂应用开发｜CORE + DLC 学习仓库

唯一目标：让具备 C++/Python 基础、ROS/机器人接近零基础的学习者，尽快达到第一份 ROS2 机械臂应用开发岗位的可项目、可排错、可面试水平。

## 两个系统

- **CORE**：不学就会阻止完整机械臂项目继续推进的最短主线。
- **DLC**：计划外扩展包；不影响 CORE completion、Application Gate 或开始投递。

不再使用 P0/P1/P2/Advanced 作为学习主树，也不存在“Standard Track 没完成所以不能投”的逻辑。

## CORE 成功链

~~~text
完整开发环境
→ ROS2 graph / communication / programming
→ Launch / YAML / Parameter
→ 参观完整 6/7 DOF 系统
→ MiniArm URDF / TF / RViz
→ Gazebo
→ ros2_control
→ Direct FollowJointTrajectory + A2 controller baseline
→ MoveIt2 RViz + programming
→ 6/7 DOF integration
→ TaskNode
→ Cancel / Timeout / Error
→ 五类高频故障
→ 最低测试与文档交付
→ Application Gate
→ 立即投递
~~~

## Anti-Rabbit-Hole Rule

遇到辅助知识时：

1. 只解释继续当前实践所需的最小知识。
2. 值得深入则标记 `DLC_REF: <DLC_ID>`。
3. 立即返回当前 CORE。

除非辅助主题确实阻塞主线，或学习者明确说“进入 DLC-XXX”，否则不得展开 DLC。CORE 中至少 80–90% 注意力用于当前 ROS/机械臂任务，辅助知识最多 10–20%。

## 入口

- [`core/CORE_INDEX.md`](core/CORE_INDEX.md)：最短主线与 CORE AFTER APPLY。
- [`core/APPLICATION_GATE.md`](core/APPLICATION_GATE.md)：最低可投递证据。
- [`dlc/DLC_INDEX.md`](dlc/DLC_INDEX.md)：按 Trigger 选择的扩展包。
- [`migration/MIGRATION_TABLE.md`](migration/MIGRATION_TABLE.md)：旧模块/知识点的新归宿。
- [`prompts/CORE_TEACHING_PROMPT_TEMPLATE.md`](prompts/CORE_TEACHING_PROMPT_TEMPLATE.md)：新聊天启动 CORE。
- [`prompts/DLC_TEACHING_PROMPT_TEMPLATE.md`](prompts/DLC_TEACHING_PROMPT_TEMPLATE.md)：明确进入 DLC 时使用。

Docker、Linux、Git、CMake、网络、GPU、测试理论和文档理论不得抢走主线。Docker 在 ENV-01 一次搭建完整环境；Linux/Git/CMake 作为 Embedded Skills 随任务学习。

范围外：强化学习、Isaac Lab、灵巧手、视觉伺服、触觉、CUDA/TensorRT、具身智能和高级控制算法。除非目标岗位改变，不进入 CORE。
