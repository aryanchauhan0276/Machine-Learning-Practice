from setuptools import setup,find_packages
from typing import List
HYPEN_E_DOT="-e ."

def get_requirements()->List[str]:
    lines:List[str]=[]
    """ This function return list of requirements"""
    try:
        with open("requirements.txt","r") as file:
            lines=file.readlines()
            lines=[line.strip() for line in lines]

            if HYPEN_E_DOT in lines:
                lines.remove(HYPEN_E_DOT)
        print(lines)
        return lines

    except FileNotFoundError:
        print("Requirements.txt Not Found")
setup(
    name="Project2-NetworkSecurity",
    version="0.0.1",
    author="Aryan Chauhan",
    packages=find_packages(),
    install_requires=get_requirements()
)