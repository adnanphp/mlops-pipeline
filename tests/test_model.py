"""
Unit tests for model
"""
import pytest
import joblib
import numpy as np
import os

def test_model_exists():
    """Test that model file exists"""
    assert os.path.exists('models/best_model.joblib'), "Model file not found"

def test_model_loading():
    """Test that model loads correctly"""
    try:
        model = joblib.load('models/best_model.joblib')
        assert model is not None
    except Exception as e:
        pytest.fail(f"Model loading failed: {e}")

def test_model_prediction():
    """Test model makes predictions"""
    model = joblib.load('models/best_model.joblib')
    # Create sample input (8 features for California Housing)
    X_test = np.random.rand(1, 8)
    try:
        prediction = model.predict(X_test)
        assert len(prediction) == 1
        assert isinstance(prediction[0], (float, np.float64))
    except Exception as e:
        pytest.fail(f"Prediction failed: {e}")

def test_model_output_range():
    """Test that predictions are in expected range"""
    model = joblib.load('models/best_model.joblib')
    X_test = np.random.rand(1, 8)
    prediction = model.predict(X_test)[0]
    # California housing prices are in 0-5 range (approximately)
    assert 0 <= prediction <= 6
