
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()


setup(
    name = 'hello-cli',
    version = '0.0.2',
    author = 'Sharhan Alhassan',
    author_email = 'sharhanalhassan@gmail.com',
    license = 'MIT',
    description = 'A simple python CLI tool built with click',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/sharhan-alhassan/python-click-cli',
    py_modules = ['hello'],
    install_requires = [requirements],
    python_requires ='>=3.7',
    classifiers = [
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        cooltool=hello:cli
    '''
)
