# `collections`

```python
>>> l = ['a', 'b', 'c']
```

^ Let's think about the functions we have for a list

---

# `collections`

```python
>>> l = ['a', 'b', 'c']
>>> l.append('d')
>>> l
['a', 'b', 'c', 'd']
```

^ We can append an element to the list

^ What's the complexity? O(1) average, amortized worst case

---

# `collections`

```python
>>> l = ['a', 'b', 'c']
>>> l.extend(['d', 'e'])
>>> l
['a', 'b', 'c', 'd', 'e']
```

^ We can extend the list with another list

^ What's the complexity? O(k) average, amortized worst case

---

# `collections`

```python
>>> l = ['a', 'b', 'c']
>>> l.pop()
'c'
>>> l
['a', 'b']
```

^ We can pop an element off the end of the list

^ What's the complexity. O(1)... for the end of the list only

---

# `collections`

```python
>>> l = ['a', 'b', 'c']
>>> l.pop(0)
'c'
>>> l
['b', 'c']
```

^ Now what's the complexity? O(n).

^ When we want to do anything that modifies the list that isn't on the end
^ it's always going to be O(n) because, potentially, everything must move

---

# `collections`

```python
>>> l = ['a', 'b', 'c']
>>> def appendleft(l, element):
...     pass
...
>>> def extendleft(l, elements):
...     pass
...
>>> def popleft(l, i=0):
...     pass
...
```

^ Just to motivate this, let's implement these three functions

^ without using any of the builtin list functions, just indexing

---

# `collections`

```python
>>> l = ['a', 'b', 'c']
>>> def appendleft(l, element):
...     l.append(None)
...     for i, x in enumerate(l[:-1]):
...         l[i+1] = x
...     l[0] = element
...
>>> appendleft(l, 'z')
>>> l
['z', 'a', 'b', 'c']
```

^ complexity is O(n)

---


# `collections`

```python
>>> l = ['a', 'b', 'c']
>>> def extendleft(l, elements):
...     for element in elements:
...         appendleft(l, element)
...
>>> extendleft(l, ['z', 'y'])
>>> l
['y', 'z', 'a', 'b', 'c']
```

^ Complexity is O(n*k), or ~O(n^2)

---

# `collections`

```python
>>> l = ['a', 'b', 'c']
>>> def extendleft(l, elements):
...     l.extend([None]*len(elements))
...     newlist = elements[::-1] + l[:-len(elements)]
...     for i, x in enumerate(newlist):
...         l[i] = x
...
>>> extendleft(l, ['z', 'y'])
>>> l
['y', 'z', 'a', 'b', 'c']
```

^ Complexity is O(n+k)

---

# `collections`

```python
>>> l = ['a', 'b', 'c']
>>> def popleft(l, i=0):
...     ret = l[i]
...     del l[i]
...     return ret
...
>>> popleft(l)
'a'
>>> l
['b', 'c']
```

^ This one is a little simpler because we can use delete

---

# `collections`

```python
>>> l = ['a', 'b', 'c']
>>> def popleft(l, i=0):
...     ret = l[i]
...     del l[i]
...     return ret
...
>>> popleft(l, 1)
'b'
>>> l
['a', 'c']
```

^ And we can give it an index just like `pop()`

^ Complexity is O(n) (due to del)

^ lists are optimized for fast fixed-length operations

^ they incur O(n) memory movement costs for pop(0) and insert(0, v) operations

^ So, what am I about tell you?

---

# `collections.deque`

```python
>>> l = ['a', 'b', 'c']
>>> from collections import deque
>>> q = deque(l)
>>> q.appendleft('z')
>>> q
['z', 'a', 'b', 'c']
```

^ deque has it all, and it's better, and by better I mean faster

^ appendLeft runs in O(1) average, amortized worst case

---

# `collections.deque`

```python
>>> l = ['a', 'b', 'c']
>>> from collections import deque
>>> q = deque(l)
>>> q.extendleft(['z', 'y'])
>>> q
['y', 'z', 'a', 'b', 'c']
```

^ extendLeft runs in O(k) average, amortized worst case

---

# `collections.deque`

```python
>>> l = ['a', 'b', 'c']
>>> from collections import deque
>>> q = deque(l)
>>> q.popleft('z')
>>> q
['z', 'a', 'b', 'c']
```

^ popLeft runs in O(1) average, amortized worst case

---

# Some inspiration from:

* https://codefisher.org/catch/blog/2015/04/22/python-how-group-and-count-dictionaries/
* http://ivansmirnov.io/python-metaclasses/
* https://github.com/cosmologicon/pywat

---

# `slice`

---

# `slice`

```python
>>> a = ['a', 'b', 'c', 'd', 'e', 'f']
>>> LAST = slice(-1, None)
>>> a[LAST]
['f']
>>> EVENS = slice(None, None, 2)
>>> a[EVENS]
['a', 'c', 'e']
>>> ODDS = slice(1, None, 2)
>>> a[ODDS]
['b', 'd', 'f']
```

^ One more. Did you know slice is a builtin?

^ Why? If you ever need to use a slice more than once, you can define it once.
