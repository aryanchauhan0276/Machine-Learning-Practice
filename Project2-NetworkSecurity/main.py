from NetworkSecurity.Components.data_ingestion import DataIngestion
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.entity.config_entity import DataIngestionConfig
from NetworkSecurity.entity.config_entity import TrainingPipelineConfig
import sys
if __name__=="__main__":
    try:
        data_training_config=TrainingPipelineConfig()
        data_inges_config=DataIngestionConfig(data_training_config)
        data_ingestion=DataIngestion(data_inges_config)
        logging.info("Running Data Ingestion")
        dataingestion_artifact=data_ingestion.initiate_data_ingestion()
        print("Working Fine")
    except Exception as e:
        raise NetworkSecurityException(e,sys)