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
    def repos(self):
        pass

    @abstractmethod
    def repo(self, repository_name):
        pass

    @abstractmethod
    def languages(self, repository):
        pass

    @abstractmethod
    def rate_limit(self):
        pass

    @abstractmethod
    def commits(self, repository):
        pass

    @abstractmethod
    def user(self):
        pass

    @abstractmethod
    def branches(self, repository):
        pass

    @abstractmethod
    def branch(self, repository, branch_name):
        pass

    @abstractmethod
    def merge_branches(self, repository, base_branch, head_branch):
        pass

    @abstractmethod
    def pull_requests(self, repository):
        pass

