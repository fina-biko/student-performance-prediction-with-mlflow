import pandas as pd
from src.mlproject.utils.common import evaluate_score,save_model
import mlflow
from mlflow import sklearn
from sklearn.model_selection import RandomizedSearchCV
from src.mlproject.utils.common import read_yaml_keys
from src.mlproject.entity.config_entity import ModelEntity,ModelTrainerConfig
from sklearn.ensemble import AdaBoostRegressor
from src.mlproject.configuration.configuration import ConfigurationManager
class ModelTrainerService:
    def __init__(self,config_instance:ModelTrainerConfig,models_entity:ModelEntity) :
        self.config_instance=config_instance
        self.model_train=config_instance.train_csv
        self.model_test=config_instance.test_csv
        self.model_pickle=config_instance.model_file
        self.report_file=config_instance.report_file
        
        self.model_schema=self.config_instance.schema_data
        
        #self.model_schema=self.config_instance.schema_data,# why is it that if we put a comma it becomes a tuple
        
        self.models_dict=models_entity.models

        configurationmanagerinstance=ConfigurationManager()
        self.parameters=configurationmanagerinstance.params
        self.hyperparameter=self.parameters.get('hyperparameters',{})
        print("Loaded hyperparam:", self.hyperparameter)
        
    def splitting(self):
        cat_col,num_cal,target_col=read_yaml_keys(self.model_schema)
        train_df=pd.read_csv(self.config_instance.train_csv,header='infer',delimiter=',')
        #train_df=pd.read_csv(filepath_or_buffer=self.model_train)
        test_df=pd.read_csv(self.model_test)

        x_train=train_df.drop(target_col,axis=1)
        y_train=train_df[target_col]

        x_test=test_df.drop(target_col,axis=1)
        y_test=test_df[target_col]

        return x_test,y_test,x_train,y_train
    
    
    def get_best_model(self):
        report={}
        x_test,y_test,x_train,y_train=self.splitting()
        '''for i in range(len(self.models_dict)):
           print('..........................................')
           model_name =list(self.models_dict.keys())[i]
           print(model_name)
           model_instance =list(self.models_dict.values())[i]
           
           parameters=self.hyperparameter.get(list(self.models_dict.keys())[i],{})
           print(parameters)'''

           
        for model_name,model_instance in self.models_dict.items():
            print('..........................................')
           
            parameters=self.hyperparameter.get(model_name,{})# i forgot to use get to retrieve the model name such that is resulted into category name and attributes but i wanted attributes only,the 
            
            if parameters:#check if parameters is not empty
                     rs=RandomizedSearchCV(estimator=model_instance,param_distributions=parameters,cv=5)
                     rs.fit(x_train,y_train)
                     predict=rs.predict(x_test)
                     mae,mse,score=evaluate_score(y_test,predicted_value=predict)
                     #tuning the parameters manually below has resulted in error in passing the hyperparameters,using Gridsearch cv takes forever
                     '''for key, value in parameters.items():
                     model_instance.set_params(**{key: value})
                     #model_instance.set_params(**parameters)
                     model_instance.fit(x_train,y_train)
                     y_pred=model_instance.predict(x_test)
                     score=r2_score(y_test,y_pred)'''
                
                     try:
                        with open(self.report_file, 'a') as file:
                            file.write(f"{model_name}: {score} \t {mae}\t {mse} \n")
                        print(f"Score for {model_name} written to report file.")
                     except Exception as e:
                        print(f"Error writing to report file: {e}")

                     try:
                        with mlflow.start_run(run_name='tired_3') as run:
                                mlflow.log_metric('r2_score', score)
                                mlflow.log_metric('mae', mae)
                                mlflow.log_metric('mse', mse)
                                mlflow.log_params(rs.best_params_)
                                mlflow.sklearn.log_model(rs.best_estimator_, "model_" + model_name)
                                # Print the run id of each model but its not a must
                                print(f"Run ID: {run.info.run_id}")
                               # runid=run.info.run_id
                        print(f"Model {model_name} logged to mlflow.")
                     except Exception as e:
                            print(f"Error logging to mlflow: {e}")

        best_run_id='f95b9d08d6404162815bb3c19fce79f1'
        
        best_run=mlflow.get_run(best_run_id)#i was using search_runs so it resulted into empty runs.
        if  best_run:
            best_hyperparameters= best_run.data.params
            best_model=AdaBoostRegressor(**best_hyperparameters)
            save_model(model=best_model,path=self.model_pickle)
        
        else:
             print(f"No runs found for run_id: {best_run_id}")
        
        
    

        
                    
                
            

    
    

    
    
    
           


          



           

           
        

            
            

        
        
        