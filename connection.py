import json
import requests
import 

rescuetime = ""

def rescuetime():
    # define headers and URL
    headers = {
        'Host': 'https://www.rescuetime.com/anapi/data',
        'format': 'json' 
    }
    url = 'https://api.ouraring.com/v1/sleep?start=2022-07-16&end=2022-07-16'

    response = requests.get(url, headers=headers)
    return response