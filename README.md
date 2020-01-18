# Requirements

1) Filter memes based on which ones have over 60,000
2) Sum all of the points on the retrieved memes
3) Determine the minimum amount of points needed to become a top X meme

# Implementation

Python has a built in module for reading json. Using the requests library, a call is made to the provided API and the data is read using the module. Then, most of these problems can be tackled with various Python list comprehensions. 

# Getting Started
###### These instructions were written for Ubuntu. Your experience may vary.

Clone the repo and navigate to the root folder. 

~~~~
$ git clone git@github.com:keving3ng/rbc-meme-challenge.git
$ cd rbc-meme-challenge
~~~~
OR
~~~~
$ git clone https://github.com/keving3ng/rbc-meme-challenge.git
$ cd rbc-meme-challenge
~~~~

Create a virtualenv, name it 'venv', and activate it.
~~~~
$ virtualenv venv
$ source venv/bin/activate
~~~~

Install the requirements using pip
~~~~
$ pip install -r requirements.txt
~~~~

To run the functions with a demo scenario:
~~~~
$ src/meme_filter.py
~~~~

# Unit Testing

You may have to install pytest on your own.
~~~~
$ pip install pytest
OR
$ sudo apt install python-pytest
~~~~

Unit tests are written in pytest. To run the pytest, run the following command

~~~~
$ pytest
~~~~

From the root folder, pytest will recursively find all the unit tests. The folder structure is important as pytest will use it to find the file in the source folders.
