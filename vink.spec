# -*- mode: python ; coding: utf-8 -*-

import glob
import os
import sys

# Under some circumstances, we are doing a *lot* of recursion.
sys.setrecursionlimit(sys.getrecursionlimit() * 5)

block_cipher = None

a = Analysis(
    ['vink.py'],
    pathex=[],
    binaries=[],
    datas=[('LICENSE.*', '.')],
    hiddenimports=[],
    hookspath=['.'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['readline', 'tkinter'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# Remove any MS API dll's from the binaries
a.binaries = TOC([x for x in a.binaries if "api-ms-win" not in x[0]])

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='vink',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='vink',
)
