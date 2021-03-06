import requests, os

try:
	from UID import UID
	# print UID
except:
	print "coinquery: UID not set, please rerun installation."
	exit()

URLHEAD="http://altsheets.ddns.net:8001/altsheets/"

def askDataserver(what, key):
	try:
		url=URLHEAD+what+'?auth=%s&id=%s' % (key, UID)
		r=requests.get(url)
	except Exception as e:
		print url
		print type(e), e
		return ""
	if r.status_code != requests.codes.ok:
	    return ""
	return r.text
