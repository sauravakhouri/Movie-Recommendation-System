import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import joblib

from flask import Flask, request, render_template

import json
import bs4
import urllib.request
import requests




app=Flask(__name__)


# Loading the model and tfidf vectorizer ffrom the disk

vector= joblib.load('NLP_vector.pkl')
model=joblib.load('NLP_model.pkl')

def create_similarity():
    data=pd.read_csv('main_data.csv')
    
    #creating a count matrix
    cv=CountVectorizer()
    count_matrix=cv.fit_transform(data['comb'])
    
    # creating similarity score matrix
    similarity=cosine_similarity(count_matrix)
    return data,similarity

data,similarity=create_similarity()


#functions to get movie title from movie index and vice versa

def get_titlefromindex(movieindex):
    return data[data.index==movieindex]['movie_title'].values[0]

def get_indexfromtitle(title):
    return data[data.movie_title==title].index.values[0]



# function to take a movie and return the recommendations

def recommendation(movie_user_likes):
    movie_user_likes=movie_user_likes.lower()
    data,similarity=create_similarity()
 
    if movie_user_likes not in data['movie_title'].unique():
        # return (movie_user_likes)

        return ('Sorry !! The movie you requested is not in our database. Please check the spelling or try with some other movies' )
    else:
        movie_index=get_indexfromtitle(movie_user_likes)
        similar_movies=list(enumerate(similarity[movie_index]))
        sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:] 
        # [1:] to remove first movie from the sorted list as it's the searched movie itself
        
        #list of recommended movies
        recommended_movies = []
        for mov in (sorted_similar_movies[0:10]):
            recommended_movies.append(get_titlefromindex(mov[0]))
        return recommended_movies



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend',methods=['POST'])
def recommend():
    movie_user_likes=request.form['Movie']
    recommendedmovies=recommendation(movie_user_likes)

    return render_template('index.html',recommend_text=recommendedmovies)

if __name__== "__main__":
    app.run(debug=True)
