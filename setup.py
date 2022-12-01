from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
   name='snowflake',
   version='1.0',
   description='A useful module',
   author='Mohsin',
   author_email='meghani.mohsin@gmail.com',
   packages=find_packages(),
   install_requires= required
)