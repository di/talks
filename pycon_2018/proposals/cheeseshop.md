# Title

* Inside the Cheeseshop: How Python Packaging Works
* what is setup.py

# Description

Questions and confusion about the Python packaging ecosystem abound. What is this `setup.py` file? What's the difference between wheels and eggs? Do I use setuptools or distutils? Why should I use twine? Do I put my projects dependencies in a `requirements.txt` or in `setup.py`? How do I just get my module up on PyPI? Wait, what is Warehouse?

This talk will identify the key tools one might encounter when trying to distribute Python software, what they are used for, why they exist, and their history (including where their weird names come from). In addition, we'll see how they all work together, what it takes to make them work, and what the future has in store for Python packaging.

# Who and Why

This talk is for any Pythonista that has been confused by Python Packaging (read: everyone).

This talk requires that the audience has just the slightest familiarity with how Python Packaging works -- that you need to upload your source code, that there are a few popular and familiar tools, and that they are all a little confusing. Attendees do not need to be publishers of Python Packages but likely will be people interested in publishing someday.

After watching this talk, attendees should have a significant amount of their confusion about the Python packaging ecosystem resolved, and should be able to make informed, reasonable decisions when they want to publish a package (without having to be told step by step instructions, or given extremely opinionated advice).

# Outline

* Introduction (2 min)
  - Who am I?
  - What is a package?
* Dependencies (5 min)
  - setup.py
  - requirements.txt
* Distributions (6 min)
  - source
  - eggs
  - wheels
* Publishing (6 min)
  - setuptools
  - twine
  - flit
* The Package Index (4 min)
* The Future (6 min)
  - Pipfiles
  - Warehouse
  - setup.cfg
* Conclusion (2 min)
  - The Python Packaging Guide
  - How to ask for help
