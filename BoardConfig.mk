#
# Copyright (C) 2025 The Android Open Source Project
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

DEVICE_PATH := device/samsung/e2s

# Display
TARGET_SCREEN_DENSITY := 450

# DTS
BOARD_DTBO_CFG := $(DEVICE_PATH)/configs/kernel/e2s.cfg

# Modules
BOARD_RECOVERY_RAMDISK_KERNEL_MODULES_LOAD := mcd-panel-s6e3haf_e2s.ko s2dos07.ko qm35.ko synaptics_ts_spi.ko

# Inherit from common
include device/samsung/s5e9945/BoardConfigCommon.mk
