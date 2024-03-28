# -*- mode: python ; coding: utf-8 -*-
import os
import six
import ansible
import ansible_collections


block_cipher = None

print(six.__file__)
print(ansible.__file__)
print(os.path.dirname(ansible.__file__))
a = Analysis(
    ['ansible-playbook.py'],
    pathex=[],
    binaries=[],
    datas=[
        (six.__file__, '.'),
        
        (os.path.dirname(ansible.__file__), 'ansible')
    ],
    hiddenimports=['uuid', 'ansible', 'configparser', 'smtplib', 'logging.handlers', 'distutils.version', 'pty','xml.etree.ElementTree','xml.dom','cmd'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher
)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ansible-playbook',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
