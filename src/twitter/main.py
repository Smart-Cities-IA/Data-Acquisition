import requests
from datetime import date
import pandas as pd
from .conf import BASE_URL, TOKEN, keywords_conf
from .clean import clean_data

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

def export_csv(df):
    date_today = date.today()
    date_today = date_today.strftime("%Y-%m-%d")
    df.to_csv("clean-data/twitter_{}.csv".format(date_today), sep=";")
    
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

df = pd.DataFrame(list(zip(start_dates, end_dates, counts, keywords)),
               columns =["start_date","end_date", "counts", "keywords"])

clean_df = clean_data(df)

export_csv(clean_df)