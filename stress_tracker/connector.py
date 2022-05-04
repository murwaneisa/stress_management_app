import configparser
import mysql.connector


class Database:
    def __init__(self):
        self.connector = None
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    def connect_database(self):
        try:
            self.connector = mysql.connector.connect(
                host=self.config.get(
                    "database", "db_host_key"
                ),  # get the credential from the config file
                user=self.config.get("database", "db_user_key"),
                password=self.config.get("database", "db_password_key"),
                database=self.config.get("database", "db_database_key"),
            )

        except Exception as er:
            print(er)

    def select_user(self):
        mycursor = self.connector.cursor()
        mycursor.execute("SELECT * FROM user")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def select_admin(self):
        mycursor = self.connector.cursor()
        mycursor.execute("SELECT * FROM admin")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def insert_user(self,
                    first_name,
                    last_name,
                    gender,
                    email,
                    program,
                    degree,
                    password,
                    age,
                    study_year
                    ):
        try:
            mycursor = self.connector.cursor()
            query = f"""INSERT INTO user (user_firstname, user_lastname, user_gender,
            user_email, user_program, user_degree, user_password, user_age, user_studyYear)
            VALUES ("{first_name}", "{last_name}", "{gender}", "{email}", "{program}", "{degree}", "{password}", "{age}", "{study_year}")"""
            mycursor.execute(query)
        except Exception as er:
            print(er)

    def insert_admin(self, first_name, last_name, email, password, title):
        try:
            mycursor = self.connector.cursor()
            query = f"""INSERT INTO admin (admin_firstname, admin_lastname, admin_email, admin_password, admin_title)
                VALUES ("{first_name}", "{last_name}", "{email}", "{password}", "{title}")"""
            mycursor.execute(query)
        except Exception as er:
            print(er)


# connect = Database.connect_database()
# Database.insert_user(
#     connect,
#     "Ahmed",
#     "moh",
#     "male",
#     "ahmed@gmail.com",
#     "management",
#     "master",
#     "ahmed123",
#     "21",
#     "second year",
# )
# Database.insert_admin(connect, "lisa", "adem", "lisa@gmail.com", "lisa123", "IT")
# Database.select_user(connect)
# Database.select_admin(connect)
