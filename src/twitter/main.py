import requests
from datetime import date
import pandas as pd

BASE_URL = "https://api.twitter.com/2/tweets/" 
TOKEN = "AAAAAAAAAAAAAAAAAAAAAFB%2BcQEAAAAAt5tgj7ZfpgJdyat47yy0irA1w6I%3DqBG5Pn22bAYDdHYOgkGjfTBx434WOHmcA8KKSKxTtK3T7Mphor"

keywords_conf = [
    "electric cars",
    "renewable energy",
    "sustainable energy",
    "energy efficiency",
    "energy consumption",
    "urban planning",
    "environment",
    "urban",
    "save energy",
    "solar energy"
]

def make_url(url, keyword):
    if " " in keyword:
        keyword_no_space = keyword.replace(" ", "")
        url = url + "counts/recent?query=" + keyword + " OR " + keyword_no_space
    else:
        url = url + "counts/recent?query=" + keyword
    return url

def count_tweets(keywords):
    headers = {
        "Authorization": "Bearer " + TOKEN
    }   
    url = make_url(BASE_URL, keywords)
    result = requests.get(url, headers=headers)
    return result.json()["data"]

def export_csv(start_dates, end_dates, counts, keywords):
    df = pd.DataFrame(list(zip(start_dates, end_dates, counts, keywords)),
               columns =["start_date","end_date", "counts", "keywords"])
    date_today = date.today()
    date_today = date_today.strftime("%Y-%m-%d")
    df.to_csv("exports/twitter_{}.csv".format(date_today), sep=";")
    
start_dates = []
end_dates = []
counts = []
keywords = []

for keyword in keywords_conf:
    num_tweets = count_tweets(keyword)
    for tweet_record in num_tweets:
        start_dates.append(tweet_record["start"])
        end_dates.append(tweet_record["end"])
        counts.append(tweet_record["tweet_count"])
        keywords.append(keyword)

export_csv(start_dates, end_dates, counts, keywords)