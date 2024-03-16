from flask import Flask,render_template,request
import os
import numpy as np
import pandas as pd
from src.mlproject.pipeline.prediction_pipeline import PredictionPipeline



#initialize the flask app
app= Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')
''' this route definition specifies that when a user accesses the root URL of your application using a GET request, 
Flask will execute the homepage function, and the function will render the index.html template as a response.'''
