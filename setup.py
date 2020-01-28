from setuptools import setup, find_packages


with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name='eisen',
    version="0.1.1",
    description='Eisen Meta Package (installs all components of Eisen)',
    packages=find_packages(),
    install_requires=install_requires,
)