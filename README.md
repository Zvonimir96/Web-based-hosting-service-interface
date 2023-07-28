# About

This library is an interface to access the [GitHub REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28). It enables you to retrieve information about user,
repository, branch and commits on desired repository. 

GitHub class contains following methods:
- GitHub(username) - create instance of class. To generate token follow the link:
        https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

        :param username: GitHub account username.
        :param optional token: GitHub personal access token. Identifies user account and gives more possibilities.
- repos() - return all repository's found in the user's GitHub account.

        :param optional page: page number of the results to fetch. Default: 1
        :param optional per_page: the number of results per page (max 100). Default: 30
        :param optional direction: the order to sort by. Default: asc when using full_name, otherwise desc. Can be one of: asc, desc
        :param optional sort: the property to sort the results by. Can be one of: created, updated, pushed, full_name. Default: created.
        :param optional type: specifies the types of repositories you want returned. Can be one of: all, public, private, forks, sources, member. Default: all
        :param optional language: filters results by programing language.
        :return: list filled with instances of Repository class.
- repo(repository_name) - returns repository searched by name in the user's GitHub account.

        :param repository_name: repository name to be searched.
        :return: instances of Repository class.
- commits(repository) - return all commits on repository.

        :param repository: instance of a class Repository.
        :return: list filled with instances of Commit class.
- languages(repository) - returns all programing languages used in repository.

        :param repository: instances of Repository class.
        :return: list of language names.
- rate_limit() - print number of request that can be sent to GitHub API from this interface.
- user() - requires that token is set. Returns authorized user information.

        :return: instance of class User
- branches(repository) - return all branches on repository.

        :param repository: instance of a class Repository.
        :param optional protected: setting to true returns only protected branches. When set to false, only unprotected branches are returned. Omitting this parameter returns all branches.
        :param optional per_page: the number of results per page (max 100).
        :param optional page: page number of the results to fetch.
        :return: list filled with instances of Branch class.
- branch(repository, branch_name) - returns branch searched by name.

        :param repository: instance of a class Repository.
        :param branch_name: branch name.
        :return: instance of Branch class.
- merge_branches(repository, base_branch, head_branch) - merge two branches on given repository.

        :param repository: instance of a class Repository.
        :param base_branch: instance of a class Branch that the head will be merged into.
        :param head_branch: instance of a class Branch that will be merged.
        :param optional commit_message: commit message to use for the merge commit.
- pull_requests(repository) - return all pulls created on repository.
        
        :param repository: instance of a class Repository.
        :return: list filled with instances of Commit class.


