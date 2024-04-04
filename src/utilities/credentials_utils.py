from dotenv import load_dotenv
import os

load_dotenv()


class CredentialsUtils(object):
    def __init__(self):
        pass

    @staticmethod
    def get_db_credentials() -> dict:
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")

        if not db_user or not db_password:
            raise Exception(
                "Then API credentials 'db_user' and 'db_password' must be in env variables!"
            )
        else:
            return {"db_user": db_user, "db_password": db_password}

    @staticmethod
    def get_credentials() -> dict:
        wc_key = os.getenv("WC_KEY")
        wc_secret = os.getenv("WC_SECRET")

        if not wc_key or not wc_secret:
            raise Exception(
                "Then API credentials 'wc_key' and 'wc_secret' must be in env variables!"
            )
        else:
            return {"wc_key": wc_key, "wc_secret": wc_secret}
