import pandas as pd
from sklearn.preprocessing import StandardScaler

def process_datetime(data):
    """Convert datetime and extract useful features."""
    data['datetime'] = pd.to_datetime(data['datetime'])
    data['hour'] = data['datetime'].dt.hour
    data['day'] = data['datetime'].dt.day
    data['month'] = data['datetime'].dt.month
    data['year'] = data['datetime'].dt.year
    data['weekday'] = data['datetime'].dt.weekday
    data['is_weekend'] = data['weekday'].apply(lambda x: 1 if x >= 5 else 0)  # 1 for Saturday/Sunday
    return data


def encode_categorical(data):
    """Convert specific columns to categorical types."""
    categorical_cols = ['season', 'weather', 'workingday']
    for col in categorical_cols:
        data[col] = data[col].astype('category')
    return data

def scale_features(data, feature_columns):
    """Scale numerical features."""
    scaler = StandardScaler()
    data[feature_columns] = scaler.fit_transform(data[feature_columns])
    return data

def preprocess_data(data):
    """Full preprocessing pipeline."""
    data = process_datetime(data)
    data = encode_categorical(data)
    numeric_features = ['temp', 'atemp', 'humidity', 'windspeed']
    data = scale_features(data, numeric_features)
    return data
