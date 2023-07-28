from github import GitHub

language = 'Python'
username = 'Zvonimir96'
TOKEN = None


def main():
    gh = GitHub(username, token=TOKEN)

    # Retrieve all repository's
    print('All repos', end=': ')
    print(*gh.repos(), sep=', ')

    # Retrieve all repository's with a desired language in descending order
    print(f'Only {language} repos', end=': ')
    print(*gh.repos(language, direction='desc'), sep=", ")

    # Retrieve repository by name
    repo = gh.repo("NeoPixel-strip")

    # Retrieve all commits from NeoPixel-strip repository
    print(f'{repo} commits: ')
    print(*gh.commits(repo), sep="\n")

    # Retrieve all languages from NeoPixel-strip repository
    print(f'{repo} languages', end=': ')
    print(*gh.languages(repo), sep=", ")

    # Print number of request that can be sent to Github API from this interface
    gh.rate_limit()

    # Retrieve authorized user information
    if TOKEN is not None:
        print(gh.user())

    repo = gh.repo('Test-repo')
    # Retrieve all unprotected branches from Test-repo repository
    print(*gh.branches(repo, protected='false'), sep=', ')

    # Retrieve main branch from Test-repo repository
    print(gh.branch(repo, 'main'))

    # Retrieve all pull requests from Test-repo repository
    print(*gh.pull_requests(repo), sep=', ')

    # Retrieve repository branches to be merged
    base_b = gh.branch(repo, 'B2')
    head_b = gh.branch(repo, 'B1')

    # Merge branches
    gh.merge_branches(repo, base_b, head_b)


if __name__ == "__main__":
    main()
