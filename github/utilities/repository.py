class Repository:
    def __init__(self, repo_data):
        self.__data = repo_data

    @property
    def name(self):
        return self.__data['name']

    def __str__(self):
        return f'{self.name}'
