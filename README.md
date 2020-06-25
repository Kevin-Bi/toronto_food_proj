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

**Packages**: pandas, geopandas, numpy, matplotlib, seaborn, json, folium

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
### Distribution of Numerical Variables 
![Summary Distribution](https://user-images.githubusercontent.com/65966223/85639244-15f45c00-b656-11ea-86ee-e3072b5fb33b.png)

### Top Five Categories
![Top five](https://user-images.githubusercontent.com/65966223/85639270-2e647680-b656-11ea-8dd8-703f93eeee91.png)

### Restaurants Density by Ward
![Total Restaurants](https://user-images.githubusercontent.com/65966223/85639638-53a5b480-b657-11ea-9540-ef62e883e92c.png)

### Average Price by Ward
![Average Price](https://user-images.githubusercontent.com/65966223/85639706-9071ab80-b657-11ea-9bd3-cdb050c1397d.png)

In summary, Spadina-Fort York and University-Rosedale area have highest density of restaurants. It is expected that most of the expensive restaurants are located in downtown Toronto and clustered in the Financial and Entertainment Districts. Uptown Toronto also have a high average price because of upscale restaurants located in Lawrance-Yonge and Yorkdale area.

## Use
The jupyter notebook for this project can be viewed in [here](https://nbviewer.jupyter.org/github/Kevin-Bi/toronto_food_proj/blob/master/Toronto_Food_EDA.ipynb#).

## Legality
This project uses the Yelp Fusion API, and terms and conditions can be found here: https://www.yelp.ca/developers/api_terms 

This is a personal project made for non-commercial uses only. If there are any legal issues with this project please contact me.  
