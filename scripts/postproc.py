assert __name__ == "__main__"

import sys
import os
import shutil
import subprocess
import glob

from . import config

nodeSrcFolder = 'node-{}'.format(config.version)
resultFolder = 'libnode'

libFolder = os.path.join(resultFolder, 'lib')

shutil.rmtree(resultFolder, ignore_errors=True)

os.mkdir(resultFolder)
os.mkdir(libFolder)

if sys.platform == 'win32':
    for libFile in os.scandir(nodeSrcFolder + ('\\out\\Release' if config.configuration == 'release' else '\\out\\Debug')):
        if libFile.is_file() and (libFile.name.endswith('.dll') or libFile.name.endswith('.lib') or libFile.name.endswith('.exe') or libFile.name.endswith('.pdb')):
            print('Copying', libFile.name)
            shutil.copy(libFile.path, libFolder)
elif sys.platform == 'darwin':
    for libFile in os.scandir(nodeSrcFolder + ('/out/Release' if config.configuration == 'release' else '/out/Debug')):
        if libFile.is_file():
            print('Copying', libFile.name)
            shutil.copy(libFile.path, libFolder)
            print('Striping', libFile.name)
            subprocess.check_call(['strip', '-x', os.path.join(libFolder, libFile.name)])
elif sys.platform == 'linux':
    for libFile in os.scandir(nodeSrcFolder + ('/out/Release' if config.configuration == 'release' else '/out/Debug')):
        if libFile.is_file():
            print('Copying', libFile.name)
            shutil.copy(libFile.path, libFolder)

shutil.copytree(os.path.join(nodeSrcFolder, 'include'), os.path.join(resultFolder, 'include'))
shutil.copyfile('CMakeLists.txt', os.path.join(resultFolder, 'CMakeLists.txt'))
