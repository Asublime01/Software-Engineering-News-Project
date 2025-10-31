import requests
from bs4 import BeautifulSoup
import csv
import os
from dotenv import load_dotenv
import json
import feedparser

load_dotenv()
nyt_apiKey = os.getenv("NYT_API_KEY")
thenews_apiKEY = os.getenv("thenews_apiKEY")

nyt_endpoint = f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={nyt_apiKey}'

guardian_url = 'https://www.theguardian.com/us/technology/rss' 
hacker_news = 'https://hnrss.org/frontpage'

guardian_feed = feedparser.parse(guardian_url)
responseNYT = requests.get(nyt_endpoint)
print(responseNYT)
hacker_feed = feedparser.parse(hacker_news)


responseNYT_parsed = responseNYT.json()



nyt_data = responseNYT_parsed["results"]

with open("News.txt", "w") as file:
    file.write("---------------------HACKER NEWS-----------------------------\n\n")
    for entry in hacker_feed.entries:
        file.write(f"Title: {entry.title}\nLink: {entry.link}\n\n")
    file.write("---------------------New York Times News-----------------------------\n\n")
    for result in nyt_data:
        file.write(f"Title: {result["title"]}\nDescription: {result["abstract"]}\nUrl: {result["url"]}\n\n")
    file.write("---------------------Guardian Tech News-----------------------------\n\n")    
    for entry in guardian_feed.entries:
        file.write(f"Title: {entry.title}\nLink: {entry.link}\n\n")




with open("response.json", "w") as file:
    json.dump(responseNYT_parsed, file, indent=2)



print("Finished.")







    




