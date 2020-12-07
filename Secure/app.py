import io
import sys
import csv
import os
import uuid
import csv
import json
import flask_pymongo
from flask_pymongo import PyMongo
from pprint import pprint
import datetime
import flask
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,)
import bson
from bson.json_util import dumps



# Use PyMongo to establish Mongo connection

# try:
#     uri = os.environ["MONGODB_URI"]
    


app=Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb+srv://squ0sh:JBml100$@tododata.mutlv.mongodb.net/flight?retryWrites=true&w=majority")


# Call the Database and Collection
flight = mongo.db
flightData = flight.db


@app.route("/")
def home():
    
    return render_template("index.html", flightData=flightData)
        
# Dump json into Database
#loaded json to Mongo, json created from a df using pandas to clean a csv
jsonpath = os.path.join("data", "airports.json")
with open(jsonpath) as datafile:
    air_data = json.load(datafile)
    if isinstance(air_data, list):
        flightData.insert_many(air_data)
    else:
        flightData.insert_one(air_data)
        
jsonpathO = os.path.join("data", "Airport_Output.json")
with open(jsonpathO) as datafile:
    airportOut = json.load(datafile)
    if isinstance(airportOut, list):
        flightData.insert_many(airportOut)
    else:
        flightData.insert_one(airportOut)

@app.route("/flight")    
def index():
    flightData = list(mongo.db.find())
    resp = json.dumps(flightData)   
    return resp
# @app.route('/users')
# def users():
#     users = flight.flightData.find()
#     resp = json.dumps(users)
#     return resp

#Pull javascript Data to run with flask
# @app.route('/data')
# def get_javascript_data(json_from_csv):
    
#     return json.load("data", "airports.csv")[0]       


# def create_csv(text):
#     unique_id = str(uuid.uuid4())
#     with open('images/'+unique_id+'.csv', 'a') as file:
#         file.write(text[1:-1]+"\n")
#     return unique_id    

# def get_file_content(uuid):
#     with open(uuid+'.csv', 'r') as file:
#         return file.read()
    
   
    #return render_template("index.html", flightData=(flightOutput, flightPorts)


       #return redirect("/", code=302)

if __name__=="__main__":
    # client = MongoClient()
    # db = client.flight
    # collection = db.flightData
    # cursor = collection.find({})
    # # with open('collection.json', 'w') as file:
    # #     file.write('[')
    # #     for document in cursor:
    #         file.write(dumps(document))
   
    
    app.run(debug=True)