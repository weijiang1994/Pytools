"""
@Time    : 2020/1/20 15:11
@Author  : weijiang
@Site    : 
@File    : sql_window.py
@Software: PyCharm
@License: (@)Copyright 2001-2019,SZ_Colibri
@Contact:weijiang@colibri.com.cn
"""
import subprocess
from threading import Thread

from PyQt5.QtCore import pyqtSignal

from view.sql_window import Ui_Form
from PyQt5.QtWidgets import QWidget
from util.common_util import open_choose_file_dialog, open_folder, read_qss, SUPER_DIR, APP_ICON
from util.style import CAL_PUSHBUTTON_STYLE, VERTICAL_SCROLL_BAR_STYLE
from util.db import DBOperator
from util.common_util import hint_dialog, display_cmd_info


# noinspection PyBroadException,DuplicatedCode
class SQLWindow(Ui_Form, QWidget):
    exe_info_signal = pyqtSignal(str)
    exe_done_state_signal = pyqtSignal(int)

    def __init__(self):
        super(SQLWindow, self).__init__()
        self.setupUi(self)
        self.load_db_table_tag = False
        self.ls = [self.sqlacodegen_path_lineEdit, self.generate_file_path_lineEdit, self.db_host_lineEdit,
                   self.db_port_lineEdit, self.db_username_lineEdit, self.db_pwd_lineEdit,
                   self.export_filename_lineEdit, self.db_name_lineEdit]
        self.init_ui()
        self.init_slot()

    def init_ui(self):
        for ls in self.ls:
            ls.setStyleSheet(read_qss(SUPER_DIR + r'/res/qss/lineedit_qss.qss'))
        self.db_conn_test_pushButton.setStyleSheet(CAL_PUSHBUTTON_STYLE)
        self.generate_file_pushButton.setStyleSheet(CAL_PUSHBUTTON_STYLE)
        self.db_table_comboBox.setStyleSheet(read_qss(SUPER_DIR + r'/res/qss/combobox_qss.qss'))
        self.export_mode_comboBox.setStyleSheet(read_qss(SUPER_DIR + r'/res/qss/combobox_qss.qss'))
        self.db_table_comboBox.setVisible(False)
        self.db_table_label.setVisible(False)
        self.textBrowser.verticalScrollBar().setStyleSheet(VERTICAL_SCROLL_BAR_STYLE)

    def init_slot(self):
        self.exe_info_signal.connect(self.display_info)
        self.sqlacodegen_path_lineEdit.selectionChanged.connect(lambda: self.choose_path(1))
        self.generate_file_path_lineEdit.selectionChanged.connect(lambda: self.choose_path(2))
        self.export_mode_comboBox.currentIndexChanged.connect(self.change_export_mode)
        self.db_conn_test_pushButton.clicked.connect(lambda: self.btn_slot('test'))
        self.generate_file_pushButton.clicked.connect(lambda: self.btn_slot('generate'))

    def btn_slot(self, tag):
        if tag == 'test':
            db_name, host, port, pwd, username = self.get_db_info()
            if '' in [host, port, username, pwd, db_name]:
                hint_dialog(self, APP_ICON, '提示', '请输入数据库关键信息!')
                return
            try:
                db = DBOperator(host=host, port=port, username=username, pwd=pwd, db=db_name)
                self.textBrowser.append('<span style="color:#00ff00">>>>the '
                                        'connection to the database was successful.</span>')
                db.clear()
                del db
            except Exception as e:
                self.textBrowser.append('<span style="color:#ff0000">>>>{}</span>'.format(str(e.args)))

        if tag == 'generate':
            sqlacodegen_path = self.sqlacodegen_path_lineEdit.text()
            save_file_path = self.generate_file_path_lineEdit.text()
            db_name, host, port, pwd, username = self.get_db_info()
            file_name = self.export_filename_lineEdit.text()
            if '' in [sqlacodegen_path, save_file_path, file_name, db_name, host, port, pwd, username]:
                hint_dialog(self, APP_ICON, '提示', '请输入执行命令的关键信息!')
                return
            if self.export_mode_comboBox.currentIndex() == 1:
                sqlacodegen_cmd = '{} {} mysql+pymysql://{}:{}@{}:{}/{} > {}'.format(sqlacodegen_path,
                                                                                     self.db_table_comboBox.
                                                                                     currentText(),
                                                                                     username, pwd, host, port, db_name,
                                                                                     save_file_path + '/' + file_name)
            else:
                sqlacodegen_cmd = '{} mysql+pymysql://{}:{}@{}:{}/{} > {}'.format(sqlacodegen_path,
                                                                                  username, pwd, host, port, db_name,
                                                                                  save_file_path + '/' + file_name)
            th = Thread(target=self.sh, args=(sqlacodegen_cmd,))
            th.setDaemon(True)
            th.start()

    def sh(self, command):
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(p.stdout.readline, b''):
            line = line.strip().decode('utf-8')
            self.exe_info_signal.emit('>>>' + line)
        # self.cmd_execute_state_signal.emit(int(p.wait()))

    def choose_path(self, tag):
        if tag == 1:
            file_name, file_type = open_choose_file_dialog('选择sqlacodegen路径', '', 'exe文件(*.exe)')
            self.sqlacodegen_path_lineEdit.setText(file_name)
        if tag == 2:
            _path = open_folder(self, '选择保存文件夹', '')
            self.generate_file_path_lineEdit.setText(_path)

    def change_export_mode(self):
        if self.export_mode_comboBox.currentIndex() == 0:
            self.db_table_label.setVisible(False)
            self.db_table_comboBox.setVisible(False)
        else:
            self.db_table_label.setVisible(True)
            self.db_table_comboBox.setVisible(True)
            th = Thread(target=self.load_db_table)
            th.setDaemon(True)
            th.start()

    def display_info(self, tag):
        display_cmd_info(self.textBrowser, tag)

    def load_db_table(self):
        self.db_table_comboBox.clear()
        db_name, host, port, pwd, username = self.get_db_info()
        if '' in [host, port, username, pwd, db_name]:
            hint_dialog(self, APP_ICON, '提示', '请输入数据库关键信息!')
            return
        try:
            db = DBOperator(host=host, port=port, username=username, pwd=pwd, db=db_name)
            self.db_table_comboBox.addItems(db.get_all_table())
            self.textBrowser.append('<span style="color:#00ff00">>>>get '
                                    'the tables of this database was successful.</span>')
        except Exception as e:
            self.textBrowser.append('<span style="color: #ff0000">>>>{}</span>'.format(str(e.args)))
        finally:
            db.clear()
            del db

    def get_db_info(self):
        host = self.db_host_lineEdit.text()
        port = self.db_port_lineEdit.text()
        username = self.db_username_lineEdit.text()
        pwd = self.db_pwd_lineEdit.text()
        db_name = self.db_name_lineEdit.text()
        return db_name, host, port, pwd, username
