import click
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import mlflow
import mlflow.sklearn
import joblib
from mlflow.models.signature import infer_signature

def train_random_forest_with_mlflow(train_path):
    """Train and log a Random Forest model with MLflow."""
    # Enable MLflow autolog
    mlflow.sklearn.autolog()
    
    with mlflow.start_run():
        # Load and preprocess training data
        train_data = pd.read_csv(train_path)
        # Example of feature engineering
        train_data['hour'] = pd.to_datetime(train_data['datetime']).dt.hour
        train_data['is_weekend'] = (pd.to_datetime(train_data['datetime']).dt.weekday >= 5).astype(int)
        
        # Define features and target
        features = ['hour', 'temp', 'humidity', 'windspeed', 'season', 'weather', 'workingday', 'is_weekend']
        X = train_data[features]
        y = train_data['count']
        
        # Split data into training and validation sets
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Initialize and train the model
        model = RandomForestRegressor(random_state=42, n_estimators=100, max_depth=10)
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_val)
        
        # Evaluate the model
        mse = mean_squared_error(y_val, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_val, y_pred)
        
        print(f"Random Forest Model Performance:\nRMSE: {rmse}\nR²: {r2}")
        
        # Infer the signature
        signature = infer_signature(X_train, model.predict(X_train))
        input_example = X_train.head(1)
        
        # Log metrics manually (optional, since autolog does this too)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        
        # Save the model with signature and input example
        mlflow.sklearn.log_model(model, "random_forest_model", signature=signature, input_example=input_example)
        
    return model


@click.command()
@click.argument('train_path')
@click.argument('output_model_path')
def train_model(train_path, output_model_path):
    """
    CLI for training the model.
    Arguments:
    - train_path: Path to the training data.
    - output_model_path: Path to save the trained model.
    """
    model = train_random_forest_with_mlflow(train_path)
    joblib.dump(model, output_model_path)
    click.echo(f"Model trained and saved to {output_model_path}")


if __name__ == "__main__":
    train_model()
