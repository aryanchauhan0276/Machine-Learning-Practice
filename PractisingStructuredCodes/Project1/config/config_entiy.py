from constants import training_pipeline
import os
import sys
class training_pipeline_config:
    def __init__(self,training_pipeline):
        self.artifact_file_path=training_pipeline.Artifact_File_Path
        self.dataset_path=training_pipeline.Dataset_Path

   
class data_ingestion_config:
    def __init__(self,training_pipeline_config):
        self.data_ingestion_dir=os.path.join(training_pipeline_config.artifact_file_path,training_pipeline.Data_Ingested_Dir)
        self.data_ingestion_path=os.path.join(self.data_ingestion_dir,training_pipeline.Data_Ingested)
        self.training_dataset=os.path.join(training_pipeline_config.artifact_file_path,training_pipeline.Training_Data_Path)
        self.test_dataset=os.path.join(training_pipeline_config.artifact_file_path,training_pipeline.Test_Data_Path)
