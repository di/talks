## _The_
# Fastest FizzBuzz
## _in the_
# West

^ So I'm sure almost everyone's heard of FizzBuzz

^ If you haven't, FizzBuzz is a mythical interview question to see how well you can write code in an environment in which you will never actually write code

^ The goal is to sufficiently intimidate junior developers so they will know to steer clear of your organization

^ It also has the nice effect of offending senior developers too.

^ So it's great for quickly narrowing down your hiring pipeline.

---

# FizzBuzz

> "Write a program that prints the numbers 1 through `n`, however
> for every number divisible by 3, print `'fizz'` and for every
> number divisible by 5, print `'buzz'`. If a number is divisible by
> both 3 and 5, print `'fizzbuzz'`."

^ The general idea is ...

^ If you gave me this question in an interview, I might ask "Can I use python"

^ And if you said yes, I might write something like this:

---

# Oh come on

```python
>>> def fizzbuzz(n):
...    for i in range(1, n+1):
...        if i % 15 == 0:
...            print 'fizzbuzz'
...        elif i % 3 == 0:
...            print 'fizz'
...        elif i % 5 == 0:
...            print 'buzz'
...        else:
...            print i
...
```

^ (explain)

---

```python
>>> fizzbuzz(15)
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
```

^ And that might output the correct result

---

# NO FUN

^ But that's no fun!

---

# DIVSPL
##

^ Which is why I created my own programming language

---

# DIVSPL
## (Dustin Ingram's Very Special Programming Language)

^ AKA

^ Really well suited for implementing fizzbuzz

^ I'm going to show you how I built it

---

# RPLY

* RPLY: <https://github.com/alex/rply>
    * RPython: <https://en.wikipedia.org/wiki/PyPy#RPython>
    * PLY: <http://www.dabeaz.com/ply/>
        * Lex: <https://en.wikipedia.org/wiki/Lex_(software)>
        * Yacc: <https://en.wikipedia.org/wiki/Yacc>

^ DIVSPL is built with RPLY

^ RPLY is an implementation of PLY compatible with RPython (and with a cooler API)

^ RPython is a restricted subset of Python

^ PLY is a Python implementation of the Lex and Yacc tools

^ Lex is unix tool which generates lexical analyzers

^ Yacc is a parser generator, aka "Yet Another Compiler Compiler"

^ Got that?

---

# Let's make a lexer

^ The lexer is simple: It takes a stream of characters

^ And gives an iterator which provides tokens from the language

---

# Let's make a lexer

```python
>>> from rply import LexerGenerator
>>> lg = LexerGenerator()
>>>
```

^ Create a new LexerGenerator

^ We'll add some rules for our language as named regular expressions

---

# Let's make a lexer

```python
>>> from rply import LexerGenerator
>>> lg = LexerGenerator()
>>> lg.add("ELLIPSIS", r"\.\.\.")
>>>
```

^ An Ellipsis token is a series of three literal periods

---

# Let's make a lexer

```python
>>> from rply import LexerGenerator
>>> lg = LexerGenerator()
>>> lg.add("ELLIPSIS", r"\.\.\.")
>>> lg.add("NUMBER", r"\d+")
>>>
```

^ A number token is any numeric characters in a sequence

---

# Let's make a lexer

```python
>>> from rply import LexerGenerator
>>> lg = LexerGenerator()
>>> lg.add("ELLIPSIS", r"\.\.\.")
>>> lg.add("NUMBER", r"\d+")
>>> lg.add("EQUALS", r"=")
>>>
```

^ An assignment token is the equals sign

---

# Let's make a lexer

```python
>>> from rply import LexerGenerator
>>> lg = LexerGenerator()
>>> lg.add("ELLIPSIS", r"\.\.\.")
>>> lg.add("NUMBER", r"\d+")
>>> lg.add("EQUALS", r"=")
>>> lg.add("WORD", r"[a-z]+")
>>>
```

^ A word token is any alphabetical characters in a sequence

---

# Let's make a lexer

```python
>>> from rply import LexerGenerator
>>> lg = LexerGenerator()
>>> lg.add("ELLIPSIS", r"\.\.\.")
>>> lg.add("NUMBER", r"\d+")
>>> lg.add("EQUALS", r"=")
>>> lg.add("WORD", r"[a-z]+")
>>> lg.ignore(r"\s+")  # Ignore whitespace
>>>
```

^ Because we're cool we won't care about whitespace characters

---

# Let's make a lexer

```python
>>> from rply import LexerGenerator
>>> lg = LexerGenerator()
>>> lg.add("ELLIPSIS", r"\.\.\.")
>>> lg.add("NUMBER", r"\d+")
>>> lg.add("EQUALS", r"=")
>>> lg.add("WORD", r"[a-z]+")
>>> lg.ignore(r"\s+")  # Ignore whitespace
>>> lg.ignore(r"#.*\n")  # Ignore comments
>>>
```

^ Because we're good devs we'll allow for comments, which is anything between a pound sign and a newline character

---

# Let's make a lexer

```python
>>> from rply import LexerGenerator
>>> lg = LexerGenerator()
>>> lg.add("ELLIPSIS", r"\.\.\.")
>>> lg.add("NUMBER", r"\d+")
>>> lg.add("EQUALS", r"=")
>>> lg.add("WORD", r"[a-z]+")
>>> lg.ignore(r"\s+")  # Ignore whitespace
>>> lg.ignore(r"#.*\n")  # Ignore comments
>>> lexer = lg.build()
>>>
```

^ And finally we'll build our lexer

---

# Let's make a lexer

```python
>>> iterator = lexer.lex('...foo42hut=')
>>>
```


---

# Let's make a lexer

```python
>>> iterator = lexer.lex('...foo42hut=')
>>> iterator.next()
Token('ELLIPSIS', '...')
>>>
```

^ So every time we call next on it

---

# Let's make a lexer

```python
>>> iterator = lexer.lex('...foo42hut=')
>>> iterator.next()
Token('ELLIPSIS', '...')
>>> iterator.next()
Token('WORD', 'foo')
>>>
```

---

# Let's make a lexer

```python
>>> iterator = lexer.lex('...foo42hut=')
>>> iterator.next()
Token('ELLIPSIS', '...')
>>> iterator.next()
Token('WORD', 'foo')
>>> iterator.next()
Token('NUMBER', '42')
>>>
```

---

# Let's make a lexer

```python
>>> iterator = lexer.lex('...foo42hut=')
>>> iterator.next()
Token('ELLIPSIS', '...')
>>> iterator.next()
Token('WORD', 'foo')
>>> iterator.next()
Token('NUMBER', '42')
>>> iterator.next()
Token('WORD', 'hut')
>>>
```

---

# Let's make a lexer

```python
>>> iterator = lexer.lex('foobar!')
>>>
```

^ If our stream has invalid tokens

---

# Let's make a lexer

```python
>>> iterator = lexer.lex('foobar!')
>>> iterator.next()
Token('WORD', 'foobar')
>>>
```

^ It works, until

---

# Let's make a lexer

```python
>>> iterator = lexer.lex('foobar!')
>>> iterator.next()
Token('WORD', 'foobar')
>>> iterator.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "lexer.py", line 53, in next
    raise LexingError(...)
rply.errors.LexingError
>>>
```

^ We get to a token the lexer doesn't understand

---

# Let's make a parser

^ Specifically, we're going to make a Look-Ahead Left-Right parser

^ You might have thought what we just did was considered "parsing", but it's not!

^ That's why it's called lexing

^ The parser will take the token stream from the lexer

^ and separate and analyze the tokens according to a set of production rules specified by a formal grammar

^ Let's define our grammar

---

# Let's make a parser

_range_ ⟶ NUMBER ELLIPSIS NUMBER

---

# Let's make a parser

_range_ ⟶ NUMBER ELLIPSIS NUMBER
_assignment_ ⟶ WORD EQUALS NUMBER

---

# Let's make a parser

_range_ ⟶ NUMBER ELLIPSIS NUMBER
_assignment_ ⟶ WORD EQUALS NUMBER
_assignments_ ⟶ _assignments_ _assignment_

---

# Let's make a parser

_range_ ⟶ NUMBER ELLIPSIS NUMBER
_assignment_ ⟶ WORD EQUALS NUMBER
_assignments_ ⟶ _assignments_ _assignment_
_assignments_ ⟶ 𝜀

---

# Let's make a parser

_range_ ⟶ NUMBER ELLIPSIS NUMBER
_assignment_ ⟶ WORD EQUALS NUMBER
_assignments_ ⟶ _assignments_ _assignment_
_assignments_ ⟶ 𝜀
_main_ ⟶ _range_ _assignments_

---

# Let's make a parser

```python
>>> from rply import ParserGenerator
>>> pg = ParserGenerator([
...   "ELLIPSIS",
...   "EQUALS",
...   "NUMBER",
...   "WORD"
... ])
>>>
```

^ We get a ParserGenerator from rply, and initialize it with our list of tokens

---

# Let's make a parser

_range_ ⟶ NUMBER ELLIPSIS NUMBER

```python
>>> @pg.production("range : NUMBER ELLIPSIS NUMBER")
... def range_op(p):
...     return RangeBox(int(p[0].value), int(p[2].value))
...
>>>
```

^ This is how we define our rule in python

^ You might notice the RangeBox

---

## Python `!=` Statically Typed
## RPython `==` Statically Typed

^ One quick difference between Python and RPython

---

# Let's make a parser

```python
>>> class RangeBox(BaseBox):
...     def __init__(self, low, high):
...         self.low = low
...         self.high = high
...     def eval(self):
...         return range(self.low, self.high + 1)
...
>>>
```

---

# Let's make a parser

```python
>>> box = RangeBox(1, 3)
<__main__.RangeBox object at 0x1046ba650>
>>>
```

---

# Let's make a parser

```python
>>> box = RangeBox(1, 3)
<__main__.RangeBox object at 0x1046ba650>
>>> box.eval()
[1, 2, 3]
>>>
```

---

# Let's make a parser

_assignment_ ⟶ WORD EQUALS NUMBER

```python
>>> @pg.production("assignment : WORD EQUALS NUMBER")
... def assignment_op(p):
...     return AssignmentBox(p[0].value, int(p[2].value))
...
>>>
```

---

# Let's make a parser

```python
>>> class AssignmentBox(BaseBox):
...     def __init__(self, word, number):
...         self.word = word
...         self.number = number
...     def eval(self, i):
...         if not i % int(self.number):
...             return self.word
...         return ''
>>>
```

---

# Let's make a parser

```python
>>> box = AssignmentBox('foo', 7)
>>> box.eval(40)
''
>>> box.eval(42)
'foo'
>>>
```

---

# Let's make a parser

_assignments_ ⟶ _assignments_ _assignment_
_assignments_ ⟶ 𝜀

```python
>>> @pg.production("assignments : assignments assignment")
... @pg.production("assignments : ")
... def expr_assignments(p):
...     if p:
...         return p[0] + [p[1]]
...     return []
...
>>>
```

^ Doesn't need a box, it's just a list

---

# Let's make a parser

_main_ ⟶ _range_ _assignments_

```python
>>> @pg.production("main : range assignments")
... def main(p):
...     return ProgramBox(p[0], p[1])
...
>>>
```

---

# Let's make a parser

```python
>>> class ProgramBox(BaseBox):
...     def __init__(self, range_box, assignment_boxes):
...         self.range_box = range_box
...         self.assignment_boxes = assignment_boxes
...
```

---

# Let's make a parser

```python
...     def eval(self):
...         return "\n".join(
...             "".join(
...               assignment.eval(i)
...               for assignment in self.assignment_boxes
...             ) or str(i)
...             for i in self.range_box.eval()
...         ) + "\n"
...
>>>
```

^ Evals the range box

^ For every integer in the range

^ Eval every assignment box and concatenate the results

^ If the result is an empty string, cast the integer to a string instead

^ Join the results with newlines and return!

---

# Let's make a parser

```python
>>> parser = pg.build()
```

---

# Let's make an interpreter

^ What does an interpreter do?

---

# Let's make an interpreter

```python
>>> def main():
...     if len(sys.argv) > 1:
...         with open(sys.argv[1], 'r') as f:
...             result = parser.parse(lexer.lex(f.read()))
...             sys.stdout.write(result.eval())
...     else:
...         sys.stdout.write("Please provide a filename.")
...
>>>
```

^ Reads in a file

^ Hands the character stream to the lexer

^ Lexer hands the token stream to the parser

^ Parser returns a result

^ We evaluate and print the result


---

# LIVECODING!

^ So now we have an interpreter, let's write some code!

^ Why don't we, oh I don't know, implement fizzbuzz!
