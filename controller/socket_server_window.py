"""
@Time    : 2020/1/21 15:13
@Author  : weijiang
@Site    : 
@File    : socket_server_window.py
@Software: PyCharm
"""
import sys
from threading import Thread

from view.socker_server_window import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication
from util.common_util import read_qss, SUPER_DIR, hint_dialog, APP_ICON
from util.style import CAL_PUSHBUTTON_STYLE, VERTICAL_SCROLL_BAR_STYLE
from util.socket_model import TCPSocketServer


class SocketServerWindow(Ui_Form, QWidget):

    def __init__(self):
        super(SocketServerWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.init_slot()

    def init_ui(self):
        self.tcp_checkBox.setChecked(True)
        self.tcp_checkBox.setStyleSheet(read_qss(SUPER_DIR+r'/res/qss/checkbox_qss.qss'))
        self.udp_checkBox.setStyleSheet(read_qss(SUPER_DIR+r'/res/qss/checkbox_qss.qss'))
        self.start_server_pushButton.setStyleSheet(CAL_PUSHBUTTON_STYLE)
        self.open_folder_pushButton.setStyleSheet(CAL_PUSHBUTTON_STYLE)
        self.host_lineEdit.setStyleSheet(read_qss(SUPER_DIR+r'/res/qss/lineedit_qss.qss'))
        self.port_lineEdit.setStyleSheet(read_qss(SUPER_DIR+r'/res/qss/lineedit_qss.qss'))
        self.save_path_lineEdit.setStyleSheet(read_qss(SUPER_DIR+r'/res/qss/lineedit_qss.qss'))
        self.textBrowser.verticalScrollBar().setStyleSheet(VERTICAL_SCROLL_BAR_STYLE)

    def init_slot(self):
        self.start_server_pushButton.clicked.connect(self.start_server)

    def start_server(self):
        if self.tcp_checkBox.isChecked():
            try:
                host = self.host_lineEdit.text()
                port = self.port_lineEdit.text()
                if '' in [port, host]:
                    hint_dialog(self, APP_ICON, '提示', '请输入服务关键信息!')
                    return
                sock = TCPSocketServer(host=host, port=int(port))
                sock.send_info_signal.connect(self.display_socket_info)
                th = Thread(target=sock.star_server)
                th.setDaemon(True)
                th.start()
                self.textBrowser.append('<span style="color: green">>>>bind host {} and port {}</span>'.format(host,
                                                                                                               port))
                self.textBrowser.append('<span style="color: green">>>>listening...</span>')
            except Exception as e:
                print(e.args)
                import traceback
                traceback.print_exc()
        else:
            pass
        pass

    def display_socket_info(self, msg):
        self.textBrowser.append(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SocketServerWindow()
    win.show()
    sys.exit(app.exec_())
