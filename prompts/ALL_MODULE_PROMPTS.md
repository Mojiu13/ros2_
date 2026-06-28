# ALL_MODULE_PROMPTS｜ROS2 + MoveIt2 + ros2_control 全模块提示词库

本文件保存所有学习模块的可复用提示词。

使用方式：在新对话框中读取 `prompts/PROMPT_INDEX.md`，指定模块编号，然后让 ChatGPT 按本文件对应模块执行。

---

# 通用教学约束

无论学习哪个模块，都必须遵守：

```text
1. 把我当作真正的新手，但不要降低工程标准。
2. 不要百科式堆知识点。
3. 每次只给少量命令，等我贴输出后再判断。
4. 优先让我运行、观察、修改、故障注入、修复、总结。
5. 不要过早深入源码、算法、实时控制、DDS、QoS 深层细节，除非当前模块要求。
6. 每个模块结束时，帮我更新 GitHub 文档：README、LEARNING_STATUS、docs/ERROR_LOG、docs/SYSTEM_MAP、docs/INTERVIEW_QA 或模块 README。
7. 如果报错，先判断错误层级：环境层、workspace 层、launch 层、ROS2 通信层、URDF/TF 层、MoveIt 层、ros2_control 层、controller 层、RViz 层、GitHub 文档层。
8. 每个模块最终要产出：可运行结果、观察命令、故障记录、总结文档、面试问答。
```

---

# R0-M0｜环境、仓库、学习记录基线

```text
我正在学习 ROS2 + MoveIt2 + ros2_control，当前模块是 R0-M0｜环境、仓库、学习记录基线。

请把我当作新手工程学习者，不要百科式讲解。本模块只做环境确认、仓库整理和基线记录，不深入源码、不深入算法。

我的仓库是 Mojiu13/ros2_。

本模块目标：
1. 确认 ROS2 Jazzy 环境可用；
2. 确认 MoveIt2 可用；
3. 确认 ros2_control 可用；
4. 启动 Panda MoveIt demo；
5. 确认 RViz 能显示机器人；
6. 尝试 Plan / Execute；
7. 用 ros2 命令观察 node / topic / action / controller / parameter；
8. 把结果记录到 README.md、LEARNING_STATUS.md、docs/COMMAND_CHEATSHEET.md、docs/ERROR_LOG.md。

请按步骤带我执行，每次只给少量命令。看到输出后判断是否正常。

验收命令：
- printenv ROS_DISTRO
- ros2 node list
- ros2 topic list
- ros2 action list
- ros2 control list_controllers
- ros2 param list /move_group

本模块结束时，我要能回答：我的 ROS2 版本是什么？MoveIt2 demo 怎么启动？有哪些关键节点？有哪些 controller？FollowJointTrajectory action 名称是什么？Plan/Execute 是否成功？如果失败，问题大概在哪一层？
```

---

# R1-M1｜ROS2 最小通信与命令行观察

```text
当前模块是 R1-M1｜ROS2 最小通信与命令行观察。

请从新手角度带我建立 ROS2 最小通信地图。本模块目标不是学完整 ROS2，而是理解 node、topic、service、action、parameter、launch 的最小工程用法，并学会用 ros2 CLI 观察系统。

本模块要完成：
1. 创建一个最小 ROS2 package；
2. 写 publisher / subscriber；
3. 写 service server / client；
4. 写 action server / client；
5. 写一个带 parameter 的 node；
6. 用 launch 启动多个 node；
7. 用 ros2 node/topic/service/action/param 命令观察。

请不要深入 DDS、QoS 深层机制、executor 源码、callback group 复杂并发。

教学方式：
- 先解释本模块解决什么问题；
- 每次给我一小组命令或一小段代码；
- 等我贴输出后再判断；
- 出错时先判断是 package 结构、source、build、运行命令还是代码问题；
- 最后帮我写 docs/ROS2_COMMUNICATION_NOTES.md 和 3～5 个面试问答。

验收问题：topic、service、action 的区别是什么？为什么机械臂执行轨迹适合用 action？parameter 和 YAML 有什么关系？launch 文件解决了什么问题？
```

---

# R1-M2｜URDF / Xacro / TF 最小机器人模型

```text
当前模块是 R1-M2｜URDF / Xacro / TF 最小机器人模型。

请带我做一个最小两关节机器人模型，让我理解机器人为什么能在 RViz 中显示，TF 为什么是 MoveIt 的基础。

本模块要完成：
1. 创建一个最小描述包；
2. 编写 base_link → link1 → link2 的 URDF / xacro；
3. 包含 fixed joint 和 revolute joint；
4. 启动 robot_state_publisher；
5. 使用 joint_state_publisher 或 joint_state_publisher_gui 模拟关节状态；
6. 在 RViz 中显示 RobotModel；
7. 查看 TF tree；
8. 故意制造 origin、axis、fixed frame 错误并修复。

请不要深入复杂 xacro 宏、精确惯量建模、mesh 处理、高级 tf2 API。

教学方式：先跑最小模型，再观察 /tf、/joint_states、RViz Fixed Frame。每次只给少量命令或代码，等我贴输出后再继续。

本模块输出：docs/URDF_TF_NOTES.md，模块 README，ERROR_LOG 记录至少一个故障。

验收问题：URDF 和 TF 的区别是什么？link 和 joint 分别是什么？origin/axis 写错会怎样？robot_state_publisher 做什么？Fixed Frame 错了有什么现象？
```

---

# R1-M3｜ros2_control 最小执行链路

```text
当前模块是 R1-M3｜ros2_control 最小执行链路。

请带我理解 controller 是谁，以及 MoveIt 最终把轨迹交给谁执行。本模块只学最小执行链路，不读 controller 源码。

本模块要完成：
1. 启动一个已有的 ros2_control 示例或 Panda MoveIt demo；
2. 查看 controller_manager；
3. 查看 joint_state_broadcaster 和 joint_trajectory_controller；
4. 查看 controller 状态 active/inactive；
5. 查看 hardware interfaces；
6. 找到 FollowJointTrajectory action；
7. 不经过 MoveIt，直接用 ros2 action send_goal 给 controller 发一条简单轨迹；
8. 故意制造 controller inactive 或 joint name mismatch 并观察。

请不要深入自定义 controller、hardware_interface 源码、实时控制、update() 源码。

教学方式：每次给我少量观察命令，让我贴输出后你判断。重点解释 controller_manager、joint_state_broadcaster、joint_trajectory_controller、command interface、state interface。

本模块输出：docs/ROS2_CONTROL_MINIMAL_NOTES.md，ERROR_LOG 至少一条。

验收问题：controller_manager 做什么？joint_state_broadcaster 做什么？joint_trajectory_controller 做什么？MoveIt 最终把轨迹发给哪个 action？controller inactive 会怎样？
```

---

# R1-M4｜MoveIt2 RViz 规划执行流程

```text
当前模块是 R1-M4｜MoveIt2 RViz 规划执行流程。

请带我通过 RViz MotionPlanning 插件理解 MoveIt2 的最小规划执行流程。本模块目标是理解 Plan 和 Execute 的边界，不深入算法。

本模块要完成：
1. 启动 Panda MoveIt demo；
2. 在 RViz 中选择 planning group；
3. 设置 goal state；
4. 执行 Plan；
5. 执行 Execute；
6. 观察 move_group 节点；
7. 观察 FollowJointTrajectory action；
8. 观察 joint_states 变化；
9. 故意制造不可达目标或 start state 问题并记录。

请不要深入 OMPL 算法、IK 数学、PlanningScene 内部源码、碰撞检测底层算法。

教学方式：先带我跑 RViz Plan/Execute，再逐步观察 node/topic/action/param/controller。每一步只给少量命令。

本模块输出：docs/MOVEIT_RVIZ_FLOW_NOTES.md，更新 docs/SYSTEM_MAP.md。

验收问题：MoveIt 输入是什么？输出是什么？Plan 和 Execute 区别是什么？planning group 来自哪里？trajectory 为什么能被 controller 执行？MoveIt 和 ros2_control 的边界是什么？
```

---

# R1-M5｜MoveItPy Python 代码闭环

```text
当前模块是 R1-M5｜MoveItPy Python 代码闭环。

请带我从“会用 RViz 点按钮”升级到“会写 Python 节点调用 MoveIt 完成一次 plan + execute”。

本模块要完成：
1. 创建 Python ROS2 package；
2. 编写 MoveItPy 节点；
3. 初始化 MoveItPy；
4. 获取 planning component；
5. set_start_state_to_current_state；
6. 设置目标；
7. plan；
8. 如果 plan 成功则 execute；
9. 打印规划结果、执行结果、失败原因；
10. 用 launch 启动。

请不要深入 MoveItPy 内部源码、复杂 task planning、多规划器切换、复杂约束规划。

教学方式：代码必须小步构建。每次给我一段可运行代码或一个命令，等我贴输出后再继续。出错时判断是包结构、依赖、source、MoveIt demo 未启动、move_group 未连接、plan 失败还是 execute 失败。

本模块输出：round1_fast_flow/r1_m5_moveitpy_code_loop/，docs/MOVEITPY_NOTES.md。

验收问题：MoveItPy 初始化需要什么？为什么要 set_start_state_to_current_state？plan 成功代表机器人已经动了吗？execute 失败可能是哪几层原因？Python 节点、move_group、controller 的关系是什么？
```

---

# R1-M6｜全链路串联与最小故障定位

```text
当前模块是 R1-M6｜全链路串联与最小故障定位。

请带我把前面模块串成完整链路：Python TaskNode → MoveItPy → move_group → planning pipeline → trajectory → FollowJointTrajectory Action → joint_trajectory_controller → command interface → fake hardware → joint_states → TF → RViz。

本模块要完成：
1. 画出完整执行链路；
2. 用命令观察链路中的每一层；
3. 区分 plan failed 和 execute failed；
4. 故意制造 controller inactive、action server missing、joint mismatch、TF missing、goal unreachable、start state invalid；
5. 每个故障记录现象、命令、日志、根因、修复方式。

本模块不深入源码，只做层级定位。

教学方式：不要一次性讲完，按链路一层一层验证。每个故障只先做最小复现和定位。

本模块输出：docs/FULL_EXECUTION_CHAIN.md，docs/ERROR_LOG.md，更新 docs/SYSTEM_MAP.md。

验收问题：trajectory 从哪里生成？FollowJointTrajectory action 处于什么位置？Plan 成功但 Execute 失败查哪里？RViz 不显示查哪里？controller 收不到 goal 查哪里？
```

---

# R1-M7｜第一遍整合小项目

```text
当前模块是 R1-M7｜第一遍整合小项目。

请带我把第一遍学到的内容整合成一个可展示的最小项目：启动 MoveIt demo，启动自写 TaskNode，TaskNode 调用 MoveItPy，让 Panda 完成一次 plan + execute，并输出规划和执行结果。

项目目录建议：round1_fast_flow/r1_m7_minimal_task_demo/

本模块要完成：
1. 整理 package 结构；
2. 写 task_node.py；
3. 写 launch/task_demo.launch.py；
4. 确认能和 MoveIt demo 配合运行；
5. 打印关键结果；
6. 写项目 README；
7. 写系统架构图；
8. 写常见错误表。

教学方式：先保证最小可运行，再优化结构。不要引入复杂功能。

本模块输出：round1_fast_flow/r1_m7_minimal_task_demo/README.md，更新 LEARNING_STATUS.md。

验收问题：URDF/TF 是为谁服务的？MoveIt 负责什么？controller 负责什么？trajectory 为什么是接口？Python execute 后轨迹去了哪里？失败时如何粗略定位？
```

---

# R2-M1｜ROS2 工程组织：package / launch / parameter / YAML

```text
当前模块是 R2-M1｜ROS2 工程组织：package / launch / parameter / YAML。

请带我从 demo 级别升级到真实 ROS2 项目组织能力。本模块重点是 package 结构、launch 分层、parameter、YAML、namespace、remap。

本模块要完成：
1. 创建 ament_python 和 ament_cmake 的最小示例；
2. 写多节点 launch；
3. 用 YAML 加载参数；
4. 用 launch argument 修改参数；
5. 给节点加 namespace；
6. 做一次 remap；
7. 整理工程目录；
8. 解释 MoveIt 和 controller 的 launch/config 文件如何组织。

请不要深入 DDS、复杂 lifecycle、复杂 composable node。

教学方式：必须边写边运行。每次给我一小段 launch 或 YAML，让我运行并贴输出。

本模块输出：docs/ROS2_PROJECT_STRUCTURE.md，一个小型工程组织 demo。

验收问题：launch 文件如何传参？YAML 如何进入 node？namespace 和 remap 分别解决什么问题？真实 ROS2 项目为什么要分 launch/config/src/docs？
```

---

# R2-M2｜机器人模型工程：URDF / Xacro / SRDF / TF / MoveIt config

```text
当前模块是 R2-M2｜机器人模型工程：URDF / Xacro / SRDF / TF / MoveIt config。

请带我从“能显示机器人”升级到“能看懂和修改机械臂模型配置”。本模块核心是模型链：URDF 描述身体，SRDF 描述 MoveIt 如何理解身体，YAML 描述规划和限制参数，TF 描述运行时坐标关系。

本模块要完成：
1. 阅读 Panda URDF / xacro；
2. 找 link、joint、origin、axis、limit、collision、visual、inertial；
3. 找 ros2_control tag；
4. 阅读 SRDF；
5. 找 planning group、end effector、disabled collision；
6. 阅读 kinematics.yaml、joint_limits.yaml；
7. 修改一个 harmless 的 visual 或 joint limit；
8. 观察 MoveIt/RViz 变化；
9. 故意制造 joint name 或 TF 问题并记录。

请不要深入复杂 mesh、精确动力学建模、MoveIt Setup Assistant 全量细节。

本模块输出：docs/ROBOT_MODEL_CONFIG_CHAIN.md。

验收问题：URDF 和 SRDF 的区别是什么？planning group 来自哪里？joint name 如何贯穿 URDF、SRDF、trajectory、controller.yaml、ros2_control interface？TF 错误会影响什么？
```

---

# R2-M3｜ros2_control 配置深化：controller / interface / lifecycle

```text
当前模块是 R2-M3｜ros2_control 配置深化：controller / interface / lifecycle。

请带我从“知道 controller 是谁”升级到“能配置和排查 controller”。

本模块要完成：
1. 阅读 ros2_control tag；
2. 阅读 controller yaml；
3. 理解 hardware plugin、command interface、state interface；
4. 查看 controller_manager；
5. 手动 load/configure/activate/deactivate controller；
6. 查看 hardware interfaces；
7. 故意改错 joint name；
8. 故意造成 interface missing 或 controller inactive；
9. 记录报错和修复方式。

请不要深入自定义 controller 源码和实时控制。

教学方式：以命令观察为主，每次只给少量 ros2 control 命令。看到输出后帮我判断 controller 状态和错误层级。

本模块输出：docs/ROS2_CONTROL_CONFIG_DEEP_DIVE.md。

验收问题：controller 为什么能拿到 joint interface？controller failed to load、inactive、interface missing、joint mismatch 分别怎么查？
```

---

# R2-M4｜MoveIt 架构深化：RobotModel / RobotState / PlanningScene

```text
当前模块是 R2-M4｜MoveIt 架构深化：RobotModel / RobotState / PlanningScene。

请带我理解 MoveIt 如何把机器人模型变成可规划对象。本模块不追求源码细节，而是理解关键对象和工程现象。

本模块要完成：
1. 查看 move_group 参数；
2. 理解 RobotModel、RobotState、JointModelGroup、PlanningScene；
3. 观察 current state；
4. 理解 start state 和 goal state；
5. 制造 start state 不同步问题；
6. 制造不可达目标或简单碰撞问题；
7. 记录 plan failed 的现象和原因。

请不要深入碰撞检测底层算法、PlanningScene 内部源码、IK 数学推导。

教学方式：用实际 demo 观察 MoveIt 的状态，不空讲架构。每次先给命令或操作，再解释输出。

本模块输出：docs/MOVEIT_ARCHITECTURE_NOTES.md。

验收问题：MoveIt 如何知道机器人当前状态？planning group 是什么？start state/goal state 是什么？模型问题、状态问题、目标问题、碰撞问题如何区分？
```

---

# R2-M5｜MoveIt Planning Pipeline 与 trajectory 生成

```text
当前模块是 R2-M5｜MoveIt Planning Pipeline 与 trajectory 生成。

请带我理解 MoveIt 如何生成一条带时间的 trajectory。本模块重点是 trajectory 的结构和 time_from_start，不深入 OMPL 数学。

本模块要完成：
1. 生成一条 MoveIt 轨迹；
2. 打印 trajectory.joint_names；
3. 打印 trajectory.points；
4. 观察 positions、velocities、accelerations、time_from_start；
5. 修改 velocity scaling 和 acceleration scaling；
6. 观察轨迹时间变化；
7. 理解 path planning 和 time parameterization 的区别。

请不要深入 OMPL 算法源码、采样规划数学、复杂 path constraints。

教学方式：先让我看到真实 trajectory 数据，再解释每个字段。每一步都要求我贴输出。

本模块输出：docs/MOVEIT_TRAJECTORY_GENERATION.md。

验收问题：trajectory 的结构是什么？time_from_start 有什么用？速度/加速度限制如何影响轨迹？为什么 controller 能按时间执行轨迹？规划路径和时间参数化有什么区别？
```

---

# R2-M6｜MoveIt Execution 与 controller 对接

```text
当前模块是 R2-M6｜MoveIt Execution 与 controller 对接。

请带我深入理解 Plan 成功后 Execute 到底发生什么，以及 MoveIt 如何找到对应 controller。

本模块要完成：
1. 阅读 MoveIt controllers.yaml；
2. 查看 /move_group 的 controller 相关参数；
3. 找到 moveit_simple_controller_manager；
4. 找到 action namespace；
5. Execute 时观察 FollowJointTrajectory action；
6. 故意改错 action_ns；
7. 故意让 controller inactive；
8. 记录 action server missing、timeout、abort 的区别。

请不要深入 TrajectoryExecutionManager 源码实现，只理解工程链路。

教学方式：一边执行，一边观察参数、action、controller。出错时判断是 MoveIt 配置、action namespace、controller 状态还是 trajectory 本身。

本模块输出：docs/MOVEIT_EXECUTION_TO_CONTROLLER.md。

验收问题：MoveIt 怎么知道把轨迹发给哪个 controller？controllers.yaml 中 action_ns 有什么用？execute failed 可能是哪几层问题？MoveIt controller manager 和 ros2_control controller_manager 有什么区别？
```

---

# R2-M7｜ROS2 Action 与 C++ 工程基础

```text
当前模块是 R2-M7｜ROS2 Action 与 C++ 工程基础。

请带我补齐机器人岗位常见 C++ ROS2 基础能力。本模块目标是能写基础 rclcpp node、service、action client，并能用 C++ 发送简单 FollowJointTrajectory goal。

本模块要完成：
1. 创建 ament_cmake package；
2. 写 C++ publisher/subscriber；
3. 写 C++ service server/client；
4. 写 C++ action client；
5. 写 C++ parameter node；
6. 写 FollowJointTrajectory C++ action client；
7. 用 launch 启动；
8. 写 CMakeLists.txt 和 package.xml。

请不要深入复杂模板、callback group 并发、高级生命周期节点。

教学方式：每次给一小段 C++，让我 build、source、run，然后贴输出。出错时优先判断 CMake、依赖、头文件、命名空间、source、action server 是否存在。

本模块输出：docs/ROS2_CPP_ACTION_NOTES.md，一个 C++ action client demo。

验收问题：rclcpp node 最小结构是什么？C++ action client 如何发送 goal？CMakeLists/package.xml 如何声明依赖？如何用 C++ 发送 FollowJointTrajectory？
```

---

# R2-M8｜joint_trajectory_controller 源码主线

```text
当前模块是 R2-M8｜joint_trajectory_controller 源码主线。

请带我按主线阅读 joint_trajectory_controller，不要逐行啃源码。本模块唯一主线是：一条 JointTrajectory 进入 controller 后，如何按时间变成 command。

本模块要完成：
1. 找到 controller lifecycle；
2. 找到 FollowJointTrajectory action server；
3. 理解 goal validation；
4. 理解 trajectory 如何进入 realtime buffer；
5. 阅读 update() 主循环；
6. 理解 trajectory time；
7. 理解 sample() 插值；
8. 理解 path tolerance / goal tolerance；
9. 理解 hold position；
10. 理解 command interface 写入边界。

请不要要求我完整背源码，不深入实时编程所有细节，不扩散到 hardware_interface 全源码。

教学方式：每次只读一个源码块，先解释它在主线中的位置，再解释关键变量和数据流。遇到复杂细节要回到主线。

本模块输出：docs/JTC_SOURCE_READING.md。

验收问题：controller 如何接收 action goal？为什么 trajectory 是时间函数？update() 如何按时间采样？tolerance abort 是什么？command interface 写入意味着什么？
```

---

# R2-M9｜自定义 controller 与 mock hardware，可选进阶

```text
当前模块是 R2-M9｜自定义 controller 与 mock hardware，可选进阶。

请带我写一个最小 ros2_control controller，证明我不只是会用 controller，也理解 controller 的基本接入方式。本模块是可选进阶，优先保证最小闭环。

本模块要完成：
1. 创建 controller package；
2. 继承 ControllerInterface；
3. 实现 on_init、on_configure、on_activate、update；
4. 读取 state interface；
5. 写入 command interface；
6. pluginlib 导出；
7. controller_manager 加载；
8. 在 fake/mock hardware 上测试。

请不要一开始追求复杂控制算法、PID、实时优化。

教学方式：每一步都要能 build、load、activate、观察状态。出错时优先查 pluginlib、CMake、package.xml、controller yaml、interface 名称。

本模块输出：mini_projects/mp_d_custom_controller/，docs/CUSTOM_CONTROLLER_NOTES.md。

验收问题：controller 最小结构是什么？pluginlib 如何让 controller_manager 找到它？state interface 和 command interface 在自定义 controller 中如何使用？
```

---

# MP-A｜MoveItPy TaskNode 任务节点项目

```text
当前模块是 MP-A｜MoveItPy TaskNode 任务节点项目。

请带我做一个可展示的 MoveItPy TaskNode，而不是散乱 demo。项目目标是封装任务级接口，内部调用 MoveItPy plan + execute，并记录结果和失败原因。

项目功能：
1. TaskNode 提供 execute_named_target()；
2. TaskNode 提供 execute_pose_goal()，如果暂时复杂可先保留接口；
3. 内部封装 plan + execute；
4. 打印规划结果、执行结果、耗时、失败原因；
5. 提供 launch 文件；
6. 提供 README、架构图、常见错误。

建议目录：mini_projects/mp_a_moveitpy_task_node/

教学方式：先做最小 named target，再逐步封装。不要一开始搞复杂抓取或多机械臂。

本项目关联：R1-M5、R1-M6、R1-M7、R2-M4、R2-M5、R2-M6。

项目验收：能启动 MoveIt demo，启动 TaskNode，机械臂完成一次 plan + execute，并能解释 Python Node、MoveIt、trajectory、controller 的关系。
```

---

# MP-B｜arm + gripper 顺序执行项目

```text
当前模块是 MP-B｜arm + gripper 顺序执行项目。

请带我从单机械臂运动升级到 arm + gripper 协调。目标不是做完整抓取算法，而是理解两个 controller 的顺序协调。

项目功能：
1. arm 移动到预抓取位置；
2. gripper 打开；
3. arm 移动到抓取位置；
4. gripper 闭合；
5. arm 移动到放置位置；
6. gripper 打开；
7. 打印每一步成功/失败；
8. 失败时停止或进入安全状态。

教学方式：先确认 arm controller 和 gripper controller 的 action，然后分别测试，再做顺序状态机。

请不要引入视觉识别、真实抓取物理、复杂规划约束。

项目输出：mini_projects/mp_b_arm_gripper_sequence/。

验收问题：arm controller 和 gripper controller 为什么是两个 controller？任务级程序如何协调顺序？如果 gripper 失败，arm 是否继续？如何记录每一步结果？
```

---

# MP-C｜故障注入与自动恢复项目

```text
当前模块是 MP-C｜故障注入与自动恢复项目。

请带我做一个能展示工程调试能力的项目：故意制造常见故障，并实现错误检测、分类、retry、replan、cancel、safe stop、最终失败原因上报。

需要故意制造：
1. TF missing；
2. joint name mismatch；
3. controller inactive；
4. action timeout；
5. goal unreachable；
6. start state invalid；
7. tolerance abort。

项目要完成：
1. 故障注入脚本或配置；
2. 错误分类表；
3. 最小恢复策略；
4. ERROR_LOG 记录；
5. README 说明每类故障的现象、定位命令、根因、修复方式。

教学方式：一次只制造一种故障，先复现，再定位，再修复，再总结。不要同时制造多个错误。

项目输出：mini_projects/mp_c_failure_recovery_demo/。

验收问题：如何区分 planning failure、execution failure、controller failure、TF failure、configuration failure？哪些错误可以 retry，哪些必须 abort？
```

---

# MP-D｜自定义 controller 项目，可选

```text
当前模块是 MP-D｜自定义 controller 项目，可选。

请带我做一个最小自定义 ros2_control controller，用于展示底层控制理解。目标是可加载、可激活、可读取 state interface、可写 command interface。

本项目要完成：
1. 创建 controller package；
2. 编写最小 controller；
3. pluginlib 导出；
4. 写 controller yaml；
5. 使用 mock/fake hardware；
6. controller_manager 加载；
7. 观察 update() 行为；
8. README 说明 controller 生命周期。

教学方式：先做最小可加载 controller，不要追求复杂控制律。

项目输出：mini_projects/mp_d_custom_controller/。

验收问题：controller_interface 的最小结构是什么？controller_manager 如何找到 controller？on_configure/on_activate/update 分别做什么？
```

---

# JOB-M1｜README / 架构图 / 调试文档

```text
当前模块是 JOB-M1｜README / 架构图 / 调试文档。

请带我把已有学习代码和项目包装成别人能看懂的工程成果。目标不是继续写功能，而是整理表达。

本模块要完成：
1. 总 README；
2. 每个项目 README；
3. 系统架构图；
4. 执行链路图；
5. 调试命令表；
6. 错误日志；
7. 运行截图说明；
8. 模块完成状态表。

推荐图：ROS2 node 通信图、URDF/TF/RViz 显示链路图、MoveIt plan+execute 数据流图、MoveIt→controller→hardware 执行链路图、故障定位决策树。

教学方式：读取仓库现状后，帮我指出 README 缺什么，再逐步生成文档。

验收标准：陌生面试官打开 GitHub，能在 3 分钟内知道项目做了什么、怎么运行、体现什么能力。
```

---

# JOB-M2｜简历项目描述

```text
当前模块是 JOB-M2｜简历项目描述。

请带我把 GitHub 项目转成简历上的项目经历。目标是避免写成“运行了 MoveIt demo”，而要表达为“基于 ROS2 Jazzy + MoveIt2 + ros2_control 封装机械臂任务节点，并完成规划、执行、controller 对接和故障排查”。

本模块要完成：
1. 梳理项目名称；
2. 梳理技术栈；
3. 梳理我实际做了什么；
4. 梳理工程难点；
5. 梳理可量化或可验证结果；
6. 写一版简历项目描述；
7. 写一版面试口述版；
8. 写一版更技术化的长版说明。

教学方式：先读取仓库和项目 README，再问我目标岗位，然后生成简历描述。不要夸大，不要编造未完成的功能。

验收标准：项目描述能体现 ROS2 通信、MoveIt 规划执行、ros2_control controller 对接、URDF/SRDF/TF 理解、故障排查、C++/Python 工程能力。
```

---

# JOB-M3｜面试问答库

```text
当前模块是 JOB-M3｜面试问答库。

请带我建立 ROS2 + MoveIt2 + ros2_control 面试问答库。目标是让我能清楚讲出项目和系统链路，而不是背概念。

本模块要完成：
1. 基于仓库内容整理问题；
2. 按 ROS2 基础、URDF/TF、MoveIt 架构、Planning Pipeline、Trajectory Execution、ros2_control、joint_trajectory_controller、故障排查、项目介绍 分类；
3. 每个问题给出新手可理解但面试够用的答案；
4. 对关键问题给出 30 秒版、2 分钟版；
5. 标注哪些问题我必须会，哪些是加分项。

教学方式：先问我目标岗位，然后根据仓库实际完成内容生成问答。不要编造我没做过的经历。

必须覆盖：MoveIt 和 ros2_control 的关系；URDF 和 SRDF 区别；TF 错误影响；FollowJointTrajectory；controller_manager；controller active；time_from_start；plan failed vs execute failed；joint name mismatch；机械臂不动的排查顺序。

验收标准：我能用 3 分钟讲项目，用 10 分钟讲完整执行链路，用结构化方式回答常见故障排查。
```
