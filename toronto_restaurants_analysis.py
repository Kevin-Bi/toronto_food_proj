# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:34:43 2020

@author: Kevin
"""
import json

with open('toronto_restaurants.json') as f:
    data = json.load(f)

df = pd.DataFrame.from_dict(data, orient='columns')
print("Missing data:")
print(df.isnull().sum())