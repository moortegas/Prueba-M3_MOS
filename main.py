# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

from get_module import request_get

# url = "https://aves.ninjas.cl/api/birds"
# r = requests.get(url)
# # response = r.text
# # print(response)

# j = r.json()

# status=j["name"]
# print(name)

i = 1
while i < 20:
    url = "https://aves.ninjas.cl/api/birds/{}".format(i)
    r = request_get(url)
    # response = r
    j = r.json()
   
    name = j["name"]
    images = j["images"]
    print("{}   {}".format(name, images))
    i += 1
















# def get_module(url, offset=0):
#     args = {'offset': offset} if offset else {}

#     response = requests.get(url, params=args)

#     if response.status_code == 200:

#         payload = response.json()
#         results = payload.get(results, [])
#         return json.loads(requests.get(url).text)

#         if results:
#             for ave in results:
#                 name = ave ['name']
#                 print(name)

#         raw_input=input()
#         next = raw_input("¿Continuar listado? [Y/N]").lower()
#         if next == 'y':
#             get_module(offset=offset+20)

# if __name__ == '__main__':
#   url = "https://aves.ninjas.cl/api/birds"  
