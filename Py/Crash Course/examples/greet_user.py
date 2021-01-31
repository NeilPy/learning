import json

filename = 'username.json'

with open(filename) as f_ofj:
    username = json.load(f_ofj)
    print('С возвращением ' + username + "!")
