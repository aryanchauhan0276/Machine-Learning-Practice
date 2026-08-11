import os
import sys
import pandas as pd
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.exception.exception import NetworkSecurityException
from Constants import training_pipeline
from entity.config_entity import DataIngestionConfig
import pymongo
from typing import List
import numpy as np
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self,data_ingestion_config : DataIngestionConfig):
        try:
            self.data_ingestion_config=DataIngestionConfig()
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def export_collection_as_dataframe(self):
        try:
            database_name=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name
            self.mongo_cleint=pymongo.MongoClient(MONGO_DB_URL)
            collection=self.mongo_client[database_name][collection_name]
            df=pd.DataFrame(list(collection.find())) #mongoaddsacoloumnnamed"id"
            if "_id" in df.columns.to_list():
                df=df.drop(columns=["_id"])
            df.replace({"na",np.nan},inplace=True)
            return df

        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def export_collection_into_feature_store(self,dataframe : pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            NetworkSecurityException(e,sys)

    def split_train_test_split(self, dataframe : pd.DataFrame):
        try:
            train_set,test_set=train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio,random_state=42)
            logging.info("Train Test Split")
            logging.info("Exited Train Test Split")

            dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info("Directory Creates Successfully")
            train_set.to_csv(
                self.data_ingestion_config.training_file_path,index=False,header=True
            )

            
            dir_path_test=os.path.dirname(self.data_ingestion_config.testing_file_path)
            os.makedirs(dir_path_test,exist_ok=True)
            logging.info("testing Directory Creates Successfully")
            test_set.to_csv(
                self.data_ingestion_config.testing_file_path,index=False,header=True
            )

        except Exception as e:
            raise NetworkSecurityException(e,sys)


    def initiate_data_ingestion(self):
        try:
            dataframe=self.export_collection_as_dataframe()
            dataframe=self.export_collection_into_feature_store(dataframe)
            self.split_train_test_split(dataframe)

        except Exception as e :
            raise NetworkSecurityException(e,sys)
        
