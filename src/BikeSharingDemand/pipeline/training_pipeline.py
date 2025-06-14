from src.BikeSharingDemand.config.configuration import ConfigurationManager
from logging_part.logger import logger
from src.BikeSharingDemand.components.Data_Ingestion import DataIngestionModule
from exception.exception import BikeSharingDemand
from src.BikeSharingDemand.components.Data_Validation import DataValidation

if __name__=="__main__":

    try:
        logger.info("Data Ingestion Stage Started")
        obj=ConfigurationManager()
        config_details_of_ingestion=obj.get_data_ingestion_details()
        data_ingetion=DataIngestionModule(config=config_details_of_ingestion)
        data_ingetion.downloading_data_from_kaggle()
        data_ingetion.extracting_zip_file()

        logger.info("Data Validation Stage Started")
        config_details_of_validation=obj.get_data_validation_config()
        data_validation=DataValidation(config=config_details_of_validation)
        logger.info("Data Validation Function started")
        data_validation.data_validation()

    except Exception as e:
        raise BikeSharingDemand(e)