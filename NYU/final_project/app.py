from flask import Flask, render_template
from flask import request
import requests
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import googlemaps

app = Flask(__name__)



def address_to_coordnates(address):
  API_KEY = # API key
  data_type = 'json'
  endpoint = f'https://maps.googleapis.com/maps/api/place/details/{data_type}'
  google_places_API_URL = 'https://maps.googleapis.com/maps/api/place/details/json?'
  gmaps = googlemaps.Client(key=API_KEY)
  geolocator = Nominatim(user_agent="specify_here")
  location = geolocator.geocode(address)
  spot = {'latitude':location.latitude,'longitude':location.longitude}
  return spot


def get_restaurants(location):
    key = 'iI4dsdXt-g13ESGVicCEP7g8svwE657yNKQtQx0UXtrjgteJuPjddz_RYf92YIWiUJxpMx_To53E2hXoMQmnpOSc3Jws0L7SAQTH2Qdno9XFlOih236mUlx6AIEhW3Yx'
    auth_header = {'Authorization': 'Bearer ' + key}
    url = 'https://api.yelp.com/v3/businesses/search'

    parameters = {"latitude": location["latitude"], "longitude": location["longitude"], "radius": 30, "limit": 30,
                  "sort_by": "rating", "open_now": False}
    resp = requests.get(url, headers=auth_header, params=parameters)
    data = resp.json()

    df = pd.DataFrame(data['businesses'])
    df = pd.json_normalize(data['businesses'])
    df.drop('categories', axis='columns', inplace=True)
    df.drop('transactions', axis='columns', inplace=True)
    df.drop('image_url', axis='columns', inplace=True)
    df.drop('location.address2', axis='columns', inplace=True)
    df.drop('location.address3', axis='columns', inplace=True)
    df.drop('location.display_address', axis='columns', inplace=True)
    df.drop('phone', axis='columns', inplace=True)
    df = df.sort_values(['rating', 'review_count'], ascending=[False, False])
    df = df.head(4)
    names = list(np.array(df["name"].tolist()))
    rating = list(np.array(df["rating"].tolist()))
    numReviews = list(np.array(df["review_count"].tolist()))
    id_ = list(np.array(df["id"].tolist()))

    result = list()
    for i in range(4):
        info = {"rating": '', "review_count": 0, 'pop_reviews': []}

        n = names[i]
        info["rating"] = rating[i]
        info["review_count"] = numReviews[i]

        rev_url = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(id_[i])
        resp_ = requests.get(rev_url, headers=auth_header)
        datum = resp_.json()
        reviews = pd.DataFrame(datum["reviews"])
        reviews = reviews.sort_values(['rating'], ascending=[False])

        if len(reviews) > 4:
            reviews = reviews.head(4)
        else:
            pass
        reviews_ = reviews["text"].to_list()
        info["pop_reviews"] = "1. " + reviews_[0] + '; 2. ' + reviews_[1] + '; 3. ' + reviews_[2]
        info['name'] = n
        result.append(info)

    # key = restaurant name
    # values = {rating:int, review_count:int, popolur_reviews:string}
    df = pd.DataFrame.from_dict(result)
    df = df[['name', 'rating', 'review_count', 'pop_reviews']]
    return df.to_html()


def only_destination(dataframe, dataframe2):
    basic_form = '''
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>TABLE AND MAP</title>
        <h2>RESTAURANT INFO</h2>
    </head>
    <body>
    <div>
    <form action="/map" method='get'>
    <button type="submit" formaction="/map">Click to map!</button>
    </form>
    <hr style="width:50%;text-align:left;margin-left:0">
    </div>

    <h4>Restaruants @origin</h4>
    <div>{}</div>
    <hr style="width:50%;text-align:left;margin-left:0">
    <h4>Restaurants @destination</h4>
    <div>
    {}
    </div>
    </body>
    </html>
    '''.format(dataframe, dataframe2)
    return basic_form


def table_with_stops(dataframe, dataframe2, dataframe3):
    basic_form = '''
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>TABLE AND MAP</title>
        <h2>RESTAURANT INFO</h2>
    </head>
    <body>
    <div>
    <form action="/map" method='get'>
    <button type="submit" formaction="/map">Click to map!</button>
    </form>
    <hr style="width:50%;text-align:left;margin-left:0">
    </div>

    <h4>Restaruants @origin</h4>
    <div>{}</div>
    <hr style="width:50%;text-align:left;margin-left:0">
    <h4>Restaurants @destination</h4>
    <div>
    {}
    </div>
       <h4>Restaurants @stops</h4>
    <div>
    {}
    </div>
    </body>
    </html>
    '''.format(dataframe, dataframe2, dataframe3)
    return basic_form


def generate_info(spotList):
    locations = list()
    for spot in spotList:
        address = address_to_coordnates(spot)
        locations.append(address)

    if len(locations) == 2:
        df_origin = get_restaurants(locations[0])
        df_destination = get_restaurants(locations[1])
        return only_destination(df_origin, df_destination)

    elif len(locations) ==3:
        df_origin = get_restaurants(locations[0])
        df_destination = get_restaurants(locations[2])
        df_stop = get_restaurants(locations[1])
        return table_with_stops(df_origin, df_destination, df_stop)

    else:
        df_origin = get_restaurants(locations[0])
        df_destination = get_restaurants(locations[1])
        stopList = list()
        for i in range(1, len(locations) - 1):
            stopList.append(get_restaurants(locations[i]))
        df_stop = get_restaurants(stopList[0])
        for i in range(1, len(stopList)):
            df_stop2 = get_restaurants(stopList[i])
            df_stop.append(df2, ignore_index=True)
        return table_with_stops(df_origin, df_destination, df_stop)


@app.route("/")
def home():
    # origin = request.args.get('origin') #this would need to be passed as part of the url, not as an input, same as below
    # destination = request.args.get('destination')
    return render_template("location_input.html")


@app.route("/map")
def map():
    param_ori = request.args.get('origin')
    param_dest = request.args.get('destination')
    return render_template("map.html",
                           ori=param_ori,
                           dest=param_dest)


@app.route("/direction")
def direction():
    place = []
    param_ori = request.args.get('origin')
    param_dest = request.args.get('destination')
    param_avoid = request.args.get('avoid')
    stop1 = request.args.get('stop1')
    stop2 = request.args.get('stop2')
    stop3 = request.args.get('stop3')
    param_stops = str(stop1) + "|" + str(stop2) + "|" + str(stop3)
    places = [param_ori, param_dest, param_avoid, stop1, stop2, stop3]
    print(places)
    generate_info(places)
    return generate_info(places)


if __name__ == '__main__':
    app.run()
