class Repository:
    def __init__(self, repo_data):
        self.__data = repo_data

    def __str__(self):
        return f'{self.name}'

    @property
    def name(self):
        return self.__data['name']
