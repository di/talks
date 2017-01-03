# Title
Understanding Python's Simplest Edge Cases

# Description
In this talk, we'll discuss a few edge cases, and use them to explore the behaviors of some fundamental Python internals, including `zip`, `max`, `min`, and more. Even the simplest functions you think you know well may behave in ways you might not expect.

# Who and Why (Audience)
This talk is for novices who may not be aware of some quirks which can occur with a number of Python builtins. It should also be interesting to experienced Pythonistas who might not have experienced these firsthand.

This talk assumes the audience has some familiarity with Python builtins such as `min`, `max`, `len`, `set`, `list`, `zip`, etc., but will also explain them

After watching the talk, the atendees should understand how these edge cases, which seem like quirks, are actuall the language operating as intended.  Furthermore, they should have a better understanding of the mechanics behind some of Python's most widely used functions.

# Outline
- Introduction, who am I? (1 min)
- What are edge cases? (2 min)
- The edge cases:
  - Edge case #0: When `x != x` (3 min)
    - Introducing NaN
    - Producing NaN
    - Using NaN
  - Edge case #1: `min()` and `set()` (5 min)
    - Implementing `min()`
    - Overloaded comparators
  - Edge case #2: Disagreeing `count()` and `len()` (5 min)
    - Implementing `count()`
    - Counting empty strings
  - Edge case #3: Significance of order of operations (3 min)
    - Multiplying lists by integers
  - Edge case #4: When string comparison fails (3 min)
    - Lexiographic ordering
    - Zipping empty iterables
  - Edge case #5: More `min()` weirdness (3 min)
    - The unpacking the arguments to `min()`
  - Edge case #6: Comparators vs. `in` (3 min)
    - Using `in` with strngs vs. lists
- One last thing (1 min)
- Thanks (1 min)

# Additional notes

This talk is a variation of a talk I gave at PyGotham 2016 (<https://2016.pygotham.org/talks/363/wat-mind-bending-edge-cas/>) (and a number of times before, including at the Philadelphia Python Users Group).

I talk about Python in some form at least once a month, and some of my previous Python talks have included "Detecting Asteroids with Neural Networks", "wat?  Mind-bending Edge-cases in Python" (PyGotham 2016) and "What Is and What Can Be: An Exploration from `type` to Metaclasses" (PyCon 2016), which was described by one attendee as "the most concise and understandable discussion of metaclasses I've heard" (<https://twitter.com/amylouboyle/status/737707897270865925>).

I have been a professional Python developer for more than ten years and have authored a number of small open-source projects (<https://github.com/di>) including a number of Python packages (<https://pypi.org/user/di/>).

I'm a member of the Python Packaging Working Group, the Python Packaging Authority (<https://github.com/orgs/pypa/people)> and a maintainer of the Warehouse project (<https://pypi.org/>).
