"""
@Time    : 2020/1/20 16:12
@Author  : weijiang
@Site    : 
@File    : db.py
@Software: PyCharm
@License: (@)Copyright 2001-2019,SZ_Colibri
@Contact:weijiang@colibri.com.cn
"""
import pymysql


class DBOperator:

    def __init__(self, host='127.0.0.1', port=3306, username='root', pwd='root', db='rms'):
        self._conn = pymysql.connect(host=host, port=int(port), user=username, password=pwd, db=db)
        self._cur = self._conn.cursor()
        self.db = db

    def clear(self):
        self._cur.close()
        self._conn.close()

    def get_all_table(self):
        results = []
        sql = '''SHOW TABLES'''
        self._cur.execute(sql)
        result = self._cur.fetchall()
        for i in range(len(result)):
            results.append(result[i][0])
        return results
