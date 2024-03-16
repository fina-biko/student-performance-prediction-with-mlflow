'''initializes the model saved in joblib
takes the data from user and predict'''
import numpy as np
import joblib
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model=joblib.load(Path='artifacts/model_trainer/model.pkl')

    def predict(self,data):
        prediction=self.model.predict(data)
        return prediction