# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:16:04 2020

@author: justinmlam
url:https://github.com/justinmlam/foodcouver/blob/master/gather_data.ipynb
"""
import requests
import json
import time

# Testing API Endpoints

API_KEY = 'API_KEY HERE'
CLIENT_ID = 'ID_HERE'

ENDPOINT = "https://api.yelp.com/v3/businesses/search"

HEADERS = {'Authorization': 'bearer %s' % API_KEY}

PARAMETERS = {'term': 'restaurants',
              'offset': 0,
              'limit': 50,
              'radius': 40000,
              'location': 'Toronto, ON'}

response = requests.get(url=ENDPOINT, params=PARAMETERS, headers=HEADERS)
restaurant_data = response.json()

# Load all categories
# each item in restaurant is dictionary
with open("categories.json") as f:
    data = json.load(f)

restaurants = [place for place in data if 'restaurants' in place['parents']]

restaurant_aliases = [restaurant['alias'] for restaurant in restaurants]
restaurant_titles = [restaurant['title'] for restaurant in restaurants]

# Loop through all categories and collect data
restaurants_in_toronto = []

for category in restaurant_aliases:
    PARAMETERS['categories'] = category
    # Cycle through restaurants
    for offset_number in range(0,1000,50):
        PARAMETERS['offset'] = offset_number

        response = requests.get(url=ENDPOINT, params=PARAMETERS, headers=HEADERS)

        if not response.json().get('businesses', False):
            break

        restaurants_in_toronto.extend(response.json()['businesses'])

        print("{}: {}-{}".format(category, offset_number, offset_number+50))
        
        time.sleep(0.5) ## Don't want to get blocked by Yelp API

restaurants_file =  open("toronto_restaurants_duplicates.json", "w")
json.dump(restaurants_in_toronto, restaurants_file, indent=6)
restaurants_file.close()

res_list = [value for counter, value in enumerate(restaurants_in_toronto) if value not in restaurants_in_toronto[counter+1:]]

restaurants_file = open("toronto_restaurants.json", "w")
json.dump(res_list, restaurants_file, indent=6)
restaurants_file.close()

new_list = sorted(res_list,key=lambda k: k['name'])



