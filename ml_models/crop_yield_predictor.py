import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class CropYieldPredictor:
    def __init__(self):
        # Load and preprocess data
        self.training_data = pd.read_csv('data/sample_crop_data.csv')
        self._prepare_model()
    
    def _prepare_model(self):
        # Define features and target
        features = ['Annual_Rainfall', 'Fertilizer', 'Pesticide', 'Area']
        target = 'Yield'

        # Split data
        X = self.training_data[features]
        y = self.training_data[target]
        
        # Scale features
        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)
        
        # Train the model
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_scaled, y)

    def predict(self, farm_data):
        # Prepare input data
        input_df = pd.DataFrame([farm_data])
        features = ['Annual_Rainfall', 'Fertilizer', 'Pesticide', 'Area']
        X_input = input_df[features]
        X_scaled = self.scaler.transform(X_input)

        # Make prediction
        yield_prediction = self.model.predict(X_scaled)[0]
        return {
            'predicted_yield': round(yield_prediction, 2)
        }
