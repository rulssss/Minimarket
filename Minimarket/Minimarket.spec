# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [('archivos_py\\resources\\r.ico', 'archivos_py\\resources'), ('archivos_py\\resources\\eye_visible_hide_hidden_show_icon_145988.png', 'archivos_py\\resources')]
binaries = []
hiddenimports = ['cryptography', 'cryptography.hazmat.bindings._rust', 'cryptography.hazmat.bindings._openssl', 'matplotlib.backends.backend_qt5agg', 'matplotlib.figure']
tmp_ret = collect_all('matplotlib')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Minimarket',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['archivos_py\\resources\\r.ico'],
)
