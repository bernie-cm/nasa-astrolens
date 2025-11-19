import requests
from dotenv import load_dotenv
import os
from pprint import pprint
from pymongo import MongoClient

load_dotenv()  # reads variables from a .env file and sets them in os.environ
api_key = os.getenv("API_KEY")

'''The model should be
{
    'date': str,
    'explanation': str,
    'url': str The URL of the APOD image or video of the day.,
    'title': str The title of the image,
}'''


# date A string in YYYY-MM-DD format indicating the date of the APOD image (example: 2014-11-03). 
# Defaults to today's date. Must be after 1995-06-16, the first day an APOD picture was posted. 
# There are no images for tomorrow available through this API.

url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date=2025-06-27'
MONGO_URI = "mongodb://localhost:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.9"  # local instance
client = MongoClient(MONGO_URI)
db = client["nasa_apod"]
collection = db["apod_entries"]

response = requests.get(url)
data = response.json()

document = {
    'date': data.get('date'),
    'title': data.get('title'),
    'explanation': data.get('explanation'),
    'url': data.get('url')
}

result = collection.insert_one(document)
print(f'Finished inserting document with ID: {result.inserted_id}')