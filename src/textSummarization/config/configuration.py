from textSummarization.constants import *
from textSummarization.utils.common import read_yaml, create_directories
from textSummarization.entity import (DataIngestionConfig, 
                                      DataValidationConfig, 
                                      DataTransformationConfig, 
                                      ModelTrainerConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_file_path: Path = CONFIG_FILE_PATH,
        params_file_path: Path = PARAMS_FILE_PATH
    ) -> None:
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
    
        create_directories([self.config.artificats_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            all_required_files=config.all_required_files
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        model_trainer_config = self.config.model_trainer
        model_trainer_params = self.params.TrainingArguments

        create_directories([model_trainer_config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=model_trainer_config.root_dir,
            data_path=model_trainer_config.data_path,
            model_ckpt=model_trainer_config.model_ckpt,
            num_train_epochs=model_trainer_params.num_train_epochs,
            warmup_steps=model_trainer_params.warmup_steps,
            per_device_train_batch_size=model_trainer_params.per_device_train_batch_size,
            per_device_eval_batch_size=model_trainer_params.per_device_eval_batch_size,
            weight_decay=model_trainer_params.weight_decay,
            logging_steps=model_trainer_params.logging_steps,
            eval_strategy=model_trainer_params.eval_strategy,
            eval_steps=model_trainer_params.eval_steps,
            save_steps=model_trainer_params.save_steps,
            gradient_accumulation_steps=model_trainer_params.gradient_accumulation_steps
        )

        return model_trainer_config