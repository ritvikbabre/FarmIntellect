import pandas as pd
import numpy as np

class RecommendationGenerator:
    def __init__(self):
        # Could load additional reference data if needed
        pass
    
    def generate_recommendations(self, yield_prediction, soil_health, productivity_recommendations):
        """
        Generate holistic farm recommendations
        
        :param yield_prediction: Predicted crop yield
        :param soil_health: Soil health assessment
        :param productivity_recommendations: Productivity optimization suggestions
        :return: Comprehensive recommendations
        """
        recommendations = {
            'yield_improvement': self._generate_yield_recommendations(yield_prediction),
            'soil_health': self._generate_soil_recommendations(soil_health),
            'productivity': self._generate_productivity_recommendations(productivity_recommendations)
        }
        
        return recommendations
    
    def _generate_yield_recommendations(self, yield_data):
        """
        Generate yield-specific recommendations
        """
        recommendations = []
        
        if yield_data['predicted_yield'] < 3.0:  # Example threshold
            recommendations.extend([
                'Consider high-yield crop varieties',
                'Improve irrigation techniques',
                'Optimize fertilization strategy'
            ])
        
        recommendations.extend(yield_data['potential_improvement']['recommendations'])
        
        return recommendations
    
    def _generate_soil_recommendations(self, soil_health):
        """
        Generate soil health-specific recommendations
        """
        recommendations = []
        
        if soil_health['ph_level'] < 6.0 or soil_health['ph_level'] > 7.5:
            recommendations.append('Adjust soil pH through targeted amendments')
        
        if soil_health['organic_matter'] < 2.0:
            recommendations.append('Increase organic matter content')
        
        return recommendations
    
    def _generate_productivity_recommendations(self, productivity_data):
        """
        Generate productivity-specific recommendations
        """
        recommendations = []
        
        if productivity_data['efficiency_score'] < 0.6:
            recommendations.extend([
                'Implement precision farming techniques',
                'Invest in modern agricultural equipment',
                'Optimize crop scheduling'
            ])
        
        return recommendations