import json
from datetime import datetime

from .hosting_service import HostingService
from .utilities import User, Commit, Repository, Branch, add_query_parameters

# Host ip address is same for all instances of the class Github
HOST = 'api.github.com'


class GitHub(HostingService):
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
            'User-Agent': 'Web-based-hosting-service-interface',    # Mandatory header that identifies client
            'Accept': 'application/vnd.github+json'                 # Recommended header
        }

        # Add token header if it exists
        if token is not None:
            self.header['Authorization'] = token

    def repos(self, language=None, type=None, sort=None, direction=None, per_page=None, page=None):
        """
        Return all repository's found on users account GitHub account.

        :param optional page: page number of the results to fetch. Default: 1
        :param optional per_page: the number of results per page (max 100). Default: 30
        :param optional direction: the order to sort by. Default: asc when using full_name, otherwise desc. Can be one of: asc, desc
        :param optional sort: the property to sort the results by. Can be one of: created, updated, pushed, full_name. Default: created.
        :param optional type: specifies the types of repositories you want returned. Can be one of: all, public, private, forks, sources, member. Default: all
        :param optional language: filters results by programing language.
        :return: list filled with instances of Repository class.
        """

        url = f'/users/{self.username}/repos'

        # Add query parameters
        query_parameters = {}
        if type is not None:
            query_parameters['type'] = type

        if sort is not None:
            query_parameters['sort'] = sort

        if direction is not None:
            query_parameters['direction'] = direction

        if per_page is not None:
            query_parameters['per_page'] = per_page

        if page is not None:
            query_parameters['page'] = page

        # Build url
        url = add_query_parameters(url, query_parameters)

        # Send request and read response as a JSON format
        self.conn.request('GET', url, headers=self.header)
        response = self.conn.getresponse()
        response_body = json.loads(response.read().decode())

        # Parse repository information and filter results
        repos = []
        for repo_data in response_body:
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

    def repo(self, repository_name):
        """
        Returns repository searched by name in the user's GitHub account.

        :param repository_name: repository name to be searched.
        :return: instances of Repository class.
        """

        url = f'/repos/{self.username}/{repository_name}'

        # Send request and read response as a JSON format
        self.conn.request('GET', url, headers=self.header)
        response = self.conn.getresponse()
        response_body = json.loads(response.read().decode())

        return Repository(response_body)

    def commits(self, repository):
        """
        Return all commits on repository.

        :param repository: instance of a class Repository.
        :return: list filled with instances of Commit class.
        """

        url = f'/repos/{self.username}/{repository.name}/commits'

        # Send request and read response
        self.conn.request('GET', url, headers=self.header)
        response = self.conn.getresponse()
        response_body = json.loads(response.read().decode())

        # Parse commit information
        commits = []
        for commit in response_body:
            commits.append(Commit(commit))

        return commits

    def languages(self, repository):
        """
        Returns all programing languages used in repository.

        :param repository: instances of Repository class.
        :return: list of language names.
        """

        url = f'/repos/{self.username}/{repository.name}/languages'

        # Send request and read response
        self.conn.request('GET', url, headers=self.header)
        response = self.conn.getresponse()
        response_body = response.read().decode()

        return json.loads(response_body)

    def rate_limit(self):
        """
        Print number of request that can be sent to Github API from this interface.
        """

        url = f'/rate_limit'

        # Send request and read response
        self.conn.request('GET', url, headers=self.header)
        response = self.conn.getresponse()
        response_body = json.loads(response.read().decode())

        print(f'Core:')
        print(f'\tRate limit: {response_body["resources"]["core"]["limit"]}')
        print(f'\tRemaining: {response_body["resources"]["core"]["remaining"]}')
        print(f'\tReset: {datetime.fromtimestamp(response_body["resources"]["core"]["reset"])}')

        print(f'Search:')
        print(f'\tRate limit: {response_body["resources"]["search"]["limit"]}')
        print(f'\tRemaining: {response_body["resources"]["search"]["remaining"]}')
        print(f'\tReset: {datetime.fromtimestamp(response_body["resources"]["search"]["reset"])}')

    def user(self):
        """
        Requires that token is set. Returns authorized user information.

        :return: instance of class User
        """

        url = f'/user'

        # Send request and read response as a JSON format
        self.conn.request('GET', url, headers=self.header)
        response = self.conn.getresponse()
        response_body = json.loads(response.read().decode())

        return User(response_body)

    def branches(self, repository, protected=None, per_page=None, page=None):
        """
        Return all branches on repository.

        :param repository: instance of a class Repository.
        :param optional protected: setting to true returns only protected branches. When set to false, only unprotected branches are returned. Omitting this parameter returns all branches.
        :param optional per_page: the number of results per page (max 100).
        :param optional page: page number of the results to fetch.
        :return: list filled with instances of Branch class.
        """

        url = f'/repos/{self.username}/{repository.name}/branches'

        # Add query parameters
        query_parameters = {}
        if protected is not None:
            query_parameters['protected'] = protected

        if per_page is not None:
            query_parameters['per_page'] = per_page

        if page is not None:
            query_parameters['page'] = page

        # Build url
        url = add_query_parameters(url, query_parameters)

        # Send request and read response as a JSON format
        self.conn.request('GET', url, headers=self.header)
        response = self.conn.getresponse()
        response_body = json.loads(response.read().decode())

        # Parse branch information
        branches = []
        for branch_data in response_body:
            branches.append(Branch(branch_data))

        return branches

    def branch(self, repository, branch_name):
        """
        Returns branch searched by name.

        :param repository: instance of a class Repository.
        :param branch_name: branch name.
        :return: instance of Branch class.
        """

        url = f'/repos/{self.username}/{repository.name}/branches/{branch_name}'

        # Send request and read response as a JSON format
        self.conn.request('GET', url, headers=self.header)
        response = self.conn.getresponse()
        response_body = json.loads(response.read().decode())

        return Branch(response_body)
