import requests
import os

def GettingRandomJokes():
    apiKey = os.getenv('API_KEY')

    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

    headers = {
        "accept": "application/json",
        "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
        "X-RapidAPI-Key": apiKey
    }

    response = requests.request("GET", url, headers=headers)
    response = response.json()

    ranJoke = response['value']
    return ranJoke