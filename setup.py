from setuptools import setup

setup(
    name='wiki-dump-reader',
    version='0.0.3',
    packages=['wiki_dump_reader'],
    url='https://github.com/CyberZHG/wiki-dump-reader',
    license='MIT',
    author='CyberZHG',
    author_email='CyberZHG@gmail.com',
    description='Extract corpora from Wikipedia dumps',
    long_description=open('README.rst', 'r').read(),
    install_requires=[],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
