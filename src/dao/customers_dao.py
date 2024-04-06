import logging as logger
from src.utilities.db_utils import DBUtils


class CustomersDAO(object):
    def __init__(self):
        self.db_utils = DBUtils()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM `wp_users` WHERE `user_email` = '{email}';"
        rs_db = self.db_utils.execute_select(sql)
        logger.debug("Executed DB query for get customer by email: %s", sql)
        return rs_db

    def get_all_customers(self):
        sql = "SELECT * FROM `wp_users` LIMIT 5000;"
        rs_db = self.db_utils.execute_select(sql)
        logger.debug("Executed DB query for get customer by email: %s", sql)
        return rs_db
