import pickle
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd

class RandomForestPipeline:
    def __init__(self, features, target):
        self.features = features
        self.target = target
        self.pipeline = None

    def fit_model(self, df):
        # Create feature matrix X and target vector y
        X = df[self.features]
        y = df[self.target]
        
        # Split the data into train and test sets
        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Define the pipeline
        self.pipeline = Pipeline([
            ('scaler', StandardScaler()),  # Standard scaling
            ('rf', RandomForestClassifier(random_state=42))  # Random Forest classifier
        ])
        
        # Fit the pipeline on the training data
        self.pipeline.fit(X_train, y_train)
        
        # Save the pipeline as a pickle file
        self.save_pipeline()

    def save_pipeline(self):
        # Save the pipeline as a pickle file
        with open('pipeline.pkl', 'wb') as file:
            pickle.dump(self.pipeline, file)

# Load the DataFrame saved earlier
df = pd.read_csv('wine_features.csv')

# Usage example:
pipeline = RandomForestPipeline(features=['alcohol', 'flavanoids', 'total_phenols'], target='target')
pipeline.fit_model(df)
