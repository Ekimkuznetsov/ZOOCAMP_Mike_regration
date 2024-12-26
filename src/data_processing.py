import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(filepath):
    """
    Preprocess the input CSV data file.
    
    Args:
    filepath (str): The path to the CSV file to be processed.
    
    Returns:
    pd.DataFrame: The processed DataFrame with additional features and normalized numeric values.
    """
    # Load data
    data = pd.read_csv(filepath)
    
    # Convert 'datetime' to datetime format
    data['datetime'] = pd.to_datetime(data['datetime'])
    
    # Extract features from datetime
    data['hour'] = data['datetime'].dt.hour
    data['day_of_week'] = data['datetime'].dt.dayofweek
    data['month'] = data['datetime'].dt.month
    
    # Drop unnecessary columns
    data = data.drop(['datetime', 'atemp'], axis=1)
    
    # Normalize data
    scaler = StandardScaler()
    numeric_features = ['temp', 'humidity', 'windspeed']
    data[numeric_features] = scaler.fit_transform(data[numeric_features])
    
    return data