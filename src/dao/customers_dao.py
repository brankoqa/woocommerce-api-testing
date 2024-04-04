from src.utilities.db_utils import DBUtils
import logging as logger


class CustomersDAO(object):
    def __init__(self):
        self.db_utils = DBUtils()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM `wp_users` WHERE `user_email` = '{email}';"
        rs_db = self.db_utils.execute_select(sql)
        logger.debug(f"Executed DB query for get customer by email: {sql}")
        return rs_db
