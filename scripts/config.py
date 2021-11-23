assert __name__ != "__main__"

import os

version = os.environ['LIBNODE_VERSION']
options = (os.environ.get('LIBNODE_OPTIONS') or '').split()
architecture = os.environ.get('LIBNODE_ARCHITECTURE')
configuration = os.environ.get('LIBNODE_CONFIGURATION')
