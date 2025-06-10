
from src.BikeSharingDemand.entity.config_entity import DatavalidationConfig
from logging_part.logger import logger
import pandas as pd
from exception.exception import BikeSharingDemand

class DataValidation:
    def __init__(self,config:DatavalidationConfig):
        self.config=config

    def data_validation(self):

        train=pd.read_csv(self.config.train_path)

        test=pd.read_csv(self.config.test_path)

        # we drop casual, registered columns because these columns we got after training
        # count is target we can drop these

        train=train.drop(["casual","registered","count"],axis=1)

        test_columns=list(test.columns)

        train_columns=list(train.columns)
        

        for i in range(len(train_columns)):

                if not (test_columns[i]==train_columns[i]) and (train[i].dtype==test[i].dtype):

                    status=False
                    with open(self.config.status_file,"w") as file:
                        file.write(f" STATUS IS :  {status} ")

                        return   logger.info(f"Data validation is unsucessfull at column {test_columns[i]}")


        status=True
        with open(self.config.status_file,"w") as file:
            file.write(f" STATUS IS : {status}")

            return    logger.info(f"Data validation is success ")
            



