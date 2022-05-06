import configparser
from distutils.log import error
import mysql.connector
import user

config = configparser.ConfigParser()
# read the configuration file to get the
config.read("config.ini")


class Database:
    
    def connect_database(self):
        try:
            mydb = mysql.connector.connect(
                host=config.get(
                    "database", "db_host_key"
                ),  # get the credential from the config file
                user=config.get("database", "db_user_key"),
                password=config.get("database", "db_password_key"),
                database=config.get("database", "db_database_key"),
            )
            return mydb
        except Exception as er:
            print(er)

    def fetch_users(self):
        conn = Database.connect_database(self)
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM user")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def fetch_admins(self):
        conn = Database.connect_database(self)
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM admin")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    
    def login_user(self, email, password):
        conn = Database.connect_database(self)
        mycursor = conn.cursor()
        mycursor.execute(f"SELECT * FROM user WHERE user_email = '{email}' AND user_password = '{password}'")
        myresult = mycursor.fetchall()
        if myresult:
            result = myresult[0]
            usr = user.User(result[0], result[1],result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9])
            return usr
        elif len(myresult) == 0:
            raise Exception("Username/password is incorrect")
        else:
            raise Exception("Unkown error occurred")
        
    def login_admin(self, email, password):
        conn = Database.connect_database(self)
        mycursor = conn.cursor()
        mycursor.execute(f"SELECT * FROM admin WHERE admin_email = '{email}' AND admin_password = '{password}'")
        myresult = mycursor.fetchall()
        if myresult:
            return myresult[0]
        elif len(myresult) == 0:
            raise Exception("Username/password is incorrect")
        else:
            raise Exception("Unkown error occurred")

    def signup_user(self, first_name,last_name,gender,email,program,degree,password,age,study_year):
        try:
            conn = Database.connect_database(self)
            mycursor = conn.cursor()
            query = f"""INSERT INTO user (user_firstname, user_lastname, user_gender, user_email, user_program, user_degree, user_password, user_age, user_studyYear)
            VALUES ("{first_name}", "{last_name}", "{gender}", "{email}", "{program}", "{degree}", "{password}", "{age}", "{study_year}")"""
            mycursor.execute(query)
        except Exception as er:
            print(er)

    def signup_admin(self, first_name, last_name, email, password, title):
        try:
            conn = Database.connect_database(self)
            mycursor = conn.cursor()
            query = f"""INSERT INTO admin (admin_firstname, admin_lastname, admin_email, admin_password, admin_title)
                VALUES ("{first_name}", "{last_name}", "{email}", "{password}", "{title}")"""
            mycursor.execute(query)
        except Exception as er:
            print(er)


#connect = Database.connect_database()
""" Database.insert_user(
    connect,
    "Ahmed",
    "moh",
    "male",
    "ahmed@gmail.com",
    "management",
    "master",
    "ahmed123",
    "21",
    "second year",
) """
# Database.insert_admin(connect, "lisa", "adem", "lisa@gmail.com", "lisa123", "IT")
# Database.select_user(connect)
# Database.select_admin(connect)
#Database.login_user(connect, "murwan@gmail.com", "murwan123")

# admin - lisa@gmai.ocm, lisa123