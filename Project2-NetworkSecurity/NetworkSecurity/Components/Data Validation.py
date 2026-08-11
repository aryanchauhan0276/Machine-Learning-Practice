from NetworkSecurity.Components import data_ingestion
from NetworkSecurity.entity import config_entity
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging
import os
import sys
from NetworkSecurity.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from NetworkSecurity.entity.config_entity import DataValidationConfig
from scipy.stats import k2_2samp
from NetworkSecurity.Constants.training_pipeline import SCHEMA_FILE_PATH
from NetworkSecurity.utils.main_utils.utils import read_yaml_file
class DataValidation:
    def __init__(self,data_ingestion_artifact:DataValidationArtifact,data_validation_config:DataValidationArtifact):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config=read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,sys)