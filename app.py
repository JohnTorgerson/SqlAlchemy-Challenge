#################################################
# 1. import tools
#################################################
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

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
        f"Welcome to the name of this program!<br/>"
        f"Available Routes:<br/>"
        f"/mypath/something-here<br/>"
        f"/mypath/something-here/table/column<br/>"
        f"/mypath/something-here/table/another-column"
    )

#################################################
# 5. Setup Additional Endpt Routes
#################################################

#@app.route("/mypath/something_here/lovely-variable/<my_variable>")
#def tableortupleorlookthisup(my_variable):
#    """Fetch the data in the database whose my_variable matches
#       the path variable supplied by the user, or a 404 if not."""
#
#    canonicalized = my_variable.replace(" ", "").lower()
#    for element in justice_league_members:
#        search_term = table["my_variable"].replace(" ", "").lower()
#
#        if search_term == canonicalized:
#            return jsonify(element)
#
#    return jsonify({"error": f"Result for lovely_variable {my_variable} not found."}), 404

#################################################
# 3. Run Main App debugger for main endpt
#################################################

if __name__ == "__main__":
    app.run(debug=True)
