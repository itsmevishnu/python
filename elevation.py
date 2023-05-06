#import necessary packages
import json
import requests
import pandas as pd

def find_elevation(lat, lng) ->str :
    """
    Findig the elevation from the lat long
    """
    url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lng}"
    print(url)
    value = {}
    try:
        response = requests.get(url, verify=False)
        value = json.loads(response.content.decode('utf-8'))
        print(value)
    except Exception as e:
        print(f"Some error occuered. Error is {e}")
        value['result'][0]["elevation"] = 0
    return value["results"][0]["elevation"]



def main():
    """
    Main function
    1. Read the input file from the folder
    2. Pass each row of panda dataframe to find_elevation function
    3. Create a new file containing elevated information
    """
    data = pd.read_csv("data_set/Lat_Long_Data.csv") # My input file is in data_set folder
    data["elevation"] = data.apply(lambda x : find_elevation(x["lat"], x["lng"]), axis=1)
    data.to_csv("data_set/modified_Lat_Long_Data.csv", index=False) # my outpul will be in data_set folder 

if __name__ == '__main__':
    main()