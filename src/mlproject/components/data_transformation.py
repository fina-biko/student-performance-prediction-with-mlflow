'''
define the categorical columns and numerical columns and the target column
split into train and test
define the train x and train y,test x and test y
define the transformation to be performed on categorical 
define the transformation to be performed on numerical 
save the transformation object
combine the trainx and train y
'''
from sklearn.model_selection import train_test_split
from src.mlproject.utils.common import read_yaml_keys

from src.mlproject.entity.config_entity import DataTransformationConfig
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import pandas as pd
#from scipy.sparse import issparse

from sklearn.preprocessing import MaxAbsScaler

class DataTransformationEntity:
    def __init__(self,config_instance:DataTransformationConfig) :
        self.transf_config=config_instance
       
        
        self.test_set_transf=self.transf_config.transf_test_set
        self.train_set_transf=self.transf_config.transf_train_set
        self.raw_data=self.transf_config.raw_data
        self.schemapath=self.transf_config.schema_data

    '''def accesss_trans_config_elements(self):
        self.transf_train_set=self.transf_config.transf_test_set
        self.trans_test_set=self.transf_config.transf_test_set'''
    def initiate_split(self):
        categorical_col,numerical_cal,target_col=read_yaml_keys(self.transf_config.schema_data)
        
        raw_data_df=pd.read_csv(self.raw_data)

        

        train,test=train_test_split(raw_data_df,random_state=42,test_size=0.2)

        

        train_df=pd.DataFrame(train,columns=raw_data_df.columns)
        test_df=pd.DataFrame(test,columns=raw_data_df.columns)

        
        train_y=train_df[target_col]
        
        
        train_x = train_df.drop(target_col, axis=1)
        

        test_y=test_df[target_col]
        test_x=test_df.drop(target_col,axis=1)
       
        
        return train_x,train_y,test_x,test_y
    def transformations(self):
        cat_pipeline=Pipeline(
            steps=[
            #('imputer',SimpleImputer(strategy="most_frequent")),
            ('encoder',OneHotEncoder(handle_unknown='ignore')),
            ]
            )
        '''num_pipeline=Pipeline(
            steps=[
            ('impute',SimpleImputer(strategy='median')),
            ('scaler',StandardScaler(with_mean=False))
            ]
        )'''


        num_pipeline = Pipeline(
           steps=[
          # ('impute', SimpleImputer(strategy='median')),
           ('scaler', StandardScaler())
    ]
)
        return cat_pipeline,num_pipeline
    

    
  
    def cols_transformer(self):
        categorical_col,numerical_cal,target_col=read_yaml_keys(self.transf_config.schema_data)
        train_x,train_y,test_x,test_y=self.initiate_split()

        cat_pipe,num_pipe=self.transformations()
        
        preprocessing_obj=ColumnTransformer(transformers=[('num',num_pipe,numerical_cal),('cat',cat_pipe,categorical_col)],remainder='drop')
        # Assuming preprocessing_obj is the ColumnTransformer
        
        
        
        return preprocessing_obj
    
    '''the actual transformation
 as it has all the transformations

pass in the entities you need from the the DataTransfofrmationEntity,an instance of the DataTransformationEntity
 
do the actujal transformation using entities from DataTransfofrmationEntity
store the transformations in the paths specified by DataTransformationConfig instnce which i put as attributtes of the DataTransformationEntity
TRANSFORMATION>PY'''
import numpy as np
import pandas as pd
class DataTransformation:
    def __init__(self,configEnt:DataTransformationEntity) :
        
        self.transformation_entity=configEnt#an ins
        
        
    def transformation(self):
        categorical_col,numerical_cal,target_col=read_yaml_keys(self.transformation_entity.schemapath)

        train_x_transf, train_y, test_x_transf,test_y=self.transformation_entity.initiate_split()
        print(test_y)
        
        self.transformation_entity.transformations()
        prep_obj=self.transformation_entity.cols_transformer()

        
        trainx_transformed_data=prep_obj.fit_transform(train_x_transf)
        
        # Get feature names after transformation
        transformed_feature_names = prep_obj.get_feature_names_out(input_features=categorical_col+ numerical_cal)

       # Create a DataFrame with the transformed data and feature names
        trainx_transformed_df = pd.DataFrame(trainx_transformed_data, columns=transformed_feature_names)
        trainx_transformed_df[target_col]=train_y.values
        

        
       
        testx_transformed_data=prep_obj.transform(test_x_transf)
        testx_transformed_df = pd.DataFrame(testx_transformed_data, columns=transformed_feature_names)
        testx_transformed_df[target_col] = test_y.values  # Use .values to get the underlying NumPy array
        print(testx_transformed_df.head(1))
        print(testx_transformed_df.shape)
        
    

       
        with open(self.transformation_entity.train_set_transf,'w') as train_csv:
           trainx_transformed_df.to_csv(train_csv,index=False)

        with open(self.transformation_entity.test_set_transf,'w') as test_csv:
            testx_transformed_df.to_csv(test_csv,index=False)
        