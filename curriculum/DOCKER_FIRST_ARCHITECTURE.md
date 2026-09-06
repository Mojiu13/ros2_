# Docker-first ROS2 开发环境

## 定位

Docker 是稳定的开发基础设施，不是贯穿每个模块反复学习的对象。ENV-01 集中搭建一次完整环境；以后 90% 以上注意力应放在 ROS2、URDF/TF、Gazebo、ros2_control、MoveIt、调试与应用开发。

~~~text
Ubuntu 24.04 Host
├─ Git repository / source ── bind mount ───────────────┐
├─ Docker Engine + Compose                              │
├─ Desktop + GPU driver                                 │
└─ Git + editor                                         │
                                                        ▼
一个稳定的 ros2-dev development container
├─ non-root user（匹配 Host UID/GID）
├─ ROS2 Jazzy + colcon + rosdep + ament
├─ RViz2
├─ Gazebo Sim + ros_gz
├─ ros2_control + ros2_controllers + Gazebo integration
├─ MoveIt2
├─ C++ / Python ROS development tools
├─ /workspace/src              ← Host source bind mount
└─ build / install / log       ← workspace outputs
~~~

## 使用方式

~~~text
git clone
→ docker compose build
→ docker compose up
→ enter ros2-dev
→ build workspace
→ run project
~~~

ENV-01 之后，后续模块通常只需启动 Compose、进入 `ros2-dev`、确认对应 package 可用并开始学习。不再按 SIM/CTRL/MOVEIT 逐段安装或频繁 rebuild。

只有 container 无法启动、mount/ownership、GUI、缺包、环境污染、版本冲突或新增项目特定依赖时才重新处理 Docker。任何真实环境变更都必须写回版本化定义并更新 Manifest。

## 刻意不学习

不深入 cgroup、namespace 内部、多阶段 build 优化、镜像缓存细节、Docker 网络内部、多容器微服务、Kubernetes、CI 镜像优化或 GPU 容器原理。ROS-01 最多临时使用第二个 container 做最小 discovery 演示。
