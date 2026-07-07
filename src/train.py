"""
MLflow Training Pipeline
"""
import mlflow
import mlflow.sklearn
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np
import os
import joblib

# Set MLflow tracking URI
mlflow.set_tracking_uri("file:./mlruns")

def load_data():
    """Load California Housing dataset"""
    data = fetch_california_housing()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name='target')
    return X, y

def train_and_log():
    """Train models and log with MLflow"""
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print("🚀 Starting training pipeline...")
    
    models = {
        'LinearRegression': LinearRegression(),
        'RandomForest': RandomForestRegressor(n_estimators=100, random_state=42),
        'GradientBoosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
    }
    
    best_model = None
    best_r2 = -float('inf')
    best_run_id = None
    best_model_name = None
    
    for name, model in models.items():
        with mlflow.start_run(run_name=name) as run:
            print(f"\n📊 Training {name}...")
            
            # Log model parameters
            mlflow.log_params(model.get_params())
            
            # Train
            model.fit(X_train, y_train)
            
            # Predict and evaluate
            y_pred = model.predict(X_test)
            rmse = np.sqrt(mean_squared_error(y_test, y_pred))
            r2 = r2_score(y_test, y_pred)
            
            # Log metrics
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            
            # Log model
            mlflow.sklearn.log_model(model, "model")
            
            print(f"  ✅ RMSE: {rmse:.4f}")
            print(f"  ✅ R²: {r2:.4f}")
            print(f"  📝 Run ID: {run.info.run_id}")
            
            # Track best model
            if r2 > best_r2:
                best_r2 = r2
                best_model = model
                best_run_id = run.info.run_id
                best_model_name = name
    
    print("\n" + "="*50)
    print(f"🏆 Best Model: {best_model_name}")
    print(f"📈 Best R² Score: {best_r2:.4f}")
    print(f"📝 Best Run ID: {best_run_id}")
    print("="*50)
    
    # Save best model
    os.makedirs('models', exist_ok=True)
    joblib.dump(best_model, 'models/best_model.joblib')
    print("💾 Best model saved to models/best_model.joblib")

if __name__ == "__main__":
    train_and_log()
    print("\n🎉 Training complete! Run 'mlflow ui' to see results.")
