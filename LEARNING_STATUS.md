# LEARNING_STATUS

## 当前模块

```text
R0-M0｜环境、仓库、学习记录基线
```

## 当前目标

确认当前 ROS2 + MoveIt2 + ros2_control 环境可复现、可观察、可记录，并整理 GitHub 仓库结构。

## 环境信息

| 项目 | 当前记录 | 验证命令 |
|---|---|---|
| OS | 待填写 | `lsb_release -a` |
| ROS2 版本 | 待填写 | `printenv ROS_DISTRO` |
| MoveIt2 是否可用 | 待填写 | `ros2 pkg list | grep moveit` |
| ros2_control 是否可用 | 待填写 | `ros2 control --help` |
| 工作空间 | 待填写 | `pwd` |
| GitHub 仓库 | Mojiu13/ros2_ | - |

## R0-M0 验收清单

- [ ] 能 source ROS2 环境
- [ ] 能启动 Panda MoveIt demo
- [ ] RViz 能显示 Panda 机器人
- [ ] RViz MotionPlanning 插件可用
- [ ] Plan 成功
- [ ] Execute 成功
- [ ] 能列出 ROS2 节点
- [ ] 能列出 ROS2 topic
- [ ] 能列出 ROS2 action
- [ ] 能列出 ros2_control controller
- [ ] 能查看 `/move_group` 参数
- [ ] 能找到 FollowJointTrajectory action
- [ ] 能把观察结果写入文档

## 关键观察结果

### ROS2 Nodes

```bash
ros2 node list
```

待填写：

```text

```

### ROS2 Topics

```bash
ros2 topic list
```

待填写：

```text

```

### ROS2 Actions

```bash
ros2 action list
```

待填写：

```text

```

### Controllers

```bash
ros2 control list_controllers
```

待填写：

```text

```

### move_group Parameters

```bash
ros2 param list /move_group
```

待填写：

```text

```

## 当前结论

待填写：

```text
我当前能稳定启动哪些东西？
我当前还不能稳定启动哪些东西？
如果失败，失败发生在哪一层？
```

## 下一模块

完成本文件后进入：

```text
R1-M1｜ROS2 最小通信与命令行观察
```
