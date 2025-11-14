import requests
import csv
import os
from dotenv import load_dotenv
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

hacker_response = requests.get(hacker_news, headers=headers)
hacker_feed = feedparser.parse(hacker_response.text)







responseNYT_parsed = responseNYT.json()



nyt_data = responseNYT_parsed["results"]

with open("News.txt", "w") as file:
    for entry in hacker_feed.entries:
        file.write(f"{entry.title}; {entry.link}")
        file.write("\n")
    
    for result in nyt_data:
        file.write(f"{result['title']}; {result['abstract']}; {result['url']}")
        file.write("\n")
       
    for entry in guardian_feed.entries:
        file.write(f"{entry.title}; {entry.link}")
        file.write("\n")





def get_newsletter_data():
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
                gathered_data.append(chosen_line.strip())
                
        return gathered_data
        

        

def get_random_news():
    with open("News.txt", "r") as file:
        lines = file.readlines()
        chosen_line = random.choice(lines)
        return chosen_line

def get_epic_news():
    os.system("wget ")
    with open('news.csv', 'r+') as csvfile:
            
        reader = csv.reader(csvfile)

    # Iterate over each row in the CSV file
        for row in reader:
            print(row) # Each row is a list of strings

get_epic_news()













    




