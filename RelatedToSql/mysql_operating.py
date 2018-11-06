import pymysql.cursors
import configparser     # 解析.ini配置的模块
import os
import time

# ================== 读取.ini配置信息 ==================
base_dir = os.path.abspath(os.path.dirname(__file__))
# base_dir = base_dir.replace('\\', '/')
# print(base_dir)
conf_path = base_dir + '\db_config.ini'
# print(file_path)
sql_path = base_dir + '\sql.txt'

cf = configparser.ConfigParser()
cf.read(conf_path)
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")
db_name = cf.get("mysqlconf", "db_name")


class Mysql:
    # ===================== mysql 操作 ======================
    def __init__(self):
        try:
            # 数据库连接
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db_name,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # 清空表数据
    def clear(self, table_name):
        real_sql = 'delete from ' + table_name + ';'
        # print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)

        self.connection.commit()

    # 插入表数据
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"

        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "insert into " + table_name + " (" + key + ") values (" + value + ")"
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()


    # 查询表
    def select(self, table_name):
        real_sql = "select * from " + table_name

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            all_data = cursor.fetchall()
            # print(all_data)
            self.result(table_name, all_data)

    # 将查询结果写入文件
    def result(self, table_name, data):
        if not os.path.exists(sql_path):
            open(sql_path, 'w')
        else:
            with open(sql_path, 'a+', encoding="utf-8") as f:
                # 写入表名
                f.write(str(table_name) + ':' + '\n')
                # # 先清空文件再写入表数据
                # f.truncate()
                for dt in data:
                    f.write(str(dt) + '\n')

    # 关闭数据库连接
    def close(self):
        self.connection.close()

    # 数据处理
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for tb_data in data:
                self.insert(table, tb_data)

            self.select(table)


if __name__ == '__main__':

    past_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()-10000))
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    future_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()+10000))

    # create data
    datas = {
        'sign_event': [
            {'id': 1, 'name': '红米Pro发布会', '`limit`': 2000, 'status': 1, 'address': '北京会展中心', 'start_time': now_time, 'create_time': future_time},
            {'id': 2, 'name': '可参加人数为0', '`limit`': 0, 'status': 1, 'address': '北京会展中心', 'start_time': now_time, 'create_time': future_time},
            {'id': 3, 'name': '当前状态为0关闭', '`limit`': 2000, 'status': 0, 'address': '北京会展中心', 'start_time': now_time, 'create_time': future_time},
            {'id': 4, 'name': '发布会已结束', '`limit`': 2000, 'status': 1, 'address': '北京会展中心', 'start_time': now_time, 'create_time': future_time},
            {'id': 5, 'name': '小米5发布会', '`limit`': 2000, 'status': 1, 'address': '北京国家会议中心', 'start_time': now_time, 'create_time': future_time},
        ],
        'sign_guest': [
            {'id': 1, 'realname': 'alen', 'phone': 13511001100, 'email': 'alen@mail.com', 'sign': 0, 'create_time': future_time, 'event_id': 1},
            {'id': 2, 'realname': 'has sign', 'phone': 13511001101, 'email': 'sign@mail.com', 'sign': 1, 'create_time': future_time, 'event_id': 1},
            {'id': 3, 'realname': 'tom', 'phone': 13511001102, 'email': 'tom@mail.com', 'sign': 0, 'create_time': future_time, 'event_id': 5},
        ],
    }

    sql = Mysql()
    sql.init_data(datas)

    sql.close()

