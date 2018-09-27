from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vis2048',
    version='1.0.2',

    description='Implementation of 2048 with visualization support',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Philipp Ploder',
    url='https://github.com/Fylipp/vis2048',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    keywords='2048 visualization',

    packages=['vis2048']
)
