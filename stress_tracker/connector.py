import configparser
import mysql.connector


class Database:
    def __init__(self, config_file="config.ini"):
        self.connector = None
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

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

    def getUserData(self, user_id, table):
        mc = self.connector.cursor()

        if table == "user":
            user_column = "user_id"
        elif table == "stats":
            user_column = "stats_userid"

        # retrieve column data
        mc.execute("show columns from "+str(table))
        result = mc.fetchall()

        # retrieve user data
        columns = []
        data = {}

        for record in result:
            colname = record[0]
            columns.append(colname)
            data[colname] = []

        mc.execute("SELECT * FROM "+str(table)+" WHERE "+user_column+" ="+str(user_id))
        result = mc.fetchall()

        for record in result:
            for i, value in enumerate(record):
                data[columns[i]].append(value)

        return data

    def getColumnData(self, column, table):
        mc = self.connector.cursor()

        mc.execute("SELECT "+column+" FROM "+table)
        result = mc.fetchall()

        data = []

        for record in result:
            data.append(record[0])

        return data

    def UpdateUserData(self, user_id, values, table):
        mc = self.connector.cursor()

        if table == "user":
            user_column = "user_id"
        elif table == "stats":
            user_column = "stats_userid"

        sql = "UPDATE "+table+" SET "
        for v in values.keys():
            if values[v][1] == "int":
                text = v + " = " + str(values[v][0])
            else:
                text = v + " ='"+str(values[v][0])+"'"

            sql += text + ","

        sql = sql[0:-1] + " WHERE "+user_column+"="+str(user_id)
        print(sql)
        mc.execute(sql)
        self.connector.commit()

    def InsertData(self, values, table):
        mc = self.connector.cursor()

        text_names = " ("
        text_values = " VALUES ("
        for v in values.keys():
            text_names += str(v)+","
            if values[v][1] == "int":
                print(values[v][1])
                text_values += v + " =" + str(values[v][0]) + ","
            else:
                text_values = v + " ='"+str(values[v][0])+"'" + ","

        text_names = text_names[0:-1]+")"
        text_values = text_values[0:-1]+")"

        sql = "INSERT INTO "+table+text_names+text_values

        mc.execute(sql)
        self.connector.commit()

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
