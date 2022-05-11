import unittest
from unittest.mock import Mock, patch, MagicMock
import configparser
import mysql.connector
from database import Database

config = configparser.ConfigParser()
# read the configuration file to get the
config.read("config.ini")


class TestDatabase(unittest.TestCase):
    def test_connect_database(self):
        try:
            mydb = mysql.connector.connect(
                host=config.get(
                    "database", "db_host_key"
                ),  # get the credential from the config file
                user=config.get("database", "db_user_key"),
                password=config.get("database", "db_password_key"),
                database=config.get("database", "db_database_key"),
            )
            self.assertIsInstance(mydb, object)
        except Exception as er:
            print(er)

    def test_userLogin(self):
        name = "murwan@gmail.com"
        password = "murwan123"
        result = Database.login_user(self, name, password)
        self.assertIsInstance(result, int)


if __name__ == "__main__":
    unittest.main()
