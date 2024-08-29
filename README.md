<img src="Pics/Header.png" width="727" height="294">

# SQLAlchemy/Flask Challenge



## GOAL
For the SQLAlchemy/Flask Challenge we were tasked with conducting a climate analysis.  The data for the analysis was gathered from nine weather out post stations Honolulu Hawaii and contains data gathered from 2010 to 2017.  The components of this two-part analysis included:
* PART 1: ANALYZE AND EXPLORE THE CLIMATE DATA (SQLAlchemy)
* PART 2: DESIGN YOUR CLIMATE APP (Flask)


## PART 1: ANALYZE AND EXPLORE THE CLIMATE DATA
Climate Data code - https://github.com/MichaelELeonard/sqlalchemy-challenge/blob/main/climate_working.ipynb

### THE SETUP

Python and SQLAlchemy were utilized to conduct this component of the analysis.  A Jupyter Source Code file climate_working was used to assess a SQLITE File hawaii.sqlite which contained the data.  The needed dependencies were imported and SQLAlchemy was used to map the code to the existing database using the create_engine() and automap_base() functions.  Finally, two references were established to the class tables in the database named station and measurement and a SQLAlchemy session was established.   

### PRECIPITATION ANALYSIS

For the precipitation analysis, we were tasked to examine the last 12 months of data in the hawaii.sqlite datsabase.  The first step in the analysis was to identify the most recent data point in the database.  This was achieved by sorting the hawaii.sqlite by measurement date and sorting it in descending order and then taking the first entry in the query which contained the most recent date.  This information was parsed into its individual components, Year, Month and Date.  Two dates were then created and from these parced date components recent_measurement_date and one_year_before_measurement_date.  These two date variables were utilized in the rest of the analysis for quaries.  The last year of precipitation data was then extracted from the hawaii.sqlite database and read into a pandas dataframe.  A line graph was created with the x-axis comprised of dates and the y-axis displaying precipitation levels in inches.  Finally summary statistics were extracted from the data.

<img src="Pics/Precipitation data.png" width="517" height="467">

<img src="Pics/Precipitation summary statistics.png" width="151" height="224">


### EXPLORATORY STATION ANALYSIS

In this section we analyzed the nine most active weather stations.  A histogram was then created from the final year data for the most active station, with the temperature on the x-axis and the frequence on the y-axis. 

<img src="Pics/Most active stations.png" width="190" height="189">

<img src="Pics/Most active station temp.png" width="527" height="383">

<br>
<br>



<img src="Pics/Flask Header.png" width="555" height="202">

## PART 2: DESIGN YOUR CLIMATE APP
Climate App code - https://github.com/MichaelELeonard/sqlalchemy-challenge/blob/main/app_working.py

For the second portion of the SQLAlchemy Challenge an interactive climate app was created using Python and Flask.  An engine was established and mapped to the hawaii.sqlite database.  The database was reflected using automap_base() and references to the station and measurement tables were established.  API Index was established to display all the available API routes for the end user to utilize.

<img src="Pics/Routes.png" width="443" height="128">

### PRECIPITATION 
For the precipitation static API route, the measurement date and precipitation amount for the last year of data was collected for the database.  This information was then stored in the variable query result and was read into a list for dictionaries and displayed.  The output data included:
* Date
* Precipitation

<img src="Pics/Precipitation.png" width="220" height="328">


### STATIONS
For the precipitation static API route all the data specific to each station was queried from the database and returned through the browser.  The station specific data included:
* Elevation
* Latitude
* Longitude
* Name
* Station

<img src="Pics/Stations.png" width="408" height="556">

### TEMPERATURE  
For the temperature static API route, the last year of temperature for the most active station was acquired and stored.  The data was then read into a list of dictionaries and displayed through the browser.  The output data included:
* Date
* Temperature

<img src="Pics/Tobs.png" width="210" height="328">

### START DATE & START DATE & END DATE
For the Start Date and Start & End Date dynamic API routes the end user will manually enter the Start or Start and End dates to establish the date range to be examined.   These input dates will be utilized to query the database and calculate the min, max and avg temperatures of the requested range.  Both API routes function identically with the only differences being if the end user inputs one or two dates and a slight difference in the query structure to accommodate for the second input.  The output fields for the Start Date/Start & End Date dynamic API routes include:
* Average
* Minimum
* Maximum

Date manually entered 2010-09-18

<img src="Pics/Enter date.png" width="446" height="232">

Date manually entered 2010-09-18 to 2010-09-24

<img src="Pics/Enter range.png" width="529" height="228">

