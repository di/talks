autoscale: true

![](images/title.jpg)

---

# Knoll's Law
## *of media accuracy*

---

# Knoll's Law

"Everything you read in the news is absolutely true...

---

# Knoll's Law

"Everything you read in the news is absolutely true... except for the rare story of which you happen to have firsthand knowledge"

^ For me, that area of firsthand knowledge is around open source and security

---

# Firsthand knowledge

* Google's Open Source Security Team
* Python Software Foundation
* Python Package Index
* Open Source Software Security Foundation

^ I have a little bit of firsthand knowledge!

^ GOSST, where our mission is to make the open source software that google -- and the rest of the world -- more secure

^ PSF board, where I help ensure the long-term success of one very big open-source Python project you've probably heard of: python itself

^ PyPI maintainers, where I help ensure the long-term success of hundreds of thousands of tiny python projects, many of which you've never heard of

^ OpenSSF TAC, where I help guide the success of the next generation of open source security technologies.

^ But also, it's literally my job to figure out the ways in which open source is insecure, and how to fix it.

---

# Headlines

* "The Next Supply Chain Attack Vector: Open-Source Software"
* "Attacks on Software Supply Chains To Increase in Severity in 2023"
* "Software Supply Chain Attacks Hit 61% of Firms"
* "Banking Sector Targeted in Open-Source Software Supply Chain Attacks"
* "Coder unpublished 17 lines of JavaScript and 'broke the internet'"
* "Researchers find 633% increase in cyber-attacks aimed at open-source repositories"
* "The Internet Is on Fire"

^ I've seen so many headlines like ...


---

# Headlines (continued...)

* "Dozens of malicious PyPI packages discovered targeting developers"
* "Malicious PyPI packages stealing credit cards and injecting code"
* "Malicious software libraries found in PyPI posing as well known libraries"
* "3500 packages uploaded to PyPI, pointing to a malicious URL"
* "This malicious PyPI package mixed source and compiled code to dodge detection"
* "Frankenstein malware stitched together from code of others disguised as PyPI package"

---

# Headline:
## *I'm tired of these headlines*

^ You'd think, "great dustin! half your job is already done, just go fix those things"

^ But to be honest, I'm tired of these headlines

^ It's not that they're wrong, per se. Just that it's sort of like declaring "water is wet!"

^ For anyone with firsthand knowledge, this is stuff that has been known for a long time.

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

# This talk

* Understanding tradeoffs
* Evaluating impact
* Making progress

---

## **Part 1:**
# Understanding tradeoffs

^ here's the thing you need to understand about tradeoffs:

---

# Everything
## *is a tradeoff*

^ there are tradeoffs in every decision, and there is never just one best solution.

^ in literally every engineering decision, a tradeoff has been made

---

# Bugs
## *are tradeoffs*

^ Your code probably has bugs. Sorry, but it's true. But it's ok!

^ You wrote those bugs as part of a tradeoff

^ You could have spendt 10x, 20x the time writing the code, reviewing the code, testing the code, and it probably would have had less bugs. Not perfect, but better.

^ Instead, you had more time to add a new feature. Or you got a feature out faster. Or you were able to fix more issues your users were experiencing.


---

# Breaking changes
## *are tradeoffs*

---

# Insecurities
## *are tradeoffs*

---

# Python is a success
## *because of its tradeoffs*

^ Python is more than 30 years old, PyPI is 20 years old, and we've made some significant tradeoffs in that time

^ This is not to say that every tradeoff we made was the _right_ tradeoff -- we've definitely learned some lessons as well (like how and when to do a major version bump)

^ But overall, each of these is a tradeoff that has ultimately led to Python's success. Here's a headline: Python is a success!

---

# Example:
## _Malware on PyPI_

^ I'll give you one example: malware on PyPI. lots of news about it! happens all the time.

---

![fit](images/malware.jpg)

^ I personally have removed thousands of malware packages from PyPI, most of them reported by third-party security researchers

^ take my word for it: this is not a thing I enjoy doing

---

# Malware
## *is a tradeoff*

^ a lot of people will say "just block all malware on pypi" or "add additional obstacles to publish" or "require an audit before a release can go live".

^ putting aside, for a moment, whether that's even possible. is it even desireable, overall?

^ people complain all the time about the complexity of python packaging, but challenges publishing to PyPI is rarely part of that, because we've put a ton of effort into making that as easy as possible.

^ the fact that it's easy to publish malware on PyPI is because it's easy for anyone to publish anything on PyPI.

^ this is noticible and not imagined

---

![fit](images/petty_tyrant.jpg)

^ when you compare the experience as a maintainer on PyPI to the experience of a maintainer on other ecosystems

^ this is not to say that this other ecosystem is bad, to be clear.

^ just that they have made a different set of tradeoffs.

^ it's easy to say that the solution to malware on pypi is "well, just block all malware"

^ CPAN has almost no malware on it, as far as I'm aware. but this comes at the cost of signficiant friction for it's users

^ classifying software is hard. especially hard in a powerful and dynamic language like Python, and harder at scale like PyPI.

^ a false negative means that malware becomes trusted. a false positive means something legitimate, that people might need, is getting blocked or removed in error.

^ as a result, you need a human in the loop, because the last thing we want to do is accidentally wipe someones legitimate project off of PyPI

^ at pypi's scale, something like what CPAN does is not really feasible

^ #TODO better transition

---

## **Part 2:**
# Evaluating impact

^ one of the key thing to take into account when evaluating a tradeoff is impact

^ in the example before, I said bugs were tradeoffs. you're ok with having a few bugs in your software because the overall impact of the average bug is negligle.

^ you probably have good procedures around detecting, triaging and resolving bugs. hopefully, you have a way to evaluate the impact of bugs and generally can limit their scope

---

# Example:
## *The Knight Capital bug*

^ https://www.henricodolfing.com/2019/06/project-failure-case-study-knight-capital.html

---

# Example:
## *The Python 2→3 migration*

---

# Example:
## *Malware on PyPI*

^ here's a question: is malware actually an impactful problem?

^ obviously it'd be preferrable to not have malware on PyPI

^ but in the grand scheme of all the thing we can work on to make PyPI users more secure, is preventing malware the most impactuful thing?

^ based on my experience, I would argue that it's not. It's a high liklihood, low impact sort of thing. It happens often, but doesn't actually affect the large majority of users

^ on the other hand, 2fa #TODO

---

## **Part 3:**
# Making progress

^ Just because you've made a tradeoff doesn't absolve you from continuing to try to make progress

^ All that said, I do think we're at an inflection point right now

^ Where we're so popular that we can stand to sacrifice some usability for security.

^ I want to share some of the substantial and significant progress the Python community has made towards increased open source security

---

# Progress:
## *2FA, Key giveaway, and mandate*

---

# Progress:
## *Trusted Publishing*

---

# Progress:
## *`pip-audit` & advisory database*

---

# Progress:
## *PyPI Organizations*

---

# Progress:
## *Security Developer in Residence*

---

# Progress:
## *PyPI Safety & Security Engineer*

---

# Progress:
## *Malware reporting project*


^ Percentage of things uploaded that are malware
^ Percentage of things we know about that is still there

---

# Progress:
## *Over $1M in funding directed to Python open-source security*

^ if that's not progress, I don't know what is

---

# Progress:
## *Is built on trust*

^ Ultimately, this community exists because we trust each other

^ Part of that trust is that we can share code with each other and it will not erase our hard drive

^ There are expectations, and those expectations extend to things like taking reasonable security measures to keep your users safe.

---

![](images/final.jpg)

^ thanks to organizers and conference staff, for inviting me to join you at your conference

^ shoutout to everyone who has already enabled 2FA on PyPI

^ and thanks to you all for listening

---

# Test *Test* **Test**
## Test *Test* **Test**

* test
* *test*
* **test**
