#!/usr/bin/env bash
set -euo pipefail

# ↓↓↓ 设置变量 ↓↓↓
CONTROLLER="${CONTROLLER:-panda_arm_controller}"
ACTION_NAME="/$CONTROLLER/follow_joint_trajectory"

#↓↓↓ 命令 ↓↓↓
