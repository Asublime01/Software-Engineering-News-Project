import requests
from bs4 import BeautifulSoup
import csv
import os
from dotenv import load_dotenv
import json

load_dotenv()
nyt_apiKey = os.getenv("NYT_API_KEY")

nyt_endpoint = f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={nyt_apiKey}'


responseNYT = requests.get(nyt_endpoint)
responseNYT_parsed = responseNYT.json()

with open("response.json", "w") as file:
    json.dump(responseNYT_parsed, file, indent=2)

print(responseNYT_parsed)

#soup = BeautifulSoup(html, 'html.parser')


