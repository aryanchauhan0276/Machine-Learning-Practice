import sys,os
from NetworkSecurity.Constants.training_pipeline import TARGET_COLUMN,DATA_TRANSFORMATION_IMPUTER_PARAMS
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
from NetworkSecurity.entity.artifact_entity import (
    DataTransformationArtifact,DataValidationArtifact
)
from NetworkSecurity.entity.config_entity import DataTransformationConfig
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.utils.main_utils.utils import save_numpy_array,save_object
class DataTransformation:
    def __init__(self,data_validation_artifact:DataValidationArtifact,
                 data_transformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifact : DataValidationArtifact =data_validation_artifact
            self.data_transformation_config:DataTransformationConfig=data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    @staticmethod
    def read_csv(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)


    def get_data_tranformer_object(cls)->Pipeline:
        """KNN Imputer"""
        logging.info("Entered get_data_tranformer_object")
        try:
            imputer:KNNImputer=KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            processor : Pipeline=Pipeline([("imputer",imputer)])
            return processor
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def initiate_data_transformation(self,)->DataTransformationArtifact:
        logging.info("Data Transformation Initiated")
        try:
            logging.info("Data Transformation Started")
            train_df=DataTransformation.read_csv(file_path=self.data_validation_artifact.valid_train_file_path)
            test_df=DataTransformation.read_csv(file_path=self.data_validation_artifact.valid_test_file_path)

            ##TrainingDataFrame
            input_feature_train=train_df.drop(columns=[TARGET_COLUMN])
            target_feature_train=train_df[TARGET_COLUMN]
            target_feature_train=target_feature_train.repalce(-1,0)

            #TESTDataframe
            input_feature_test=test_df.drop(columns=[TARGET_COLUMN])
            target_feature_test=test_df[TARGET_COLUMN]
            target_feature_test=target_feature_test.repalce(-1,0)
            preprcoessor=self.get_data_tranformer_object()
            preprcoessor_obj=preprcoessor.fit(input_feature_train)
            transformed_input_train=preprcoessor_obj.transform(input_feature_train)
            transformed_input_test=preprcoessor_obj.transform(input_feature_test)

            train_arr=np.c_[transformed_input_train,np.array(target_feature_train)]
            test_arr=np.c_[transformed_input_test,np.array(target_feature_test)]
            save_numpy_array(self.data_transformation_config.transformed_train_file_path,array=train_arr)
            save_numpy_array(self.data_transformation_config.transformed_test_file_path,array=test_arr)
            save_object(self.data_transformation_config.transformed_object_file_path,preprcoessor_obj)

            DataTransformationArtifact=DataTransformationArtifact(
                self.data_transformation_config.transformed_object_file_path,
                self.data_transformation_config.transformed_train_file_path,
                self.data_transformation_config.transformed_test_file_path
                
            )

        except Exception as e:
            raise NetworkSecurityException(e,sys)