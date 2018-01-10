# Additional Notes

This talk is the result of of my experiences ...

I love to talk about Python and software development in general. I've given talks at PyCon for the last two years, and I also speak frequently at regional Python conferences, including PyGotham, PyTexas, Florida Py. I also speak at local user groups when I can, and have had talks accepted at conferences including PyCon Canada and PyCarribean. Links to my previous talks, slides and videos can be found here: <https://di.codes/speaking>

My PyCon 2016 talk was described by one attendee as "the most concise and understandable discussion of metaclasses I've heard" (<https://twitter.com/amylouboyle/status/737707897270865925>).

I have been a professional Python developer for over ten years and have authored a number of small open-source projects (<https://github.com/di>) including a number of Python packages (<https://pypi.org/user/di/>).

I'm a member of the Python Packaging Working Group, the Python Packaging Authority (<https://github.com/orgs/pypa/people)> and a maintainer of the Warehouse project (<https://pypi.org/>).

---

# Title

* How to contribute to open source
* Everything They Told You About Contributing To Open Source Was Wrong

# Description

Making your first open source contribution isn't hard. What's hard is becoming an engaged contributor for an active project, and making meaningful and important changes that have a lasting effect.

In this talk, we'll dissect the most common pieces of advice that are given with regards to becoming an open source contributor, and why they can be problematic. We'll look at a few examples of how an attempt to contribute can go wrong on so, so many levels, and what can be learned from them.

# Who and Why

This talk is for anyone who has wanted to contribute to an open source project but isn't sure how, anyone who has tried to contribute but has failed, or anyone who actively contributes but wants to become more effective.

This talk only requires a background knowledge of how open source software works (that it's community driven, volunteer-based, etc).

After watching this talk, attendees should feel empowered to become meaningful contributors to at least one open source project of their choosing.

# Outline

* Introduction (2 min)
  - Who am I?
  - Everything they told you was wrong
* How I learned the hard way
  - The issue with "good first issues" (3 min)
  - Open-sourcing your projects (3 min)
  - Drive-by contributions (5 min)
  - Stunts & Ego (5 min)
* The one true way
  - The importance of context (2 min)
  - In search of meaning (3 min)
  - Micro-contributions (2 min)
* Lessons Learned (4 min)
  - No drive-bys
  - No stunts
  - Pay attention
  - Focus on what you know
* Conclusion (1 min)


---

# Title

* Search is Hard!

# Description

Adding the ability to search is possibly one of the easiest-to-request features for a software project, but can be considered one of the hardest to implement -- and even harder to get right!

In this talk, we'll implement an extremely naive text search engine from scratch, and then add different search techniques in an attempt to improve the quality of the results. We'll discuss different ways to measure quality of a search algorithm, as well as methods for optimization.

# Who and Why

This talk is for anyone who has used a search engine and has wondered how it works, as well as for developers who have needed to implement some form of search in their projects and have needed to understand the trade offs and the complexity that comes with different search techniques.

This talk requires that the audience understand the motivation for needing search, and a general idea for what it might take for a search algorithm to work correctly, as well as a novice-level experience with Python.

After watching this talk, attendees should have a greater understanding for the complexity of search, some specific understanding for different search techniques and how they work, as well as when to use them and when what they've got is good enough.

# Outline

* Introduction (1 min)
  - Who am I?
* Search is Hard! (3 min)
  - Why search sounds easy
  - Why we miss the complexity
* Measuring quality (3 min)
  - Precision vs Quality
  - False Positives
* Search Techniques
  - Native Approach (4 min)
    * Serial Scanning
  - Indexing vs Searching (3 min)
  - Keyword Search (4 min)
  - Tokenization (5 min)
    * Stemming
    * Lemmatization
    * Filters
    * Stop Words
  - Controlled Vocabulary (3 min)
  - Concept Search (3 min)
* Conclusion (1 min)

---

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

---

# Title

* Anatomy of a Feature
* Embracing the Glacial Pace of Open Source Software
* Embrace the Glacier: Why Open Source Moves So Slowly

# Description

Sometimes it feels like Open Source Software moves an excruciatingly slow pace. Bug reports languish, feature requests acquire +1's and thumbs up but never get shipped. Is this project dead, or are the maintainers just ignoring their users?

In this talk, we'll examine how a seemingly simple feature can become unbelievably complex and take an incredible amount of coordination to finish, taking multiple years from conception to completion.

We'll look at one of the most popular and oft-requested features for the Python Package Index, and dig in to see why it's taken so long to implement. Along the way, we'll develop some methods for identifying complexity, as well as a greater understanding for what it takes to make open source work.

# Who and Why

This talk is for the consumers of open source software, to better understand the complexities and challenges of maintaining the projects they use on a daily basis.

This talk only requires a background knowledge of how open source software works (that it's community driven, volunteer-based, etc).

After watching this talk, the audience should have tools for identifying complexity in feature requests, a greater understanding of the mechanics and limitations of large community-driven software projects, and empathy for open-source maintainers.

# Outline

* Introduction (2 min)
  - Who am I?
* How we think open source works (2 min)
* Examples of frustration (3 min)
* A specific example (12 min)
  - Background
  - Why it seems simple
  - What it actually takes
* The Paradoxes (5 min)
  - Feature Complexity Paradox
  - Paradox of Success
  - Community Constraint Paradox
* How to melt the glacier (5 min)
* Conclusion (1 min)

---

# Title

* A Brief History of Data Protection: Policy and Practice
* The Past, Present and Future of Data Protection: Policy and Practice
* Data Protection for Developers: Past, Present, and Future

# Description

In 1970, the German state of Hesse enacted what is widely considered the very first data protection laws. Nearly fifty years later, the European Union is about to implement the strongest, most comprehensive data protection regulation ever, and it's existence will have a rippling effect throughout the entire software industry, not only within the EU, but a global scale as well.

In this talk, we'll examine what the upcoming European regulation means for us as developers, with specific examples of how the existing status quo for data collection, data aggregation and data processing will need to change. When can you collect user's data? What can you collect? What can you do with it?

We'll also explore the most important milestones in the history of data protection, both in policy (the evolution of laws to protect data) and in practice (the advent of technology to better protect data) to see how we got to where we are today.

And finally, we'll take a look at the future of data protection, including what to expect from the upcoming European regulation, and the current challenges we face in the US.

# Who and Why

This talk is for developers who work with data, and want to be knowledgable and current about the latest policies and best practices for protecting their user's data. In addition, this talk is for users of technology themselves, to be able to determine what their rights are with regards to their own data.

The only background knowledge this talk requires is that which almost everyone has: some experience being a user of technology which collects data about them.

After watching this talk, developers should be able to determine if their software projects are affected by the new regulations, and should be informed about how their technology will need to change in order to become compliant with the new laws.

# Outline

* Introduction (2 min)
  - Who am I?
  - What is data?
* History of Data Protection Policy & Practice (8 min)
  - Germany
  - Sweden
  - United Kingdom
* Present Day (7 min)
  - European Union
  - United States
* Imminent: EU General Data Protection Regulation (10 min)
  - Scope
  - Core Rights
  - Examples
* Future (2 min)
* Conclusion (1 min)

---
