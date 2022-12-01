from distutils.command import install_data
from typing_extensions import Required
from setuptools import setup, find_packages

setup(
   name='snowflake',
   version='1.0',
   description='A useful module',
   author='Mohsin',
   author_email='meghani.mohsin@gmail.com',
   packages=find_packages(),
   install_requires= Required
)