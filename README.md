# project_03 - Housing Value Heatmap
Alec | Andrew | Dan | Karina | Reinhard


# Intro

The purpose of this project was to use HTML, CSS, and JavaScript to dynamically display a database of information allowing users to alter which data is being actively displayed. This allows for rapid visualization of any data desired (from within the dataset).

# Data Set 

![Housing / Property Values](clean_data/clean_home_no_dupes.csv)

link to scraped website -> https://iswdataclient.azurewebsites.net/webSearchAddress.aspx?dbkey=midlandcad



The data set was a collection of property values available to the public via the Midland Texas, County Appraisal Districts' website.
It contains roughly 6400 domestic property entries including assorted values, measurements for land, and housing space. 

# Method
## Scraping
![The Scraping Script](IPYNB_files/Home_Scrape_02.ipynb)

Each of the properties has a unique property ID that could be iterated over using a for loop to insert a modified URL into a script that would use Beautiful Soup to find and pull information from selected HTML Tags then store the vlaues in arranged lists per value before using pandas to assemble a dataframe for visual inspection.

After the data was collected and reviewed, it was then cleaned using ![The Cleaning Script](IPYNB_files/Home_Scrape_Clean.ipynb) so that a final dataset could be saved and used for the next step in the ETL process.

## Database Construction
The clean informationw as then passed through a pythn script utilizing Pymongo to breakdown entries in the CSV generated from the Cleaning Script, reformat for MongoDB insertion and then place each row as a query-able document in the MongoDB 'Midland_Property_info. ![data_insertion](PowerPoints/captures/Alec_data_insertion_mongo_db.png)

## Back-End API construction
An API was made to pull information from the database and then relay to the Front-End JavaScript Application that would chop up the data, place into selected lists and turn into visuals for the user.


![Flask_API](PowerPoints/captures/Alec_Flask_API.png)

## Fron-End JavaScript Construction
The Front end captures and holds the user query, passes query to API using D3 which reponds with a jsonified list of dictionaries for parsing and Map construction using Leaflet, and Leaflet-Heat.


> Leaflet.js -> https://leafletjs.com/


> Heatmap.js -> https://www.patrick-wied.at/static/heatmapjs/


#### JS CODE: 
![JS Code Capture](PowerPoints/captures/alec_JS_screenshot.png)

# Analysis
Creating a Full Stack application that involved taking user input, passing to API, returning the correct information, then parseing ans assembling data for use through the Javascript was a mighty task. Everything fell together one day before the Project was set for review and after some initial tinkering, the application was able to send a request, parse the response and deliver a versitile map. 

![OverView Neighborhood](PowerPoints/captures/Alec_finished_map_02.png)

# Conclusion

Having information visualization change on the whim of the user is a fantastic and powerful tool. Seeing data portrayed in different styles allows for potentially unseen trends to emerge. More impressive is that these visualizations can be built around dynamic datasets allowing for the applications to change based on the amount of information present, paving the way for utilitarian applications that are visually appealing, interesting and intuitive.

