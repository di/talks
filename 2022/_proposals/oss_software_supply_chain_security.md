# Title

* Securing the Open Source Software Supply Chain

# Description

Supply Chain Security: so hot right now. With the recently increased focus on securing software systems, there has been a incredible explosion of tools, methodologies, standards, best practices, and more. Given the sheer quantity, it's hard to keep track and stay informed: how can you know what's right for you?

The same attributes that make open source software desirable to use also make it challenging to secure. When anyone can publish an open-source library, how can you decide what's safe to use? If anyone can contribute, how can you trust the maintainers? If source code and development is in public, how can we identify and respond to vulnerabilities when attackers will know about them as soon as we do?

In this talk, we'll explore new tools and best practices that you can use today as open-source software user to improve the security of your software supply chain and trust in the ecosystem. We'll show how each of these serves a different purpose, and protects you from a unique way in which your software supply chain could be vulnerable. Finally, we'll discuss upcoming and potential improvements to the entire open-source ecosystem.

# Audience

This talk is for any developer that consumes open-source code, and wants to understand recent changes and improvements to software supply chain security, as well as learn about new tools and best practices they may not already be using.

Attendees should have a general sense of how open-source software is developed, published, and consumed, but don't need to have an understanding of any advanced security topics.

After watching this talk, attendees should understand common supply-chain vulnerabilities in the Python ecosystem, and have actionable steps they can take to improve the security of their own software supply chain.

# Outline

* Intro (4 min)
  * The state of open-source software security
  * Recent focus and changes
* Challenges of securing OSS (6 min)
  * The paradox of open-source security
  * Prior art, existing initiatives
* Tools for consumers and publishers (12 min)
  * Vulnerability discovery
    * pip-audit
    * Open Source Vulnerabilities Project
    * PyPA Advisory DB
  * Signing and trust
    * Key-resiliant signing
    * Transparancy logs
    * Sigstore, Rektor, Fulcio
  * Fuzzing & analysis
    * OSS-Fuzz
    * Deps.dev
  * Project health and compliance
    * SLSA
    * Scorecard
    * Allstar
  * Reproducibility and rebuilders
  * Secure integrations
    * OIDC
    * API Tokens
  * Developer security
    * MFA
* What else can be done? (6 min)
  * Upcoming projects
  * Proposed standards 
* Conclusion (2 min)

# Past experience

I love to talk about Python and software development in general. I've given talks at PyCon since 2016, and I also speak frequently at many regional Python conferences. Links to my previous talks, slides and videos can be found here: https://di.dev/speaking

I’m a director of the Python Software Foundation, member of the Python Packaging Working Group, the Python Packaging Authority, and a maintainer, contributor, and administrator of The Python Package Index (https://pypi.org/).

I have been a professional Python developer for over ten years. I'm a software engineer on Google's Open Source Security Team, where I focus on improving the security of open-source software that Google & the rest of the world relies on.

# Bio

Dustin works on Google's Open Source Security Team, focused on improving the security of open-source software that Google & the rest of the world relies on. He's also a director of the Python Software Foundation, and maintainer of the Python Package Index.
