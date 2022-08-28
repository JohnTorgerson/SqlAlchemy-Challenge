#################################################
# 1. import tools and Database Setup
#################################################
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Reflect database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)

# Ssve references to the tables
mea = Base.classes.measurement
sta = Base.classes.station





#################################################
# 2. Flask Setup
#################################################
app = Flask(__name__)


#################################################
# 4. Setup 1st Endpt Route
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii weather station program!</br></br><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation</br>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start> ( Enter a start date YYYY-MM-DD )<br/>"
        f"/api/v1.0/<start> ( Enter a start date YYYY-MM-DD ) /<end> ( and an additional end date YYYY-MM-DD)<br/><br/>"
        f"For best results use a start date between 2010-01-01 & 2017-08-23"
    )

#################################################
# 5. Setup Additional Endpt Routes
#################################################

@app.route("/api/v1.0/precipitation")
def precips():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precipitation data"""
    # Query all prcp data from measurement table
    results = session.query(mea.date, mea.prcp).all()

    # Convert list of tuples to list
    precip = list(np.ravel(results))

    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stas():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precipitation data"""
    # Query all prcp data from measurement table
    results = session.query(sta.station, sta.name).all()

    # Convert list of tuples to list
    sts = list(np.ravel(results))

    return jsonify(sts)

@app.route("/api/v1.0/tobs")
def tempobs():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precipitation data"""
    # Query all prcp data from measurement table
    results = session.query(mea.date, mea.tobs).filter(mea.date > '2016-08-22').order_by(mea.date).all()
    # Convert list of tuples to list
    tbs = list(np.ravel(results))

    return jsonify(tbs)

# Return another app route with user input varaibles
@app.route("/api/v1.0/<start_date>")
def star(start_date):
    """Fetch the min avg and max between available dates
       as a path variable supplied by the user, or a 404 if not."""

    canonicalized = start_date.replace(" ", "").lower()
    for query in mea:
        session.query(mea.station, func.min(mea.tobs), func.avg(mea.tobs), func.max(mea.tobs)).filter(mea.date >= {start_date}).all()

        if search_term == canonicalized:
            return jsonify(query)

    return jsonify({"error": f"That is not a date recognized by this dataframe. Please enter a startdate between {real_name} not found."}), 404

#################################################
# 3. Run Main App debugger for main endpt
#################################################

if __name__ == "__main__":
    app.run(debug=True)
