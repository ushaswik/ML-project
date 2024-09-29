from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str) ->List[str]:
    '''
    this function will return thelist of requirements 
    '''
    HYPEN_DOT='-e .' 
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace("\n","") for req in requirements]
        
        if HYPEN_DOT in requirements:
            requirements=file_obj.readlines()
            requirements=[req.replace('\n',"") for req in requirements]

 
setup(
name="mlproject",
version='0.0.1',
author="ushaswi",
author_email="ushaswikurmala@gmail.com",
packages=find_packages(),
install_requires=('requirements.txt')
)
