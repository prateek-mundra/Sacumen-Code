import setuptools
from setuptools import setup, find_packages

with open("README.md", 'r') as fh:
    long_description = fh.read()

setup(
    name='testConfig',
    version='1.0.0',
    author="Prateek Mundra",
    author_email="prateekmundra123@gmail.com",
    description="Package to create module",
    long_description=long_description,
    long_description_content_type="text",
    packages=find_packages(include=['testWheel']),
    python_requires='>=3.7',
    install_requires=['pyyaml', 'pytest']
    # packages=['testWheel'],
)

"""
The name parameter contains the name of the package, the version is the version number.
The packages parameter is a list containing the names of files/ directories or packages.
"""