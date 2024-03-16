from src.mlproject.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from src.mlproject.pipeline.stage_02_data_transformatio_pipeline import DataTransformationPipeline
from src.mlproject.pipeline.stage_03_model_trainer_pipeline import ModelTrainerPipeline
STAGE_NAME='DataIngestion'
data_ingestion_pipeline=DataIngestionPipeline()
data_ingestion_pipeline.main()



STAGE_NAME='DataTransfofrmation'
data_transformation_pipeline=DataTransformationPipeline()
data_transformation_pipeline.main()


STAGE_NAME='MODEL TRAINER'
model_trainer_pipeline=ModelTrainerPipeline()
model_trainer_pipeline.main()
