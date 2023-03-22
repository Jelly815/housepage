# -*- coding: utf-8 -*-

import mysql.connector

class DB_CONN:
    def __init__(self):
        self._db_connection = mysql.connector.connect(host="localhost", user="root",   password ="11q2a3z4@1W2S3X4", database="myweb")
        self._cursor = self._db_connection.cursor(buffered=True,dictionary=True)


    def __del__(self):
        self._db_connection.close()


    def executemany(self,sql, params=None):
        return self._cursor.executemany(sql, params or ())

    def execute(self, sql, params=None):
        return self._cursor.execute(sql, params or ())

    def fetchall(self):
        return self._cursor.fetchall()

    def fetchone(self):
        return self._cursor.fetchone()


'''
import db_connect
x = db_connect.DB_CONN()

AA = x.execute("SELECT `id` FROM `ex_user` WHERE `unid` = 'm199cdc39ee6e65811960a187ccf1fcb9'")
rows = x.fetchall()    # get all selected rows, as Barmar mentioned
for r in rows:
    print(r)
'''
