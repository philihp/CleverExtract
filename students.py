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

def fieldwalk(prefix, elem):
	fields = []
	for k, v in elem.iteritems():
		if type(v) is dict:
			fields.extend(fieldwalk(prefix+k+"_", v))
		else:
			fields.append(prefix+k)
	return fields


if len(sys.argv) <= 1:
	sys.argv.append('4fd43cc56d11340000000005')

prefix = 'https://api.clever.com/';
next = prefix + 'v1.1/districts/'+sys.argv[1]+'/students'

while next is not None:
	request = requests.get(next, headers={'Authorization':'Bearer DEMO_TOKEN'})
	o = json.loads(request.text)
	for student in o.get('data'):
		print ','.join(str(x) for x in valuewalk(student.get('data')))
	next = None
	for link in o.get('links'):
		if link.get('rel') == 'next':
			next = prefix + link.get('uri')