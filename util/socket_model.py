"""
@Time    : 2020/1/21 15:44
@Author  : weijiang
@Site    : 
@File    : socket_model.py
@Software: PyCharm
"""
import os
import socket
import time

from PyQt5.QtCore import QObject, pyqtSignal


class TCPSocketServer(QObject):
    send_info_signal = pyqtSignal(str)

    def __init__(self, host=None, port=None):
        super(TCPSocketServer, self).__init__()
        self._host = host
        self._port = port
        self._s = None
        self._count = 0
        self.rec_end_flag = False
        self.send_info_tag = 0

    def star_server(self):
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.bind((self._host, self._port))
        self._s.listen(5)
        while True:
            if self._count == 0:
                sock, addr = self._s.accept()
                self.send_info_signal.emit('<span style="color: #00ff00">>>>connect successful...</span>')
                data = sock.recv(1024)
                file_total_size = int(data.decode())
                received_size = 0
                sock.send('received'.encode())
                data = sock.recv(1024)
                filepath = str(data.decode())
                f = open(filepath, 'wb')
                self._count += 1
                self.send_info_signal.emit('<span style="color: red">>>>file size is {}</span>'.format(file_total_size))
            while received_size < file_total_size:
                data = sock.recv(1024)
                f.write(data)
                received_size += len(data)
                if self.send_info_tag == 0:
                    self.send_info_signal.emit(
                        '>>>received size is {} bytes, finished state is {}%'.format(received_size,
                                                                                     round((
                                                                                                       received_size / file_total_size) * 100,
                                                                                           2)))
                elif self.send_info_tag >= 10:
                    self.send_info_signal.emit(
                        '>>>received size is {} bytes, finished state is {}%'.format(received_size,
                                                                                     round((
                                                                                                       received_size / file_total_size) * 100,
                                                                                           2)))
                    self.send_info_tag = 0
                self.send_info_tag += 1
            data = sock.recv(1024)
            # 当前文件传输结束标志
            if data == b'end':
                self.rec_end_flag = True
            if self.rec_end_flag:
                self.send_info_signal.emit('>>>transfer was done.')
                f.close()
                sock.close()
                self._count = 0
            self.rec_end_flag = False


class TCPSocketClient(QObject):
    send_info_signal = pyqtSignal(str)

    def __init__(self, host=None, port=None, file_path=None):
        super(TCPSocketClient, self).__init__()
        self._host = host
        self._port = port
        self.file_path = file_path
        self.file_size = str(os.path.getsize(self.file_path))
        self.file_name = os.path.split(self.file_path)[1]
        self.count = 0

    def connect_server(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self._host, self._port))
            # with open(self.file_path, 'rb') as f:
            #     file = f
            file = open(self.file_path, 'rb')
            while True:
                if self.count == 0:
                    s.send(self.file_size.encode())
                    s.recv(1024)
                    s.send(self.file_name.encode())
                self.send_info_signal.emit('<span style="color: #0000ff">>>>start send file...</span>')
                st = time.time()
                for line in file:
                    s.send(line)
                s.send(b'end')
                break
            s.close()
            file.close()
            self.send_info_signal.emit('<span style="color: #ff0000">>>>send file successful, cost {} seconds...</span>'
                                       .format(time.time() - st))
        except Exception as e:
            print(e.args)
            self.send_info_signal.emit('<span style="color: #ff0000">>>>server connect failed...</span>')
