import json
import requests

import pandas as pd

data = pd.read_csv("data_set/lat_long.csv")

def find_elevation(lat, lng):
    """
    Findig the elevation from the lat long
    """
    url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lng}"
    try:
        response = requests.get(url, verify=False)
        data = json.loads(response.content.decode('utf-8'))
    except Exception as e:
        print(f"Some error occuered. Error is {e}")
    return data["results"][0]["elevation"]

data["elevation"] = data.apply(lambda x : find_elevation(x["lat"], x["lng"]), axis=1)

data.to_csv('data_set/modified_lat_long.csv', index=False)
