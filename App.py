import streamlit as st
import pickle
import requests
from dotenv import load_dotenv
import os

# Function to fetch the url of the provided movie's poster
def fetch_movie_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}&language=en-US'
    response = requests.get(url)  ## GET request to fetch information --> Returns a Response object
    data = response.json()  ## Dict to store the JSON content of the response
    poster_path = data['poster_path']
    image_url = 'https://image.tmdb.org/t/p/w500/' + poster_path  ## URL of the image/poster
    return image_url

# Function to recommend the top 5 movies similar to the provided movie
def recommend_movies(movie_name):
    ind = movies_df[movies_df['title'] == movie_name].index[0]  ## Get the index of the current movie
    similarity = similarities[ind]  ## Get the cosine similarity of the current movie with the other movies
    similarity_desc = sorted(
        list(enumerate(similarity)), reverse=True, key=lambda x: x[1]
    )  ## Since sorting changes the order, we need to maintain a copy of the original indices --> Thus, using enumerate --> (original index, cosine value)
    top5 = similarity_desc[1 : 6]  ## Fetching the 5 highest similarities
    top5_movies = []  ## List to store the names and poster paths of those movies
    for i, _ in top5:
        movie = movies_df.iloc[i]  ## Fetch the entire row from the dataframe
        top5_movies.append((movie['title'], fetch_movie_poster(movie['movie_id'])))
    return top5_movies

st.title('Movie Recommender System :movie_camera:')

# Loading the pickle files
with (open('pickle_files/movies_df.pkl', 'rb') as f1,
      open('pickle_files/cosine_similarities.pkl', 'rb') as f2):
    movies_df = pickle.load(f1)
    similarities = pickle.load(f2)

# Loading .env variables into the environment
load_dotenv()
tmdb_api_key = os.getenv('TMDB_API_KEY')  ## Accessing the tmdb api key

movie_names = movies_df['title']
selected_movie = st.selectbox(
    'Select a movie from the dropdown', movie_names
)

if st.button('Recommend'):
    # Invoking the recommend_movies function to get the 5 most similar movies
    recommendations = recommend_movies(selected_movie)
    st.header('5 Similar Movies:')
    cols = iter(st.columns(5))
    for name, poster in recommendations:
        col = next(cols)
        col.image(poster, caption=name)