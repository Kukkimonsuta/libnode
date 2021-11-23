assert __name__ == "__main__"

import shutil
import sys

from . import config

zipBasename = 'libnode-{}-{}-{}{}'.format(
    config.version,
    sys.platform,
    config.architecture,
    config.zipBasenameSuffix
)

shutil.make_archive(zipBasename, 'zip', base_dir='libnode')

print(zipBasename + '.zip')
