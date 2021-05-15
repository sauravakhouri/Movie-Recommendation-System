# Movie-Recommendation-System
A Basic Movie recommendation app for Hollywood movies till 2020.
Application Link: https://movie-recommendation-bysaurav.herokuapp.com/

This Movie Recommendation Sytem is a content based system where movies similar in terms of **Actors, Directors, Genre** is recommended to the users.

The application uses Cosine Similarity to rank the most similar movies and present it to the users.

The application returns Hollywood Movies up till the year 2020
This is an end to end Project right from Data Collection to Deployement.

Data Collection details:
  - Movies till 2016 are fetched from a Kaggle data set (Actor 1, Actor 2, Actor 3, Director, Genres)
  - Movies from 2017 are fetched from another Kaggle Data set which is merged with another dataset which has the details for Genres
  - Movies for 2018, 2019 and 2020 are seperately fetched through web scraping using BeautilSoup4 from Wikipedia page and the assosicated genres are pulled using API from TMDB         website

The final application is deployed on heroku platfrom and can be accessed on the Application link provided above.
