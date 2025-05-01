#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/samsung/e1s',
    'hardware/samsung',
]


blob_fixups: blob_fixups_user_type = {
    'vendor/etc/init/android.hardware.security.keymint-service.samsung.rc': blob_fixup()
        .regex_replace('keymint-service', 'keymint-service.samsung'),
    'vendor/etc/init/init.nfc.samsung.rc': blob_fixup()
        .regex_replace('system', 'secure_element'),
    'vendor/etc/init/init.s5e9945.rc': blob_fixup()
        .regex_replace('vendor_spay', 'system'),
    'vendor/etc/init/vendor.samsung.hardware.camera.provider-service_64.rc': blob_fixup()
        .regex_replace('vendor_secdir w', 'w')
        .regex_replace('vendor_secdir', 'camera'),
    (
        'vendor/lib64/hw/audio.primary.s5e9945.so',
        'vendor/lib64/libaudioproxy2.so',
        'vendor/lib64/libaudioparamupdate.so',
    ): blob_fixup()
        .replace_needed('libaudioroute.so', 'libaudioroute_samsung.so')
        .replace_needed('libtinyalsa.so', 'libtinyalsa_samsung.so'),
    'vendor/lib64/hw/camera.s5e9945.so': blob_fixup()
        .add_needed('libui_shim.so'),
    'vendor/lib64/lib_profiler.so': blob_fixup()
        .replace_needed('libprotobuf-cpp-full-21.7.so', 'libprotobuf-cpp-full-21.12.so'),
    (
        'vendor/lib64/libalsautils_sec.so',
        'vendor/lib64/libaudioroute_samsung.so',
    ): blob_fixup()
        .replace_needed('libtinyalsa.so', 'libtinyalsa_samsung.so'),
    'vendor/lib64/libexynosgraphicbuffer.so': blob_fixup()
        .add_needed('libshim_ui.so'),
    'vendor/lib64/libsec-ril.so': blob_fixup()
        .replace_needed('libprotobuf-cpp-full-21.7.so', 'libprotobuf-cpp-full-21.12.so')
        .sig_replace(
            '0e 40 f9 e1 03 16 aa 82 0c 80 52 e3 03 15 aa',
            '0e 40 f9 e1 03 16 aa 82 0c 80 52 03 00 80 d2'),
    (
        'vendor/lib64/libsensorlistener.so',
        'vendor/lib64/libvdis_core.so',
    ): blob_fixup()
        .add_needed('libshim_sensorndkbridge.so'),
    'vendor/lib64/libskeymint_cli.so': blob_fixup()
        .add_needed('libshim_crypto.so'),
}  # fmt: skip


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    'libuuid': lib_fixup_vendor_suffix,
}

module = ExtractUtilsModule(
    'e1s',
    'samsung',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
