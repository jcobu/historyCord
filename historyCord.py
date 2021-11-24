'''
Discord image history viewer
Attempts to guessimate unique ID keyspace in image URIs that are publically available
Author: @jcobu
'''

import requests

class urlTemplate:

    def __init__(self, uuid, uuid2, fname):
        self.uuid = uuid
        self.uuid2 = uuid2
        self.fname = fname

    def combinedURL(self):
        urlPrefix = 'https://media.discordapp.net/attachments'
        return (f'{urlPrefix}/{self.uuid}/{self.uuid2}/{self.fname}')


# Main menu
def menu():
    print('(1) for manual')
    print('(2) for automatic sifting')
    selection = input('Selection: ')

    if selection == '1':
        urlBuilder()

    elif selection == '2':
        automatedBuilder()

    else:
        exit()

# Manual search
def urlBuilder():
    print('Example: https://media.discordapp.net/attachments/<useruuid>/<secondaryuuid>/<unknown.png>')
    userInput = urlTemplate(input('UUID: '), input('Secondary UUID: '), input('File name (if known): '))
    resp = requests.get(userInput.combinedURL())
    print(resp.status_code)
    # Clickable link to view the image
    print(userInput.combinedURL())

# Automated search based on wordlists
def automatedBuilder():
    # Open pre-generated 6 digit list
    with open('numbers.txt') as n:
        alist = [line.rstrip() for line in n]
        for a in list:
            blist = []
            blist.append(a)
            #combinedNumbers

        # Snap in the numbers
        '''
        automatedInput = urlTemplate('232323', '232323', 'unknown.png')
        resp = requests.get(automatedInput.combinedURL())
        print(resp.status_code)
        '''
    n.close()

menu()