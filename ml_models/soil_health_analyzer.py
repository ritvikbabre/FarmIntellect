import numpy as np

class SoilHealthAnalyzer:
    def __init__(self):
        pass

    def assess_health(self, farm_data):
        """
        Assess the health of the soil based on farm data.

        :param farm_data: Dictionary containing soil and farm details
        :return: Dictionary with soil health metrics and recommendations
        """
        soil_ph = farm_data.get('soil_ph', None)
        organic_matter = farm_data.get('organic_matter', 2.5)  # Example default value
        nutrient_levels = farm_data.get('nutrient_levels', {'N': 50, 'P': 40, 'K': 60})  # Example default levels
        
        ph_status = self._evaluate_ph(soil_ph)
        organic_matter_status = self._evaluate_organic_matter(organic_matter)
        nutrient_status = self._evaluate_nutrient_levels(nutrient_levels)
        
        return {
            'ph_level': soil_ph,
            'ph_status': ph_status,
            'organic_matter': organic_matter,
            'organic_matter_status': organic_matter_status,
            'nutrient_status': nutrient_status,
        }

    def _evaluate_ph(self, ph):
        """
        Evaluate soil pH level and determine its status.

        :param ph: Soil pH value
        :return: Status of soil pH
        """
        if ph is None:
            return "Unknown"
        elif 6.0 <= ph <= 7.5:
            return "Optimal"
        elif ph < 6.0:
            return "Too acidic"
        else:
            return "Too alkaline"

    def _evaluate_organic_matter(self, organic_matter):
        """
        Evaluate organic matter content in the soil.

        :param organic_matter: Organic matter percentage
        :return: Status of organic matter
        """
        if organic_matter < 2.0:
            return "Low"
        elif 2.0 <= organic_matter <= 4.0:
            return "Optimal"
        else:
            return "High"

    def _evaluate_nutrient_levels(self, nutrients):
        """
        Evaluate the levels of key nutrients in the soil.

        :param nutrients: Dictionary with 'N', 'P', 'K' levels
        :return: Status of each nutrient
        """
        status = {}
        for nutrient, level in nutrients.items():
            if level < 40:
                status[nutrient] = "Low"
            elif 40 <= level <= 80:
                status[nutrient] = "Optimal"
            else:
                status[nutrient] = "High"
        return status
