# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/Main_App.py'],
    pathex=[],
    binaries=[],
    datas=[('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/5ff98edf-0b47-11ed-9adf-d8d09037ecb2.pkl', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/a791675d-0b47-11ed-9474-d8d09037ecb2.pkl', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/ac3377b2-0a4d-11ed-bfa3-d8d09037ecb2.pkl', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/App.py', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/Bill_Payment_GUI.py', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/database.json', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/Deposit_GUI.py', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/Exceptions.py', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/Login.py', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/Login_GUI.py', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/logo.ico', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/logo.png', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/Main_App.py', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/Main_GUI.py', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/SignUp.py', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/SignUp_GUI.py', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/Trans_log_GUI.py', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/Transfer_GUI.py', '.'), ('F:/humam/sem2/oops Lab/Project ideas/Easy paisa app/App/GUI/Money-Droid-Banking-App/Withdraw_GUI.py', '.')],
    hiddenimports=[],
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
    name='Main_App',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='F:\\humam\\sem2\\oops Lab\\Project ideas\\Easy paisa app\\App\\GUI\\Money-Droid-Banking-App\\logo.ico',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Main_App',
)
