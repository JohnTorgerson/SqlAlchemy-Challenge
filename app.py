#################################################
# 1. import tools and Database Setup
#################################################
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Reflect database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)

# Ssve references to the tables
mea = Base.classes.measurement
sta = Base.classes.station

MI = func.min(mea.tobs)
AV = func.avg(mea.tobs)
MA = func.max(mea.tobs)

#################################################
# 2. Flask Setup
#################################################
app = Flask(__name__)


#################################################
# 4. Setup 1st Endpt Route
#################################################

@app.route("/")

def welcome():
    session = Session(engine)

    # desc tool currently not supported
    first_date = session.query(mea.date).order_by(mea.date).first()[0]
    #last_date = session.query(mea.date).order_by(mea.date.desc).first()[0]
    last_date = '2017-08-23'

    return (
        f"Welcome to the Hawaii weather station program!</br></br><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation</br>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start> ( Enter a start date YYYY-MM-DD )<br/>"
        f"/api/v1.0/<start> ( Enter a start date YYYY-MM-DD ) /<end> ( and an additional end date YYYY-MM-DD)<br/><br/>"
        f"For best results use a start date between {first_date} & {last_date} and enter them in chronological order"
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

# Return another app route with user start date input varaibles
@app.route("/api/v1.0/<start_date>")

def query_by_startdate(start_date):
    """Fetch the min avg and max temps between available dates
       as a path variable supplied by the user, or a 404 if not."""

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # define barriers # desc currently not supported
    first_date = session.query(mea.date).order_by(mea.date).first()[0]
    #last_date = session.query(mea.date).order_by(mea.date.desc).first()
    last_date = '2017-08-23'

    # #for query in mea:
        #search = ['date']

    if start_date > last_date:
        return (f"Error: That is not a date recognized by this dataframe. 404<br/><br/>Please enter a startdate between 2010-01-01 and 2017-08-23, and in the format of YYYY-MM-DD.")

    elif start_date < first_date:
        return (f"Error: That is not a date recognized by this dataframe. 404<br/><br/>Please enter a startdate between 2010-01-01 and 2017-08-23, and in the format of YYYY-MM-DD.")
        
    else:
        query = session.query(MI, AV, MA).filter(mea.date >= start_date).all()
    
        sd = list(np.ravel(query))
        return jsonify(f"Min, Avg, Max temps from {start_date} to {last_date}.", sd)

# Now add an end date
@app.route("/api/v1.0/<start_date>/<end_date>")

def query_by_end_date(start_date, end_date):
    """Fetch the min avg and max temps between available dates
       as a path variable supplied by the user, or a 404 if not."""

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # define barriers # desc currently not supported
    first_date = session.query(mea.date).order_by(mea.date).first()[0]
    #last_date = session.query(mea.date).order_by(mea.date.desc).first()
    last_date = '2017-08-23'

    # #for query in mea:
        #search = ['date']

    if start_date < first_date:
        return (f"Error: That is not a date recognized by this dataframe. 404<br/><br/>Please enter a startdate between 2010-01-01 and 2017-08-23, and in the format of YYYY-MM-DD.")

    elif start_date > last_date:
        return (f"Error: That is not a date recognized by this dataframe. 404<br/><br/>Please enter a startdate between 2010-01-01 and 2017-08-23, and in the format of YYYY-MM-DD.")
        
    elif end_date < first_date:
        return (f"Error: That is not a date recognized by this dataframe. 404<br/><br/>Please enter a startdate between 2010-01-01 and 2017-08-23, and in the format of YYYY-MM-DD.")

    elif end_date < start_date:
        return (f"Error: Those two dates are not chronological. 404<br/><br/>Please enter a startdate between 2010-01-01 and 2017-08-23, and in the format of YYYY-MM-DD.")

    elif end_date < last_date:
        query = session.query(MI, AV, MA).filter(mea.date >= start_date).filter(mea.date <= end_date).all()
    
        sd = list(np.ravel(query))
        return jsonify(f"Min, Avg, Max temps from {start_date} to {end_date}.", sd)

    else:
        query = session.query(MI, AV, MA).filter(mea.date >= start_date).all()
    
        sd = list(np.ravel(query))
        
        return jsonify(f"Sorry. Laast Date in table is {last_date} - Min, Avg, Max temps from {start_date} to {last_date}.", sd)

#################################################
# 3. Run Main App debugger for main endpt
#################################################

if __name__ == "__main__":
    app.run(debug=True)
