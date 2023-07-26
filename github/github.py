import json
from datetime import datetime

from .hosting_service import HostingService
from .utilities import User, Commit, Repository

# Host ip address is same for all instances of the class Github
HOST = 'api.github.com'


class Github(HostingService):
    """
    Interface for Github API. Github rest api documentation https://docs.github.com/en/rest?apiVersion=2022-11-28.
    """

    def __init__(self, username, token=None):
        """
        To generate token follow the link:
        https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

        :param username: Github account username.
        :param optional token: Github personal access token. Identifies user account and gives more possibilities.
        """
        # Create HTTPS socket
        super().__init__(HOST, username)
        # Create default header
        self.header = {
            'Host': HOST,
            'User-Agent': 'Web-based-hosting-service-interface'  # Mandatory header that identifies client
        }

        # Add token header if it exists
        if token is not None:
            self.header['Authorization'] = token

    def repos(self, language=None):
        """
        Return all repository's found on users account Github page.

        :param optional language: filters results by programing language.
        :return: list filled with instances of Repository class.
        """

        # Set recommended header for repository search
        self.header['accept'] = 'application/vnd.github+json'

        # Send request and read response as a JSON format
        self.conn.request('GET', f'/users/{self.username}/repos', headers=self.header)
        response = json.loads(self.conn.getresponse().read().decode())

        # Parse repository information and filter results
        repos = []
        for repo_data in response:
            # Parse repository
            repo = Repository(repo_data)

            if language is None:
                # If language is no set, fill list with all repository's
                repos.append(repo)
            else:
                # Filter repository's by programing language
                for repo_language in self.languages(repo):
                    # If repository contains desired language, append repository to list
                    if repo_language.lower() == language.lower():
                        repos.append(Repository(repo_data))
                        break

        return repos

    def repo(self, repo_name):
        """
        Return repository search by name

        :param repo_name: repository name to be searched.
        :return: instances of Repository class.
        """

        # Set recommended header
        self.header['accept'] = 'application/vnd.github+json'

        # Send request and read response as a JSON format
        self.conn.request('GET', f'/repos/{self.username}/{repo_name}', headers=self.header)
        response = json.loads(self.conn.getresponse().read().decode())

        return Repository(response)

    def languages(self, repo):
        """
        Returns all programing languages used in repository.

        :param repo: instances of Repository class.
        :return: list of language names.
        """

        # Set recommended header
        self.header['accept'] = 'application/vnd.github+json'

        # Send request and read response
        self.conn.request('GET', f'/repos/{self.username}/{repo.name}/languages', headers=self.header)
        response = self.conn.getresponse().read().decode()

        return json.loads(response)

    def rate_limit(self):
        """
        Print number of request that can be sent to Github API from this interface.
        """

        # No special headers is needed

        # Send request and read response
        self.conn.request('GET', f'/rate_limit', headers=self.header)
        response = json.loads(self.conn.getresponse().read().decode())

        print(f'Core:')
        print(f'\tRate limit: {response["resources"]["core"]["limit"]}')
        print(f'\tRemaining: {response["resources"]["core"]["remaining"]}')
        print(f'\tReset: {datetime.fromtimestamp(response["resources"]["core"]["reset"])}')

        print(f'Search:')
        print(f'\tRate limit: {response["resources"]["search"]["limit"]}')
        print(f'\tRemaining: {response["resources"]["search"]["remaining"]}')
        print(f'\tReset: {datetime.fromtimestamp(response["resources"]["search"]["reset"])}')

    def user(self):
        """
        Requires that token is set. Returns authorized user information.

        :return: instance of class User
        """

        # Send request and read response as a JSON format
        self.conn.request('GET', f'/user', headers=self.header)
        response = json.loads(self.conn.getresponse().read().decode())

        return User(response)

    def commits(self, repo):
        """
        Return all commits on repository.

        :param repo: instance of a class Repository.
        :return: list filled with instances of Commit class.
        """
        # No special headers is needed

        # Send request and read response
        self.conn.request('GET', f'/repos/{self.username}/{repo.name}/commits', headers=self.header)
        response = json.loads(self.conn.getresponse().read().decode())

        # Parse commit information
        commits = []
        for commit in response:
            commits.append(Commit(commit))

        return commits
