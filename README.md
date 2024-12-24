# Movie Recommender System
This is a Python-based movie recommender system that recommends 5 movies most similar to a selected movie. The system is built using the TMDB 5000 dataset from Kaggle and employs various natural language processing (NLP) techniques to generate movie recommendations.

## Dataset
Here's a link to the dataset: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

## Data Preprocessing and Feature Engineering
To create the tags used for recommendation, the following columns were utilized:
- **Overview**
- **Genre**
- **Keywords**
- **Top 3 Cast Members**
- **Director (Crew)**
These features were combined and preprocessed using **PorterStemmer** for stemming and **CountVectorizer** (BoW technique) for word vectorization.

## Recommendation Algorithm
The system uses **Cosine Similarity** to calculate the similarity between the selected movie and others in the dataset. The top 5 most similar movies are recommended to the user based on the cosine similarity scores.

## Frontend
The frontend of the system is built using **Streamlit**, which allows users to interact with the movie recommender system in an easy-to-use interface.
