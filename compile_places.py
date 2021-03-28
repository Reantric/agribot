########################################## THIS CODE IS USED FOR  FINDING PLACES ##################################

import urllib.request

# Python program to get a set of
# places according to your search
# query using Google Places API

# importing required modules
import requests

# enter your api key here
api_key = 'AIzaSyBfe9ewy_s7jTP6_sBzgwRONuiWQX004TU'

# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# The text string on which to search
query = input('Search query: ')

# get method of requests module
# return response object
r = requests.get(url + 'query=' + query +
                 '&key=' + api_key)

# json method of response object convert
#  json format data into python format data
x = r.json()

# now x contains list of nested dictionaries
# we know dictionary contain key value pair
# store the value of result key in variable y
y = x['results']


for i in y:
    fp = urllib.request.urlopen(f"https://maps.googleapis.com/maps/api/place/details/json?place_id={i['place_id']}&fields=formatted_address,type,website,name,rating,formatted_phone_number&key=AIzaSyBfe9ewy_s7jTP6_sBzgwRONuiWQX004TU")
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
   # print(yi["name"]) # make sure it matches
    print(mystr)