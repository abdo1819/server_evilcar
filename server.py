#!/usr/bin/env python3
import os
from flask import Flask,jsonify,request,render_template
import json
import logging

app = Flask(__name__)


violations_list= []
speedLimit = 0.1
obstacles = []

@app.route('/speed',methods=["GET"])
def getSpeed():
    # return request.args.get('long')+" - "+request.args.get('lat')
    # TODO: do some server logic here
    long = float(request.args.get('long'))
    lat = float(request.args.get('lat'))
    return jsonify(speed = speedLimit,endingLong=long+1,endingLat=lat+1)

@app.route('/report',methods=["GET","POST"])
def report():
    if request.method=="POST":
        #TODO: do more than printing the data here
        violations_list.append(request.get_data(as_text=True))
        print(violations_list)
        return "thanks for using our service"
    else:
        return "use post to post your violation"


@app.route('/violations/json',methods=["GET"])
def get_violations_json():
    objects =[]
    for string in violations_list : 
        objects.append( json.loads(string))
    response = jsonify(objects)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/violations', methods=['GET'])
def get_violations():
    return render_template('index.html',violations_list = violations_list)

@app.route("/")
def hello():
    return render_template('index.html',violations_list = violations_list)

@app.route("/obstacles",methods=['GET'])
def send_obstacles():
    print(request.args.get('long'),request.args.get('lat'))
    obstacles.append((request.args.get('long'),request.args.get('lat')))
    return jsonify(obstacles)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)