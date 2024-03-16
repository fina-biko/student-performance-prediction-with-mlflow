'''pipeline'''
from src.mlproject.configuration.configuration import ConfigurationManager
from src.mlproject.components.data_transformation import DataTransformationEntity,DataTransformation
class DataTransformationPipeline():
    def __init__(self) -> None:
        pass

    def main(self):
        configmanager=ConfigurationManager()
        data_config_instance=configmanager.get_data_transformation_config()
        
        entity_instance=DataTransformationEntity(data_config_instance)
        data_transf_instance=DataTransformation(entity_instance)
        data_transf_instance.transformation()
     
if __name__=='__main__':
   obj=DataTransformationPipeline()
   obj.main()
     