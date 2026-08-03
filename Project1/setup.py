# Building a application as a package so that it can be used by other also on PyPi
from setuptools import find_packages,setup
from typing import List
hyphem='-e .'
def get_req(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines() #\n will get added
        requirments=[req.replace("\n","") for req in requirments]
        if hyphem in requirments:
            requirments.remove(hyphem)
    return requirments
         
setup(
    name="Mlproject1",version="1.0",author="AryanChauhan",
    author_email="aryanchauhan0276@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_req("requirments.txt")
    )
