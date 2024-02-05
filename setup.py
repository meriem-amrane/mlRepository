from setuptools import find_packages,setup
from typing import List
Hypehn_e = '-e .'
def get_requirments(file_path:str)->List[str]:
    
    requirments=[]
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n","") for req in requirments]
        if Hypehn_e in requirments:
            requirments.remove(Hypehn_e)
setup(
    name='mlprojects',
    version='0.0.1',
    author='Meriem',
    packages=find_packages(),
    install_requires=get_requirments('requerments.txt')
    
)