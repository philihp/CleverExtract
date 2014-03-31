import json
import requests
request = requests.get('https://api.clever.com/v1.1/districts', headers={'Authorization':'Bearer DEMO_TOKEN'})
o = json.loads(request.text)

for district in o.get('data'):
	id = district.get('data').get('id')
	name = district.get('data').get('name')
	print id+',"'+name+'"'