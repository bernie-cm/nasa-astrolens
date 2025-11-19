import requests
from dotenv import load_dotenv
import os
from pprint import pprint
import pymongo

load_dotenv()  # reads variables from a .env file and sets them in os.environ
api_key = os.getenv("API_KEY")

# date A string in YYYY-MM-DD format indicating the date of the APOD image (example: 2014-11-03). 
# Defaults to today's date. Must be after 1995-06-16, the first day an APOD picture was posted. 
# There are no images for tomorrow available through this API.
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date=2025-10-10'

response = requests.get(url)
pprint(response.json())

'''The model should be
{
    'date': str,
    'explanation': str,
    'url': str The URL of the APOD image or video of the day.,
    'title': str The title of the image,
}'''
