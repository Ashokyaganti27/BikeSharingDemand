
from setuptools import find_packages,setup
from typing import List

def get_requirements(path)->List[str]:
    requirments:List[str]=[]
    try:
        with open(path,"r") as  file:
        # read lines from file
          lines=file.readlines()
          for line in lines:
            requirment=line.strip()

            if requirment and requirment!="-e .":
               requirments.append(requirment)
    except FileNotFoundError:
       print("path is not found")

    return requirments

setup(
   name="BikeSharingDemand",
   version="0.1.1",
   author="Yaganti Ashok",
   author_email="yagantiashok177@gmail.com",
   packages=find_packages(),
   install_requires=get_requirements()

)
