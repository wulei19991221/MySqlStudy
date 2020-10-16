# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年08月31日10时
# @File: 班级表.py
import pymysql
from print_color import *


class ClassMateSql:
    def __init__(self):
        self.connect = pymysql.Connect()

    def run(self):
        pass


if __name__ == '__main__':
    sql = ClassMateSql()
    sql.run()
