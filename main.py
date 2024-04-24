
# # import streamlit as st
# # import pickle
# # import pandas as pd
# # import requests
# # from streamlit_authenticator import Authenticate
# # from database import User, create_database, add_user, get_user

# # # Load the custom CSS file
# # with open('styles.css') as f:
# #     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# # # Create the SQLite database and tables
# # create_database()

# # # Create an authentication object
# # authenticator = Authenticate(
# #     User,
# #     "movie_recommender",
# #     "abcdef",
# #     cookie_expiry_days=1,
# #     allow_register=True,
# # )

# # # Check if the user is authenticated or wants to register
# # name, authentication_status, username = authenticator.login("Login", "main")

# # # If the user is not authenticated and wants to register
# # if authentication_status is None:
# #     try:
# #         # Get the user input for registration
# #         username = st.text_input("Username")
# #         password = st.text_input("Password", type="password")
# #         if st.button("Register"):
# #             # Add the user to the database
# #             add_user(username, password)
# #             st.success("Registration successful!")
# #     except Exception as e:
# #         st.error(f"Error: {e}")

# # # If the user is not authenticated, show the login page
# # elif not authentication_status:
# #     st.error("Please login or register to access the movie recommender system.")
# #     st.stop()

# # # If the user is authenticated or registers, show the app content
# # else:
# #     st.write(f"Welcome, {name}!")

# #     # Your existing code here
# #     # ...

# # def fetch_poster(movie_id):
# #     url = "https://api.themoviedb.org/3/movie/{}?api_key=5193a1b6768bfe00d7a6ec9caceda376&language=en-US".format(movie_id)
# #     data = requests.get(url)
# #     data = data.json()
# #     poster_path = data['poster_path']
# #     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
# #     return full_path

# # def recommend(movie):
# #     movie_index = movies[movies['title'] == movie].index[0]
# #     movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:7]
# #     recommended_movies = []
# #     recommended_movie_posters = []
# #     for i in movie_list:
# #         # fetch the movie poster
# #         movie_id = movies.iloc[i[0]].movie_id
# #         recommended_movie_posters.append(fetch_poster(movie_id))
# #         recommended_movies.append(movies.iloc[i[0]].title)
# #     return recommended_movies, recommended_movie_posters

# # movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# # similarity = pickle.load(open('similarity.pkl', 'rb'))
# # movies = pd.DataFrame(movies_dict)

# # st.title("Movie Recommender System")
# # selected_movie_name = st.selectbox('How would you like to contacted?', movies['title'].values)

# # if st.button('Show Recommendation'):
# #     recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
# #     col1, col2, col3 = st.columns(3)
# #     with col1:
# #         st.text(recommended_movie_names[0])
# #         st.image(recommended_movie_posters[0])
# #         st.text(recommended_movie_names[3])
# #         st.image(recommended_movie_posters[3])
# #     with col2:
# #         st.text(recommended_movie_names[1])
# #         st.image(recommended_movie_posters[1])
# #         st.text(recommended_movie_names[4])
# #         st.image(recommended_movie_posters[4])
# #     with col3:
# #         st.text(recommended_movie_names[2])
# #         st.image(recommended_movie_posters[2])
# #         st.text(recommended_movie_names[5])
# #         st.image(recommended_movie_posters[5])


# import streamlit as st
# import pickle
# import pandas as pd
# import requests

# # Load the custom CSS file
# with open('styles.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)




# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=5193a1b6768bfe00d7a6ec9caceda376&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path


# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:7]
#     recommended_movies=[]
#     recommended_movie_posters = []
#     for i in movie_list:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movies.append(movies.iloc[i[0]].title)
#     return recommended_movies,recommended_movie_posters

# movies_dict=pickle.load(open('movie_dict.pkl','rb'))
# similarity=pickle.load((open('similarity.pkl','rb')))
# movies=pd.DataFrame(movies_dict)

# st.title("Movie Recommender System")

# selected_movie_name=st.selectbox(
#     'How would you like to contacted?',
#     movies['title'].values
# )

# # if st.button('Recommend'):
# #     recommendations=recommend(selected_movie_name)
# #     for i in recommendations:
# #          st.write(i)
# if st.button('Show Recommendation'):
#     recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
#     col1, col2, col3= st.columns(3)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])

#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#         st.text(recommended_movie_names[5])
#         st.image(recommended_movie_posters[5])

import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_authenticator import Authenticate

# Load the custom CSS file
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Authentication credentials
credentials = {
    "usernames": {
        "YOUR_USERNAME": "YOUR_PASSWORD"
    }
}

# Create an authentication object
authenticator = Authenticate(credentials, "movie_recommender", "abcdef", cookie_expiry_days=1)

# Check if the user is authenticated
name, authentication_status, username = authenticator.login("Login", "main")

# If the user is not authenticated, show the login page
if not authentication_status:
    st.error("Please login to access the movie recommender system.")
    st.stop()

# If the user is authenticated, show the app content
st.write(f"Welcome, {name}!")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=5193a1b6768bfe00d7a6ec9caceda376&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:7]
    recommended_movies = []
    recommended_movie_posters = []
    for i in movie_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies, recommended_movie_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title("Movie Recommender System")
selected_movie_name = st.selectbox('How would you like to contacted?', movies['title'].values)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
