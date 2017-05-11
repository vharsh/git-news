#/usr/bin/env python3
import requests
import datetime

def askGithub(dateCreated, lang, sortOrder = True):
    payload = { 'q' : ['language:' + lang,
                'created:>' + str(dateCreated)],
		'sort': 'stars',
		'order': 'desc' if sortOrder else 'asc',
              }
    head = { 'Accept' : 'application/vnd.github.mercy-preview+json' }
    x = requests.get('https://api.github.com/search/repositories', params = payload, headers = head)
    print(x.content)

if __name__ == '__main__':
    askGithub(datetime.date.today(), 'go')
