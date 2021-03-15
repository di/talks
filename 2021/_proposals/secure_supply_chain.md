# Recording

https://www.youtube.com/watch?v=9IwKM61gtk0

# Title

* Secure Software Supply Chains for Python

# Description

One of the most powerful parts of Python lies not within the language itself, but within the robust ecosystem of open-source Python packages available to use along with it. The Python Package Index, the canonical repository for Python code, hosts nearly 300,000 different projects. However, integrating software from so many third-parties comes at a cost: how can we be sure it's secure?

In this talk, we'll explore the common Python software supply chain, various ways in which such a supply chain can be attacked, as well as protected. We'll examine some tools and methodologies that help improve supply-chain security, and discuss the challenges and benefits these tools provide. Finally, we'll look at what fundamental improvements we can make to the overall ecosystem.

# Audience

This talk is for Python developers who want to ensure the security of the applications and libraries that they develop, as well as the third-party dependencies they have are secure, but don't know what attacks they may be vulnerable to or how to mitigate them.

Attendees should know the basics about what a Python package is, how to install it and where it comes from, but don't need to have an understanding of any advanced security topics.

After watching this talk, attendees should understand common supply-chain vulnerabilities in the Python ecosystem, and have actionable steps they can take to improve the security of their own software supply chain.

# Outline

* Intro (2 min)
  * Recent news and press about supply chain attacks
* What is a "secure supply chain"? (3 min)
  * What makes a Python package malicious?
  * Arbitrary code execution at install-time
* Examples of supply chain attacks in Python (8 min)
  * Typo squatting
  * Private dep squatting
  * Unpinned versions
  * MITM & Unhashed versions
  * Other compromises
* Tools that help secure the supply chain (4 min)
  * Pipenv / pip-compile
  * Dependabot / PyUP
  * pip itself
* Challenges of a secure supply chain (3 min)
  * Compromise of less flexibility for the developer
* What vulnerabilites remain? (3 min)
  * Developer can still install arbitrary code
  * Maintainers can still go rogue (leftpad)
* How do we fix it? (2 min)
  * Recent projects (HTTPS-only, etc.)
  * New standards (lockfiles, TUF)


* Intro
  * https://dustingram.com/
  * https://twitter.com/di_codes
  * https://www.python.org/psf/
  * https://www.pypa.io/en/latest/
  * https://pypi.org/
* News
  * https://i.giphy.com/media/Zd0DYHlBmZTGaiIFRY/giphy.webp
  * https://arstechnica.com/information-technology/2021/02/supply-chain-attack-that-fooled-apple-and-microsoft-is-attracting-copycats/
  * https://www.theregister.com/2021/03/02/python_pypi_purges/
  * https://www.zdnet.com/article/python-programming-language-google-funds-projects-aimed-at-supply-chain-security/
* SSSC
  * https://i.giphy.com/media/XECiLxeHvwdD96Jc6Z/giphy.webp
  * https://www.google.com/search?q=%22secure+software+supply+chain%22
* Attacks
  * https://i.giphy.com/media/Z543HuFdQAmkg/giphy.webp
  * https://snyk.io/blog/malicious-packages-found-to-be-typo-squatting-in-pypi/
  * https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610
  * https://pip.pypa.io/en/stable/reference/pip_install/#install-index-url
  * https://en.wikipedia.org/wiki/Man-in-the-middle_attack
* Tools
  * https://i.giphy.com/media/10dHotK4K8R0AM/giphy.webp
  * https://pypi.org/project/pipenv/
  * https://pypi.org/project/pip-tools/
  * https://github.com/pypa/warehouse/blob/main/requirements/main.txt
  * https://pyup.io/
  * https://dependabot.com/
  * https://github.com/pypa/warehouse/pull/9192
  * https://pip.pypa.io/en/stable/reference/pip_install/#hash-checking-mode
* Fixes
  * https://i.imgur.com/2JAHYYc.gif
  * https://mail.python.org/pipermail/distutils-sig/2017-October/031712.html
  * https://packaging.python.org/
  * https://www.python.org/dev/peps/pep-0458/
  * https://github.com/pypa/warehouse/issues/2589
  * https://github.com/psf/fundable-packaging-improvements/blob/master/FUNDABLES.md
  * https://cloud.google.com/blog/products/open-source/supporting-the-python-ecosystem
  * https://security.googleblog.com/2021/03/introducing-sigstore-easy-code-signing.html
* Outro
  * https://i.giphy.com/media/AhJIPUnoUYgyA/giphy.webp
