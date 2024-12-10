import pandas as pd

class DataPreprocessor:
    def __init__(self):
        pass

    def preprocess_crop_data(self, file_path):
        data = pd.read_csv(file_path)
        # Select and preprocess necessary columns
        data['Fertilizer'] = data['Fertilizer'].astype(float)
        data['Pesticide'] = data['Pesticide'].astype(float)
        return data

    def preprocess_productivity_data(self, file_path):
        data = pd.read_csv(file_path)
        # Convert TRUE/FALSE to 1/0
        data['Fertilizer_Used'] = data['Fertilizer_Used'].apply(lambda x: 1 if x == 'TRUE' else 0)
        data['Irrigation_Used'] = data['Irrigation_Used'].apply(lambda x: 1 if x == 'TRUE' else 0)
        return data

    def preprocess_soil_data(self, file_path):
        data = pd.read_csv(file_path)
        return data
