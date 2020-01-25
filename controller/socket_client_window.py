"""
@Time    : 2020/1/25 13:32
@Author  : weijiang
@Site    : 
@File    : socket_client_window.py
@Software: PyCharm
"""
import sys

from view.socker_client_window import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication
from util.style import CAL_PUSHBUTTON_STYLE
from util.common_util import read_qss, SUPER_DIR, hint_dialog, APP_ICON, open_choose_file_dialog
from util.socket_model import TCPSocketClient


class SocketClientWindow(Ui_Form, QWidget):

    def __init__(self):
        super(SocketClientWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.init_slot()

    def init_ui(self):
        self.connect_server_pushButton.setStyleSheet(CAL_PUSHBUTTON_STYLE)
        self.send_file_pushButton.setStyleSheet(CAL_PUSHBUTTON_STYLE)
        self.host_lineEdit.setStyleSheet(read_qss(SUPER_DIR+r'/res/qss/lineedit_qss.qss'))
        self.choose_file_path_lineEdit.setStyleSheet(read_qss(SUPER_DIR+r'/res/qss/lineedit_qss.qss'))
        self.port_lineEdit.setStyleSheet(read_qss(SUPER_DIR+r'/res/qss/lineedit_qss.qss'))
        self.tcp_checkBox.setChecked(True)
        self.tcp_checkBox.setStyleSheet(read_qss(SUPER_DIR + r'/res/qss/checkbox_qss.qss'))
        self.udp_checkBox.setStyleSheet(read_qss(SUPER_DIR + r'/res/qss/checkbox_qss.qss'))

    def init_slot(self):
        self.connect_server_pushButton.clicked.connect(lambda: self.slot('connect'))
        self.send_file_pushButton.clicked.connect(lambda: self.slot('send'))
        self.choose_file_path_lineEdit.selectionChanged.connect(self.open_file)

    def open_file(self):
        file_name, file_type = open_choose_file_dialog('选择发送的文件', '', '所有文件 *.*;; exe文件 *.exe;; txt文件 *.txt')
        self.choose_file_path_lineEdit.setText(file_name)

    def slot(self, tag):
        if tag == 'connect':
            try:
                host = self.host_lineEdit.text()
                port = int(self.port_lineEdit.text())
                file_path = self.choose_file_path_lineEdit.text()
                if '' in [port, host, file_path]:
                    hint_dialog(self, APP_ICON, '提示', '请输入关键信息!')
                    return
                client = TCPSocketClient(host=host, port=port, file_path=file_path)
                client.send_info_signal.connect(self.display_info)
                client.connect_server()
            except Exception as e:
                print(e.args)

        if tag == 'send':
            pass

    def display_info(self, msg):
        self.textBrowser.append(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SocketClientWindow()
    win.show()
    sys.exit(app.exec_())
