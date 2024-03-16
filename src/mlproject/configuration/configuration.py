from src.mlproject.constants import CONFIG_PATH_YAML,SCHEMA_PATH_YAML,PARAMS_PATH_YAML
from src.mlproject.entity.config_entity import DataIngestionConfig,DataTransformationConfig,ModelTrainerConfig
from src.mlproject.utils.common import read_yaml,create_directories
import os
class ConfigurationManager:

   def __init__(self,config_filepath=CONFIG_PATH_YAML,schema_path=SCHEMA_PATH_YAML,params_path=PARAMS_PATH_YAML) :#inner folder,pathto csv,datastore
        self.config_data=read_yaml(config_filepath)
        self.params=read_yaml(params_path)
        print("Loaded params:", self.params)
        self.schema=read_yaml(schema_path)
        #Retrieve the parent folder 
        self.parent_folder =self.config_data.get('parent_folder', '')
         #Retrieve the artifcats root 
        self.artifacts_root =self.parent_folder.get('artifacts_root', '')
        #and create the folder 'artifacts_root'
        create_directories([self.artifacts_root])


        #DATA INGESTION
        #Retrieve data ingestion 
        self.data_ingestion = self.config_data.get('data_ingestion', '')
        #and create folders within the data ingestion
        create_directories([self.data_ingestion.get('inner_folder', '')]) 
        #join the file to the created folder
        filepath=os.path.join(self.data_ingestion.get('inner_folder', ''),self.data_ingestion.get('data_store', ''))
        
       #DATA TRANSFORMATION
        #retrieve the data ttransformation category
        self.data_transformation=self.config_data.get('data_transformation','')
        #create the folder within it 
        create_directories([self.data_transformation.get('inner_folder','')])
        
        # join the files and assign the result to variables
        self.transformed_train_set_path = os.path.join(self.data_transformation.get('inner_folder', ''),self.data_transformation.get('transformed_train_set', ''))
        #os.path.join(self.data_transormation.get('inner_folder',''),self.data_transormation.get('transformed_train_set',''))
        self.transformed_test_set_path=os.path.join(self.data_transformation.get('inner_folder',''),self.data_transformation.get('transformed_test_set',''))
        
        
        #MODEL_TRAINER
        #retrieve the model trainer
        self.model_trainer=self.config_data.get('model_trainer','')
         #get the model trainer inner folder
        
        create_directories([self.model_trainer.get('model_file_innerfolder','')])
        #join the file
        self.model_file_path=os.path.join(self.model_trainer.get('model_file_innerfolder',''),self.model_trainer.get('model_file_path',''))
        self.report_file_path=os.path.join(self.model_trainer.get('model_file_innerfolder',''),self.model_trainer.get('report_file_path',''))
   
   
   def get_data_ingestion_config(self) -> DataIngestionConfig:
            data_ingestion_config = DataIngestionConfig(
                findData=self.data_ingestion.get('path_to_csv', ''),
                innerfolder=self.data_ingestion.get('inner_folder', ''),
                datastore=self.data_ingestion.get('data_store', '')
            )
            return data_ingestion_config
        
         #instantiate the defined entities and return the instance
   def get_data_transformation_config(self)->DataTransformationConfig:

            data_transformation_config = DataTransformationConfig(
                transf_train_set=self.transformed_train_set_path,
                transf_test_set=self.transformed_test_set_path,
                raw_data=self.data_transformation.get('raw_data',''),
                schema_data=self.schema
                
                
                )
            
            return data_transformation_config
   def get_model_trainer_config(self)-> ModelTrainerConfig:
       get_model_trainer=ModelTrainerConfig(
           train_csv=self.model_trainer.get('train_csv',''), #this is where it was stores
           test_csv=self.model_trainer.get('test_csv',''),#i was using self.config.get instead of model trainer,so geting wrror cannot eopen empty string'''
           model_file=self.model_file_path,#this is where it will be stored
           schema_data=self.schema,
           report_file=self.report_file_path
           
       )

       return get_model_trainer
         
        

    