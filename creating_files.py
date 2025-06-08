import os
from pathlib import Path

PROJECT_NAME="BikeSharingDemand"

list_of_files=[
    "artifacts/",
    "notebooks/EDA.ipynb",
    "config/__init__.py",
    "config/config.yaml",
    "config/params.yaml",
    "config/schema.yaml",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/entity/config_entity.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/components/Data_Ingestion.py",
    f"src/{PROJECT_NAME}/components/Data_Validation.py",
    f"src/{PROJECT_NAME}/components/Data_Transformation.py",
    f"src/{PROJECT_NAME}/components/Model_Training.py",
    f"src/{PROJECT_NAME}/components/Model_Evaluation.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/pipeline/training_pipeline.py",
    f"src/{PROJECT_NAME}/pipeline/prediction_pipeline.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/common.py",
    "templates/index.html",
    "Dockerfile",
    "app.py",
    "setup.py",
    
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)

    if  (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):

        with open(filepath,"w"):
            pass

