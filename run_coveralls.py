# -*- coding: utf-8 -*-

import os
import subprocess


if __name__ == '__main__':
    if 'TRAVIS' in os.environ:
        coveralls = subprocess.call('coveralls')
        raise SystemExit(coveralls)
