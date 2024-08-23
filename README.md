<img src="Pics/Header.png" width="727" height="294">

# SQLAlchemy Challenge
Climate Data code - https://github.com/MichaelELeonard/sqlalchemy-challenge/blob/main/climate_working.ipynb

Climate App code - https://github.com/MichaelELeonard/sqlalchemy-challenge/blob/main/app_working.py

<br>

## GOAL
For the SQLAlchemy Challenge we were tasked with conducting a climate analysis.  The data for the analysis was gathered from nine weather out post stations Honolulu Hawaii and contains data gathered from 2010 to 2017.  The components of this two-part analysis included:
* PART 1: ANALYZE AND EXPLORE THE CLIMATE DATA
* PART 2: DESIGN YOUR CLIMATE APP


## PART 1: ANALYZE AND EXPLORE THE CLIMATE DATA

### THE SETUP

Python and SQLAlchemy were utilized to conduct this component of the analysis.  A Jupyter Source Code file climate_working was used to assess a SQLITE File hawaii.sqlite which contained the data.  The needed dependencies were imported and SQLAlchemy was used to map the code to the existing database using the create_engine() and automap_base() functions.  Finally, two references were established to the class tables in the database named station and measurement and a SQLAlchemy session was established.   

### PRECIPITATION ANALYSIS

For the precipitation analysis, I was tasked to examine the last 12 months of data in the hawaii.sqlite datsabase.  The first step in the analysis was to identify the most recent data point in the database.  This was achieved by sorting the hawaii.sqlite by measurement date and sorting it in descending order and then taking the first entry in the query which contained the most recent date.  This information was stored in the variable recent_measurement_date and parsed into its individual components, Year, Month and Date.  Two dates were then created and from these parced date components recent_measurement_date and one_year_before_measurement_date.  These two date variables were utilized in the rest of the analysis for quaries.  The last year of precipitation data was then extracted from the hawaii.sqlite database and read into a pandas dataframe.  A line graph was created with the x-axis comprised of dates and the y-axis displaying precipitation levels in inches.  Finally summary statistics were extracted from the data using prcp_results_pd.describe()

### EXPLORATORY STATION ANALYSIS

In this section of the analysis the nine weather analysis stations and their corresponding data were queried and sorted by activity, with the most active station as first in the list and least active station in the last entry.  The name of the most active station was stored in the variable most_active_station_name and the min, max and average temperature was queried for the most active station.  A histogram was then created from the final year data for the most active station, with the temperature on the x-axis and the frequence on the y-axis. 

## PART 2: DESIGN YOUR CLIMATE APP

For the second portion of the SQLAlchemy Challenge an interactive climate app was created using Python and Flask.  An engine was established and mapped to the hawaii.sqlite database.  The database was reflected using automap_base() and references to the station and measurement tables were established.  The variable one_year_before_measurement_date was acquired, and the most active station was established in the same manner as in the first portion of the analysis.  An app was then created through flask and Flask(__name__) was passed.  An API Index was set up to display all the available API routes for the end user to utilize.

### PRECIPITATION 
For the precipitation static API route, the measurement date and precipitation amount for the last year of data was collected for the database.  This information was then stored in the variable query result with was read into a list for dictionaries and displayed through the browser using the return jsonify(precipitation) function.  The output data included:
* Date
* Precipitation

### STATIONS
For the precipitation static API route all the data specific to each station was queried from the database and returned through the browser utilizing the return jsonify(the_stations) function.  The station specific data included:
* Station
* Name
* Latitude
* Longitude
* Elevation

### TEMPERATURE  
For the temperature static API route, the last year of temperature for the most active station was acquired and stored in the variable active_station using our previously established variables most_active_station_name and one_year_before_measurement_date in the query.  The data was then read into a list of dictionaries and displayed through the browser using the return jsonify(temperature) function.  The output data included:
* Date
* Temperature

### START DATE & START DATE & END DATE
For the Start Date/Start & End Date dynamic API routes the end user will manually enter the Start/Start and End dates to identify the date range to be examined.   These specific input dates will be utilized to query the database and calculate the min, max and avg temperatures of the requested range.  Both API routes function identically with the only differences being if the end user inputs one or two dates and a slight difference in the query structure to accommodate for the second input.  The output fields for the Start Date/Start & End Date dynamic API routes include:
* Minimum
* Maximum
* Average

