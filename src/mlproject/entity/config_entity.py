from dataclasses import dataclass
from pathlib import Path
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.ensemble import RandomForestClassifier,AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor


@dataclass
class DataIngestionConfig:
    findData: Path
    datastore:Path
    innerfolder:Path


'''update the config.yaml file
the constants will be unchanged
update the entity
update the configuration manager
do the test train split
'''
from dataclasses import dataclass
from pathlib import Path
@dataclass
class DataTransformationConfig:
    raw_data:Path
    schema_data:Path
    transf_train_set:Path
    transf_test_set:Path
@dataclass
class ModelTrainerConfig:
   train_csv:Path# what we need is train csv, where was it stored
   test_csv:Path
   model_file: Path#what we need is model file,where will we store it?
   schema_data:Path
   report_file: Path#we will also need a report of all the models performcance,where will we store it?


class ModelEntity:
    models={'RandomForest':RandomForestRegressor(),
                    "DecisionTree": DecisionTreeRegressor(),
                    "GradientBoosting": GradientBoostingRegressor(),
                    "LinearRegression": LinearRegression(),
                   
                    #"CatBoosting Regressor": CatBoostRegressor(verbose=False),#
                    "AdaBoost Regressor": AdaBoostRegressor()
                    }





