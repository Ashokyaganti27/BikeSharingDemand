import os
from src.BikeSharingDemand.entity.config_entity import DataIngestionConfig
os.environ["KAGGLE_CONFIG_DIR"]=os.path.join(os.getcwd(),".kaggle")
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
from logging_part.logger import logger
from pathlib import Path
from exception.exception import BikeSharingDemand
class DataIngestionModule:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    def downloading_data_from_kaggle(self):

        if os.path.exists(self.config.unzip_path):
           return logger.info(f"Datset already downloaded at {self.config.unzip_path}")


        config=self.config

        api=KaggleApi()
        api.authenticate()

        api.competition_download_files(
            competition=config.link,
            path=config.filepath,
        )

        # combining dataset path to dataset.zip

        dataset_path=os.path.join(config.filepath,config.link + ".zip")
        actual_path=Path(config.unzip_path)

        try:
            if os.path.exists(dataset_path):
               os.rename(dataset_path,actual_path)
               logger.info("Dataset name successfully renamed to dataset.zip")
        except Exception as e:
            raise BikeSharingDemand(e)
        

    def extracting_zip_file(self):

        files=["train.csv","test.csv","sampleSubmission.csv"]

        if all((os.path.exists(os.path.join(self.config.filepath,file)) for file in files)):
            return logger.info(f"File is already unzipped")
        
        else:
            
            logger.info(f"Extracting Zip file from {self.config.unzip_path}")
            with zipfile.ZipFile(self.config.unzip_path,"r") as zip_file:

                zip_file.extractall(self.config.filepath)

        
    





