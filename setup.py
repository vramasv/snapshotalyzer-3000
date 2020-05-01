from setuptools import setup

setup(
    name = 'snapshotalyzer-3000',
    version = '0.1',
    author ="Venky Ram",
    author_email="vrlearnpython@gmail.com",
    description ="Tool to manage EC2 snapshots",
    license ="GPLv3+",
    packages =['shotty'],
    url = "https://github.com/vramasv/snapshotalyzer-3000",
    install_requires =[
    'click',
    'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty = shotty.shotty:cli
        ''',
)
