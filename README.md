# Exploratory Data Analysis on Dining Culture in Toronto, Ontario

## Background 
Toronto is renowned for its excellent culinary diversity. As a food enthusiast, I'd love to dive deeper into the local dining culture and explore characteristics of restaurants in Toronto with statistical and geospatial analysis.

  - What are the most popular categories of restaurants?
  - What are the highest rated cuisines?
  - Where are the most expensive restaurants?
  - Which city ward has the most restaurants?
  
I will be using data collected from Yelp API and an online dataset to answer the above questions.

## Code and Resources Used
**Python Version**: 3.7
**Packages**: pandas, numpy, matplotlib, seaborn, selenium, json, folium
**Extra Dataset**: https://public.tableau.com/profile/stephanie.o.gay.garcia#!/vizhome/TorontoRestaurants/TorontoRestaurantsByCategory

**API Data Collector and Visualization References**: https://github.com/justinmlam/foodcouver/blob/master/
https://github.com/heidijiang/new-porkers/

## Data Preparation
After importing the datasets, I cleaned it up and merged them together for analysis. I made the following changes:

  - Remove Unnecessary Columns
  - Develop function for extracting categories
  - Simplify Columns
  - Convert "listed" categories into a series which will be joined to existing dataset
  - Eliminate duplicated information with the same category, address, and name
  - Concatenate dataframe into df3_expanded
  - Droped duplicates for df3_expanded and craete df3 that remains only one category per restaurant 

## EDA
![](images/Summary%20Dist.png)


## Legality
This project uses the Yelp Fusion API, and terms and conditions can be found here: https://www.yelp.ca/developers/api_terms 

This is a personal project made for non-commercial uses only. If there are any legal issues with this project please contact me.  
