import hashlib
import random
import sqlite3
from _md5 import md5

from Crypto import Random
from Crypto.Cipher import AES
import base64, os


class QueryProcessor:
    def __init__(self, original_query):
        self.original_query = original_query

    def transform_query(self):
        transformed_query = self.original_query
        return transformed_query

    @staticmethod
    def plain_text_result(encrypted_result):
        plain_text = encrypted_result
        return plain_text
