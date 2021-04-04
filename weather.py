# importing requests and json
import requests, json

# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "New Paltz"
API_KEY = "9c7444b50ea8a026853543c77343e584"
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)


# checking the status code of the request
def get_weather_for_today():
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        return report[0]["description"]

    else:
        # showing the error message
        return "Error in the HTTP request"
