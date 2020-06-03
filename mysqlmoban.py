# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年05月27日15时
# @File: mysqlmoban.py
from print_color import *
import pymysql


class MoBan(object):
    # 初始化
    def __init__(self):
        # 链接数据库
        self.connect = pymysql.Connection(host='localhost', port=3306, user='root', password='wulei',
                                          database='yinwu1801',
                                          charset='utf8')
        self.cursor = self.connect.cursor()
        self.all_tables = {}
        self.all_databases = {}
        self.sys_database = ['information_schema', 'mysql', 'performance_schema', 'sys']

    # 结束时,断开mysql
    def __del__(self):
        # 关闭数据库
        self.cursor.close()
        self.connect.close()

    # 显示自己创建的数据库
    def show_database(self):
        sql = 'show databases;'
        self.execute_sql(sql)
        mysqls = [i[0] for i in self.cursor.fetchall() if i[0] not in self.sys_database]
        self.all_databases = dict(enumerate(mysqls, 1))
        for k, v in self.all_databases.items():
            print_c(fcyan, str(k) + ':\t' + v)
        self.select_database()

    def select_database(self):
        database = input('输入对应序号,选择数据库(exit退出): ')
        if database == 'exit':
            exit()
        try:
            sql = f'''use {self.all_databases.get(int(database))}'''
            self.execute_sql(sql)
        except (NameError, pymysql.err.ProgrammingError, ValueError):
            print_c(fred, '输入有误, 请重新输入')
            self.select_database()

    # 执行sql语句
    def execute_sql(self, sql):
        self.cursor.execute(sql)
        self.connect.commit()

    def show_tables(self):
        sql = 'show tables;'
        self.execute_sql(sql)
        result = self.cursor.fetchall()
        if result:
            for i in result:
                print_c(fgreen, i[0])
        else:
            print_c(fred, '还没创建表')

    def run(self):
        # 显示所有创建的数据库并提供选择
        self.show_database()
        self.show_tables()
        # self.addtables()
        # self.add_numericField()


if __name__ == '__main__':
    mysql = MoBan()
    mysql.run()
