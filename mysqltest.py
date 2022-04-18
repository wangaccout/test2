import pymysql.connections

# 打开数据库连接
mydb = pymysql.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='test',
    # auth_plugin='mysql_native_password'
)
print(mydb)

# 使用cursor()方法创建一个游标对象cursor
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE runoob_db")
# mycursor.execute('show databases')
# for i in mycursor:
#     print(i)

# 使用execute()方法执行SQL语句
mycursor.execute('select * from books')
# data = mycursor.fetchone()  # 获取单条数据
# print('单条数据', data)

# 获取所有记录
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# 关闭数据库连接
mydb.close()