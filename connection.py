import json
import requests
import csv

def cred_data_processed(unprocessed_creds):
    rown = 0
    for i in unprocessed_creds:
        if rown = 0:
            continue
        

def crediental_list():
    with open('time-tracker-credientals.csv', mode='r') as c_file:
        csv_reader = csv.DictReader(c_file, delimiter=',')
        return csv_reader        

def json_request(url):
    # define headers and URL
    headers = {
        'format': 'json'
    }

    response = requests.get(url, headers=headers)
    return response

def main():
    cred_list = crediental_list()
    cred_data = cred_data_processed(cred_list)
main()


    