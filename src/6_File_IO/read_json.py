import json
import os

script_dir = os.path.abspath(__file__)
with open(os.path.join(script_dir, 'sample.json'), 'r', encoding='utf-8') as fp:
    json_reader = json.load(fp)
