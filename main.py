import requests
import os
from dotenv import load_dotenv
from pathlib import Path

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

for movie in movies:
    print(movie)
