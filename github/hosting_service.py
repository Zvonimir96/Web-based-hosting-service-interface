from http.client import HTTPSConnection
from abc import ABC, abstractmethod


class HostingService(ABC):
    def __init__(self, host, username):
        """
        :param host: IP address of hosting service.
        :param username: account username.
        """

        # Create HTTPS socket
        self.conn = HTTPSConnection(host)
        self.username = username

    @abstractmethod
    def repos(self, language=None):
        pass

    @abstractmethod
    def repo(self, repo_name):
        pass

    @abstractmethod
    def languages(self, repo):
        pass

    @abstractmethod
    def rate_limit(self):
        pass

    @abstractmethod
    def commits(self, repo):
        pass
