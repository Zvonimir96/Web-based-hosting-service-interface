class Commit:
    def __init__(self, data):
        self.__data = data

    @property
    def author(self):
        return self.__data['commit']['author']['name']

    @property
    def message(self):
        return self.__data['commit']['message']

    @property
    def committer(self):
        return self.__data['commit']['committer']['name']

    @property
    def date(self):
        return self.__data['commit']['author']['date']

    def __str__(self):
        return f'Author {self.author} with a message:{self.message}, updated: {self.date}'
