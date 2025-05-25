#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'vendor/samsung/s5e9945',
]


blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/hw/audio.primary.s5e9945.so': blob_fixup()
        .replace_needed('libaudioroute.so', 'libaudioroute_samsung.so')
        .replace_needed('libtinyalsa.so', 'libtinyalsa_samsung.so'),
    'vendor/lib64/hw/camera.s5e9945.so': blob_fixup()
        .add_needed('libui_shim.so'),
}

module = ExtractUtilsModule(
    'e2s',
    'samsung',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 's5e9945', module.vendor)
    utils.run()
