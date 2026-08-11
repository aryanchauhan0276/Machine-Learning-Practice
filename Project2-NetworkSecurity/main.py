from NetworkSecurity.Components.data_ingestion import DataIngestion
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from NetworkSecurity.entity.config_entity import TrainingPipelineConfig
from NetworkSecurity.Components.Data_Validation import DataValidation
import sys
if __name__=="__main__":
    try:
        data_training_config=TrainingPipelineConfig()
        data_inges_config=DataIngestionConfig(data_training_config)
        data_ingestion=DataIngestion(data_inges_config)
        logging.info("Running Data Ingestion")
        dataingestion_artifact=data_ingestion.initiate_data_ingestion()
        print("Working Fine")
        logging.info("Data Initiation Completed")
        DataValidation(data_inges_config)
        data_valid_config=DataValidationConfig(data_training_config)
        data_valid=DataValidation(dataingestion_artifact,data_valid_config)
        data_valid_artifact=data_valid.initiate_data_validation()
    except Exception as e:
        raise NetworkSecurityException(e,sys)