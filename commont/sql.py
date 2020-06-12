import pymysql
import pytest

from commont.logger import Logger


class Sql:
    def __init__(self):
        self.logger=Logger().logger()

    def select_sql(self):


        self.connect = pymysql.connect(host="10.7.129.247",
                                                              user="mysql",
                                                              password="YGBXygbx123!",
                                                              database="ipsdb_dev")
        # print(self.connect)
        self.cursor = self.connect.cursor()
        self.sql = "select * from policy_analysis_comcode"
        self.cursor.execute(self.sql)
        self.data = self.cursor.fetchall()  ##所有的数据
        # print(self.data)

        self.logger.debug("查询到的数据为{}".format(self.data))


        # print(type(self.data))

# print(len(self.data))
# print(self.cmd.fetchone()) #获取结果集中的第一行，每执行一次就指向下一行
#         print(self.cmd.fetchmany(3))  # 获取结果集中的num行记录
# print(self.res)

# 批量插入使用 executemany()方法，该方法的第二个参数是一个元组列表，第一个参数是sql语句
# commit()对数据进行更新（插入、删除、修改），一定用到这个方法，否则数据没有做更新。

# ssql='select * from student where sname=%s and sid=%s'
# sval=('tifa',2)

# self.ssql = 'insert into student(sid,sname)values(%s,%s)'
# self.sval = [(10, 'susu'), (11, '待招恶徒'), (12, '不必追')]
# self.cursor.executemany(self.ssql, self.sval)  # 批量插入记录
# self.connect.commit()  # 对数据进行更新（插入、删除、更新）的话，必须用到这个方法，才会把更新的数据更新到数据库
# print(self.cmd.rowcount, '条记录插入成功')  # 对数据更新（插入、删除、修改）返回影响行数
# self.cursor.execute('select * from student')
# print(self.cursor.fetchall())


if __name__ == '__main__':
    s = Sql()
s.select_sql()
