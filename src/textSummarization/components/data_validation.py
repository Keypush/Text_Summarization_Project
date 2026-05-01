import os
from textSummarization.logging import logger
from textSummarization.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig) -> None:
        self.config = config

    def validate_all_files(self) -> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            with open(self.config.status_file, 'w') as f:
                pass 

            for file in all_files:
                if file not in self.config.all_required_files:
                    validation_status = False
                    with open(self.config.status_file, "a") as f:
                        f.write(f"File Validation Failed: {file}\n")
                else:
                    validation_status = True
                    with open(self.config.status_file, "a") as f:
                        f.write(f"File Validation Successful: {file}\n")

            return validation_status

        except Exception as e:
            logger.info(f"Error occurred during file validation: {e}")
            raise e