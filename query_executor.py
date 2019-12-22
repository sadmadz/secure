from database import Database


class QueryExecutor:
    def __init__(self, transformed_query):
        self.transformed_query = transformed_query

    def execute_query(self):
        cipher_records = Database.get_cipher_records(self.transformed_query.split('=')[1])
        return cipher_records
