#!/usr/bin/python3

# 3rd party import
import requests
import json
from pprint import pprint as pp

# define variable for constant API
url = "https://statsapi.web.nhl.com/api/v1/teams"

# Call the webservice
apicall = requests.get(url)

# read the file-like ojbect
api_read = apicall.json()

# print  our python data)
print(api_read)
input('\nThis is converted json. Press ENTER to continue.')

# Show Pretty Print json
pp(api_read)
input('\nThis is pretty printed JSON. Press ENTER to continue.')

# Grab specific value
pp(api_read["franchiseID"])
input('\nThis is the team franchiseID number')

#team = url.json()

#print(team["name"])

#for teamdict in team["city"]:
#    print(teamdict["city"]["name"]i)
