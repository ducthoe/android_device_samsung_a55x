#!/bin/env python3
#
# Copyright (C) 2024 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import common
import re

def AddImage(info, basename, dest):
  data = info.input_zip.read("IMAGES/" + basename)
  common.ZipWriteStr(info.output_zip, basename, data)
  info.script.Print("Flashing {} image...".format(dest.split('/')[-1]))
  info.script.AppendExtra('package_extract_file("%s", "%s");' % (basename, dest))

def FullOTA_InstallEnd(info):
  AddImage(info, "dtbo.img", "/dev/block/by-name/dtbo")
  AddImage(info, "init_boot.img", "/dev/block/by-name/init_boot")
  AddImage(info, "vbmeta.img", "/dev/block/by-name/vbmeta")
  AddImage(info, "vendor_boot.img", "/dev/block/by-name/vendor_boot")
  return
