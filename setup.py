from setuptools import find_packages, setup
import os


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()


version = []
with open("Kronos/version.py", "r") as f:
    for line in f:
        version.append(str(line.strip()))

version = version[0].split("'")[1]

# version go
# version end

setup(
    name='xautomata-kronos',
    python_requires='>=3.8.0',
    version=version,
    packages=find_packages(include=['Kronos*']),
    license='MIT',
    author='Andrea Jacassi',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    author_email='',
    description='',
    url="https://github.com/sherlogic/xautomata-kronos.git",
install_requires=[],
)
