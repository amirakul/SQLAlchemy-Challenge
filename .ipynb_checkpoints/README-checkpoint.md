# SQLAlchemy Challenge

## Step 1 - Climate Analysis and Exploration

To begin, I used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. 
I randomly chose a start date and end date for my trip, where vacation range is approximately 3-15 days total.
Then, I used SQLAlchemy create_engine to connect to the sqlite database.
Next, I used SQLAlchemy automap_base() to reflect your tables into classes and saved a reference to those classes called Station and Measurement.


Precipitation Analysis
Design a query to retrieve the last 12 months of precipitation data.

Select only the date and prcp values.

Load the query results into a Pandas DataFrame and set the index to the date column.

Sort the DataFrame values by date.

Plot the results using the DataFrame plot method

Step 2- Station Analysis
Design a query to calculate the total number of stations.

Design a query to find the most active stations.

List the stations and observation counts in descending order.

Which station has the highest number of observations?

Hint: You will need to use a function such as func.min, func.max, func.avg, and func.count in your queries.

Design a query to retrieve the last 12 months of temperature observation data (TOBS).

Filter by the station with the highest number of observations.

Plot the results as a histogram with bins=12.