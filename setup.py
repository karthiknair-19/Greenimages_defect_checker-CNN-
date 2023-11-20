from setuptools import setup,find_packages
from typing import List

def get_requirements(filepath:str)->List[str]:
    list1=[]
    with open(filepath)as f:
        requirements=f.read().splitlines()
    
    for req in requirements:
        req=req.replace('\n','')
        list1.append(req)
        
    if "-e ." in list1:
        list1.remove('-e .')
    
    return list1

setup(
    name="Plant Disease identifier",
    version="0.0.0.1",
    author="Karthik Nair",
    author_email="rajnairkarthik9325@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    )
        