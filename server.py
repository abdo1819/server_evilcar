#!/usr/bin/env python3
import os
from flask import Flask, jsonify, request, render_template
import json
from model.user_car import UserCar
import sql_db_connection
import db_setup
import datetime
import names
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)

data_manager = db_setup.data_manager()
#
# engine = create_engine('sqlite:///violations.db?check_same_thread=False')
# Base.metadata.create_all(engine)

engine = sql_db_connection.create_engine(host="localhost",
                                         database_type = "oracle",
                                         port=1521,
                                         sid="xe",
                                         user="abdullah",
                                         password="a")

DBSession = sessionmaker(bind=engine)
session = DBSession()

# violations_list= []
speedLimit = 0.1
# obstacles = []

print("NOTE: Remember to edit the javascript hardcoded url")


@app.route('/speed', methods=["GET"])
def getSpeed():
    # return request.args.get('long')+" - "+request.args.get('lat')
    # TODO: do some server logic here
    longitude = float(request.args.get('long'))
    lat = float(request.args.get('lat'))
    data = data_manager.get_data(names.roads, collection_filter={names.starting_longitude: longitude,
                                                                 names.starting_latitude: lat})
    print({names.starting_longitude: longitude, names.starting_latitude: lat})
    print(data)
    result = [i for i in data]
    return result[0]
    # return jsonify(speed = speedLimit,endingLong=longitude+1,endingLat=lat+1)


@app.route('/report', methods=["POST"])
def report():
    if request.method == "POST":
        # TODO: do more than printing the data here
        data = json.loads(request.get_data(as_text=True))
        data['time'] = str(datetime.datetime.now())
        data_manager.add_data(names.violations_collection, data)
        return "thanks for using our service"
    else:
        return "use post to post your violation"


@app.route('/violations/json', methods=["GET"])
def get_violations_json_():
    # qryresult = session.query(Violation).all()
    result = [c for c in data_manager.get_data(names.violations_collection)]
    result.reverse()
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/violations', methods=['GET'])
def get_violations():
    return render_template('index.html')


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/obstacles", methods=['GET'])
def send_obstacles():
    data_manager.add_data(names.obstacles_collection, {'long': request.args.get('long'),
                                                       'lat': request.args.get('lat'),
                                                       'time': str(datetime.datetime.now())})
    # obstacles.append((request.args.get('long'),request.args.get('lat'),datetime.datetime.now()))
    return "thanks for reporting road"


@app.route("/obstacles/json", methods=['GET'])
def get_obstacles_():
    data = data_manager.get_data(names.obstacles_collection)
    result = [i for i in data]
    # print(request.args.get('long'),request.args.get('lat'))
    return jsonify(result)
# route to adding users
@app.route('/adduser', methods=["POST"])
def add_user():
    if request.method == "POST":
        # TODO: do more than printing the data here
        print("request is:", request.get_data())
        data = json.loads(request.get_data(as_text=True))
        u = UserCar(car_id=data['car_id'],user_id=data['user_id'])
        session.add(u)
        session.commit()
        return "thanks for using our service"
    else:
        return "use post to post your violation"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
