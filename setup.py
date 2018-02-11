# coding=utf-8
import sys


# if python version less than 3
if sys.version_info < (3, 4):
    print(sys.stderr, "{}: need Python 3.4 or later.".format(sys.argv[0]))
    print(sys.stderr, "Your Python is {}".format(sys.version))
    sys.exit(1)


from setuptools import setup, find_packages


setup(
    name='BengaliWordStemmer',
    version='1.0.1',
    install_requires = [],
    package_dir = {
        '': 'src'
    },
    packages = find_packages('src', exclude='tests'),
    url='https://bengaliwordstemmer.herokuapp.com',
    license='MIT License',
    author='Porimol Chandro',
    author_email='porimolchandroroy@gmail.com',
    description='Bengali word stemming tool',
    keywords = [
        'NLP',
        'Python',
        'Bengali Stemmer',
        'Stemming',
        'Word Stemmer',
        'Bengali Word Stemmer'
    ],
)
