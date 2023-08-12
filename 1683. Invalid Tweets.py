# Write your MySQL query statement below
# select tweet_id from tweets where length(content) > 15

import pandas as pd
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    mask = tweets['content'].str.len() > 15
    return tweets[mask][['tweet_id']]