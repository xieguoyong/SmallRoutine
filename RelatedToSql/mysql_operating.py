import pymysql.cursors
import configparser     # 解析.ini配置的模块
import os

# ================== 读取.ini配置信息 ==================
base_dir = os.path.abspath(os.path.dirname(__file__))
# base_dir = base_dir.replace('\\', '/')
# print(base_dir)
file_path = base_dir + '\db_config.ini'
# print(file_path)

cf = configparser.ConfigParser()
cf.read(file_path)
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


if '__name__' == '__main__':
    pass



