import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class ProductivityOptimizer:
    def __init__(self):
        # Load and preprocess data
        self.training_data = pd.read_csv('data/farm_productivity_data.csv')
        self._prepare_model()

    def _prepare_model(self):
        # Define features and target
        features = ['Rainfall_mm', 'Temperature_Celsius', 'Fertilizer_Used', 'Irrigation_Used', 'Days_to_Harvest']
        target = 'Yield_tons_per_hectare'

        # Split data
        X = self.training_data[features]
        y = self.training_data[target]
        
        # Scale features
        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)

        # Train the model
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_scaled, y)

    def optimize(self, farm_data):
        # Prepare input data
        input_df = pd.DataFrame([farm_data])
        features = ['Rainfall_mm', 'Temperature_Celsius', 'Fertilizer_Used', 'Irrigation_Used', 'Days_to_Harvest']
        X_input = input_df[features]
        X_scaled = self.scaler.transform(X_input)

        # Make prediction
        recommendation = self.model.predict(X_scaled)[0]
        return {
            'optimized_yield': round(recommendation, 2)
        }
