class Database(object):
    def __init__(self, db_name: str, db_host: str, db_user: str, db_pass: str, db_port: int):
        self.db_name = db_name
        self.db_host = db_host
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_port = db_port

    def conn_db(self):
        self.conn = psycopg2.connect(
                host=self.db_host,
                database=self.db_name,
                user=self.db_user,
                password=self.db_pass,
                port=self.db_port
        )
        self.cursor = self.conn.cursor()

    def query_db(self, db_query: str):
        self.conn_db()
        self.cursor.execute(db_query)

        if "select" in db_query.lower():
            logger.info(f"Shifarbot has executed a query and retrieved records from database: [ {self.db_name} ]")
            result = self.cursor.fetchall()
            self.conn.close()
            return result
        else:
            self.conn.commit()
            self.conn.close()
            logger.warn(f"Shifarbot has modified the database: [ {self.db_name} ].  Closing connection.")
