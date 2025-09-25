from typing import final

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

def getChoice() -> int:
    while True:
        try:
            choice = input("Enter your choice : ")
            intChoice = int(choice)

            if intChoice < 0 or intChoice > 10:
                raise TypeError("Enter a valid choice")
            break
        except TypeError as e:
            print(e)
            continue

    return intChoice

def print_menu() -> None:
    print('''Use the below Menu to make your choice :
    0. Exit
    1. See all the new movies 
    2. See the current most popular movie
    3. See highest rated movie
    4. See movie the highest number of votes
    5. See the movie with the closest release date to today
    6. See the Top 5 current best movies 
    7. See some outlier
    8. See the average ratings of all the movies
    9. Which moives have rating more than the average rating of all the movies
    10. See the total number of votes casted for all the movies
    ''')

def main() -> None:
    choice = 1
    while choice:
        print_menu()
        choice = getChoice()
        if choice == 0:
            print("Thanks for using our service !")
        elif choice == 1:
            df = fetch_data()
            print(df)
            continue
        else:
            print("")

    return None

main()
