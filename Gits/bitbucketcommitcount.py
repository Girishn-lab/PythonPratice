import requests
from dateutil.parser import parse

baseUrlv2 = "https://api.bitbucket.org/2.0"

username = "girishn1404"
password = "Indian@123"
repo = "pythonpratice"

year = 2019

totalCommits = 0
totalAdd = 0
totalRemove = 0
commitCount = 0
commits = []

print("")

print("Stats for {year}".format(year=year))

r = requests.get("{base}/repositories/girishn1404/pythonpratice/".format(base=baseUrlv2),
                 auth=(username, password))

repos = r.json()
print("Repos: ", repos)

repoSlug = repos['slug']
print("Repo slug: ", repoSlug)

for repo in repos:

    url = "{base}/repositories/{username}/{repo}/commits".format(base=baseUrlv2, username=username, repo=repoSlug)
    print("URL: ", url)
    r = requests.get(url, auth=(username, password))

    c = r.json()
    commits.extend(c['values'])

    while 'next' in c:
        r = requests.get("{next}".format(next=c['next']),
                         auth=(username, password))
        c = r.json()
        commits.extend(c['values'])

    for commit in commits:
        date_time_str = commit['date']
        dt = parse(date_time_str)
        commitDate = dt.date()
        if commitDate.year == year:
            commitCount += 1
            hashcode = commit['hash']

            url1 = "{base}/repositories/{username}/{repo}/diffstat/{hash}".format(base=baseUrlv2, username=username,
                                                                                  repo=repoSlug, hash=hashcode)

            r = requests.get(url1,
                             auth=(username, password))

            try:
                stats = r.json()
            except ValueError:
                # decoding failed
                continue

    print("Total commits in {user}/{repo}: {count}".format(user=username, repo=repoSlug, count=commitCount))

    totalCommits += commitCount

    # reset counters
    commitCount = 0
    commits = []

print("")
print("Total commits: {count}".format(count=totalCommits))