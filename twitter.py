import tweepy
from dotenv import load_dotenv
import os
import pyshorteners
from dateutil import parser
from datetime import datetime, timedelta
import pytz
import random
import time

shortener = pyshorteners.Shortener()

def get_client():
    
    load_dotenv()

    client = tweepy.Client(
    consumer_key = os.getenv("API_KEY"),
    consumer_secret = os.getenv("API_SECRET"),
    access_token = os.getenv("ACCESS_TOKEN"),
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    )
    
    return client


def create_tweet(client, article, state):
    title = article.title
    link = shortener.tinyurl.short(article.link)
    author = article.author
    max_attempts = 3
    
    if not is_within_last_hour(article.published):
        print(f"Article was not within the last hours! Skipping")
        return
    
    if state.is_posted(link):
        print(f"Link is already posted!: {link}")
        return
    

    for attempt in range(max_attempts):
        print(f"Attempting to post tweet: {title}")
        tweet_text = f"Title: {title}\nAuthor: {author}\n\n{link}"
        try:
            client.create_tweet(text=tweet_text)
            state.add_link(link)
            print(f"Successfully posted tweet")
            delay = random.randInt(30,120)
            print(f"Waiting for {delay} seconds before next action")
            time.sleep(delay)
            return
        except tweepy.TweepyException as e:
            print(f"Error posting tweet (Attempt {attempt + 1} / {max_attempts}): {e}")
            if attempt< max_attempts-1:
                sleep = 4 * (2**attempt)
                print(f"Retrying in {sleep} seconds")
                time.sleep(sleep)


        

def is_within_last_hour(date_string):
    
    # parse string, and return string as a datetime object
    parsed_date = parser.parse(date_string)
    
    # convert timezone to utc to have standard timezone to work with
    if parsed_date.tzinfo is None:
        parsed_date.replace(tzinfo=pytz.UTC)
    
    # subtract time
    current_time = datetime.now(pytz.UTC)
    
    difference = current_time - parsed_date
    return difference < timedelta(hours = 1)
    