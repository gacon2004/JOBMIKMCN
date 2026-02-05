# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['autoanh_gemini.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('settings.json', '.'),
        ('nsfw_mobilenet2.224x224.h5', '.'),
    ],
    hiddenimports=[
        'google.generativeai',
        'google.ai',
        'google.api_core',
        'PIL._tkinter_finder',
        'nsfw_detector',
        'cv2',
        'openpyxl',
        'pandas',
        'numpy',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ShopeeAutoPick_Gemini',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Hiện console để xem log
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Thêm icon nếu có
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ShopeeAutoPick_Gemini',
)
