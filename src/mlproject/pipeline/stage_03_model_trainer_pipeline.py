from src.mlproject.configuration.configuration import ConfigurationManager
from src.mlproject.entity.config_entity import ModelEntity
from src.mlproject.components.model_trainer import ModelTrainerService
class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config_manager=ConfigurationManager()
        model_config=config_manager.get_model_trainer_config()
        model_entity=ModelEntity()
        
        model_service=ModelTrainerService(model_config,model_entity)
        model_service.get_best_model()

if __name__=='__main__':
    ModelTrainerPipeline().main()
