import json
import os
import urllib.request

API_url = ('http://data.taipower.com.tw/'
           'opendata01/apply/file/d006001/001.txt'
           )

response = urllib.request.urlopen(url=API_url)
result_Str = response.read().decode('utf-8')

with open('TP_API_result.json', 'w', encoding='utf-8') as fp:
    fp.write(result_Str)

with open('TP_API_result.json', 'r', encoding='utf-8') as fp:
    json_loader = json.load(fp)
    for item in json_loader['aaData']:
        if item[1] == "興達CC#4":
            print(item[4])
            break
