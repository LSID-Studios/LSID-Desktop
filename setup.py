# setup.py
from setuptools import setup, find_packages

setup(
    name='lsid-desktop',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'lsid-desktop = lsid-desktop.func:main',
        ],
    },
)