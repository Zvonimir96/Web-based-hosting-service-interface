class Branch:
    def __init__(self, data):
        self.__data = data

    @property
    def name(self):
        return self.__data['name']

    @property
    def protected(self):
        return self.__data['protected']

    def __str__(self):
        return f'Branch name {self.name}'
