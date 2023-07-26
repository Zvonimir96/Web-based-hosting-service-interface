from github import Github
from credentials import TOKEN


language = 'Python'
username = 'Zvonimir96'

gh = Github(username, token=TOKEN)


repo = gh.repo('NeoPixel-strip')
print(*gh.commits(repo), sep="\n")

# print(gh.user())

# print(gh.get_repo_languages('NeoPixel-strip'))

# print('All repos', end=': ')
# print(*gh.repos(), sep=", ")

#print(f'Only {language} repos', end=': ')
#print(*gh.repos(language), sep=", ")

# print(gh.repo("NeoPixel-strip"))
