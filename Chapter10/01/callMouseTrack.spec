# -*- mode: python -*-

block_cipher = None


a = Analysis(['callMouseTrack.py'],
             pathex=['/home/jhongesell/Documentos/Biblioteca/Python/03. Tutoriales de libros/B. M. Harwarni/Qt5 Python GUI Programming Cookbook/Software-creado-con-PyQt5/Ejemplos/10/01'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          name='callMouseTrack',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
