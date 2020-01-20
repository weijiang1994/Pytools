"""
@author: weijiang
@license: (@)Copyright 2001-2018,SZ_Colibri
@file: frozenDir.py
@time: 2018/10/18 13:37
@desc:
"""
import sys
import os

def app_path():
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)
