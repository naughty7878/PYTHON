import pymysql


def query_one():
    # 打开数据库连接
    # pymysql.connect() 函数返回的是一个 PyMySQL 的 Connection 对象，该对象用于表示数据库连接。通过该对象，你可以执行 SQL 查询、获取查询结果、提交事务、关闭连接等操作
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='test')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = connect.cursor()

    # 使用 execute() 方法执行sql查询
    cursor.execute('SELECT VERSION()')

    # 使用 fetchone() 方法获取单条数据
    data = cursor.fetchone()

    print("Database version: %s" % data)

    # 关闭数据库连接
    connect.close()


def create_table():
    # 打开数据库连接
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='test')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = connect.cursor()

    # 使用 execute() 方法执行sql,创建表
    cursor.execute('''
        CREATE TABLE employee (
         first_name  varchar(20) NOT NULL,
         last_name  varchar(20),
         age INT,  
         sex varchar(1),
         income float )
    ''')

    # 关闭数据库连接
    connect.close()


def insert_data():
    # 打开数据库连接
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='test')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = connect.cursor()

    # SQL 插入语句
    sql = """INSERT INTO `test`.`employee` (`first_name`, `last_name`, `age`, `sex`, `income`) 
        VALUES ('蓝', '小', 19, '男', 2000)"""

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        connect.commit()
    except Exception as e:
        print(e)
        # 发生错误时回滚
        connect.rollback()

    # 关闭数据库连接
    connect.close()


def query_data():
    # 打开数据库连接
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='test')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = connect.cursor()

    # SQL 查询语句
    sql = """SELECT * FROM employee
        WHERE income > %s""" % 1000

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchall()
        print(type(result), result)
        # 遍历
        for row in result:
            print(type(row), row)
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print("fname=%s,lname=%s,age=%d,sex=%s,income=%s" % (fname, lname, age, sex, income))

    except Exception as e:
        print(e)

    # 关闭数据库连接
    connect.close()


def update_data():
    # 打开数据库连接
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='test')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = connect.cursor()

    sql = """UPDATE employee 
    SET age = age + 1
    WHERE sex = '%s'""" % '男'
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        connect.commit()
    except Exception as e:
        print(e)
        # 发生错误时回滚
        connect.rollback()

    # 关闭数据库连接
    connect.close()


def delete_data():
    # 打开数据库连接
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='test')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = connect.cursor()

    sql = "DELETE FROM employee WHERE age > %d" % 19
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        connect.commit()
    except Exception as e:
        print(e)
        # 发生错误时回滚
        connect.rollback()

    # 关闭数据库连接
    connect.close()


if __name__ == '__main__':
    # query_one()
    # create_table()
    # insert_data()
    # query_data()
    # update_data()
    # delete_data()
    print("执行结束")
