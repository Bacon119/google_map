import requests
from keys import MAP_API
from const import DIRECTION_URL, ADDRESS_URL

origin='Disneyland' #input('Please Enter the Origin:')
destination='Universal+Studios+Hollywood4' #input('Please Enter the Destination')

def get_direction():

    response=requests.get(DIRECTION_URL.format(start_address=origin, end_address=destination, API=MAP_API))

    data = response.json()

    steps=data['routes'][0]['legs'][0]['steps']

    for step in steps:
        print(step['distance']['text'])
        print(step['duration']['text'])
        print(step['html_instructions'])

get_direction()
