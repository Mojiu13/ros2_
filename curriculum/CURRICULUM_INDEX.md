# 课程索引

Phase 架构保持不变。模块按依赖排序；Application Gate 是投递检查点，不是课程模块。

| Module | 名称 | 阶段 | 优先级 | Prerequisites | 工作量 |
|---|---|---|---:|---|---|
| [ENV-01](modules/ENV-01.md) | Docker 化 ROS2 Jazzy 最小开发环境与可重建工作区 | Phase 0 | P0 | 基本 Linux 使用；C++ / Python 基础；不要求 ROS 或 Docker 深入知识 | M |
| [ROS-01](modules/ROS-01.md) | ROS 2 计算图、CLI、通信选择与容器网络 | Phase 0 | P0 | ENV-01 | M |
| [ROS-02](modules/ROS-02.md) | Python 与 C++ ROS 包最小工程 | Phase 0 | P0 | ROS-01 | L |
| [ROS-03](modules/ROS-03.md) | Launch、Parameter、YAML、Namespace 与 Remap | Phase 0 | P0 | ROS-02 | M |
| [SYS-01](modules/SYS-01.md) | 6/7 DOF 参考机械臂完整链路观察 | Phase 1 | P0 | ROS-03 | S |
| [MODEL-01](modules/MODEL-01.md) | MiniArm URDF、TF、RViz 与机器人空间基础 | Phase 1 | P0 | SYS-01 | L |
| [SIM-01](modules/SIM-01.md) | Xacro、碰撞/惯性与 Docker 中的 Gazebo Sim | Phase 1 | P0 | MODEL-01 | L |
| [CTRL-01](modules/CTRL-01.md) | ros2_control 接入与 Controller 生命周期 | Phase 1 | P0 | SIM-01 | L |
| [CTRL-02](modules/CTRL-02.md) | A1/A2 Direct Trajectory 与控制基线迁移 | Phase 1 | P0 | CTRL-01 | L |
| [MOVEIT-01](modules/MOVEIT-01.md) | 6/7 DOF 机械臂 SRDF、MoveIt 配置与 RViz 规划执行 | Phase 1 | P0 | CTRL-02 | L |
| [MOVEIT-02](modules/MOVEIT-02.md) | C++/Python 编程规划与执行及运动学直觉 | Phase 1 | P0 | MOVEIT-01 | L |
| [INT-01](modules/INT-01.md) | 6/7 DOF 全链路集成验收 | Phase 1 | P0 | MOVEIT-02 | M |
| [MODEL-02](modules/MODEL-02.md) | 机器人模型工程化与参数验证 | Phase 2 | P1 | INT-01 | L |
| [ROS-04](modules/ROS-04.md) | QoS、Lifecycle 与 ROS 工程边界 | Phase 2 | P1 | INT-01 | M |
| [CTRL-03](modules/CTRL-03.md) | Controller 配置、容差与夹爪协同 | Phase 2 | P1 | INT-01 | L |
| [MOVEIT-03](modules/MOVEIT-03.md) | PlanningScene、约束与轨迹质量 | Phase 2 | P1 | INT-01 | L |
| [APP-01A](modules/APP-01A.md) | 任务需求、接口设计与 Action Server 骨架 | Phase 3 | P0 | INT-01 | M |
| [APP-01B](modules/APP-01B.md) | MoveIt TaskNode 与最小状态机 | Phase 3 | P0 | APP-01A | L |
| [APP-02A](modules/APP-02A.md) | Cancel、Timeout 与错误传播 | Phase 3 | P0 | APP-01B | L |
| [DBG-01](modules/DBG-01.md) | Docker-to-Application 跨层故障注入与诊断 | Phase 3 | P0 | APP-02A | L |
| [TEST-01](modules/TEST-01.md) | 需求可追踪的功能、异常与 ROS 集成测试 | Phase 3 | P0 | APP-02A | L |
| [DOC-01](modules/DOC-01.md) | 软件设计、架构与测试文档 | Phase 3 | P0 | TEST-01 | M |
| [APP-02B](modules/APP-02B.md) | Retry、Replan 与有限恢复 | Phase 3 | P1 | APP-02A, DBG-01 | L |
| [JOB-01](modules/JOB-01.md) | 项目答辩、简历证据与综合模拟面试 | Phase 4 | P0 | DOC-01 | M |
| [ADV-01](modules/ADV-01.md) | joint_trajectory_controller 源码主线 | Advanced Optional | P2 | CTRL-03 | L |
| [ADV-02](modules/ADV-02.md) | 最小自定义 ros2_control Controller | Advanced Optional | P2 | ADV-01 | L |
| [ADV-03](modules/ADV-03.md) | 运动学与规划参数深化 | Advanced Optional | P2 | MOVEIT-03 | L |

## 阶段门

- Phase 0 Gate：最小 Dockerized ROS 环境以 non-root user 可删除、重建、恢复；双语言 topic/service/action 与配置可运行；ROS 容器网络实验通过。
- Phase 1 Gate：A1 完成原理闭环；A2 在 MoveIt 前已有独立 controller/direct trajectory baseline，随后完成规划、编程与集成。
- Application Gate：APP-02A 与 DBG-01 核心案例后，具备最低可投递证据；详见 `APPLICATION_GATE.md`。
- Phase 3 Gate：Project B 有可控失败、需求可追踪测试和工程文档。
- Phase 4 Gate：项目表达与仓库事实一致。
