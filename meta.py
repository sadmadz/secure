class Meta:
    password = '123456'

    @staticmethod
    def get_index(record):
        if record < 5:
            index = 0
        elif 5 <= record <= 20:
            index = 1
        elif 20 <= record <= 30:
            index = 2
        elif 30 <= record <= 50:
            index = 3
        else:
            index = 4
        return index
