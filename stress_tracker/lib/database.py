import configparser

import mysql.connector

config = configparser.ConfigParser()
# read the configuration file to get the
config.read("config.ini")


class Database:
    def connect_database():
        try:
            mydb = mysql.connector.connect(
                host=config.get(
                    "database", "db_host_key"
                ),  # get the credential from the config file
                user=config.get("database", "db_user_key"),
                password=config.get("database", "db_password_key"),
                database=config.get("database", "db_database_key"),
            )
            print(mydb)
            print("working")
        except Exception as er:
            print(er)


Database.connect_database()
