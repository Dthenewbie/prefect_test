import pymysql
def connect_db():
    try:
        conn = pymysql.connect(
            host = 'host.docker.internal',
            port = 3306,
            user = 'root',
            passwd = 'password',
            db = 'Anti_Fraud'
        )
        # conn = pymysql.connect(
        # host = '35.229.167.236',
        # port = 3306,
        # user = 'root',
        # passwd = 'my-secret-pw',
        # db = 'Anti_Fraud'
        #   )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None