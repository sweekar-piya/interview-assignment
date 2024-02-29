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
        ## YOUR CODE HERE
        X = None
        y= None
        
        
        # Define the pipeline
        self.pipeline = Pipeline([
            None, # Standard scaling
            None  # Random Forest classifier
        ])
        
        # Fit the pipeline on the training data
        self.pipeline.fit(X, y)
        
        # Save the pipeline as a pickle file
        self.save_pipeline()

    def save_pipeline(self):
        # Save the pipeline as a pickle file
        ## YOUR CODE HERE
        pass

# Load the DataFrame saved earlier
df = pd.read_csv('wine_features.csv')

# Instantiate RandomForestPipeline
pipeline = RandomForestPipeline(features=['alcohol', 'flavanoids', 'total_phenols'], target='target')

# Call fit model on df
pipeline.fit_model(df)
