# sqlalchemy-challenge
For week 10 SQLAlchemy we were tasked with conducting a climate analysis.  The data for the analysis was gathered from nine weather out post stations and contains data from 2010 to 2017.  The components of this two-part analysis included:
•	PART 1: ANALYZE AND EXPLORE THE CLIMATE DATA
o	Precipitation Analysis
o	Station Analysis
•	PART 2: DESIGN YOUR CLIMATE APP

PART 1: ANALYZE AND EXPLORE THE CLIMATE DATA

THE SETUP
Python and SQLAlchemy were utilized to conduct this component of the analysis.  A Jupyter Source Code file climate_working was used to assess a SQLITE File hawaii.sqlite which contained the data.  The needed dependencies were imported and SQLAlchemy used to map the code to the existing database using the create_engine() and automap_base() functions.  Finally, references were established to the class tables in the database name station and measurement and a SQLAlchemy session was established.  

PRECIPITATION ANALYSIS
For the precipitation analysis, I was tasked to examine the last 12 months of data in the hawaii.sqlite datsabase.  The first step in the analysis was to to identify the most recent data point in the database.  This was achieved by sorting the hawaii.sqlite by measurement date, organizing it in descending and then taking the first entry in the query which contained the most recent date.  This information was stored in the variable recent_measurement_date and parsed into its individual components, Year, Month and Date.  Two dates were then created and from these components recent_measurement_date and one_year_before_measurement_date which were utilized in the rest of the analysis.  The last year of precipitation was extracted from the hawaii.sqlite database and read into a pandas dataframe.  A line graph was created with dates on the x-axis and precipitation levels in inches on the y-axis and summary statistics were extracted from the data.

EXPLORATORY STATION ANALYSIS
In this section the name and frequency of the nine weather analysis stations was queried and place in order of activity with the most active station as first in the list and last active in the last place.  The name of the most active station was stored in the variable most_active_station_name and the min, max and average temperature was queried for the station.  A histogram was then created from the last year of data for the most active station with the temperature on the x-axis and the frequence on the y-axis. 

PART 2: DESIGN YOUR CLIMATE APP
For the second portion of the interactive climate was created using Python a Flask.  An engine was established and mapped to the hawaii.sqlite database.  The database was reflected using automap_base()  references to the station and measurement tables were established.  The variable one_year_before_measurement_date was acquired and the most active station was established in the same manner as in the first portion of the analysis.  An app was then created through flask and Flask(__name__) was passed.  An API Index was set up to display all the available API routes for the end user to utilize.  These routes included: 
•	f"Available Routes:<br/>"
•	f"Precipitation: /api/v1.0/precipitation<br/>" 
•	f"Stations: /api/v1.0/stations<br/>" 
•	f"Temperature: /api/v1.0/tobs<br/>" 
•	f"Enter Start Date: /api/v1.0/yyyy-mm-dd<br/>" 
•	f"Enter Start Date & End Date: /api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br/>"

PRECIPITATION 
For the precipitation static API route, the measurement date and precipitation amount for the last year of data was collected for the database.  This information was then stored in the variable queryresult with was the read into a list for dictionaries and displayed through the browser through the return jsonify(precipitation) function.  The output data included:
•	Date
•	Precipitation

STATIONS
For the precipitation static API route all the data specific to each station was queried from the database and returned through the browser through the return jsonify(precipitation) function.  The station specific data included:
•	Station
•	Name
•	Latitude
•	Longitude
•	Elevation

TEMPERATURE  
For the temperature static API route, the last year of temperature for the most active station was stored in the variable active_station using our previously established variables most_active_station_name and one_year_before_measurement_date.  The data was then read into a list of dictionaries and displayed through the browser through the return jsonify(precipitation) function.  The output data included:
•	Date
•	Temperature

START DATE & START DATE & END DATE
For the Start Date/Start & End Date dynamic API routes the end user enters the Start or Start and End dates to be searched and the app for the route will use the input to set the query date range and then return the min, max and avg temperatures in the range.  Both app’s function identically with the only difference being whether the end user inputs one or two dates and a slight difference in the Start and End query to accommodate for the second input.  The output date for the Start Date/Start & End Date dynamic API routes include:
•	Minimum
•	Maximum
•	Average
