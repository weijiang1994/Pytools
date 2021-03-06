# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pip_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(712, 310)
        Form.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setStyleSheet("font: 14pt \"Arial\";")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.add_user_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.add_user_checkBox.setObjectName("add_user_checkBox")
        self.gridLayout.addWidget(self.add_user_checkBox, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lib_version_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lib_version_lineEdit.setObjectName("lib_version_lineEdit")
        self.horizontalLayout_2.addWidget(self.lib_version_lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lib_name_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lib_name_lineEdit.setObjectName("lib_name_lineEdit")
        self.horizontalLayout.addWidget(self.lib_name_lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setStyleSheet("font: 14pt \"Arial\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 20)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.install_lib_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.install_lib_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.install_lib_pushButton.setObjectName("install_lib_pushButton")
        self.horizontalLayout_4.addWidget(self.install_lib_pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setStyleSheet("font: 13pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "PIP配置"))
        self.add_user_checkBox.setText(_translate("Form", "--user"))
        self.label_2.setText(_translate("Form", "版本:"))
        self.lib_version_lineEdit.setPlaceholderText(_translate("Form", "库版本(不强制)"))
        self.label.setText(_translate("Form", "库名:"))
        self.lib_name_lineEdit.setPlaceholderText(_translate("Form", "输入库名"))
        self.groupBox_2.setTitle(_translate("Form", "PIP源设置"))
        self.label_3.setText(_translate("Form", "源头:"))
        self.comboBox.setItemText(0, _translate("Form", "默认源"))
        self.comboBox.setItemText(1, _translate("Form", "http://mirrors.aliyun.com/pypi/simple/"))
        self.comboBox.setItemText(2, _translate("Form", "http://pypi.douban.com/simple/"))
        self.comboBox.setItemText(3, _translate("Form", "https://pypi.tuna.tsinghua.edu.cn/simple/"))
        self.comboBox.setItemText(4, _translate("Form", "http://pypi.mirrors.ustc.edu.cn/simple/"))
        self.comboBox.setItemText(5, _translate("Form", "http://pypi.hustunique.com/"))
        self.install_lib_pushButton.setText(_translate("Form", "开始安装"))

