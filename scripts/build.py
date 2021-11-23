assert __name__ == "__main__"

import sys
import os
import subprocess
import shutil

from . import config

os.chdir('node-{}'.format(config.version))

configureArgvs = [ '--shared' ] + config.options

if sys.platform == 'win32':
    env = os.environ.copy()
    env['config_flags'] = ' '.join(configureArgvs)
    
    subprocess.check_call(
        ['cmd', '/c', 'vcbuild.bat', config.configuration] + ([] if config.architecture == 'x64' else [config.architecture]),
        env=env
    )
else:
    if (config.configuration == 'debug'):
        configureArgvs += [ '--debug' ]
    subprocess.check_call([ sys.executable, 'configure.py' ] + configureArgvs)
    subprocess.check_call(['make', '-j4'])
