from src.BikeSharingDemand.entity.config_entity import DataIngestionConfig
from src.BikeSharingDemand.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH,SCHEMA_FILE_PATH
from src.BikeSharingDemand.utils.common import create_directories,read_yaml
from src.BikeSharingDemand.entity.config_entity import DatavalidationConfig
class ConfigurationManager:
    def __init__(self,config=CONFIG_FILE_PATH,params=PARAMS_FILE_PATH,schema=SCHEMA_FILE_PATH):
        self.config=read_yaml(config)
        self.params=read_yaml(params)
        self.schema=read_yaml(schema)

        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_details(self)->DataIngestionConfig:
        config=self.config.data_ingestion

        create_directories([config.filepath])

        data_ingestion_config=DataIngestionConfig(

            filepath=config.filepath,
            link=config.link,
            unzip_path=config.unzip_path

        )
        
        return data_ingestion_config
    
    def get_data_validation_config(self)->DatavalidationConfig:

        config=self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config=DatavalidationConfig(
            root_dir=config.root_dir,
            train_path=config.train_path,
            test_path=config.test_path,
            status_file=config.status_file
        )
        
        return data_validation_config
 