import sys
sys.stdout.reconfigure(encoding='utf-8')

import requests
import json

def request_get(url):
    return json.loads(requests.get(url).text)

if __name__ == '__main__':
    response = request_get('https://aves.ninjas.cl/api/birds')

    len(response)
    print(response)
