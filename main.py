import hashlib
import random
import sqlite3

from meta import Meta
from cipher import AESCipher
from database import Database
from query_processor import QueryProcessor


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'


records = []
encrypted_records = []

try:
    database = Database('db.sqlite3')

    while True:
        print(f'{bcolors.HEADER}Enter Command or Query {bcolors.OKBLUE}(query format--> age=?): ')
        query = input()
        query = query.replace(" ", "")
        if query == 'createdb':
            database.connect()
            database.insert_test_data()
        elif query == 'createcipherdb':
            records = database.get_records()
            cipher = AESCipher(Meta.password)
            for i in records:
                encrypted_records.append((cipher.encrypt(str(i)), Meta.get_index(i[3])))
            Database.insert_cipher_data(encrypted_records)
        elif query == 'quit':
            break
        elif query.__contains__('age='):
            try:
                queryProcessor = QueryProcessor(query)
                queryProcessor.transform_query()
                queryProcessor.execute_query()
                queryProcessor.decrypt_result()
                final_result = queryProcessor.final_result()
                print(final_result)
            except Exception as e:
                print(e)
                print(f"{bcolors.FAIL}Wrong query")

        else:
            print(f"{bcolors.FAIL}Wrong query")


except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
