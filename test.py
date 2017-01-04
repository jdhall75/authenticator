import json
import sys
from pprint import pprint
import base64

with open('keys.json') as data_file:
    data = json.load(data_file)

pprint(data)

key1 = base64.b32encode(b"test1")
key2 = base64.b32encode(b"test2")

try:
    data['keys'][0]['key'] = key1.decode('UTF-8')
    data['keys'][1]['key'] = key2.decode('UTF-8')
except ValueError:
    print("Not the right encodeing")
    sys.exit()

with open('keys.json', 'w') as data_file:
    json.dump(data, data_file)

