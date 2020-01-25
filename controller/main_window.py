"""
@Time    : 2020/1/20 13:36
@Author  : weijiang
@Site    : 
@File    : main_window.py
@Software: PyCharm
"""
from PyQt5.QtGui import QFont, QIcon

from view.mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from util.style import LEFT_WIDGET_STYLE
from controller.pip_window import PipWindow
from util.common_util import APP_ICON
from controller.sql_window import SQLWindow
from controller.socket_window import SocketWindow


class CmdMainWindow(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(CmdMainWindow, self).__init__()
        self.setupUi(self)
        self.pip_window = PipWindow()
        self.sql_window = SQLWindow()
        self.socket_window = SocketWindow()
        self.init_ui()
        self.init_slot()

    def init_ui(self):
        font = QFont()
        font.setFamily('Arial')
        font.setPointSize(14)
        self.listWidget.setCurrentRow(0)
        self.setWindowTitle('PyTools Version 1.0.0 Beta')
        self.listWidget.setStyleSheet(LEFT_WIDGET_STYLE)
        self.setStyleSheet("QWidget:focus{outline: none;}")
        self.setWindowIcon(QIcon(APP_ICON))
        self.stackedWidget.addWidget(self.pip_window)
        self.stackedWidget.removeWidget(self.page)
        self.stackedWidget.removeWidget(self.page_2)
        self.stackedWidget.addWidget(self.sql_window)
        self.stackedWidget.addWidget(self.socket_window)

    def init_slot(self):
        self.listWidget.currentItemChanged.connect(self.change_frame)

    def change_frame(self):
        self.stackedWidget.setCurrentIndex(self.listWidget.currentRow())
