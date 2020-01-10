import random
import sqlite3


class Database:
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(self.dbname)

    def connect(self):
        try:
            self.conn.execute(
                'CREATE TABLE PERSON (id INT PRIMARY KEY NOT NULL , name TEXT  NOT NULL, last_name TEXT  NOT NULL, age INT NOT NULL);')
        except Exception as e:
            print(e)
        return self.conn

    def disconnect(self):
        self.conn.close()

    def get_records(self):
        cursor = self.conn.cursor()
        sqlite_select_query = "SELECT * FROM PERSON"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        return records

    def insert_test_data(self):

        names = ['علی', 'رضا', 'زهرا']
        fNames = ['اکبری', 'زارع', 'محمدی', 'حمیدی', 'حسینی']
        id = 1

        for i in names:
            for j in fNames:
                age = random.randint(1, 60)
                params = (id, i, j, age)
                self.conn.execute("INSERT INTO PERSON VALUES (?,?, ?, ?)", params)
                self.conn.commit()
                id += 1

    @staticmethod
    def get_cipher_records(age_param):
        connection = sqlite3.connect('cipher.sqlite3')
        try:
            connection.execute(
                'CREATE TABLE CIPHER (data TEXT  NOT NULL, age_index TEXT  NOT NULL);')
        except Exception as e:
            pass
        cursor = connection.cursor()
        sqlite_select_query = f"SELECT * FROM CIPHER WHERE age_index={age_param}"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        return records

    @staticmethod
    def insert_cipher_data(items):
        connection = sqlite3.connect('cipher.sqlite3')
        try:
            connection.execute(
                'CREATE TABLE CIPHER (data TEXT  NOT NULL, age_index TEXT  NOT NULL);')
        except Exception as e:
            pass
        for i in items:
            data = i[0]
            index = i[1]
            params = (data, index)
            connection.execute("INSERT INTO CIPHER VALUES (?,?)", params)
            connection.commit()
