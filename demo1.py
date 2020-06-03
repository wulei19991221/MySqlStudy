# !/usr/bin/python3
# --coding:utf-8--
# @Author:吴磊
# @Time: 2020年05月20日20时
# @File: demo1.py
import pymysql
from print_color import *


class MyClasses:
    # 初始化
    def __init__(self):
        # 链接数据库
        self.connect = pymysql.Connection(host='localhost', port=3306, user='root', password='wulei',
                                          database='python_demo2',
                                          charset='utf8')
        self.cursor = self.connect.cursor()
        self.all_tables = {}

    # 结束时,断开mysql
    def __del__(self):
        # 关闭数据库
        self.cursor.close()
        self.connect.close()

    # 执行sql语句
    def execute_sql(self, sql):
        self.cursor.execute(sql)

    # 解析元组
    def parse_truple(self):
        for i in self.cursor.fetchall():
            for j in i:
                yield j

    # 判断查询语句
    def judge_input(self):
        print_c(fyellow, "输入序号,查看对应表格".center(30, '-'))
        for k, v in self.all_tables.items():
            print_c(fblue, f'{k}:\t{v}')
        get_id = input('输入对应序号(exit退出): ')
        if get_id == 'exit':
            exit()
        try:
            self.show_table_datas(self.all_tables.get(int(get_id)))
        except (NameError, pymysql.err.ProgrammingError, ValueError):
            print_c(fred, '输入有误, 请重新输入')
        finally:
            self.judge_input()

    # 查询表
    def select_tables(self):
        sql = 'show tables;'
        self.execute_sql(sql)
        self.all_tables = dict(enumerate(self.parse_truple()))
        self.judge_input()

    # 美化输出
    @staticmethod
    def beautiful(ts):
        temp = ''
        for t in ts:
            temp += f'{t}\t '
        return temp

    # 展示表中数据
    def show_table_datas(self, name, page=1):
        sql = f'select * from {name} limit {10 * (page - 1)}, 10;'
        self.execute_sql(sql)
        for i in self.cursor.fetchall():
            print_c(fgreen, self.beautiful(i))
        self.execute_sql(sql)
        if self.cursor.fetchone() is None:
            print_c(fred, '已到末尾')
        else:
            a = input('回车查看下一页? (y/n): ')
            if a == 'y' or a == 'Y':
                self.show_table_datas(name, page + 1)

    def run(self):
        # 选择表格
        self.select_tables()


if __name__ == '__main__':
    classes = MyClasses()
    classes.run()
