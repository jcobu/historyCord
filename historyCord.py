'''
Discord image history viewer
Attempts to guessimate unique ID keyspace in image URIs that are publically available
Author: @jcobu
'''
from sys import exit
import requests, random
foundList = []

class urlTemplate:

    def __init__(self, uuid, uuid2, fname):
        self.uuid = uuid
        self.uuid2 = uuid2
        self.fname = fname

    def combinedURL(self):
        urlPrefix = 'https://media.discordapp.net/attachments'
        urlComplete = (f'{urlPrefix}/{self.uuid}/{self.uuid2}/{self.fname}')
        print(urlComplete)
        return urlComplete

# Temporary array keeping track of valid urls
def ifFound(code, url):
    if code == 200:
        for a in foundList:
            if url != a:
                foundList.append(url)

# Prints the final foundList array vertically
def printStuff():
    for i in foundList:
        print('Valid links: ' + i)

# Main menu
def menu():
    while(True):
        print('(1) for manual')
        print('(2) for automatic sifting')
        selection = input('Selection: ')

        if selection == '1':
            print('Starting manual\n')
            manualBuilder()
        elif selection == '2':
            print('Starting automatic\n')
            automatedBuilder()
        else:
            print('Exiting\n')
            exit(0)

# Picks random 3, 6 digit numbers and appends them to a single str var
def combiner():
    # Open pre-generated 6 digit list
    lines = open('numbers.txt').read().splitlines()
    list = str(random.choice(lines))
    return list
    # Closes the file
    lines.close()

# Manual search
def manualBuilder():
    print('Example: https://media.discordapp.net/attachments/<useruuid>/<secondaryuuid>/<unknown.png>')
    userUUID = input('User UUID: ')
    userFile = input('File name (if known): ')
    if userFile == '':
        userFile = 'unknown.png'

    for a in range(10):
        alist = ''
        for x in range(3):
            alist += combiner()

        # Combines the provided info
        userInput = urlTemplate(userUUID, '909926715197902868', userFile)
        resp = requests.get(userInput.combinedURL())
        print(resp.status_code)
        ifFound(resp.status_code, userInput.combinedURL())

        printStuff()

# Automated search based on wordlists
def automatedBuilder():
    for z in range(10):
        alist = ''
        blist = ''
        for x in range(3):
            alist += combiner()
            blist += combiner()
        
        # Combines the provided info using classes
        automatedInput = urlTemplate(alist, blist, 'unknown.png')
        resp = requests.get(automatedInput.combinedURL())
        print(resp.status_code)
        ifFound(resp.status_code, automatedInput.combinedURL())

        printStuff()

menu()