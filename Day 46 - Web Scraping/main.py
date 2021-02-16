from bs4 import BeautifulSoup
import requests

URL = "https://www.timeout.com/newyork/movies/best-movies-of-all-time"
response = requests.get(URL)

# loading the website's content
website = response.text

# using BeautifulSoup to scrape the website
soup = BeautifulSoup(website, "html.parser")
website_headings = soup.find_all(name="h3", class_="card-title")

# list of the top 100 movies from the website
top_100_movies = [movie.getText() for movie in website_headings]
top_100_movies.pop(len(top_100_movies)-1)

# adding the top 100 movies to a new txt file
movies = ''
for movie in top_100_movies:
    movies += f"{movie.strip()}\n"

with open("top_100_movies.txt", "w") as file:
    file.write(movies)

