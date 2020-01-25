"""
@Time    : 2020/1/21 14:47
@Author  : weijiang
@Site    : 
@File    : socket_window.py
@Software: PyCharm
"""
import sys

from view.socket_window import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication
from util.style import TOP_WIDGET_STYLE
from controller.socket_server_window import SocketServerWindow
from controller.socket_client_window import SocketClientWindow


class SocketWindow(Ui_Form, QWidget):

    def __init__(self):
        super(SocketWindow, self).__init__()
        self.setupUi(self)
        self.socket_server_win = SocketServerWindow()
        self.socket_client_win = SocketClientWindow()
        self.init_ui()
        self.init_slot()

    def init_ui(self):
        self.socket_listWidget.setCurrentRow(0)
        self.socket_listWidget.setStyleSheet(TOP_WIDGET_STYLE)
        self.setStyleSheet("QWidget:focus{outline: none;}")
        self.socket_stackedWidget.removeWidget(self.page)
        self.socket_stackedWidget.removeWidget(self.page_2)
        self.socket_stackedWidget.addWidget(self.socket_server_win)
        self.socket_stackedWidget.addWidget(self.socket_client_win)

    def init_slot(self):
        self.socket_listWidget.currentItemChanged.connect(self.change_win)

    def change_win(self):
        self.socket_stackedWidget.setCurrentIndex(self.socket_listWidget.currentRow())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SocketWindow()
    win.show()
    sys.exit(app.exec_())
