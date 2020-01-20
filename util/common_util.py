"""
@Time    : 2020/1/20 14:10
@Author  : weijiang
@Site    : 
@File    : common_util.py
@Software: PyCharm
@License: (@)Copyright 2001-2019,SZ_Colibri
@Contact:weijiang@colibri.com.cn
"""
import traceback
from functools import wraps

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog

import frozen_dir

SUPER_DIR = frozen_dir.app_path()
APP_ICON = SUPER_DIR+r'/res/img/app_icon.png'


def read_qss(file_path: str) -> object:
    """
    According to the file path to read qss file
    :param file_path: the qss file path
    :return: the qss file stream
    """
    with open(file_path, 'r') as f:
        return f.read()


def hint_dialog(widget: QWidget, icon_path: str, title: str, content: str) -> None:
    """
    display a dialog with choose button
    :param widget: the dialog rely on the father window
    :param icon_path: the dialog icon path
    :param title: the dialog title word
    :param content: the dialog content is used to hint user's
    :return: None
    """
    tip_box = QMessageBox(QMessageBox.Information, title, content)
    tip_box.setWindowIcon(QIcon(icon_path))
    submit = tip_box.addButton(widget.tr('确定'), QMessageBox.YesRole)
    tip_box.setModal(True)
    tip_box.exec_()
    if tip_box.clickedButton() == submit:
        pass
    else:
        return


def except_handler(fun):
    """
    异常处理装饰器函数
    :param fun: 待装饰的函数
    :return: 异常处理结果
    """
    @wraps(fun)
    def wrapper(*args, **kwargs):
        try:
            try_result = fun(*args, **kwargs)
            return try_result
        except KeyError as e:
            error_warning = {
                'error_warning': 'A key error has occurred. Please check if the keys of the uploaded json are correct.'
                                 + repr(e), 'error_tag': 1}
            print(error_warning)
            traceback.print_exc()
        except TypeError as e:
            error_warning = {
                'error_warning': 'A type error has occurred. Please check if the uploaded json data type is correct.'
                                 + repr(e), 'error_tag': 1}
            print(error_warning)
            traceback.print_exc()
        except Exception as e:
            error_warning = {'error_warning': repr(e), 'error_tag': 1}
            print(error_warning)
            traceback.print_exc()
    return wrapper


def open_choose_file_dialog(dialog_title: str, file_path: str, file_type_format: str) -> tuple:
    try:
        file_name, file_type = QFileDialog.getOpenFileName(None, dialog_title, file_path, file_type_format)
        if file_name is not None and file_type is not None:
            return file_name, file_type
        else:
            return None
    except Exception as e:
        print(e.args)


def open_folder(parent, title, file_path):
    path = QFileDialog.getExistingDirectory(parent, title, file_path)
    return path


def display_cmd_info(widget, msg):
    if 'Traceback' in msg or 'Exception' in msg or 'Failed' in msg:
        msg = '<span style=" color:#ff0000;">' + msg + '</span>'
    if 'Successful' in msg:
        msg = '<span style=" color:#00ff00;">' + msg + '</span>'
    widget.append(msg)
