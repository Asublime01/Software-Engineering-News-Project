import requests
from bs4 import BeautifulSoup
import csv
import os
from dotenv import load_dotenv
import json

load_dotenv()
nyt_apiKey = os.getenv("NYT_API_KEY")

nyt_endpoint = f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={nyt_apiKey}'


#responseNYT = requests.get(nyt_endpoint)
responseCNN = requests.get("https://www.cnn.com/business/tech")

#responseNYT_parsed = responseNYT.json()
CNN_html = responseCNN.content



#with open("response.json", "w") as file:
#    json.dump(responseNYT_parsed, file, indent=2)

#print(responseNYT_parsed)

soup = BeautifulSoup(CNN_html, 'html.parser')

outerdivs = soup.find_all('div',{'class': 'zone zone--t-light', "data-collapsed-text": ""})

for div in outerdivs:
    soup = div
    spans = soup.find_all("span", {"class": "container__headline container_vertical-strip__headline"})
    print(spans)




