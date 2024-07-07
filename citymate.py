from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import pickle


class CityMateRecommender:

    def __init__(self):
        self.model = None
        self.tfidf = TfidfVectorizer()
        self.citymate_df = None
        self.is_model_trained = False  # Track if model is trained

    def preprocess_data(self, citymate_df):
        self.citymate_df = citymate_df
        self.citymate_df['combined'] = self.citymate_df.apply(
            lambda row: ' '.join(row['languages_spoken'].split(',')
                                 ) + ' ' + row['about'],
            axis=1)

    def train_model(self):
        if self.citymate_df is None:
            raise ValueError(
                "Data is not loaded. Please call preprocess_data first.")

        tfidf_matrix = self.tfidf.fit_transform(self.citymate_df['combined'])
        self.model = NearestNeighbors(n_neighbors=4,
                                      metric='cosine').fit(tfidf_matrix)
        self.is_model_trained = True  # Mark model as trained

    def get_recommendations(self, user_languages, user_age_group):
        if not self.is_model_trained:
            raise ValueError(
                "Model is not trained. Please train the model first.")

        user_input = ' '.join(user_languages) + ' ' + user_age_group
        user_vector = self.tfidf.transform([user_input])
        distances, indices = self.model.kneighbors(user_vector)
        recommendations = self.citymate_df.iloc[indices[0]]
        recommendations['similarity_score'] = 1 - distances[0]
        return recommendations


def save_model(recommender, filepath):
    with open(filepath, 'wb') as f:
        pickle.dump(recommender.model, f)


def load_model(filepath):
    with open(filepath, 'rb') as f:
        model = pickle.load(f)
        recommender = CityMateRecommender()
        recommender.model = model
        recommender.tfidf = TfidfVectorizer(
        )  # Initialize a new TfidfVectorizer
        recommender.is_model_trained = True  # Assume loaded model is already trained
        return recommender
