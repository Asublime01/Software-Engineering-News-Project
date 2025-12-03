import requests
import csv
import os
from dotenv import load_dotenv
import feedparser
import random
import datetime
import time


dateString = datetime.date.today()
year, month, day = dateString.__str__().split("-")
todays_date = [month, day, year]

def Refresh_News():
    load_dotenv()
    nyt_apiKey = os.getenv("NYT_API_KEY")

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
        if chosen_line.count(";") == 2:
            title, des, url = chosen_line.strip().split(";")
            return f"{title}: {des}"
        elif chosen_line.count(";") == 1:
            title, url = chosen_line.strip().split(";")
            return title
        

def get_epic_news():
    data_list = []
    os.system("wget https://raw.githubusercontent.com/EPIC-Campus-LPS/EPIC-News/refs/heads/main/news.csv")
    with open('news.csv', 'r+') as csvfile:
            
        reader = csv.reader(csvfile)
        next(reader)
        
        
    # Iterate over each row in the CSV file
        for row in reader:
            month, day, year = row[2].split("/")
            if int(month) < int(todays_date[0]) or int(day) < int(todays_date[1]) or int(year) < int(todays_date[2]):
                continue # Get a new row 
            else:
                data_list.append(f"{row[0]} | {row[1]}")
            
    time.sleep(1)
    os.system("rm news.csv")
    if len(data_list) == 0:
        return 2
    else:
        return ''.join([str(item) for item in data_list])























    




