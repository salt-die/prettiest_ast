from setuptools import setup

# Description from README.md
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='prettiest_ast',
      version='0.0.1.dev1',
      url='https://github.com/salt-die/prettiest_ast',
      author='salt-die',
      author_email='saltdie.py@gmail.com',
      license='MIT',
      packages=['prettiest_ast'],
      long_description=long_description,
      long_description_content_type='text/markdown')