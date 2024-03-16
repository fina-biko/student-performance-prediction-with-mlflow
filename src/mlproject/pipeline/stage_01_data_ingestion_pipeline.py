from src.mlproject.configuration.configuration import ConfigurationManager
from src.mlproject.components.data_ingestion import DataIngestion
class DataIngestionPipeline:

    def __init__(self) -> None:
        pass
    def main(self):
        data_injestion_config=ConfigurationManager()
        ingestion=data_injestion_config.get_data_ingestion_config()
        data=DataIngestion(ingestion)
    
        data.reading_csv()
        

if __name__=='__main__':
    obj=DataIngestionPipeline()
    obj.main()