#!/usr/bin/env python3
import requests

def getItemsById(id):
    try:
        id = int(id)
    except ValueError:
        return None #Something to indicate error
    
    return requests.get('http://hn.algolia.com/api/v1/items/' + str(id))

def getItemsByUsers(username): # Useful for identity resolution
    return requests.get('http://hn.algolia.com/api/v1/users/' + str(username))

class Search():
    def getItemsByURL(url): # URL linking to the git repo
        return requests.get('http://hn.algolia.com/api/v1/search?query=' + str(url)
                + '&restrictSearchableAttributes=url')

    def getItemsByStory(query): # Story carrying similar content to a pop git repo
        return requests.get('http://hn.algolia.com/api/v1/search?query=' 
                + str(query) + '&tags=story')

    def getItemsByComment(comment): # Comments referring to the github repo, url
        return requests.get('http://hn.algolia.com/api/v1/search?query=' 
                + str(comment) + '&tags=comment')

    def getFrontPageArticles():
        front_page = requests.get('http://hn.algolia.com/api/v1/search?tags=front_page')
        return front_page

    def getCommentsOfStory(storyID):
        comments = 'http://hn.algolia.com/api/v1/search?tags=comment,story_' + str(storyID)
        return requests.get(comments)
        
