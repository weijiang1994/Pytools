"""
@Time    : 2020/1/20 14:02
@Author  : weijiang
@Site    : 
@File    : pip_window.py
@Software: PyCharm
@License: (@)Copyright 2001-2019,SZ_Colibri
@Contact:weijiang@colibri.com.cn
"""
import subprocess
from threading import Thread

from PyQt5.QtCore import pyqtSignal

from view.pip_window import Ui_Form
from PyQt5.QtWidgets import QWidget
from util.style import CAL_PUSHBUTTON_STYLE, VERTICAL_SCROLL_BAR_STYLE
from util.common_util import read_qss, SUPER_DIR, hint_dialog, APP_ICON, except_handler


class PipWindow(Ui_Form, QWidget):
    cmd_info_signal = pyqtSignal(str)
    cmd_execute_state_signal = pyqtSignal(int)

    def __init__(self):
        super(PipWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.init_slot()

    def init_slot(self):
        self.cmd_info_signal.connect(self.display_cmd_info)
        self.install_lib_pushButton.clicked.connect(self.install)
        self.cmd_execute_state_signal.connect(self.display_execute_state)

    def init_ui(self):
        self.install_lib_pushButton.setStyleSheet(CAL_PUSHBUTTON_STYLE)
        self.lib_name_lineEdit.setStyleSheet(read_qss(SUPER_DIR+r'/res/qss/lineedit_qss.qss'))
        self.lib_version_lineEdit.setStyleSheet(read_qss(SUPER_DIR+r'/res/qss/lineedit_qss.qss'))
        self.comboBox.setStyleSheet(read_qss(SUPER_DIR+r'/res/qss/combobox_qss.qss'))
        self.add_user_checkBox.setStyleSheet(read_qss(SUPER_DIR+r'/res/qss/checkbox_qss.qss'))
        self.setStyleSheet("QWidget:focus{outline: none;}")
        self.textBrowser.verticalScrollBar().setStyleSheet(VERTICAL_SCROLL_BAR_STYLE)

    def install(self):
        try:
            lib_name = self.lib_name_lineEdit.text()
            lib_version = self.lib_version_lineEdit.text()
            source_path = self.comboBox.currentText()
            if lib_name == '':
                hint_dialog(self, APP_ICON, '提示', '请输入pip库名!')
                return
            if lib_version != '':
                lib_name = lib_name + '==' + lib_version

            if self.comboBox.currentIndex() == 0:
                pip_cmd = 'pip install --user {}'.format(lib_name)
            else:
                pip_cmd = 'pip install --user -i {} --trusted-host {} {}'.format(source_path,
                                                                                 source_path.split('//')[1].split('/')[
                                                                                     0],
                                                                                 lib_name)
            if not self.add_user_checkBox.isChecked():
                pip_cmd = pip_cmd.replace('--user', '')
            print(pip_cmd)
            th = Thread(target=self.sh, args=(pip_cmd, ))
            th.setDaemon(True)
            th.start()
        except Exception as e:
            print(e.args)

    @except_handler
    def sh(self, command):
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(p.stdout.readline, b''):
            line = line.strip().decode('utf-8')
            self.cmd_info_signal.emit('>>>' + line)
        self.cmd_execute_state_signal.emit(int(p.wait()))

    def display_cmd_info(self, msg):
        if 'Traceback' in msg or 'Exception' in msg or 'Failed' in msg:
            msg = '<span style=" color:#ff0000;">' + msg + '</span>'
        if 'Successful' in msg:
            msg = '<span style=" color:#00ff00;">' + msg + '</span>'
        self.textBrowser.append(msg)

    def display_execute_state(self, tag):
        if tag == 1:
            self.textBrowser.append('<span style="color: #ff0000">>>>some error occurred, please check the logs and '
                                    'retry.</span>')
        else:
            self.textBrowser.append('<span style="color: #00ff00">>>>Execute successful.</span>')
