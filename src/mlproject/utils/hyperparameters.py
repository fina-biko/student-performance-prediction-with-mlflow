from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.ensemble import RandomForestClassifier,AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
import os

import yaml
from pathlib import Path
#from xgboost import XGBRegressor
parent_folder='config'
file_path='hyperparameter.yaml'
os.makedirs(parent_folder,exist_ok=True)
yaml_file_path=os.path.join(parent_folder,file_path)

class hyperparameters:
    models={'RandomForest':RandomForestRegressor(),
                    "Decision Tree": DecisionTreeRegressor(),
                    "Gradient Boosting": GradientBoostingRegressor(),
                    "Linear Regression": LinearRegression(),
                
                    #"CatBoosting Regressor": CatBoostRegressor(verbose=False),#
                    "AdaBoost Regressor": AdaBoostRegressor()
                    }


hyperparameters={
                'DecisionTree':{
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    'splitter':['best','random'],
                    'max_features':['sqrt','log2'] },

                'RandomForest':{
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]},

                'GradientBoosting':{
                    'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    'criterion':['squared_error', 'friedman_mse'],
                    'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]},

                    "Linear Regression":{},

                    "XGBRegressor":{
                        'learning_rate':[.1,.01,.05,.001],
                        'n_estimators': [8,16,32,64,128,256] },

                   ''' "CatBoosting Regressor":{
                        'depth': [6,8,10],
                        'learning_rate': [0.01, 0.05, 0.1],
                        'iterations': [30, 50, 100]},'''

                    "AdaBoost Regressor":{
                        'learning_rate':[.1,.01,0.5,.001],
                        # 'loss':['linear','square','exponential'],
                        'n_estimators': [8,16,32,64,128,256]}
                }

with open (yaml_file_path,'w') as file_path:
                 yaml.dump(hyperparameters,file_path,default_flow_style=False)




