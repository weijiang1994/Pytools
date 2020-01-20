"""
@Time    : 2020/1/20 13:35
@Author  : weijiang
@Site    : 
@File    : run.py
@Software: PyCharm
@License: (@)Copyright 2001-2019,SZ_Colibri
@Contact:weijiang@colibri.com.cn
"""
from controller.main_window import CmdMainWindow
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CmdMainWindow()
    win.show()
    sys.exit(app.exec_())
