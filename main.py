import requests
import os
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def fetch_data() -> pd.DataFrame:
    dotenv_path = Path('/Users/siddharthshrivastav/IdeaProjects/dataEngineer/secrets.env')
    load_dotenv(dotenv_path=dotenv_path)

    url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv("API_READ_ACCESS_KEY")}"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    movies = data['results']

    data = []

    for movie in movies:
        row = [movie['title'],movie['popularity'],movie['release_date'],movie['vote_average'],movie['vote_count']]
        data.append(row)

    movie_df = pd.DataFrame(data, columns = ["title","popularity","release_date","vote_average","vote_count"])
    return movie_df

df = fetch_data()
print(df)
