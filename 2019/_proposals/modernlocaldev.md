# Title

* The end of "it works on my machine"
* Modern development environments for Pythonistas
* Modernizing your local dev experience

# Abstract



# Description

If you've ever created a new software project from scratch, you've probably struggled with the "n+1" problem, or "it works on my machine, now can we make it work on yours?". Between Python versions, local dependencies, different package installers, different platforms, and more, the likelihood that we can quickly set up a development environment and move on to productive work sometimes feels slim.

In this talk, we'll take a look at common patterns for improving the local development environment for your Python package, enabling your new developers to get up and running fast, your current developers to write code and iterate faster, and to improve portability of your environment between developers and their respective platforms. We'll examine specific techniques, tools, and methodologies that will enable us to do this, and take a look at some prominent Python software projects to see what they can teach us.

# Audience

This talk is for anyone who has struggled to set up their local development environment for a software project. This talk is useful for both open-source maintainers and for those working on

After watching this talk, attendees should know exactly what they need to change to make any given codebase more accessible and approachable for new and current developers alike.

# Outline

* Introduction ( mins)
* An environment for development ( mins)
  * Eliminating inconsistencies between environments
  * Optimizing for onboarding
* An environment for your test suite ( mins)
  * Ensuring non-determinism
  * Applications vs. libraries
* A modern dependency workflow ( mins)
  * Hashing and pinning
  * Auto-upgrading
  * Ensuring nondeterministic behavior
* Miscellanous: linting and autoformatting ( mins)
* Taking your environment to prod ( mins)
* Conclusion ( mins)
