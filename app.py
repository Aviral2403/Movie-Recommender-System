import pickle
import streamlit as st
import requests
from streamlit_lottie import st_lottie
#import json


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=54df90b6c96849d75d5dee63af8b62db&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        # Use the TMDB API to search for the movie
        api_key = "54df90b6c96849d75d5dee63af8b62db"  # Replace with your actual TMDB API key
        url = f"https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": api_key,
            "query": recommended_movie_names[0]
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            if data['results']:
                # Get the first result
                movie_id = data['results'][0]['id']
                # Generate the link
                movie_link = f"https://www.themoviedb.org/movie/{movie_id}"
                st.success(f"Here is the link for {recommended_movie_names[0]}: {movie_link}")
            else:
                st.error(f"No results found for {recommended_movie_names[0]}")
        else:
            st.error("Error fetching data from TMDB. Please try again later.")


    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

        api_key = "54df90b6c96849d75d5dee63af8b62db"  # Replace with your actual TMDB API key
        url = f"https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": api_key,
            "query": recommended_movie_names[1]
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            if data['results']:
                # Get the first result
                movie_id = data['results'][0]['id']
                # Generate the link
                movie_link = f"https://www.themoviedb.org/movie/{movie_id}"
                st.success(f"Here is the link for {recommended_movie_names[1]}: {movie_link}")
            else:
                st.error(f"No results found for {recommended_movie_names[1]}")
        else:
            st.error("Error fetching data from TMDB. Please try again later.")

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])

        api_key = "54df90b6c96849d75d5dee63af8b62db"  # Replace with your actual TMDB API key
        url = f"https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": api_key,
            "query": recommended_movie_names[2]
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            if data['results']:
                # Get the first result
                movie_id = data['results'][0]['id']
                # Generate the link
                movie_link = f"https://www.themoviedb.org/movie/{movie_id}"
                st.success(f"Here is the link for {recommended_movie_names[2]}: {movie_link}")
            else:
                st.error(f"No results found for {recommended_movie_names[2]}")
        else:
            st.error("Error fetching data from TMDB. Please try again later.")

    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])

        api_key = "54df90b6c96849d75d5dee63af8b62db"  # Replace with your actual TMDB API key
        url = f"https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": api_key,
            "query": recommended_movie_names[3]
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            if data['results']:
                # Get the first result
                movie_id = data['results'][0]['id']
                # Generate the link
                movie_link = f"https://www.themoviedb.org/movie/{movie_id}"
                st.success(f"Here is the link for {recommended_movie_names[3]}: {movie_link}")
            else:
                st.error(f"No results found for {recommended_movie_names[3]}")
        else:
            st.error("Error fetching data from TMDB. Please try again later.")

    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

        api_key = "54df90b6c96849d75d5dee63af8b62db"  # Replace with your actual TMDB API key
        url = f"https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": api_key,
            "query": recommended_movie_names[4]
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            if data['results']:
                # Get the first result
                movie_id = data['results'][0]['id']
                # Generate the link
                movie_link = f"https://www.themoviedb.org/movie/{movie_id}"
                st.success(f"Here is the link for {recommended_movie_names[4]}: {movie_link}")
            else:
                st.error(f"No results found for {recommended_movie_names[4]}")
        else:
            st.error("Error fetching data from TMDB. Please try again later.")

#from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/90d54638-2399-4935-ae9d-84f443fef545/wfxGpmjS4Z.json"
lottie_hello = load_lottieurl(lottie_url_hello)
def st_lottie_with_size(lottie, width, height, key=None):
    st_lottie(lottie, key=key, width=width, height=height)

st_lottie_with_size(lottie_hello, width=300, height=300, key="hi")




