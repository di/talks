![](dumb_face.png)

# I'm Dustin
## [`http://github.com/di`](http://github.com/di)

---

![](jumbotron-081.jpg)

^ I work at PromptWorks

^ who I'd like to thank for sponsoring my work in the open source community

^ as well as this talk, which I call

---

# [fit] wat‽
## _Mind-Bending_
### _Edge Cases_
#### _(in Python)_

^ So we're going to talk about some `wats` in Python

^ You might ask "what is a wat?"

^ wats are not trick questions

^ wats are not bugs in the language

^ A 'wat' is an edge-case in a language that makes you say:

---

# [fit] wat‽

^ they seem weird, but if you understand why they happen, they make sense

^ we're going to look at ten different wats

^ but to make things interesting, a few are actually impossible

^ and you'll need to decide if they're real or not

---

# [fit] wat #0

^ Let's start with an example to get started

---

# wat #0

```python
>>> x = ...
>>> x == x
False
```


^ The first goal here is to determine if this is possible or not

^ If it is possible, what can we replace the ellipsis with

^ To give us the desired result

^ The missing values in these wats are limited to the built-in primitive types and collections

^ booleans, integers, strings

^ as well as collections like lists and sets, and combinations of these

^ No lambdas, partials, classes, or other tricky business (bytecode)

^ Is it possible?

---

![](possible.png)

---

# wat #0

```python
>>> x = ...
>>> x == x
False
```

^ so if x is equal to

---

# wat #0 - Possible!

```python
>>> x = 0*1e309
>>> x == x
False
```

^ zero times one times ten raised to the 309th power

---

# wat #0 - Possible!

```python
>>> x = 0*1e309
>>> x == x
False
>>> x
nan
```

^ this is because 0*1e309 is interpreted by python as Not A Number

---

# wat #0 - Possible!

```python
>>> x = 0*1e309
>>> x == x
False
>>> x
nan
>>> 0*float('inf')
nan
```

^ This is the same thing as zero times infinity

---

# wat #0 - Possible!

```python
>>> x = 0*1e309
>>> x == x
False
>>> x
nan
>>> 0*float('inf')
nan
>>> float('nan')
nan
```

^ Or just float nan

---

# [fit] NaN

^ A brief word on NaN

^ There's a good reason why nan is not equal to itself, or anything else

^ It's because it's not a number!

^ NaN is designed to propagate through all calculations, so if somewhere in your deep, complex calculations you hit upon a NaN, you don't bubble out a seemingly sensible answer.

^ So because of this, NaN is definitely the source of many wats

---

# A brief word on NaN

This is not Python:

```javascript
> Array(16).join("wat" - 1) + " Batman!"
"NaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaN Batman!"
```

<https://www.destroyallsoftware.com/talks/wat>

^ In fact, it's the star of Gary Bernhardt's infamous talk

^ which is definitely inspiration for this talk

---

# A brief word on NaN

```python
>>> 0*1e309
nan
>>> float('nan')
nan
>>> from decimal import Decimal; Decimal('nan')
Decimal('NaN')
>>> complex('nan')
(nan+0j)
```

^ There are a number of sensible ways to generate a NaN in Python

^ None of them are equal to themselves

^ For the purposes of this talk, none of the "solutions" to the wats involve using a NaN

---

# [fit] wat #1

---

# wat #1

```python
>>> x = ...
>>> a = ...
>>> b = ...
>>> c = ...
>>> max(x) < max(x[a:b:c])
True
```

^ can we create a list x such that when sliced by a, b, and c it has a new max

---

![](not_possible.png)

---

# wat #1 - Not Possible

```python
>>> x = ...
>>> a = ...
>>> b = ...
>>> c = ...
>>> max(x) < max(x[a:b:c])
True
```

^ This wat is impossible

^ This will always compare the list with some subset of the list

^ no matter how you slice it

---

# [fit] wat #2

---

# wat #2

```python
>>> x = ...
>>> y = ...
>>> min(x, y) == min(y, x)
False
```

^ Can we make x and y such that min(x, y) is different than min(y, x)?

^ This wat is possible

---

![](possible.png)

---

# wat #2 - Possible!

```python
>>> x = ...
>>> y = ...
>>> min(x, y) == min(y, x)
False
```

---

# wat #2 - Possible!

```python
>>> x = {0}
>>> y = ...
>>> min(x, y) == min(y, x)
False
```

^ if x is the set containing zero

---

# wat #2 - Possible!

```python
>>> x = {0}
>>> y = {1}
>>> min(x, y) == min(y, x)
False
```

^ and y is the set containing anything but zero

^ Only if x and y are sets, though. Why?

---

# wat #2 - Possible!

```python
>>> min({0}, {1})
set([0])
```

^ If we take the min of the set containing zero, and the set containing one

^ We get the set containing zero

---

# wat #2 - Possible!

```python
>>> min({0}, {1})
set([0])
>>> min({1}, {0})
set([1])
```

^ If we do the opposite, we get the set containing one!

^ Seems like min is broken and just returning the first element

---

# wat #2 - Possible!

```python
>>> min({0}, {1})
set([0])
>>> min({1}, {0})
set([1])
>>> min({0, 1}, {0})
set([0])
```

^ Well, maybe not. What's happening?

^ Let's imagine what the min function might look like

^ If we implemented it in python

---

# wat #2 - Possible!

```python
>>> def min(*args):
...
```

^ The min function can take any number of arguments

^ It finds the min of all of them

^ It can also take just one, an iterator, but let's ignore that for now

---
# wat #2 - Possible!

```python
>>> def min(*args):
...     has_item = False
...     min_item = None
...
```

^ We need two variables

^ has_item tells us if min_item has been set yet

^ min_item holds the smallest item found at any point

---
# wat #2 - Possible!

```python
>>> def min(*args):
...     has_item = False
...     min_item = None
...     for x in args:
...
```

^ We'll iterate through the arguments

---
# wat #2 - Possible!

```python
>>> def min(*args):
...     has_item = False
...     min_item = None
...     for x in args:
...         if not has_item or x < min_item:
...
```

^ If we haven't set min_item yet, or if x is less than min_item

---
# wat #2 - Possible!

```python
>>> def min(*args):
...     has_item = False
...     min_item = None
...     for x in args:
...         if not has_item or x < min_item:
...             has_item = True
...             min_item = x
...
```

^ We set has_item to true and set min_item to x

---
# wat #2 - Possible!

```python
>>> def min(*args):
...     has_item = False
...     min_item = None
...     for x in args:
...         if not has_item or x < min_item:
...             has_item = True
...             min_item = x
...     return min_item
...
```

^ Finally we return the smallest item found

^ This is a really simplified approach -- doesn't handle no args, etc.

^ What's the key? It's that less than operator comparing x to min_item

---

# wat #2 - Possible!

```python
>>> 0 < 1
True
```

^ The less than operator works as you'd expect for something like integers

---

# wat #2 - Possible!

```python
>>> 0 < 1
True
>>> {0} < {1}
False
```

^ But the operator is overloaded for set comparison

^ Meaning it behaves differently for two sets than it would for two ints

---


# wat #2 - Possible!

```python
>>> 0 < 1
True
>>> {0} < {1}
False
>>> {0} < {0, 1}
True
```

^ Specifically, it is the inclusion operator

^ Here, it's checking if what's in the set on the left

^ is included in the set on the right

---

# wat #2 - Possible!

```python
>>> 0 < 1
True
>>> {0} < {1}
False
>>> {0} < {0, 1}
True
>>> min({0}, {1})
set([0])
```

^ So when we call the min on these two one-element sets

^ We will always get the first argument back, regardless

---

# [fit] wat #3

---

# wat #3

```python
>>> x = ...
>>> y = ...
>>> any(x) and not any(x + y)
True
```

^ Can we create two lists x and y such that at least one element in x is true

^ But when appended with y, none of them are true?

^ This wat is impossible

---

![](not_possible.png)

---

# wat #3 - Not Possible

```python
>>> x = ...
>>> y = ...
>>> any(x) and not any(x + y)
True
```

^ This wat is impossible

^ The elements of y have no effect on those in x

^ If anything in x is true, something in x+y will be true as well

---

# [fit] wat #4

---

# wat #4

```python
>>> x = ...
>>> y = ...
>>> x.count(y) > len(x)
True
```

^ This wat is possible

---

![](possible.png)

---

# wat #4 - Possible!

```python
>>> x = ...
>>> y = ...
>>> x.count(y) > len(x)
True
```

^ This wat is possible

---

# wat #4 - Possible!

```python
>>> x = 'foobar'
>>> y = ...
>>> x.count(y) > len(x)
True
```

^ If x is any string

---

# wat #4 - Possible!

```python
>>> x = 'foobar'
>>> y = ''
>>> x.count(y) > len(x)
True
```

^ But only if y is an empty string

---

# wat #4 - Possible!

```python
>>> x = 'foobar'
>>> y = ''
>>> x.count(y) > len(x)
True
>>> len('foobar')
6
```

---

# wat #4 - Possible!

```python
>>> x = 'foobar'
>>> y = ''
>>> x.count(y) > len(x)
True
>>> len('foobar')
6
>>> 'foobar'.count('')
7
```

^ Let's imagine what the count function might look like

---

# wat #4 - Possible!

```python
>>> def count(s, sub):
...
```

^ To make things easy let's just make a function that takes a string s and sub

---


# wat #4 - Possible!

```python
>>> def count(s, sub):
...     result = 0
...
```

^ We initialize the result to return as zero

---

# wat #4 - Possible!

```python
>>> def count(s, sub):
...     result = 0
...     for i in range(len(s) + 1 - len(sub)):
...
```

^ We iterate through all the indexes at which sub could start in s

---

# wat #4 - Possible!

```python
>>> def count(s='foo', sub='foobar'):
...     result = 0
...     for i in range(len(s) + 1 - len(sub)):
...            # range(3 + 1 - 6)
...            # range(-2)
...            # []
```

^ If the substring is larger than the string, we get an empty list of indexes

---

# wat #4 - Possible!

```python
>>> def count(s='foobar', sub='foobar'):
...     result = 0
...     for i in range(len(s) + 1 - len(sub)):
...            # range(6 + 1 - 6)
...            # range(1)
...            # [0]
```

^ If the substring is the same size as string, we get one index, [0]

---

# wat #4 - Possible!

```python
>>> def count(s='foobar', sub='foo'):
...     result = 0
...     for i in range(len(s) + 1 - len(sub)):
...            # range(6 + 1 - 3)
...            # range(4)
...            # [0, 1, 2, 3]
```

^ If the substring is smaller than the string, we get possible start indexes

---

# wat #4 - Possible!

```python
>>> def count(s='foobar', sub=''):
...     result = 0
...     for i in range(len(s) + 1 - len(sub)):
...            # range(6 + 1 - 0)
...            # range(7)
...            # [0, 1, 2, 3, 4, 5, 6]
```

^ But if substring is empty string, we get one more index than the length

---

# wat #4 - Possible!

```python
>>> def count(s, sub):
...     result = 0
...     for i in range(len(s) + 1 - len(sub)):
...         possible_match = s[i:i + len(sub)]
...
```

^ Using the index, we get a slice of the string as our possible match

---

# wat #4 - Possible!

```python
>>> def count(s='foobar', sub='foo'):
...     result = 0
...     for i in range(len(s) + 1 - len(sub)):
...         possible_match = s[i:i + len(sub)]
...                        # s[0:0 + 3]
...                        # s[0:3]
...                        # 'foo'
```

^ When the substring has a length, this gives us a slice the same size

---

# wat #4 - Possible!

```python
>>> def count(s='foobar', sub=''):
...     result = 0
...     for i in range(len(s) + 1 - len(sub)):
...         possible_match = s[i:i + len(sub)]
...                        # s[0:0 + 0]
...                        # s[0:0]
...                        # ''
```

^ When it's empty though, we just get another empty string

---

# wat #4 - Possible!

```python
>>> def count(s='foobar', sub=''):
...     result = 0
...     for i in range(len(s) + 1 - len(sub)):
...         possible_match = s[i:i + len(sub)]
...                        # s[6:6 + 0]
...                        # s[6:6]
...                        # ''
```

^ Slicing also won't raise an IndexError when the index is longer than the string

---


# wat #4 - Possible!

```python
>>> def count(s, sub):
...     result = 0
...     for i in range(len(s) + 1 - len(sub)):
...         possible_match = s[i:i + len(sub)]
...         if possible_match == sub:
...             result += 1
...     return result
...
```

^ Finally if the possible match is the same as the substring

^ We increment the result counter

---

# wat #4 - Possible!

```python
>>> def count(s, sub):
...     result = 0
...     for i in range(len(s) + 1 - len(sub)):
...         possible_match = s[i:i + len(sub)]
...         if possible_match == sub:
...             result += 1
...     return result
...
>>> count('foobar', '')
7
```

^ For an empty string, the range is the indexes 0 through 6, for seven total

^ And the possible_match matches every time! Giving us a count of 7

---

# [fit] wat #5

---

# wat #5

```python
>>> x = ...
>>> y = ...
>>> z = ...
>>> x * (y * z) == (x * y) * z
False
```

---

![](possible.png)

---

# wat #5 - Possible!

```python
>>> x = ...
>>> y = ...
>>> z = ...
>>> x * (y * z) == (x * y) * z
False
```

---

# wat #5 - Possible!

```python
>>> x = [0]
>>> y = ...
>>> z = ...
>>> x * (y * z) == (x * y) * z
False
```

---

# wat #5 - Possible!

```python
>>> x = [0]
>>> y = -1
>>> z = ...
>>> x * (y * z) == (x * y) * z
False
```

---

# wat #5 - Possible!

```python
>>> x = [0]
>>> y = -1
>>> z = -1
>>> x * (y * z) == (x * y) * z
False
```

---

# wat #5 - Possible!

```python
>>> x = [0]
>>> y = -1
>>> z = -1
>>> x * (y * z) == (x * y) * z
False
>>> x * (y * z) == [0]*(-1*-1)
```

---

# wat #5 - Possible!

```python
>>> x = [0]
>>> y = -1
>>> z = -1
>>> x * (y * z) == (x * y) * z
False
>>> x * (y * z) == [0]*(-1*-1) == [0]*1
```

^ A list times one is itself

---

# wat #5 - Possible!

```python
>>> x = [0]
>>> y = -1
>>> z = -1
>>> x * (y * z) == (x * y) * z
False
>>> x * (y * z) == [0]*(-1*-1) == [0]*1 == [0]
True
```

^ A list times one is itself

^ This makes sense

---

# wat #5 - Possible!

```python
>>> x = [0]
>>> y = -1
>>> z = -1
>>> x * (y * z) == (x * y) * z
False
>>> x * (y * z) == [0]*(-1*-1) == [0]*1 == [0]
True
>>> (x * y) * z == ([0]*-1)*-1
```

^ What happens when we multiple a list by a negative number?

---

# wat #5 - Possible!

```python
>>> x = [0]
>>> y = -1
>>> z = -1
>>> x * (y * z) == (x * y) * z
False
>>> x * (y * z) == [0]*(-1*-1) == [0]*1 == [0]
True
>>> (x * y) * z == ([0]*-1)*-1 == []*-1
```

^ Values of n less than 0 are treated as 0

^ which yields an empty sequence of the same type as s.

^ in this case, an empty list

---

# wat #5 - Possible!

```python
>>> x = [0]
>>> y = -1
>>> z = -1
>>> x * (y * z) == (x * y) * z
False
>>> x * (y * z) == [0]*(-1*-1) == [0]*1 == [0]
True
>>> (x * y) * z == ([0]*-1)*-1 == []*-1 == []
True
```

^ Again, an empty list

---

# wat #5 - Possible!

```python
>>> x = ...
>>> y = ...
>>> z = ...
>>> x * (y * z) == (x * y) * z
False
```

^ There are actually other ways to make this wat possible as well

^ for example

---

# wat #5 - Possible!

```python
>>> x = 5e-234
>>> y = 3
>>> z = 9007199254740993
>>> x * (y * z) == (x * y) * z
False
```

^ if we set x, y and z to these mysterious values

---

# wat #5 - Possible!

```python
>>> x = 5e-234
>>> y = 3
>>> z = 9007199254740993
>>> x * (y * z) == (x * y) * z
False
>>> x * (y * z)
1.335044315104321e-307
```

^ we get this value for the first half

---

# wat #5 - Possible!

```python
>>> x = 5e-234
>>> y = 3
>>> z = 9007199254740993
>>> x * (y * z) == (x * y) * z
False
>>> x * (y * z)
1.335044315104321e-307
>>> (x * y) * z
1.3350443151043208e-307
```

^ and this one for the second half

^ this is due to the way floats are, by their nature, imprecise

^ basically the two results are off by the difference of the least significant bit

---

# [fit] wat #6

---

# wat #6

```python
>>> x = ...
>>> y = ...
>>> x < y and all(a >= b for a, b in zip(x, y))
True
```

^ Can we define two lists x and y such that x < y

^ But when we compare each individual element, every element in x > y

^ This wat is possible

---

![](possible.png)

---

# wat #6 - Possible!

```python
>>> x = ...
>>> y = ...
>>> x < y and all(a >= b for a, b in zip(x, y))
True
```

---

# wat #6 - Possible!

```python
>>> x = ''
>>> y = ...
>>> x < y and all(a >= b for a, b in zip(x, y))
True
```

^ True for any interables where x is zero-length

---

# wat #6 - Possible!

```python
>>> x = ''
>>> y = 'foobar'
>>> x < y and all(a >= b for a, b in zip(x, y))
True
```

^ And y is any iterable

---

# wat #6 - Possible!

```python
>>> x = ''
>>> y = 'foobar'
>>> x < y and all(a >= b for a, b in zip(x, y))
True
>>> '' < 'foobar'
True
```

^ Comparison of sequences uses lexicographical ordering

^ Basically alphabetization. 'dog' comes before 'dogfish'

^ Empty list comes before non empty lists

---

# wat #6 - Possible!

```python
>>> x = ''
>>> y = 'foobar'
>>> x < y and all(a >= b for a, b in zip(x, y))
True
>>> '' < 'foobar'
True
>>> zip('', 'foobar')
[]
```

^ Zipping two lists of uneven length will give a list of the shorter length

---


# wat #6 - Possible!

```python
>>> x = ''
>>> y = 'foobar'
>>> x < y and all(a >= b for a, b in zip(x, y))
True
>>> '' < 'foobar'
True
>>> zip('', 'foobar')
[]
>>> all([])
True
```

^ all of an empty list is true!

^ all short-circuits -- if anything is false return false, otherwise true

---

# [fit] wat #7

---

# wat #7

```python
>>> x = ...
>>> len(set(list(x))) == len(list(set(x)))
False
```

^ This wat is not possible.

---

![](not_possible.png)

---

# wat #7 - Not Possible

```python
>>> x = ...
>>> len(set(list(x))) == len(list(set(x)))
False
```

^ This wat is not possible.

^ Converting a list to a set might reduce the length of x

^ But converting a set to a list will never add elementes

---

# [fit] wat #8

---

# wat #8

```python
>>> x = ...
>>> min(x) == min(*x)
False
```

^ Can we make x such that min(x) is not the same as min(x unpacked)

^ This wat is possible

---

![](possible.png)

---

# wat #8 - Possible!

```python
>>> x = ...
>>> min(x) == min(*x)
False
```

---

# wat #8 - Possible!

```python
>>> x = [[0]]
>>> min(x) == min(*x)
False
```

^ Remember earlier when I said min could take either a series of arguments

^ Or just an iterable?

^ This wat exists because of the different ways min handles its args

---

# wat #8 - Possible!

```python
>>> x = [[0]]
>>> min(x) == min(*x)
False
>>> min([1, 2, 3]) == min(*[1, 2, 3]) == min(1, 2, 3)
True
```

^ These are all the same

---

# wat #8 - Possible!

```python
>>> x = [[0]]
>>> min(x) == min(*x)
False
>>> min([1, 2, 3]) == min(*[1, 2, 3]) == min(1, 2, 3)
True
>>> min(x) == [0]
True
```

^ So the min of x is just the first element in it

---

# wat #8 - Possible!

```python
>>> x = [[0]]
>>> min(x) == min(*x)
False
>>> min([1, 2, 3]) == min(*[1, 2, 3]) == min(1, 2, 3)
True
>>> min(x) == [0]
True
>>> min(*x) == min([0]) == 0
True
```

^ But the min of x unpacked is the min of the list containing zero

^ Which is just zero

---

# [fit] wat #9

---

# wat #9

```python
>>> x = ...
>>> y = ...
>>> sum(0 * x, y) == y
False
```

^ This wat is impossible

---

![](not_possible.png)

---

# wat #9 - Not Possible

```python
>>> x = ...
>>> y = ...
>>> sum(0 * x, y) == y
False
```

^ This wat is impossible

^ Anything times zero is either zero or an empty sequence

^ The sum of zero or an empty sequence is always zero

---

# wat #9 - Not Possible

```python
>>> x = ...
>>> y = ...
>>> sum(0 * x, y) == y
False
>>> sum([1, 1, 1], 7)
10
```

^ Here, y is the "start" of the sum

---

# wat #9 - Not Possible

```python
>>> x = ...
>>> y = ...
>>> sum(0 * x, y) == y
False
>>> sum([1, 1, 1], 7)
10
>>> sum([], 7)
7
```

^ When the sequence is empty we just get the start value

---

# [fit] wat #10

---

# wat #10

```python
>>> x = ...
>>> y = ...
>>> y > max(x) and y in x
True
```

^ Can we find two values x and y such that y > max(x), but y is also in x

^ This wat is possible

---

![](possible.png)

---

# wat #10 - Possible!

```python
>>> x = ...
>>> y = ...
>>> y > max(x) and y in x
True
```

---

# wat #10 - Possible!

```python
>>> x = 'aa'
>>> y = ...
>>> y > max(x) and y in x
True
```

---

# wat #10 - Possible!

```python
>>> x = 'aa'
>>> y = 'aa'
>>> y > max(x) and y in x
True
```

^ This wat is possible

^ Only if x and y are strings!

---

# wat #10 - Possible!

```python
>>> x = 'aa'
>>> y = 'aa'
>>> y > max(x) and y in x
True
>>> max('aa')
'a'
```

^ The max of the string 'aa' is 'a'

---

# wat #10 - Possible!

```python
>>> x = 'aa'
>>> y = 'aa'
>>> y > max(x) and y in x
True
>>> max('aa')
'a'
>>> 'aa' > 'a'
True
```

^ Again, lexiographic ordering. 'dog' < 'dogfish'

---

# wat #10 - Possible!

```python
>>> x = 'aa'
>>> y = 'aa'
>>> y > max(x) and y in x
True
>>> max('aa')
'a'
>>> 'aa' > 'a'
True
>>> 'aa' in 'aa'
True
```

^ Also, python handles 'in' differently for strings

^ For strings, it performs a substring search

---

# wat #10 - Possible!

```python
>>> x = 'aa'
>>> y = 'aa'
>>> y > max(x) and y in x
True
>>> max('aa')
'a'
>>> 'aa' > 'a'
True
>>> 'aa' in ['a', 'a']
False
```

^ Where with lists, it's comparing 'aa' to each individual element

---

# One last thing...

^ These wats may seem really technically interesting

^ But I can almost guarantee that you'll never encounter these in the wild

^ In fact, I've been writing Python for a long time, and I've only seen one of these

^ The only reason I have them to share with you is because a smart fellow named Christopher Night collected a bunch of them together in a repo somewhere

^ Which is why I must implore you, please

^ Do not use these wats in a job interview

---

# Thanks!

# [fit] <https://github.com/di/talks/pygotham_2016/>

^ Again, thanks to Promptworks

^ Thanks to Christopher Night for introducing me to these wats

^ Thanks to PyGotham for this event

^ And thanks to you all for listening!

---

# Questions?

---

# wat #0 - Possible!

```python
>>> x = 0*1e309
>>> x == x
False
```

---

# wat #1 - Not Possible

```python
>>> x = ...
>>> a = ...
>>> b = ...
>>> c = ...
>>> max(x) < max(x[a:b:c])
True
```

---

# wat #2 - Possible!

```python
>>> x = {0}
>>> y = {1}
>>> min(x, y) == min(y, x)
False
```

---

# wat #3 - Not Possible

```python
>>> x = ...
>>> y = ...
>>> any(x) and not any(x + y)
True
```

---

# wat #4 - Possible!

```python
>>> x = 'foobar'
>>> y = ''
>>> x.count(y) > len(x)
True
```

---

# wat #5 - Possible!

```python
>>> x = [0]
>>> y = -1
>>> z = -1
>>> x * (y * z) == (x * y) * z
False
```

---

# wat #5

```python
>>> x = 5e-234
>>> y = 3
>>> z = 9007199254740993
>>> x * (y * z) == (x * y) * z
False
```

---

# wat #6 - Possible!

```python
>>> x = ''
>>> y = 'foobar'
>>> x < y and all(a >= b for a, b in zip(x, y))
True
```

---

# wat #7 - Not Possible

```python
>>> x = ...
>>> len(set(list(x))) == len(list(set(x)))
False
```

---

# wat #8 - Possible!

```python
>>> x = [[0]]
>>> min(x) == min(*x)
False
```

---

# wat #9 - Not Possible

```python
>>> x = ...
>>> y = ...
>>> sum(0 * x, y) == y
False
```

---

# wat #10 - Possible!

```python
>>> x = 'aa'
>>> y = 'aa'
>>> y > max(x) and y in x
True
```
