import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime("%m-%d-%y_%H-%M--%p")}.log"

log_path=os.path.join(os.getcwd(),"log",LOG_FILE)

os.makedirs(log_path,exist_ok=True)

filepath=os.path.join(log_path,LOG_FILE)


logging.basicConfig(
    filename=filepath,
    format="[ %(asctime)s ] %(lineno)d-%(name)s-%(levelname)s-%(message)s",
    level=logging.INFO
)

logger=logging.getLogger("BikeSharingDemand")
