# Building a application as a package so that it can be used by other also
from setuptools import find_packages,setup
setup(
    name="Mlproject1",version=1.0,author="AryanChauhan",
    author_email="aryanchauhan0276@gmail.com",
    packages=find_packages(),
    install_requires=['pandas','numpy','seaborn']
    )
