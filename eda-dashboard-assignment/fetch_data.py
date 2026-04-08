import requests
import pandas as pd

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        raise Exception("Failed to fetch data")

def clean_data(df):
    # Rename column
    df = df.rename(columns={"userId": "user_id"})
    
    # Drop 'id' column
    df = df.drop(columns=["id"])
    
    # Create post_length column
    df["post_length"] = df["body"].apply(len)
    
    return df

def get_posts_per_user(df):
    return df.groupby("user_id").size().reset_index(name="post_count")