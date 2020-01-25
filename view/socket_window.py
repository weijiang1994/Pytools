# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'socket_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(677, 376)
        Form.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.socket_listWidget = QtWidgets.QListWidget(Form)
        self.socket_listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.socket_listWidget.setFlow(QtWidgets.QListView.LeftToRight)
        self.socket_listWidget.setObjectName("socket_listWidget")
        item = QtWidgets.QListWidgetItem()
        self.socket_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.socket_listWidget.addItem(item)
        self.verticalLayout.addWidget(self.socket_listWidget)
        self.socket_stackedWidget = QtWidgets.QStackedWidget(Form)
        self.socket_stackedWidget.setObjectName("socket_stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.socket_stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.socket_stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.socket_stackedWidget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.socket_listWidget.isSortingEnabled()
        self.socket_listWidget.setSortingEnabled(False)
        item = self.socket_listWidget.item(0)
        item.setText(_translate("Form", "服务端"))
        item = self.socket_listWidget.item(1)
        item.setText(_translate("Form", "客户端"))
        self.socket_listWidget.setSortingEnabled(__sortingEnabled)

