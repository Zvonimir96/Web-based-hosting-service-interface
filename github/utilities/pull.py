class Pull:
    def __init__(self, data):
        self.__data = data

    @property
    def number(self):
        return self.__data['number']

    def __str__(self):
        return f'Pull number {self.number}'
