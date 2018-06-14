import requests
from keys import MAP_API
from const import DIRECTION_URL, ADDRESS_URL
from datetime import datetime, timedelta

origin=input('Please Enter the Origin:')
destination=input('Please Enter the Destination:')

def get_direction():

    response=requests.get(DIRECTION_URL.format(start_address=origin, end_address=destination, API=MAP_API))

    data = response.json()

    steps=data['routes'][0]['legs'][0]['steps']

    for step in steps:
        print(step['distance']['text'])
        print(step['duration']['text'])
        print(step['html_instructions'])

def arrival_time():

    response=requests.get(DIRECTION_URL.format(start_address=origin, end_address=destination, API=MAP_API))

    data = response.json()

    duration=data['routes'][0]['legs'][0]['duration']['value']

    arv_time=datetime.now()+timedelta(days=duration/86400)

    print('The estimated arrival time is', arv_time)


arrival_time()
