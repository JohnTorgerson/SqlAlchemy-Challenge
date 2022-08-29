# SqlAlchemy-Challenge

### Exploring and Analyzing Climate to Design Travel App Based on Conditions

##### Authors:
* John Torgerson (JohnTorgerson)
---
   
##### Tools and Supplies:
* < Database and table description here >

* Python, SQLAlchemy, Pandas, Matplotlib and Flask; SQLAlchemy ORM session queriies were made from SQLite data and Flask sessions and jsonify
---

### Guide to Repo Contents:

* `climate_notebook.ipynb` is the jupyter notebook used with Matplotlib, Pandas, SQLAlchemy to explore the tables and execute the analysis
* `app.py` contains the SQLite code for the Flask Endpoint app with SQLAlchemy and JSONify
* In folder, `Resources` are the following 6 tables:
    1. `hawaii.sqlite` is a database of precipitation measurements at 9 stations
    2. `hawaii_measurements.csv` is a table of precip measurements over time from all stations
    3. `hawaii_stations.csv` is a table of geographic stations where the measurements were taken
    4. `Precipitation.png` is a plot of precipitation values over the most recent year
    5. `tobs_year.png` is a histogram showing time of observation changes over the most recent year
---

### Flask Endpoints:
* /
* /api/v1.0/precipitation
* /api/v1.0/stations
* /api/v1.0/tobs
* /api/v1.0/<start_date>
* /api/v1.0/<start_date>/<end_date>
---

### Credits and Special Thanks

* Thanks to Sanoo Singh for helping me clean up my plot labels and legend