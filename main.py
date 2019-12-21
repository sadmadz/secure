import hashlib
import random
import sqlite3

from Crypto import Random
from Crypto.Cipher import AES
import base64, os

from cipher import AESCipher
from database import Database

meta = {'password': '123456'}
records = []
encrypted_records = []

try:
    database = Database('db.sqlite3')
    records = database.get_records()
    print(records)
    cipher = AESCipher(meta['password'])
    for i in records:
        if i[3] < 5:
            index = 0
        elif 5 <= i[3] <= 20:
            index = 1
        elif 20 <= i[3] <= 30:
            index = 2
        elif 30 <= i[3] <= 50:
            index = 3
        else:
            index = 4
        encrypted_records.append((cipher.encrypt(str(i)), index))
    print(encrypted_records)

    # database.insert_test_data()
    Database.insert_cipher_data(encrypted_records)


except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
