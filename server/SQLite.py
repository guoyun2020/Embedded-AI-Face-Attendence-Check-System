# 导入数据库驱动
import sqlite3
import pickle


# path = 'facedata.pkl'  # path='/root/……/aus_openface.pkl'   pkl文件所在路径
#
# f = open(path, 'rb')
# data = pickle.load(f)

def dict_factory(cursor, row):
    d = {}
    for index, col in enumerate(cursor.description):
        d[col[0]] = row[index]
    return d


def getInfo(name):
    # 连接到数据库
    # 数据库文件是“test.db”
    # 如果数据库不存在的话，将会自动创建一个 数据库
    conn = sqlite3.connect("student.db")

    conn.row_factory = dict_factory
    cursor = conn.cursor()

    # 查询一条记录：
    sql = "select name from student"
    cursor.execute(sql)
    # 获取查询结果：
    values = cursor.fetchall()
    index = 0
    for i in values:
        if i['name'] == name:
            sql = "select * from student"
            cursor.execute(sql)
            value = cursor.fetchall()
            return value[index]
        index = index + 1
    # 关闭游标：
    cursor.close()
    # 提交事物
    conn.commit()
    # 关闭连接
    conn.close()


def getNameList():
    conn = sqlite3.connect("student.db")

    conn.row_factory = dict_factory
    cursor = conn.cursor()

    # 查询一条记录：
    sql = "select name from student"
    cursor.execute(sql)
    # 获取查询结果：
    values = cursor.fetchall()
    names=[]
    for i in values:
        if i['name'] != 'Unknown':
            names.append(i['name'])
    return names
