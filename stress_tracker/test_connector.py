import unittest
from unittest.mock import Mock, patch, MagicMock
import configparser
import mysql.connector
from connector import Database

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

    def test_getUserData(self):
        db = Database("config.ini")
        db.connect_database()
        result = db.getUserData("user", "1")
        self.assertIsInstance(result, dict)

    def test_InsertUser(self):
        db = Database("config.ini")
        result = db.insert_user(
            "lisa",
            "lasr",
            "x",
            "lisa@gmail.com",
            "IT",
            "master",
            "lisa123",
            "1994-2-2",
            2020,
        )
        self.assertFalse(result, msg="Error faild to insert to table")


if __name__ == "__main__":
    unittest.main()
