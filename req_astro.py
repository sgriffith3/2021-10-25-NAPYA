#!/usr/bin/python3
"""Alta3 || Tracking ISS"""

import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
        
    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
    
    ## decode JSON to Python data structure
    helmetson = groundctrl.json()
    
    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)
    
    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)
    
main()
