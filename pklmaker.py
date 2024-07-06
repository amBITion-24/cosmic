import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pickle

def create_citymate_model(data_file='data/citymate_data.csv', model_file='data/citymate_model.pkl'):
    """
    Loads CityMate data, trains a KNN model, and saves the model to a pickle file.

    Args:
        data_file (str): Path to the CSV file containing CityMate data.
        model_file (str): Path to save the trained model.
    """
    try:
        df = pd.read_csv(data_file)
        
        if df.empty:
            raise ValueError("The CSV file is empty. Please provide a valid data file.")

        # 1. Preprocess Data
        df['languages_spoken'] = df['languages_spoken'].str.lower().str.strip().str.split(',')
        df['about'] = df['about'].str.lower().str.strip()
        df['combined_features'] = df['languages_spoken'].astype(str) + ' ' + df['about']

        # 2. Train the KNN Model 
        tfidf = TfidfVectorizer()
        tfidf_matrix = tfidf.fit_transform(df['combined_features'])

        # Experiment with different K values for NearestNeighbors
        knn_models = [NearestNeighbors(n_neighbors=k, metric='cosine') for k in range(3, 7)]  

        # 3. Evaluation - Use cross-validation to find the best K
        # (You'll need to implement a cross-validation loop here)
        # For this example, we'll assume K=4 is the best
        best_knn = knn_models[1]  # K=4

        best_knn.fit(tfidf_matrix)

        # 4. Save the Model
        with open(model_file, 'wb') as f:
            pickle.dump((tfidf, best_knn), f)  # Save TF-IDF and KNN

        print(f"CityMate model created and saved to '{model_file}'")
    
    except FileNotFoundError:
        print(f"File not found: {data_file}. Please check the file path.")
    
    except pd.errors.EmptyDataError:
        print("No columns to parse from file. The file might be empty.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    create_citymate_model()