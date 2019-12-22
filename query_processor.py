from cipher import AESCipher
from meta import Meta
from query_executor import QueryExecutor
import ast


def parse_tuple(string):
    try:
        s = ast.literal_eval(str(string))
        if type(s) == tuple:
            return s
        return
    except:
        return


class QueryProcessor:
    def __init__(self, original_query):
        self.original_query = original_query
        self.transformed_query = ""
        self.encrypted_result = ""
        self.decrypted_result = ""

    def transform_query(self):
        index = int(self.original_query.split('=')[1])
        self.transformed_query = f'index={Meta.get_index(index)}'

    def execute_query(self):
        query_executor = QueryExecutor(self.transformed_query)
        self.encrypted_result = query_executor.execute_query()

    def decrypt_result(self):
        cipher = AESCipher(Meta.password)
        self.decrypted_result = [cipher.decrypt(bytes(i[0])) for i in self.encrypted_result]

    def final_result(self):
        response = []
        for i in self.decrypted_result:
            if str(parse_tuple(i)[3]) == self.original_query.split('=')[1]:
                response.append(parse_tuple(i))
        return response

    @staticmethod
    def plain_text_result(encrypted_result):
        plain_text = encrypted_result
        return plain_text
