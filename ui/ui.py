# -*- coding: utf-8 -*-

import os
import sys
sys.path.append('../cdpl')

import pyperclip

from cdpl import cdpl
from wox import Wox, WoxAPI

from .constants import *


class Main(Wox):

    def query(self, param: str):
        result = []
        param = param.strip()

        res_format = RESULT_TEMPLATE.copy()

        if param:
            if os.path.exists(param):
                # normal message
                res_format['Title'] = "The path is not folder."
                res_format['SubTitle'] = "Copy the Path to Clipboard."

                # action message
                action = ACTION_TEMPLATE.copy()
                action['JsonRPCAction']['method'] = 'copy2clipboard'
                action['JsonRPCAction']['parameters'] = [param]

                if os.path.isdir(param):
                    cdpl(param)

                    # normal message update
                    res_format['Title'] = "Done."
                    res_format['SubTitle'] = "Open the Path."

                    # normal message update
                    action['JsonRPCAction']['method'] = 'openFolder'

            res_format.update(action)
        else:
            res_format['Title'] = "cDPL"
            res_format['SubTitle'] = "Input the path of video folder."

        result.append(res_format)

        return result

    def copy2clipboard(self, value):
        pyperclip.copy(value)

    def openFolder(self, path: str):
        os.startfile(path)
        WoxAPI.change_query(path)
