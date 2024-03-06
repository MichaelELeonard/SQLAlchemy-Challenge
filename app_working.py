# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



#################################################
# Database Setup
#################################################

# Create Engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect = True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station



########################################################################
# Figure out one year back date from end of data in the hawaii.sqlite DB
########################################################################

# Create session
session = Session(engine)

# Find the last date in the DB
recent_measurement_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

# Separate year/month/date info
last_measurement_date = dt.datetime.strptime(recent_measurement_date[0], '%Y-%m-%d') # Concept from https://community.esri.com/t5/python-questions/python-complains-about-date-format/td-p/494167

# Set most recent measurement date in data set (reassemble)
recent_measurement_date = dt.date(last_measurement_date.year, last_measurement_date.month, last_measurement_date.day)

# Calculate the date one year earlier from most recent measurement date (reassemble)
one_year_before_measurement_date = dt.date(last_measurement_date.year - 1, last_measurement_date.month, last_measurement_date.day)



#########################################################
# Find the most active station name from hawaii.sqlite DB
#########################################################

# Sort the stations with the most active on top
active_stations = session.query(Measurement.station,func.count(Measurement.id)).\
        group_by(Measurement.station).order_by(func.count(Measurement.id).desc()).all()

#Pull the most active station name
most_active_station_name = active_stations[0][0]



#################################################
# Flask Setup
#################################################

# Create an app, being sure to pass __name__
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

# Define index route

@app.route("/")
def index():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"Precipitation: /api/v1.0/precipitation<br/>" 
        f"Stations: /api/v1.0/stations<br/>" 
        f"Temperature: /api/v1.0/tobs<br/>" 
        f"Enter Start Date: /api/v1.0/yyyy-mm-dd<br/>" 
        f"Enter Start Date & End Date: /api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br/>" 
    )



#####################################################

# Define precipitation route

@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    sel = [Measurement.date,Measurement.prcp]
    
    queryresult = session.query(*sel).filter(Measurement.date >= one_year_before_measurement_date).all()
    
    session.close()

    precipitation = []
    for date, prcp in queryresult:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        precipitation.append(prcp_dict)

    return jsonify(precipitation)



#####################################################

# Define stations route

@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    sel = [Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation]
    
    queryresult = session.query(*sel).all()
    
    session.close()

    the_stations = []
    for station,name,latitude,longitude,elevation in queryresult:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Latitude"] = latitude
        station_dict["Longitude"] = longitude
        station_dict["Elevation"] = elevation
        the_stations.append(station_dict)

    return jsonify(the_stations)



#####################################################

# Define tobs route

@app.route('/api/v1.0/tobs')
def temperature():
    session = Session(engine)
    sel = [Measurement.date,Measurement.tobs]

    most_active_station = session.query(*sel).filter(Measurement.station == most_active_station_name)\
        .filter(Measurement.date >= one_year_before_measurement_date).order_by(Measurement.date).all()
    
    session.close()

    temperature = []
    for date, tobs in most_active_station:
        temp_dict = {}
        temp_dict["Date"] = date
        temp_dict["Temperature"] = tobs
        temperature.append(temp_dict)

    return jsonify(temperature)



#####################################################

# Define user entered start date route

@app.route('/api/v1.0/<start_date>')
def entered_start(start_date):
    session = Session(engine)
    sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    
    queryresult = session.query(*sel).filter(Measurement.date >= start_date).all()
    
    session.close()

    results = []
    for min, max, avg in queryresult:
        start_date_dict = {}
        start_date_dict["Minimum"] = min
        start_date_dict["Maximum"] = max
        start_date_dict["Average"] = avg      
        results.append(start_date_dict)

    return jsonify(results)



#####################################################

# Define user entered start date & end date route

@app.route('/api/v1.0/<start_date>/<end_date>')
def entered_start_end(start_date, end_date):
    session = Session(engine)
    sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    
    queryresult = session.query(*sel).filter(Measurement.date >= start_date)\
        .filter(Measurement.date <= end_date).all()
    
    session.close()

    results = []
    for min, max, avg in queryresult:
        start_end_date_dict = {}
        start_end_date_dict["Minimum"] = min
        start_end_date_dict["Maximum"] = max
        start_end_date_dict["Average"] = avg      
        results.append(start_end_date_dict)

    return jsonify(results)



#####################################################

if __name__ == '__main__':
    app.run(debug=True)
