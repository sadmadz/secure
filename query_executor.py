import hashlib
import random
import sqlite3
from _md5 import md5

from Crypto import Random
from Crypto.Cipher import AES
import base64, os


class QueryExecutor:
    def __init__(self, dbname):
        self.dbname = dbname


    def connect(self):
        try:
            self.conn.execute(
                'CREATE TABLE PERSON (id INT PRIMARY KEY NOT NULL , name TEXT  NOT NULL, last_name TEXT  NOT NULL, age INT NOT NULL);')
        except Exception as e:
            print(e)
        return self.conn
