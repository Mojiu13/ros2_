# 课程索引

所有模块按依赖排序；模块文件是新对话的唯一课程边界定义。

| Module | 名称 | 阶段 | 优先级 | Prerequisites | 工作量 |
|---|---|---|---:|---|---|
| [ENV-01](modules/ENV-01.md) | ROS 工程环境与可复现工作区 | Phase 0 | P0 | C++/Python 基础 | S |
| [ROS-01](modules/ROS-01.md) | ROS 2 计算图、CLI 与通信选择 | Phase 0 | P0 | ENV-01 | M |
| [ROS-02](modules/ROS-02.md) | Python 与 C++ ROS 包最小工程 | Phase 0 | P0 | ROS-01 | M |
| [ROS-03](modules/ROS-03.md) | Launch、Parameter、YAML、Namespace 与 Remap | Phase 0 | P0 | ROS-02 | M |
| [SYS-01](modules/SYS-01.md) | 参考机械臂完整链路观察 | Phase 1 | P0 | ROS-03 | S |
| [MODEL-01](modules/MODEL-01.md) | 最小机械臂 URDF、TF 与 RViz | Phase 1 | P0 | SYS-01 | M |
| [SIM-01](modules/SIM-01.md) | Xacro、碰撞/惯性与 Gazebo Sim 入门 | Phase 1 | P0 | MODEL-01 | L |
| [CTRL-01](modules/CTRL-01.md) | ros2_control 接入与 Controller 生命周期 | Phase 1 | P0 | SIM-01 | L |
| [CTRL-02](modules/CTRL-02.md) | 绕过 MoveIt 直接执行 JointTrajectory | Phase 1 | P0 | CTRL-01 | M |
| [MOVEIT-01](modules/MOVEIT-01.md) | SRDF、MoveIt 配置与 RViz 规划执行 | Phase 1 | P0 | CTRL-02 | L |
| [MOVEIT-02](modules/MOVEIT-02.md) | C++/Python 编程规划与执行 | Phase 1 | P0 | MOVEIT-01 | L |
| [INT-01](modules/INT-01.md) | 第一遍全链路集成验收 | Phase 1 | P0 | MOVEIT-02 | M |
| [MODEL-02](modules/MODEL-02.md) | 机器人模型工程化与参数验证 | Phase 2 | P1 | INT-01 | L |
| [ROS-04](modules/ROS-04.md) | QoS、Lifecycle 与 ROS 工程边界 | Phase 2 | P1 | INT-01 | M |
| [CTRL-03](modules/CTRL-03.md) | Controller 配置、容差与夹爪协同 | Phase 2 | P1 | INT-01 | L |
| [MOVEIT-03](modules/MOVEIT-03.md) | PlanningScene、约束与轨迹质量 | Phase 2 | P1 | INT-01 | L |
| [APP-01](modules/APP-01.md) | TaskNode 任务接口与状态机 | Phase 3 | P0 | INT-01 | XL |
| [APP-02](modules/APP-02.md) | 超时、取消、重试与基本恢复 | Phase 3 | P1 | APP-01,DBG-01 | XL |
| [DBG-01](modules/DBG-01.md) | 跨层故障注入与诊断手册 | Phase 3 | P0 | INT-01 | L |
| [TEST-01](modules/TEST-01.md) | 功能、边界、异常与 ROS 集成测试 | Phase 3 | P0 | APP-01 | L |
| [DOC-01](modules/DOC-01.md) | 软件设计、架构与测试文档 | Phase 3 | P0 | APP-01,TEST-01 | M |
| [JOB-01](modules/JOB-01.md) | 项目答辩、简历证据与综合模拟面试 | Phase 4 | P0 | DOC-01,APP-02(标准路线) | M |
| [ADV-01](modules/ADV-01.md) | joint_trajectory_controller 源码主线 | Advanced Optional | P2 | CTRL-03 | L |
| [ADV-02](modules/ADV-02.md) | 最小自定义 ros2_control Controller | Advanced Optional | P2 | ADV-01 | XL |
| [ADV-03](modules/ADV-03.md) | 运动学与规划参数深化 | Advanced Optional | P2 | MOVEIT-03 | L |

## 阶段门

- Phase 0 Gate：能维护双语言 ROS 包与配置，能用 CLI 建立证据链。
- Phase 1 Gate：Project A v1 从模型到规划执行全链路可重复。
- Phase 2 Gate：能处理常见模型、controller、PlanningScene 与轨迹质量问题。
- Phase 3 Gate：Project B 有可控失败、自动测试和完整工程文档。
- Phase 4 Gate：项目表达与仓库证据一致。
