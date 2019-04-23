# Title

The Fastest FizzBuzz in the West: Make Your Own Language with RPLY and RPython

# Description
In this talk, you'll learn how I built DIVSPL (Dustin Ingram's Very Special Programming Language), a tongue-in-cheek domain-specific language, which is particularly good for implementing FizzBuzz -- as quickly as possible.

We'll build DIVSPL with RPLY, an implementation of David Beazley's PLY (but with a "cooler" API) and make it compatible with RPython, a restricted subset of the Python programming language. Along the way, you'll learn about lexers, parsers, and grammars, and in the end, you'll know how to build your own language.'

# Who and Why (Audience)

This talk is for anyone who has ever wondered how computers understand programming languages, or how to create your own programming language. It will be approachable for novices who have never studied programming language design, but will offer tools and concepts that will enable experienced users to actually build their own language, if they so desire.

The audience should understand that a programming language consists of a set of symbols and patterns, and that an interpreter determines whether any given set of symbols and patterns is "valid" or "invalid". The audience will NOT need prior experience or knowledge of advanced programming language concepts.

After watching the talk, the novice users in the audience should gain an understanding of how a computer understands a programming language, including programming language concepts such as tokens, lexers, parsers and grammars.  Furthermore, experienced users should be able to implement a very simple DSL of their own using the tools discussed.


# Outline
- Introduction, who am I? (1 min)
- Faux Motivation: A brief introduction to FizzBuzz (1 min)
- Actual Motivation: A brief introduction to language design (1 min)
- Let's design a language (4 min)
    - Parallels to human language
        - Goals
        - Tokens
        - Expressions
    - DIVSPL, a FizzBuzz DSL
        - Goals
        - Tokens
        - Expressions
- Let's make a lexer (8 min)
    - How we "lex" human language
    - How we can "lex" DIVSPL
    - How we can make a lexer
- Let's make a parser (8 min)
    - How we "parse" human language
    - How we can "parse" DIVSPL
        - Let's define our grammar
        - Let's play with boxes
    - How we can make a parser
- Let's make an interpreter (2 min)
- Let's code! (1 min)
- Let's figure out what happened (2 min)
    - Our program
    - How it was tokenized by the lexer
    - How it was structured by the parser
    - How it was evaluated by the interpreter
    - The result
- Let's take it a step further (1 min)
    - Going beyond the basic FizzBuzz problem with DIVSPL
- Thanks (1 min)

# Additional notes

This talk is the result of a now-finished project to create a FizzBuzz DSL in Python (<https://github.com/di/divspl>) and my popular blog post about the project (<https://www.promptworks.com/blog/the-fastest-fizzbuzz-in-the-west>).

I have given this talk a number of times in various forms, including most recently at the Philadelphia Python User's Group (where I have been an active member for a number of years) and it has been well-received.

I talk about Python in some form at least once a month, and some of my previous Python talks have included "Detecting Asteroids with Neural Networks", "wat?  Mind-bending Edge-cases in Python" (PyGotham 2016) and "What Is and What Can Be: An Exploration from `type` to Metaclasses" (PyCon 2016), which was described by one attendee as "the most concise and understandable discussion of metaclasses I've heard" (<https://twitter.com/amylouboyle/status/737707897270865925>).

I have been a professional Python developer for more than ten years and have authored a number of small open-source projects (<https://github.com/di>) including a number of Python packages (<https://pypi.org/user/di/>).

I'm a member of the Python Packaging Working Group, the Python Packaging Authority (<https://github.com/orgs/pypa/people)> and a maintainer of the Warehouse project (<https://pypi.org/>).

Of all the talks I've proposed this year, I would be most excited to give this one at PyCon 2017!
