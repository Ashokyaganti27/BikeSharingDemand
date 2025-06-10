from pathlib import Path
import os
from ensure import ensure_annotations
from box import ConfigBox
import yaml
from exception.exception import BikeSharingDemand
from logging_part.logger import logger

@ensure_annotations
def read_yaml(path:Path)->ConfigBox:
    try :
        with open(path) as file:
            content=yaml.safe_load(file)

            if content is None:
                content={}

            return ConfigBox(content)
    except Exception as e:
        raise BikeSharingDemand(e)

@ensure_annotations
def create_directories(folders:list,verbose=True):

    for folder in folders:

        os.makedirs(folder,exist_ok=True)
        
        if verbose:
            logger.info(f"folder is created {folder}")
