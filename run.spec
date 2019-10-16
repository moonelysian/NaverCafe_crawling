# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['run.py'],
             pathex=['C:\\Users\\JSPARK\\Desktop\\myj\\crawling'],
             binaries=[],
             datas=[
                    ('./ui/*.ui','./ui'),
                ],
             hiddenimports=[
                 "crawl.naver",
                 "crawl.kakao",
                 "selenium",
                 "chromedriver_binary",
                 "bs4",
                 "urllib.request",
                 "pandas",
                 "time",
                 "os",
                 "sys",
                 "json",
                 "re"
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='run',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='run')