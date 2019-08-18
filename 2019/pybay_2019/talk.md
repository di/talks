footer: ![](images/twitter-logo.png) @di_codes

# *Building a Sustainable Python Package Index*
### PyBay 2019

---

![](images/dumb_face.png)

# [fit] *Hi, I'm Dustin*

---

![](images/dumb_face.png)

# [fit] *Hi, I'm Dustin*

* Developer Advocate @ Google
* PyTexas (Austin, TX, May 16-17th 2020)
* Python Package Index

^ here to answer the most important question

---

# Q: How do you pronounce "PyPI"?

---

![](images/eye.png)

---

- What PyPI is
- What PyPI *isn't*
- How PyPI works
  - Technically
  - Organizationally
  - Financially
- How we can improve

---

# *PyPI is...*

---

# *PyPI is...*

# the cannonical repository for Python software.

---

> "What happens when you type `google.com` into your browser and press enter?"

---

> "What happens when you type `pip install django` into your terminal and press enter?"

---

![fit](images/pypi-org.png)

---

![fit](images/simple-1.png)

---

![fit](images/simple-2.png)

---

![fit](images/simple-3.png)

---

![fit](images/simple-4.png)

---

# *PyPI is...*

# basically just a huge list of links to files with very specific filenames.

---

# *PyPI is...*

# old.

^ first commit: 2002

---

![fit](images/pypi-2003.png)

^ didn't exist until a while after Python was created

^ hence "batteries included"

^ still, predates many other package language repos

---

# *PyPI isn't*...

---

# *PyPI isn't*...
# a collection of audited software.

---

![](images/wild-west.png)

^ kind of like Github

---

# *PyPI isn't*...
# literally Github.

---

![fit](images/golang.png)

---

# *PyPI isn't*...
# a for-profit organization.

---

![fit](images/npm.png)

^ $10.6MM in VC funding, 60 employees

^ aha, suckers, going to make my own for-profit pypi

---







# How to build a PyPI

## *In just 5 easy steps!*

---

# 1. Define some APIs

## — Simple API<br>— Upload API<br>— JSON/XML-RPC APIs<br>— Web UI

---

# 2. Implement said APIs

## — Python 3<br>— Pyramid web framework<br>— Postgres/Redis<br>— Kubernetes<br>— A sprinkle of JS/SCSS

---

# 3. Put all of that behind a big ol' CDN

## (content distribution network)

---

![](images/fastly.png)

---

![](images/fastly-2.png)

---

![](images/mirror-size.png)

---

# 4. ???
# <br>
# 5. Profit!

---

# 4. ~~???~~ Try to make that sustainable<br>
# 5. Profit!

---

# 4. ~~???~~ Try to make that sustainable<br>
# 5. ~~Profit!~~ Hope you break even

---

# [fit] *Technical*
# [fit] *sustainability*

---

# *Technical sustainability*

## - Longevity<br>- Maintainability<br>- Transparency<br>- Evolvability<br>- Scalability

^ longevity - needs minimal maintenance

^ maintainability - when it does need maintenance, we can fix it

^ transparency - anyone can walk up and figure out how to fix it

^ evolvability - can adapt to the changing ecosystem

^ scalability - can handle the load

---

# *Technical sustainability*

## Using the latest and greatest

^ python 3, latest dependencies, releases, etc

^ longevity, evolvability

---

# *Technical sustainability*

## ...but not using anything too weird

^ maintainability

---

# *Technical sustainability*

## Everything is open source

^ transparency

---

# *Technical sustainability*

## Strong local development experience

^ maintainability

---

# *Technical sustainability*

## Tests!

---

# *Technical sustainability*

## Tests!<br><br>Lots of tests!!

---

# *Technical sustainability*

## Tests!<br><br>Lots of tests!!<br><br>100% test coverage!!!

---

![](images/test-coverage.jpeg)

---

# *Technical sustainability*

## Read-heavy and cacheable

^ scaleability

---

# *Technical sustainability*

## Resilient to downtime

^ scalability

---










# [fit] *Organizational*
# [fit] *sustainability*

^ said before we're not for-profit, what are we?

---

# [fit] *Organizational sustainability*
# <br>

## PyPI is a project of the Python Software Foundation, a non-profit.

---

# [fit] *Organizational sustainability*
# <br>

## PyPI is run (almost entirely) by a team of volunteers

^ because we all know how sustainable volunteers are

---

# Quick poll ✋

## Q: How many people have the 'commit bit' for PyPI?
## <br>

---

# Quick poll ✋

## Q: How many people have the 'commit bit' for PyPI?
## A: Six people

^ was three until recently

---

# Quick poll ✋

## Q: How many people have contributed to PyPI?
## <br>

---

# Quick poll ✋

## Q: How many people have contributed to PyPI?
## A: 200 people

^ since 2015

---

# Quick poll ✋

## Q: How many people have contributed 90% of the codebase?
## <br>

---

# Quick poll ✋

## Q: How many people have contributed 90% of the codebase?
## A: 12 people

---

# [fit] *Organizational sustainability*
# <br>

## Administrators:
### - Donald Stufft (Amazon)
### - Ernest Durbin (Python Software Foundation)
### - myself (Google)

---

# [fit] *Organizational sustainability*
# <br>

## Maintainers:
### - Nicole Harris (Kabu Creative)
### - Sumana Harihareswara (Changeset Consulting)
### - Alex Gaynor

---

# [fit] *Organizational sustainability*
# <br>

## Moderators:
### - Pradyun Gedam
### - Jason Madden
### - Thea Flowers
### - Yeray Diaz Diaz

^ triage issues, etc

---

# [fit] *Organizational sustainability*
# <br>

## Contributors:

### 200 individuals

---

# [fit] *Organizational sustainability*
# <br>

## a) someones company is paying them to work on open source

---

# [fit] *Organizational sustainability*
# <br>

## b) someone is unemployed & bored

^ possibly because they spent too much time working on open source

---

# [fit] *Organizational sustainability*
# <br>

## c) someone is not getting enough sleep

^ I've been all three of these

---










# [fit] *Financial*
# [fit] *sustainability*

---

# *Financial sustainability*

## Sponsors: individual donors

### Total: USD $250/mo

^ $3000 per year

---

# *Financial sustainability*

## Sponsors: in-kind donations

###- Metrics: Datadog<br>- Alerting: Sentry<br>- Seach: Elastic<br>- Compute/storage: AWS/GCP<br>- CDN: Fastly

^ More than $200K per month, $2.5 million per year

---

![](images/fastly-logo.png)

---

# *Financial sustainability*

## Grants & awards

^ for specific projects

---

![fit](images/pypi-2003.png)

---

![fit](images/pypi-2007.png)

---

![fit](images/pypi-2018.png)

---

![fit](images/pypi-2007.png)
![fit](images/pypi-2018.png)

^ less than 3K to almost 140K

---

![fit](images/projects-per-year.png)

^ not linear

---

![fit](images/warehouse.png)

---

![fit](images/moss-1.png)

---

![fit](images/moss-2.png)

^ USD $170,000

^ 2 devs, 1 UI/UX, 1 PM

---

![fit](images/pypi-2018.png)
![fit](images/pypi-org.png)

---

# *Financial sustainability*

## Mozilla Open Source Support

### Amount: USD $170,000<br>Goal: full-stack rewrite & launch<br>Status: Finished, April 2018

---

![fit](images/otf.png)

---

![fit](images/otf-award.png)

---

![fit](images/otf-commence.png)

---

# *Financial sustainability*

## Open Technology Fund

### Amount: USD $80,000<br>Goal: security & accessibility & launch<br>Status: Almost finished

---

![fit](images/2fa.png)

---

![fit](images/api.png)

---

# *Financial sustainability*

## Facebook Award

### Amount: USD $100,000<br>Goal: cryptographic package signing & launch<br>Status: Not yet started

---

# *Financial sustainability*

## <insert future award here>

---

# [fit] *More*
# [fit] *sustainability?*
# [fit] <br><br>
# [fit] <br><br>

---

# [fit] *A*
# [fit] *for-profit*
# [fit] *PyPI?*

---

# *A for-profit PyPI?*

## - private repositories<br>- support for on-site mirrors<br>- custom badges for PRO users<br>- auction off the best package names to the highest bidder

---

# *A for-profit PyPI?*

## Challenge: our non-profit status

---

# *A for-profit PyPI?*

## Challenge: our donated services

---

# *A for-profit PyPI?*

## Challenge: the current ecosystem

^ bandersnatch, devpi

---

# *A for-profit PyPI?*

## Challenge: our volunteers

^ don't want to work for free for for-profit

---

# *A for-profit PyPI?*

## Challenge: the transition

^ pycon

---

![fit](images/npm-layoffs.png)

---

![fit](images/npm-uninstall.png)

---

# *More sustainability?*

## Donate

---

# *More sustainability?*

## Donate your money:

### <https://www.python.org/psf/donations>

---

# *More sustainability?*

## Donate your time:

### <https://github.com/pypa/warehouse>


^ Grant writing and discovery
^ Project management

---

[.hide-footer]

# *Thanks!*
## ![](images/twitter-logo.png) @di_codes


<!--




* pip is going to do this and that, look at the cache
* but at some point it's going to decide it doesn't have the source code you want

* and that's where PyPI comes in

* How PyPI works, architecturly ( mins)
    * What happens when you type "pip install ..."
    * PyPI Legacy vs Warehouse
    * A modern Python codebase
    * Handling traffic at scale
* How PyPI works, organizationally ( mins)
    * Administrators
    * Maintainers
    * Moderators
    * Volunteers
    * Contributors
* How PyPI works, financially ( mins)
    * Non-profit status, PSF sponsorship
    * In-kind donations from sponsors
    * Contributions from individual donors

* pip knows the URL for PyPI
* simple API
* package

* pypi used to not be behind a CDN






https://dustingram.com/articles/2019/04/02/pypi-as-a-service/

*


Most of us have installed a Python package, but do we know what it takes to make that work in a consistent, reliable way?

Unlike some other languages, Python has a centralized repository for third-party Python packages. Also unlike some other languages, this repository, the Python Package Index, is entirely supported by the community and operated by the non-profit Python Software Foundation.

In this talk, we'll discuss why we have the PyPI we all know and love, and why the current status quo is preferred.  We'll go a bit into how PyPI works, both from a technical perspective, and from the perspective as an open-source and non-profit project.

Finally, we'll have a call to action to help improve, and more importantly sustain, this critical piece of Python infrastructure.


# Audience

This talk is for any Pythonista that has installed a package before (read: everyone).

After watching this talk, attendees should have a better idea of how the infrastructure they depend on works, and why it is so important

# Outline

* Introduction ( mins)
* A call to action ( mins)
* Conclusion ( mins)

-->
