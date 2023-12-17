

import praw
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
reddit_user_agent = os.getenv("REDDIT_USER_AGENT")


def get_top_products(subreddit, time_filter='month', limit=10):
    # Initialize PRAW with your Reddit app credentials
    reddit = praw.Reddit(client_id=reddit_client_id,
                         client_secret=reddit_client_secret,
                         user_agent=reddit_user_agent)

    # Fetch subreddit data
    subreddit = reddit.subreddit(subreddit)

    # Set time filter
    if time_filter == 'month':
        time_range = 'month'
    elif time_filter == 'year':
        time_range = 'year'
    else:
        time_range = 'all'

    # Get top submissions
    top_submissions = subreddit.top(time_range, limit=limit)

    # Extract product information
    products = [submission.title for submission in top_submissions]

    return products

if __name__ == "__main__":
    subreddit_name = 'xxfitness'  # Change this to the desired subreddit
    top_products = get_top_products(subreddit_name)
    print(top_products)
