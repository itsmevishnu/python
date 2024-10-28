from flask import Flask
from flask import request
import requests

import requests


API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en"

app = Flask("app")

# util functions
def return_response(message, data = {}):
    return {
        "message": message,
        "data": data
    }

@app.route("/")
def home():
    return return_response(message="Welcome to free Dictionary")


@app.route("/search", methods=["POST", "GET"])
def search_words():
    if request.method != 'POST':
        return return_response(message="The method is not implemented")
    
    request_body = request.get_json()
    
    if "word" in request_body:
        word = request_body.get("word")
        request_url = f"{API_URL}/{word}"
        response_from = requests.get(request_url)
       
        if response_from.status_code == 200:
            response_content = response_from.json()
            data = {"word": word,
                    "meanings": response_content[0].get("meanings") }
            return return_response(message="Meaning found", data=data)
        else:
            return return_response(message="Unknown error has occured")
    else:
         return return_response(message="No words found")
