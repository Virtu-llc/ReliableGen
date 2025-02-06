from setuptools import setup, find_packages

setup(
    name="reliable-gen",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        'openai>=1.50.0',
    ]
)