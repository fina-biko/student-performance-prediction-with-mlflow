import logging
from datetime import date
from pathlib import Path
import yaml
import os
from sklearn.metrics import r2_score,mean_absolute_error, mean_squared_error
import joblib
import logging


'''def read_yaml (filepath):
    try :
        with open (filepath,'r') as f:
            filepath=yaml.safe_load(f)

    except Exception:
        raise FileNotFoundError'''
    


def read_yaml(filepath):
    with open(filepath, 'r') as file:
        data = yaml.safe_load(file)
    return data


def create_directories(lists_of_filepath:list):
    for path in lists_of_filepath:#provide the parent folder ,inner folder and filename
        os.makedirs(path,exist_ok=True)
       
'''def extract_keys_from_yaml(yaml_filepath):
    with open(yaml_filepath, 'r') as file:
        schemadata = yaml.safe_load(file)

    # Extract keys from the yaml data, items is used when we dont want to use the get method
    how they are structured

    category, ie data ingestion:
    attribute_keys ie source ursl:attributes values ie httsp....


    keys = []
    for category, attributes in schemadata.items():
        keys.extend(attributes.keys())

    return keys
 #Example usage
yaml_filepath = 'path/to/your_yaml_file.yaml'
keys = extract_keys_from_yaml(yaml_filepath)

# Print the extracted keys
print(keys)
['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
'''
#If schemapath is a dictionary, you can directly get the keys
def read_yaml_keys(schemadata):
    #with open (schemapath,'r') as file:
        #schemadata=yaml.safe_load(file)

    #extract the keys
        
    categorical_keys=[]
    numerical_keys=[]
   
    target_key = []
# Assuming 'Target_column1' is a dictionary with column names and data types
    target_key.extend(list(schemadata.get(' the category which is 'Target_column1 , {}).' and find its 'keys() 'which is the mathscore'))
    '''the purpose of using {} in schemadata.get('Target_column1', {}) is to ensure that if the key
      'Target_column1' is not found in schemadata, an empty dictionary is returned as the default value'''

# Now target_key is a list of column names, 
    target_keys = ', '.join(target_key)
    
   
    for category,attributes in schemadata.items():#a dictionary
        if category=='categorical':
          categorical_keys.extend(attributes.keys())
        elif category=='numerical':
            numerical_keys.extend(attributes.keys())

        
   
    return categorical_keys,numerical_keys,target_keys
        



def evaluate_score(tru_value,predicted_value):
    mae=mean_absolute_error(tru_value,predicted_value)
    mse=mean_squared_error(tru_value,predicted_value)
    r2score=r2_score(tru_value,predicted_value)

    return mae,mse,r2score

def save_model(model,path:Path):
    with open(path, 'wb') as f:
        joblib.dump(model,f)
    print("Saved model",path)
    '''The error you're encountering (TypeError: write() argument must be str, not bytes) suggests that you are
      trying to write binary data to a file opened in text mode. In Python, when working with binary data 
      (such as pickled machine learning models), you should open the file in binary mode ('wb') instead of text mode
        ('w').'''



    
