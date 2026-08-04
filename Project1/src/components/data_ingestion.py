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
        self.dataingestion=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Method")
        try:
            df=pd.read_csv("Project1\notebook\StudentsPerformance.csv")
            
