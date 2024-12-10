
import pandas as pd
import numpy as np
from ml_models.crop_yield_predictor import CropYieldPredictor
from ml_models.productivity_optimizer import ProductivityOptimizer
from ml_models.soil_health_analyzer import SoilHealthAnalyzer

def main():
    # Initialize models
    yield_predictor = CropYieldPredictor()
    optimizer = ProductivityOptimizer()
    analyzer = SoilHealthAnalyzer()

    # Define test input
    farm_data = {
        'Annual_Rainfall': 2051.4,
        'Fertilizer': 7024878.38,
        'Pesticide': 22882.34,
        'Area': 73814,
        'Rainfall_mm': 897.08,
        'Temperature_Celsius': 27.68,
        'Fertilizer_Used': 1,
        'Irrigation_Used': 1,
        'Days_to_Harvest': 122,
        'N': 138,
        'P': 8.6,
        'K': 560,
        'pH': 7.46,
        'EC': 0.62,
        'OC': 0.7,
        'S': 5.9,
        'Zn': 0.24,
        'Fe': 0.31,
        'Cu': 0.77,
        'Mn': 8.71,
        'B': 0.11
    }

    # Run predictions
    crop_yield_result = yield_predictor.predict(farm_data)
    productivity_result = optimizer.optimize(farm_data)
    soil_analysis_result = analyzer.assess_health(farm_data)

    # Display results
    print("Crop Yield Prediction:", crop_yield_result)
    print("Productivity Optimization:", productivity_result)
    print("Soil Health Analysis:", soil_analysis_result)

if __name__ == "__main__":
    main()
from ml_models.soil_health_analyzer import SoilHealthAnalyzer
from ml_models.productivity_optimizer import ProductivityOptimizer
from utils.recommendation_generator import RecommendationGenerator

class AgriculturalAIAssistant:
    def __init__(self):
        # Initialize machine learning models
        self.yield_predictor = CropYieldPredictor()
        self.soil_analyzer = SoilHealthAnalyzer()
        self.productivity_optimizer = ProductivityOptimizer()
        self.recommendation_generator = RecommendationGenerator()

    def analyze_farm_data(self, farm_data):
        """
        Comprehensive analysis of farm data
        
        :param farm_data: Dictionary containing farm details
        :return: Comprehensive farm analysis and recommendations
        """
        # Predict crop yield
        yield_prediction = self.yield_predictor.predict(farm_data)
        
        # Analyze soil health
        soil_health = self.soil_analyzer.assess_health(farm_data)
        
        # Optimize productivity
        productivity_recommendations = self.productivity_optimizer.optimize(farm_data)
        
        # Generate holistic recommendations
        final_recommendations = self.recommendation_generator.generate_recommendations(
            yield_prediction,
            soil_health,
            productivity_recommendations
        )
        
        return {
            'yield_prediction': yield_prediction,
            'soil_health': soil_health,
            'productivity_recommendations': productivity_recommendations,
            'final_recommendations': final_recommendations
        }

def main():
    # Example usage
    assistant = AgriculturalAIAssistant()
    
    sample_farm_data = {
    'Annual_Rainfall': 1500,
    'Fertilizer': 500000,
    'Pesticide': 1500,
    'Area': 25,
    'Rainfall_mm': 1000,
    'Temperature_Celsius': 25,
    'Fertilizer_Used': 1,
    'Irrigation_Used': 1,
    'Days_to_Harvest': 120
}

    
    # Perform analysis
    analysis_results = assistant.analyze_farm_data(sample_farm_data)
    
    # Print results
    print("Comprehensive Farm Analysis Report")
    print("-" * 40)
    for key, value in analysis_results.items():
        print(f"{key.replace('_', ' ').title()}:")
        print(value)
        print()

if __name__ == "__main__":
    main()