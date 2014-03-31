import sys
import json
import requests

def valuewalk(elem):
	values = []
	for k, v in elem.iteritems():
		if type(v) is dict:
			values.extend(valuewalk(v))
		else:
			values.append('"'+v+'"')
	return values

#def fieldwalk(prefix, elem):
#	fields = []
#	for k, v in elem.iteritems():
#		if type(v) is dict:
#			fields.extend(fieldwalk(prefix+k+"_", v))
#		else:
#			fields.append(prefix+k)
#	return fields


if len(sys.argv) <= 1:
	sys.argv.append('4fd43cc56d11340000000005')

request = requests.get('https://api.clever.com/v1.1/districts/'+sys.argv[1]+'/schools', headers={'Authorization':'Bearer DEMO_TOKEN'})
o = json.loads(request.text)

for school in o.get('data'):
	print ','.join(str(x) for x in valuewalk(school.get('data')))
