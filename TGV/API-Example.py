"""
TGV API Example.
Returns list of movies
Refer README for more info
"""
import requests, json


endpoint = 'http://tgv.api.lb.appxtream.com/'

def getList():
	url = 'http://tgv.api.lb.appxtream.com/jsonFeed.action?service=tgvMobileService&action=getMovieList3'
	r = requests.get(url)
	return r


""" JSONify getList() returned data """
j = getList().json()


""" Print Movie titles """
for each in j['movies']:
	print(each['internalMovieName'])