import codecs
from setuptools import setup, find_packages


with codecs.open('README.md', 'r', 'utf8') as reader:
    long_description = reader.read()


with codecs.open('requirements.txt', 'r', 'utf8') as reader:
    install_requires = list(map(lambda x: x.strip(), reader.readlines()))


setup(
    name='wiki-dump-reader',
    version='0.0.4',
    packages=find_packages(),
    url='https://github.com/CyberZHG/wiki-dump-reader',
    license='MIT',
    author='CyberZHG',
    author_email='CyberZHG@gmail.com',
    description='Extract corpora from Wikipedia dumps',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=install_requires,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
