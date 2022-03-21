from flask import Flask,request
from flask_cors import CORS, cross_origin
import requests
from requests.auth import HTTPBasicAuth
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
import utils

@app.route("/create_phrase", methods=['GET', 'POST'])
@cross_origin()
def hello_world():
    # receive json from frontend
    data = request.get_json(force=True)
    zip_code = data['zipCode']
    name = utils.pig_latin(data['name'])

    # if the name have no letters,prompt user to re-enter their name
    if not name:
        ans = "Please re-enter your name"
        return {"r":ans},200

    # request the api to get json
    r_population = requests.get(
        "https://service.zipapi.us/population/zipcode/{}?X-API-KEY=d6991763e3bfea9ba9285e62d8cd65b2&fields=male_population,female_population".format(zip_code),
        auth=HTTPBasicAuth("1261835631@qq.com", "hyq5566123"))
    r_county = requests.get(
        "https://service.zipapi.us/zipcode/county/{}?X-API-KEY=d6991763e3bfea9ba9285e62d8cd65b2".format(zip_code),
        auth=HTTPBasicAuth("1261835631@qq.com", "hyq5566123"))

    popu_json = r_population.json()
    county_json = r_county.json()

    # if the api reach the time limit
    if 'error' in popu_json.keys():
        ans = popu_json['error']
        return {"r":ans},200

    # if everything ok, return the processed data
    if popu_json['status'] == True and county_json['status'] == True:
        res = popu_json['data']
        population = res['population']
        res = county_json['data']
        county = res['county'][0]
        ans = "{}’s zip code is in {} and has a population of {}".format(name,county,population)
        return {"r":ans},200

    # if the zip code have some problem
    else:
        ans = county_json['message']
        return {"r":ans},200

