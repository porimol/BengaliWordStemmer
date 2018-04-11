# Bengali Word Stemmer
Bengali word stemming tool


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development, testing purposes and as well as in production machine. See deployment for notes on how to deploy the project on a live system.


## Python Version
Minimum python version should have 3.x.x or upper

## Installing

A step by step series of examples that tell you have to get a development env running


### How do I get set up? ###

Install the virtualenv using this command(If you have not installed virtualenv yet.)

```ssh
$ [sudo] pip install virtualenv
```


Create a directory using the following command from your terminal

```ssh
$ [sudo] mkdir BengaliWordStemmer
```


Switch to BengaliWordStemmer directory

```ssh
$ cd BengaliWordStemmer
```


After then create virtual env file by the following command from your terminal

```ssh
$ virtualenv -p python3 venv
```


If you create virtual env file successfully on your development machine then run this command

```ssh
$ source venv/bin/activate
```

And clone the repo

```ssh
$ git clone https://github.com/porimol/BengaliWordStemmer .
```

Install required packages by running the following command
```ssh
$ pip install -r requirements.txt
```

Its time to run the following command
```ssh
$ python run.py
```

Now you have a local server url. Visit the [http://127.0.0.1:8080/](http://127.0.0.1:8080/)
```ssh
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 285-251-887
 ```


## Live Demo
Please visit the given link
[Bengali Word Stemmer](https://bengaliwordstemmer.herokuapp.com/)