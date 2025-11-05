import requests
from bs4 import BeautifulSoup
import csv
import os
from dotenv import load_dotenv
import json
import feedparser
import random

load_dotenv()
nyt_apiKey = os.getenv("NYT_API_KEY")
thenews_apiKEY = os.getenv("thenews_apiKEY")
headers = {"User-Agent": "Mozilla/5.0"}

nyt_endpoint = f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={nyt_apiKey}'

guardian_url = 'https://www.theguardian.com/technology/rss' 
hacker_news = 'https://hnrss.org/frontpage'

guardian_response = requests.get(guardian_url, headers=headers)
guardian_feed = feedparser.parse(guardian_response.text)
responseNYT = requests.get(nyt_endpoint)
print(responseNYT)
hacker_response = requests.get(hacker_news, headers=headers)
hacker_feed = feedparser.parse(hacker_response.text)







responseNYT_parsed = responseNYT.json()



nyt_data = responseNYT_parsed["results"]

with open("News.txt", "w") as file:
    for entry in hacker_feed.entries:
        file.write(f"[{entry.title}, {entry.link}]\n")
    
    for result in nyt_data:
        file.write(f"[{result['title']}, {result['abstract']}, {result['url']}\n")
       
    for entry in guardian_feed.entries:
        file.write(f"[{entry.title}, {entry.link}]\n")





def send_newsletter():
    with open("News.txt", "r") as file:
        lines = file.readlines()
        lines_chosen = []
        gathered_data = []
        while len(lines_chosen) < 5:
            chosen_line  = random.choice(lines)
            line_number = lines.index(chosen_line) + 1
            if line_number in lines_chosen:
                continue #Find a new line that hasn't been picked
            else:
                lines_chosen.append(line_number) #Add that new line to the lines picked list
                gathered_data.append(chosen_line)
        
        

        

def get_random_news():
    pass


send_newsletter()










    




