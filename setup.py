from setuptools import setup, find_packages

setup(
    name='fake_package',
    version='0.4.0',
    author='Author Name',
    author_email='author@gmail.com',
    description='Tests for CI',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1'],
)