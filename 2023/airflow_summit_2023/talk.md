![](images/title.jpg)

---

# [fit] Knoll's Law

---

# Knoll's Law

"Everything you read in the newspapers is absolutely true...

---

# Knoll's Law

"Everything you read in the news is absolutely true... except for the rare story of which you happen to have firsthand knowledge"

---

I work on Google's Open Source Software Security team

Literally my job to figure out the ways in which open source is insecure, and how to fix it.

---

I've seen so many headlines like ...

You'd think, "great dustin! half your job is already done, just go fix those things"

^ But to be honest, I'm tired of these headlines

^ It's not that they're wrong, per se. Just that it's sort of like declaring "water is wet!"


^ So tired, in fact, that I'm just going to write the one headline to end all headlines

^ So let me just get this out of the way

---

# Headline:
## *Python Is Not "Secure"*

^ I'm not going to lie! It's not, not by any means

^ Anybody can publish anything they want on PyPI

^ Python itself doesn't have sandboxing can do anything it wants on the machine it's running on

^ Something about CFFI and memory safety?

^ really, this isn't limited to just Python

---

# Headline:
## *Open Source Is Not "Secure"*

^ there is no perfectly secure software ecosystem, programming language, deployment environment, cloud provider.

^ some are better than others in some ways, and yes, we still have very real problems to solve

^ none of them are perfectly secure, and never will be

^ but:

---


## ...*but open source is __pretty__ secure, actually!*

^ this is my premise for my talk

^ no matter what you hear about the insecurity of open source

^ it's but a small flaw in an otherwise iceberg sized security

^ many things we consider security issues are tradeoffs, for usability, etc.

^ I want to give you a bit of context about these tradeoffs

^ what I think you should be worried about, and what you shouldn't be worried about

^ and we've continued to get better over the years -- especially recently

---

# unclear solutions

^ and there isn't always a clear solution.

^ I'll give you one example: malware on PyPI. lots of news about it! happens all the time. but the solution isn't as simple as "well, just block all malware"

^ classifying software is hard. especially hard in a powerful and dynamic language like Python, and harder at scale like PyPI.

^ a false negative means that malware becomes trusted. a false positive means something legitimate, that people might need, is getting blocked or removed in error.

^ as a result, you need a human in the loop, because the last thing we want to do is accidentally wipe someones legitimate project off of PyPI


---

# tradeoffs

Python is 30 years old
PyPI is 20 years old
Anyone out there responsible for running a project/service that long?
How well does it do?


Why
Each of these is a tradeoff that has ultimately led to Python's success
Here's a headline: Python is a success!
It's not perfect
There's a lot we've learned over the last 30 years (like how to do Major version bumps)


---

# The inflection point

^ All that said, I do think we're at an inflection point right now

^ Where we're so popular that we can stand to sacrifice some usability for security.

---

# we have been doing good!

Actually, practicaly everything we've
2fa grant, titan keys, 2fa mandate
Trusted Publishing
Remove pgp signatures
Malware reporting project
Percentage of things uploaded that are malware
Percentage of things we know about that is still there
vulnerabilities
Pip audit and advisory database
Organizations
Sigstore


Over $1m in funding directed to the PSF and it's projects


---

# this is all built on trust

Ultimately, this community exists because we trust each other

Part of that trust is that we can share code with each other and it will not erase our hard drive

There are expectations, and those expectations extend to things like taking reasonable security measures to keep your users safe.

---

![](images/final.jpg)

---

# Test *Test* **Test**
## Test *Test* **Test**

* test
* test
* test



