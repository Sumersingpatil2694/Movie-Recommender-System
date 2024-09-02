import streamlit as st
import pickle
import pandas as pd
import requests
from requests.exceptions import ConnectTimeout
from time import sleep


def fetch_poster(movie_id, retries=3, delay=2):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)  # Add timeout here to avoid hanging forever
            if response.status_code == 200:
                data = response.json()
                return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
            else:
                st.error(f"Failed to fetch poster: {response.status_code}")
                return None
        except ConnectTimeout:
            st.warning("Connection timed out. Retrying...")
            sleep(delay)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return None

    st.error("Failed to fetch poster after multiple attempts.")
    return None


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # Update this line with the correct column name

        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


# Load the movie data and similarity model
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# For debugging: check the column names in the DataFrame
print(movies.columns)

st.title('Chetan Sumersing Lokesh')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
