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
