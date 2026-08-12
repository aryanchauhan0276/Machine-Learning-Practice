from NetworkSecurity.Components.data_ingestion import DataIngestion
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from NetworkSecurity.entity.config_entity import TrainingPipelineConfig
from NetworkSecurity.Components.Data_Validation import DataValidation
from NetworkSecurity.Components.data_transformation import DataTransformation
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
        
        data_valid_config=DataValidationConfig(data_training_config)
        data_valid=DataValidation(dataingestion_artifact,data_valid_config)
        data_valid_artifact=data_valid.initiate_data_validation()

        data_transformation_config=DataTransformationConfig(data_training_config)
        logging.info("data Transformation started")
        data_transformation=DataTransformation(data_valid_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data Transformation completed")
    except Exception as e:
        raise NetworkSecurityException(e,sys)