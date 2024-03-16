import pandas as pd
from src.mlproject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig) :
        self.config=config

    def reading_csv(self):
        dataframe=pd.read_csv(self.config.findData)
        # Store the DataFrame in the specified datastore path
        #dataframe.to_csv(self.config.datastore,index=False,header=True)
        with open(self.config.datastore,'w') as csv_file:
           dataframe.to_csv(csv_file, index=False)