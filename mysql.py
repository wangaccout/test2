import pymysql

def dbconnect():
    # 建立数据库连接
    dbmysql = pymysql.connect(user='root', password='root', host='localhost',database='test', port=3306)
    # print(mysql)
    # print(type(mysql))
    # 使用cursor（）创建一个游标对象
    dbcursor = dbmysql.cursor()
    # 使用execute（）方法执行SQL
    sql = 'select * from borrw where cno=1'
    dbcursor.execute(sql)
    # 使用fetchone()方法获取单条数据
    data = dbcursor.fetchone()
    dataall = dbcursor.fetchall()
    dbcursor.close()
    dbmysql.close()
    return ('查询出来的数据为：', data, dataall)

if __name__ == '__main__':
    print(dbconnect())

