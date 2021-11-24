assert __name__ == "__main__"

import shutil
import sys

from . import config

zipFileName = 'libnode-{}-{}-{}-{}'.format(
    config.version,
    sys.platform,
    config.architecture,
    config.configuration
)

shutil.make_archive(zipFileName, 'zip', base_dir='libnode')

print(zipFileName + '.zip')
