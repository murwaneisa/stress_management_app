import unittest
from unittest.mock import Mock, patch, MagicMock
import configparser
import mysql.connector

config = configparser.ConfigParser()
# read the configuration file to get the
config.read("config.ini")


class TestGame(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
