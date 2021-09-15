#!/usr/bin/env python3

import requests ## 3rd party URL lookup
import webbrowser

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date' + input("Choose a start date (YYYY-MM-DD) ")  ## start date for data

    enddate = '&end_date' + input("Choose an end date (YYYY-MM-DD) ") ## create a mechanism to utilize enddate

    mykey = '&api_key=GUi3WOIHrksyfld4sz503GhgZlL0l9qymu4sMKTm' ## replace this with our API key

    neourl = neourl + startdate + enddate + mykey
    print(neourl)

    neojson = (requests.get(neourl)).json()

    print(neojson)

## call main
main()

