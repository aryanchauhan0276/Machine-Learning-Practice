import os
from Project1.config.config_entity import data_ingestion_config
import sys
from Exception.exception import exception
from Logging.logging import logger
class DataIngestion:
    def __init__(self,Data_ingestion_config : data_ingestion_config):
        try:
            self.Data_Ingestion_config=data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)