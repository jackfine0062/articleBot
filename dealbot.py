import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")
bearer_token = os.getenv(r"bearer_token")
access_token = os.getenv("access_token")