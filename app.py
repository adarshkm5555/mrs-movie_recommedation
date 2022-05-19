import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_posters(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{'
                            '}?api_key=2c3a4347986d9da9c8789480029825a3&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    recommended_movies_poster = []

    for j in movie_list:
        movie_id = movies.iloc[j[0]].movie_id
        recommended_movies.append(movies.iloc[j[0]].title)
        recommended_movies_poster.append(fetch_posters(movie_id))
    return recommended_movies, recommended_movies_poster


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select movies below',
    movies['title'].values)

if st.button('Recommend'):
    recommendations, poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendations[0])
        st.image(poster[0])

    with col2:
        st.text(recommendations[1])
        st.image(poster[1])

    with col3:
        st.text(recommendations[2])
        st.image(poster[2])

    with col4:
        st.text(recommendations[3])
        st.image(poster[3])

    with col5:
        st.text(recommendations[4])
        st.image(poster[4])
