from setuptools import (setup, find_packages)

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='Percentile tool',
      version='1.0',
      url='https://github.com/m-felices/percentile-tool/',
      author='Marta Felices',
      author_email='martafm@gmail.com',
      description='It is a python utility to get the taxi rides in NYC dataset over a specified percentile.',
      python_requires='>=3.9',
      packages=find_packages(),
      install_requires=['pandas==1.4.2', 'pyarrow==8.0.0', 'numpy==1.22.4']
      )
