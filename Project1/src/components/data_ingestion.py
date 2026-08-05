#Code related to reading the data
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join('Artifact',"train.csv")
    test_data_path : str = os.path.join('Artifact',"test.csv")
    raw_data_path : str = os.path.join('Artifact',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Method")
        try:
            df=pd.read_csv("Project1\notebook\StudentsPerformance.csv")
            os.makedirs((self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw,index=False,header=True)
            logging.info("train_test_split")
            train_set,test_set=train_test_split(df,test_size=0.20,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            return (self.ingestion_config.train_data_path
                ,self.ingestion_config.test_data_path)


        except CustomException as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

            
