import pymysql

class Db():

    def __init__(self, host, user, password, port):
        self.conn_info = dict(
            host = host,
            user = user,
            password = password,
            port = port
        )

    def connect(self):
        return pymysql.connect(**self.conn_info)

    def execute(self, sql):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)

    

