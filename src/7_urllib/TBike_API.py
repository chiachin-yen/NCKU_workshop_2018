import json
import os
import urllib.request

API_url = ('http://tbike.tainan.gov.tw:8081/'
           'Service/StationStatus/Json'
           )

response = urllib.request.urlopen(url=API_url)
result_Str = response.read().decode('utf-8')

with open('API_result.json', 'w', encoding='utf-8') as fp:
    fp.write(result_Str)

with open('API_result.json', 'r', encoding='utf-8') as fp:
    json_loader = json.load(fp)
    print(json_loader[0]['StationName'])
