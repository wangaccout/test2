import pymysql
import datetime

dbmysql = pymysql.connect(
    user='root',
    password='root',
    host='localhost',
    database='test',
    port=3306
)
dbcursor = dbmysql.cursor()
def dbconnect():
    # 建立数据库连接
    # dbmysql = pymysql.connect(
    #     user='root',
    #     password='root',
    #     host='localhost',
    #     database='test',
    #     port=3306)
    # print(mysql)
    # print(type(mysql))
    # 使用cursor（）创建一个游标对象
    # dbcursor = dbmysql.cursor()
    # 使用execute（）方法执行SQL
    sql = 'select * from borrw where cno=3'
    insertSql = 'insert into borrw(cno,bno,rdate) values (5,2,now())'
    dbcursor.execute(sql)
    print('execute方法影响的行数为：', dbcursor.rowcount)
    print('execute方法影响的列名为：', dbcursor.description)

    # 使用fetchone()方法获取单条数据
    data = dbcursor.fetchone()
    # dataall = dbcursor.fetchall()
    dbcursor.execute(insertSql)
    dbmysql.commit()
    print('execute方法影响的行数为：', dbcursor.rowcount)
    print('execute方法影响的列名为：', dbcursor.description)
    dbcursor.close()
    dbmysql.close()
    # return ('查出来的全部数据为', dataall)
    return('查询出来的数据为：', data)

# def update():
#     # dbmysql = pymysql.connect(
#     user='root',
#     password='root',
#     host='localhost',
#     database='test',
#     port=3306)
#     # dbcursor = dbmysql.cursor()
#     sql = 'update borrw set bno=1 where cno=3'
#     try:
#         dbcursor.execute(sql)
#         dbmysql.commit()
#         print('数据更新成功')
#     except Exception:  #常规错误的基类
#         print('数据更新失败')
#         dbmysql.rollback()  # 如果发生错误就回滚
#     finally:
#         dbcursor.close()
#         dbmysql.close()

# data = {
#     'rdate':''
# }
#
# def msgSource(data):
#     sql = """select * from borrw where 1=1"""
#     if data.get('cno'):
#         sql = sql + 'and rdate >= to_date('%s','yyyy-mm-dd hh24:mi:ss')'% data['rdate']
#     sql = sql + 'order by id'
#     return sql

if __name__ == '__main__':
    print(dbconnect())
    # update()
    # sql = msgSource(data)
    # print(sql)
