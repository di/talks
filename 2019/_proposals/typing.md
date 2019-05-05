# Title

* Static Typing in Python

# Description

Python is well-known as a programming language without static types. This means that you don't need to say what a given variable will hold, or whether your function will return a string or an integer (or sometimes one, and sometimes another!). This has historically made Python a very flexible and beginner-friendly language.

In this talk, we'll discuss the advantages and disadvantages to a static type system, as well as recent efforts to introduce static typing to Python via optional "type hints" and various tools to aid in adding types to Python code. We'll see what this means for Python, for Python programmers, and what the future has in store for Python's type system.

# Audience

This talk is for Python programmers who either don't know what static typing is, don't know why why they might want it, or who do have some understanding, but aren't sure what benefits they might get by adding type annotations to their code.

Attendees should know that there is a distinction between typed and untyped code, and understand what some types (list, int, string, etc) are, but don't need to know exactly what static typing is or have direct experience with typed code.

After watching this talk, attendees should understand that Python is untyped by default but can be typed. They should understand the class of problems that adding type annotations seeks to alleviate, and some tools they can use to add and check type annotations.

# Outline

* About types (4 min)
  * Types of type systems
  * Advantages of static typing
  * Disadvantages of static typing
* Types in other languages (3 min)
  * C
  * Ruby
  * JavaScript
  * Go
* Types in Python (10 min)
  * How Python did/does typing
  * The `type` function
  * PEP 484: Type Hints
  * The `typing` module
  * Tools
    * mypy
    * pytype
* The great benefits to static typing in Python (6 min)
  * Static code analysis
  * More documentation
  * Code completion
* The disadvantages to static typing (4 min)
* The challenges of static typing (3 min)
