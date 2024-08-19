import requests

# API endpoints
BASEZIP_API = "https://www.zipcodeapi.com/rest/"
ZIP_APIKEY = "saeLYP6mua1UbZ0gVDSiX6M4nYLhUxoODxtsrGW1wpe1dGV6zary0ByHrtLX03Ub"  # Replace with your actual API key
FORECAST_API = "https://api.weather.gov/points/"

def fetch_weather(zip_code):
    try:
        # Fetch latitude and longitude using zipcodeapi.com
        endpoint = f"/info.json/{zip_code}/degrees"
        url = f"{BASEZIP_API}{ZIP_APIKEY}{endpoint}"
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        data = response.json()
        
        # Extract latitude and longitude
        latitude = data["lat"]
        longitude = data["lng"]
        city = data["city"]
        state = data["state"]
        print(f"Location: {city}, {state}")

        # Fetch forecast URL using weather.gov
        endpoint = f"{latitude},{longitude}"
        url = f"{FORECAST_API}{endpoint}"
        response = requests.get(url)
        response.raise_for_status()
        forecast_data = response.json()

        # Extract forecast URL
        forecast_url = forecast_data["properties"]["forecastHourly"]
        print(f"Forecast URL: {forecast_url}")

        # Fetch current temperature and image URL from forecast hourly endpoint
        response = requests.get(forecast_url)
        response.raise_for_status()
        hourly_forecast_data = response.json()
        
        # Extract current temperature and image URL
        first_period = hourly_forecast_data["properties"]["periods"][0]
        temperature = first_period["temperature"]
        image_url = first_period["icon"]
        print(f"Temperature: {temperature} F")
        print(f"Image URL: {image_url}")
        
        return temperature, image_url

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

# Example usage
zip_code = "90210"  # Replace with the zip code you want to fetch weather for
fetch_weather(zip_code)
"""
Weather API Fetcher
Description
This script fetches weather data using the Zipcode API and Weather.gov API. It takes a zip code as input, fetches the latitude and longitude using the Zipcode API, and then uses the Weather.gov API to fetch the current temperature and image URL.
How to Use
Replace the ZIP_APIKEY variable with your actual Zipcode API key.
Replace the zip_code variable with the zip code you want to fetch weather for.
Run the script to fetch the weather data.
Features
Fetches latitude and longitude using Zipcode API
Fetches forecast URL using Weather.gov API
Fetches current temperature and image URL from forecast hourly endpoint
Requirements
Python 3.x
requests library
Author
Dinesha Shair
License
This script is released under the MIT License. See LICENSE.txt for details.
Note
This script is for educational purposes only and should not be used for commercial purposes without permission from the API providers.
"""