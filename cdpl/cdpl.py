# -*- coding: utf-8 -*-

import os

from .constants import *


def cdpl(path: str):
    dpl = os.path.basename(path) + '.dpl'
    with open(os.path.join(path, dpl), 'w', encoding='utf-8') as f:
        f.write('DAUMPLAYLIST\n')
        for i, file in enumerate(os.listdir(path), start=1):
            if os.path.splitext(file)[1] in mediaExtendList:
                f.write(str(i) + '*file*' + file + '\n')
