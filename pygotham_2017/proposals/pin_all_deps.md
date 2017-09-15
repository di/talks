# Title
Pin All Dependencies (and let `pip` sort 'em out)

# Description
There are significant advantages to explicitly declaring versions of your dependencies, both to the quality of your software, your developers, and the open source community which makes up your software ecosystem.

In this talk, I'll discuss what dependency pinning is, when it is appropriate to pin your dependencies, why it's a good idea, and how you should do it. I'll be talking about `pip` and it's infamous `requirements.txt`, but also discuss the future of dependency management in the Python ecosystem.

# Who and Why (Audience)
This talk is for Python developers who work on projects which have at least one third-party dependency (i.e., not in the stdlib).

It will approachable for novices, but will also provide suggestions that experienced Pythonistas will be able to take home and apply to their day-to-day work. It will presume that the audience has used `pip` before, and is aware that dependencies can be declared via a `requirements.txt` file.

After watching this talk, attendees will understand how to declare specific versions of dependencies, and when it is important to pin dependencies. They will be able to recognize scenarios when not pinning dependencies can cause issues, and identify advantages to dependency pinning. And, hopefully, they will start pinning their dependencies if they don't already!

# Outline
- Introduction, who am I? (1 min)
- What are dependencies? (2 min)
- How do we declare dependencies? (3 min)
- What is dependency pinning? (4 min)
    - Brief discussion of other ecosystems
    - `pip freeze` is not enough
- Why should you pin your dependencies? (4 min)
    - Scenario #1: A broken new version
    - Scenario #2: An insecure or incompatible old version
- When should you pin a dependency? (4 min)
- When should you _not_ pin a dependency? (4 min)
    - Instance #1: Your software is a third-party module
    - Instance #2: Your software has dependencies that are not deployed
- New problems (4 min)
    - Out of date dependencies in local development environments
    - Out of date dependencies in your requirements files
- Benefits (2 min)
    - Finding bugs quickly
    - Momentum in the ecosystem
- The future: Pipfiles (1 min)
- Thanks (1 min)

# Additional notes

This talk is the result of a blog post on the subject (<https://www.promptworks.com/blog/pin-all-dependencies>).

I talk about Python in some form at least once a month, and some of my previous Python talks have included "Detecting Asteroids with Neural Networks", "wat?  Mind-bending Edge-cases in Python" (PyGotham 2016) and "What Is and What Can Be: An Exploration from `type` to Metaclasses" (PyCon 2016), which was described by one attendee as "the most concise and understandable discussion of metaclasses I've heard" (<https://twitter.com/amylouboyle/status/737707897270865925>).

I have been a professional Python developer for more than ten years and have authored a number of small open-source projects (<https://github.com/di>) including a number of Python packages (<https://pypi.org/user/di/>).

I'm a member of the Python Packaging Working Group, the Python Packaging Authority (<https://github.com/orgs/pypa/people)> and a maintainer of the Warehouse project (<https://pypi.org/>).
