import pymysql.cursors
from dotenv import load_dotenv
import logging as logger

from src.utilities.credentials_utils import CredentialsUtils

load_dotenv()


class DBUtils(object):
    def __init__(self):
        self.creds = CredentialsUtils.get_db_credentials()
        self.host = "127.0.0.1"
        self.port = 3306

    def create_connection(self):
        conn = pymysql.connect(
            host=self.host,
            user=self.creds["db_user"],  # This is reg user password
            password=self.creds["db_password"],
            port=self.port,
            db="wordpress",
        )
        return conn

    def execute_select(self, sql):
        conn = self.create_connection()
        try:
            logger.debug(f"Executing SQL query: {sql}")
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n Error: {str(e)}")
        finally:
            conn.close()
        return rs_dict

    def execute_query(self, sql):
        pass
