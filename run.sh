#!/usr/bin/env bash
set -euo pipefail

# ↓↓↓ 设置变量 ↓↓↓
CONTROLLER="${CONTROLLER:-panda_arm_controller}"
ACTION_NAME="/$CONTROLLER/follow_joint_trajectory"

#↓↓↓ 命令 ↓↓↓
colcon build --packages-select task_node_mp_a_interfaces task_node_mp_a --symlink-install