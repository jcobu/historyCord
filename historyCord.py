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

# Main url building method
def urlBuilder():

    print('Example: https://media.discordapp.net/attachments/<useruuid>/<secondaryuuid>/<unknown.png>')

    userInput = urlTemplate(input('UUID: '), input('Secondary UUID: '), input('File name (if known): '))

    resp = requests.get(userInput.combinedURL())

    print(resp.status_code)

    # Clickable link to view the image
    print(userInput.combinedURL())

urlBuilder()