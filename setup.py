from setuptools import setup, find_packages

setup(name='pydota',
    version='0.1',
    url="https://github.com/Moeez-Muhammad/pydota.git",
    license="MIT",
    author="Moeez Muhammad",
    author_email="mmoeez48@gmail.com",
    description="A python library to issue requests to the OpenDota API as well as provide wrapper utility functions",
    packages=find_packages(),
    long_description=open('README.md').read()
    zip_safe=False)