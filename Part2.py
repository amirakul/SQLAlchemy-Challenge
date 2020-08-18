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
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station=Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session=Session(engine)
    # Query all dates with precip
    results1 = session.query(measurement.date,measurement.prcp).\
        filter(measurement.date >= '2016-08-23').all()
    session.close()
    # Convert list of tuples into normal list
    #first_dict=list(np.ravel(results1))
    d = {key: value for key,value in results1 }
    #Return JSON representation of the dictionary
    return jsonify(d)


@app.route("/api/v1.0/stations")
def stations():
    session=Session(engine)
    # Query all stations
    results2 = session.query(station.station, station. name).all()
    session.close()
    # Convert list of tuples into normal list
    #sec_dict = list(np.ravel(results2))

    return jsonify(results2)

@app.route("/api/v1.0/tobs")
def tobs():
    session=Session(engine)
    # Query all temp.
    results3 = session.query(measurement.date, measurement.tobs).filter(measurement.station == 'USC00519281').\
        filter(measurement.date >= '2016-08-23').all()
    session.close()

    # Convert list of tuples into normal list
    #third_dict = list(np.ravel(results3))


    return jsonify(results3)

@app.route("/api/v1.0/<start>")
def start(start):
    session=Session(engine)
    # Query/calculate TMIN, TAVG,TMAX for all dates greater than and equal to the start date
    results4 = session.query(measurement.date,func.min(measurement.tobs),func.avg(measurement.tobs),func.max(measurement.tobs)).\
        filter(measurement.date>=start).all()
    session.close()

    date_dict={}
    for result in results4:
        date_dict["Date"]=result[0]
        date_dict["Min/Lowest Temp"]=result[1]
        date_dict["Avg Temp"]=result[2]
        date_dict["Max/Highest Temp"]=result[3]
    return jsonify(date_dict)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    session=Session(engine)
    # Query/calculate TMIN, TAVG,TMAX for all dates greater than and equal to the start date
    results5 = session.query(measurement.date,func.min(measurement.tobs),func.avg(measurement.tobs),func.max(measurement.tobs)).\
        filter(measurement.date>=start).\
        filter( measurement.date<=end).all()
    session.close()
    date_dict={}
    for result in results5:
        date_dict["Min/Lowest Temp"]=result[1]
        date_dict["Avg Temp"]=result[2]
        date_dict["Max/Highest Temp"]=result[3]
    return jsonify(date_dict) 
if __name__ == '__main__':
    app.run(debug=True)
