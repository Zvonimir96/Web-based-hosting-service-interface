from github import GitHub
from credentials import TOKEN

language = 'Python'
username = 'Zvonimir96'

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
print(gh.user())

# Retrieve all unprotected branches from NeoPixel-strip repository
print(*gh.branches(repo, protected='false'), sep=', ')

# Retrieve main branch from NeoPixel-strip
print(gh.branch(repo, 'main'))
