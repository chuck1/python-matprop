import re
from setuptools import setup

with open('matprop/__init__.py') as f:
    version = re.findall("^__version__ = '(.*)'", f.read())[0]

setup(name='matprop',
        version=version,
        description='python makefile system',
        url='http://github.com/chuck1/matprop',
        author='Charles Rymal',
        author_email='charlesrymal@gmail.com',
        license='MIT',
        packages=[
            'matprop',
            ],
        zip_safe=False,
        )

