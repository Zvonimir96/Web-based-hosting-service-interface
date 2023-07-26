class User:
    def __init__(self, user_information):
        self.__data = user_information

    @property
    def username(self):
        return self.__data['login']

    @property
    def id(self):
        return self.__data['id']

    @property
    def avatar(self):
        return self.__data['avatar_url']

    def __str__(self):
        return f'User {self.username} with id {self.id}'
