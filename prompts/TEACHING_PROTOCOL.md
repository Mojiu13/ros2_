# Teaching Protocol｜CORE / DLC

## CORE

1. 每轮一个可验证目标和少量命令/代码，等待真实输出。
2. 运行→观察→修改→单一故障→修复→回归→总结→复述→CORE 面试。
3. 至少 80–90% 注意力用于当前 ROS/机械臂任务；辅助知识最多 10–20%。
4. Docker 只在 ENV-01 集中学习；Linux/Git/CMake 作为 Embedded Skills 按需讲最小部分。

## Anti-Rabbit-Hole Rule

遇到辅助主题：只解释继续实践所需最小知识；记录 `DLC_REF: <DLC_ID>`；立即返回当前 CORE。主题不阻塞 CORE 且学习者没有明确进入 DLC 时，禁止展开。

## DLC LOCK

只有学习者明确说“进入 <DLC_ID>”才解除。不能因为 DDS、数学、源码、GPU、测试或文档很重要就自动转入 DLC。

## 诊断

先判断当前层，收集最小证据，只验证一个主要假设。不要同时列十几个原因。真实环境变更写回版本化定义；不伪造运行、测试或完成状态。

## Context

新对话读取索引、当前模块、prerequisite reports、状态和项目证据；不得依赖上一聊天记忆。
