'''
Discord image history viewer
Attempts to guessimate unique ID keyspace in image URIs that are publically available
Author: @jcobu
'''

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

# Main menu
def menu():
    print('(1) for manual')
    print('(2) for automatic sifting')
    selection = input('Selection: ')

    if selection == '1':
        manualBuilder()
    elif selection == '2':
        automatedBuilder()
    else:
        exit()

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
    alist = ''
    for x in range(3):
        alist += combiner()

    print('Example: https://media.discordapp.net/attachments/<useruuid>/<secondaryuuid>/<unknown.png>')
    userInput = urlTemplate(input('UUID: '), alist, input('File name (if known): '))
    resp = requests.get(userInput.combinedURL())
    print(resp.status_code)

# Automated search based on wordlists
def automatedBuilder():
    for z in range(4):
        alist = ''
        blist = ''
        for x in range(3):
            alist += combiner()
            blist += combiner()

        '''
        # Debug printing
        print(f'alist: {alist}')
        print(f'blist: {blist}')
        '''
        
        # Snap in the numbers uses classes idk lol
        automatedInput = urlTemplate(alist, blist, 'unknown.png')
        resp = requests.get(automatedInput.combinedURL())

        print(resp.status_code)

menu()