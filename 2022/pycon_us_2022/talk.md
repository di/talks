theme: Minty Next
footer: ![](images/twitter-logo.png) @di_codes
[.code: auto(42)]

# *Securing*
# *the Open Source*
# *Software Supply Chain*
## PyCon US 2022

<!--

Supply Chain Security: so hot right now. With the recently increased focus on
securing software systems, there has been a incredible explosion of tools,
methodologies, standards, best practices, and more. Given the sheer quantity,
it’s hard to keep track and stay informed: how can you know what’s right for
you?

The same attributes that make open source software desirable to use also make
it challenging to secure. When anyone can publish an open-source library, how
can you decide what’s safe to use? If anyone can contribute, how can you trust
the maintainers? If source code and development is in public, how can we
identify and respond to vulnerabilities when attackers will know about them as
soon as we do?

In this talk, we’ll explore new tools and best practices that you can use today
as open-source software user to improve the security of your software supply
chain and trust in the ecosystem. We’ll show how each of these serves a
different purpose, and protects you from a unique way in which your software
supply chain could be vulnerable. Finally, we’ll discuss upcoming and potential
improvements to the entire open-source ecosystem.

-->

---

# Hi, I'm Dustin

* Software Engineer, Google Open Source Security Team (GOSST)
* Director, Python Software Foundation
* Maintainer, Python Package Index

^ GOSST, where our mission is to make the open source software that google -- and the rest of the world -- more secure

^ PSF, where I help ensure the long-term success of one very big open-source Python project you've probably heard of: python itself

^ PyPI, where I help ensure the long-term success of hundreds of thousands of tiny python projects, many of which you've never heard of

---

## *Part 1:*
# Q&A

^ I'm going to be a bit unconventional, start with a Q&A, but also I'm going to be asking the questions, and also answering them

^ I think there's some important questions we should all be asking around open-source security right now

---

# Is it *safe* to use open-source software?

^ This might be the question you came here today with

^ maybe heard a lot about security challenges open-source is having in the news

^ you might have doubts or fears about the viability of using open-source

---

## Is it safe to use open-source software?
# Yes!

^ the reality is that every day, all kinds of open source software is deployed, used by billions, and it works

^ And as someone whose career exists because people use open source software, I want to tell you yes!

^ You might say, 'but dustin, didn't you just say your job is to make open source more secure'

^ "Doesn't that also imply that open-source software isn't as safe as it could be"

^ kinda also yes

---

## *Is it safe to use open-source software?*
# Yes![^*]

[^*]: Use only as directed. Open source software is not guaranteed to be safe and usually amounts to allowing strangers to run arbitrary code on your machine. Don't talk to strangers. Talk to your doctor if you are considering switching to an ecosystem with more security guarantees. Any ecosystem claiming to be more secure probably can't make those guarantees anyway. All software is vulnerable, all we can do is accept the inevitable reality of bugs, outages, vulnerabilities, and the heat death of the universe. We don't make mistakes, we just have happy little accidents. Exposure to vulnerabilities may prevent you from ever trusting any software ever again. Closed-source software isn't less vulnerable, it just gets less press. Open source doesn't have a security problem, it has a sustainability problem. Don't blame the maintainers, pay the maintainers. Apply security patches directly to the forehead. If your job doesn't let you use open source, apply directly for a new job. Exposure to open source may lower your expectations. Remember: if you expect nothing from anybody, you’re never disappointed. Void where prohibited. Not all practices described in this talk are applicable to all persons or at all locations. Literally nothing you do will void the warranty, because there is no warranty. Use of open source may cause upset stomach, headache, and hot takes on Twitter.

^ so realistically, yes, but with a big asterisk

^ basically: it depends how you use it

^ and, depends on what your threat model is

---

## *A better question:*
# How can we use open-source software safely?

^ so maybe a better question to be asking is this

^ if we're already using open source, how can we use it more safely?

^ and if you're not, what should you be aware of

---

# What is the Software Supply Chain?

---

## *The Software Supply Chain:*
# Everything it takes to produce your software

---

# What is the _Secure_ Software Supply Chain?

---
## *The Secure Software Supply Chain:*
# All those things, and they're definitely not compromised

---

# Why is software-supply chain security such a big deal?

^ because: virtually everyone uses open-source source software

^ anyone who says they don't likely just don't have a good sense of what what they're using

^ in the past, we made a fair amount of assumptions about how open-source software is created, distributed, consumed, etc.

^ some of these assumptions where that things wouldn't go wrong, and these assumptions were wrong

^ but why now?

---

# Why is software-supply chain security such a big deal _right now_?

^ part of this is that there's an incredible amount of scrutiny being paid due to recent compromises

---

[.hide-footer]
![fit](images/register.png)

^ malicious libraries published

---

[.hide-footer]
![fit](images/ars.png)

^ new types of supplychain attacks affecting large corperations

---

[.hide-footer]
![fit](images/log4j.png)

^ we have an unintentional remote code execution in extremely widely used java logging library

---

[.hide-footer]
![fit](images/log4j2.png)

^ ...and another one

---

[.hide-footer]
![fit](images/peacenotwar.png)

^ an entirely new class of malware: protestware

---

[.hide-footer]
![fit](images/solarwinds2.png)

^ and we have solarwinds, which everyone and their mother has heard about by now

---

[.hide-footer]
![fit](images/solarwinds.png)

^ and was a 'worst nightmare' cyberattack

---

[.hide-footer]
![fit](images/breach.png)

^ mostly in the sense that it directly attacked the US government

---

# But the main reason...

^ is really that part of the response to the solarwinds attack

---

[.hide-footer]
![fit](images/eo.png)

^ was executive order 14028, on improving the nation's cybersecurity

^ which means

---

[.hide-footer]
![fit](images/eo2.png)

^ because the president said so

^ for anyone not based in the US, or for anyone based in the US but not up on how their government works, an executive order is kinda like an email from your boss telling you what to do.

^ this has the effect of setting policy for the entire executive branch and federal government

^ it's also kind of like placing an order at a restaurant, in the sense that you kinda say what you want to happen, and people go off and try and figure out how to make it happen, and maybe this takes a while

^ this EO was published almost a year ago, and we're still at the 'everyone is trying to figure out how to make it happen' stage

---

[.hide-footer]
![fit](images/eo3.png)

^ this executive order has a number of directives, but it specifically calls out the software supply chain

^ and if you think this is just limited to government entities, remember that the government uses a lot of software

^ they also use a lot of the same software you and I do
et
^ so the terms of this order sort of have a 'viral' effect of improving software security for everyone. This is a good thing

---

## *Part 2:*
# Parts of the Secure Software Supply Chain

^ so let's talk about what the software supply chain is

^ by supply chain I don't mean software for a literal physical supply chain

^ talking about a SOFTWARE supply chain

---


## *Part 3:*
# How can we use open-source software safely?

---

[.hide-footer]
![fit](images/2021.png)

---

# *What we can do (circa 2021):*
* HTTPS everywhere
* Lockfiles & compiled dependencies
* Vulnerability notifications
* TUF, namespaces, etc

^ not going to explain any of that

^ that was a year ago, we've made progress in the meantime!

---

# What _else_ can we do to fix this?

^ I'm going to guess you've at least heard of most of that

^ if not already doing it yourself

^ In my talk last year, I sort of waved my hands and said "here's some hypothetical stuff we could do to make things better"

^ Going to outline some things that are new, are in progress or have been proposed

---

## *New!*
# Community advisory databases

---

[.hide-footer]
![fit](images/osv.png)

^ This use the OpenSSF Open Source Vulnerability format, provided by the Open Source Vulnerabilities project

^ OSV also has an API and acts as a vendor-neutral aggregator and mediator for vulnerabilities

---

# *Community advisory databases*

<https://github.com/pypa/advisory-database>

^ these exist for most major ecosystems

^ but are you supposed to read each of these by hand? no!


---

## *New!*
# Vulnerability auditing software

---

## Use vulnerability auditing software:

* Python: `pip-audit`
* Go: `vulncheck`
* Rust: `cargo-audit`
* Ruby: `bundler-audit`

^ these use the advisory databases previously mentioned

^ run these locally, run these as part of your release process, your integration tests, etc

^ you should be confident that you're not deploying something with a known vulnerability

---



## Improvement:
# Artifact Signing

^ historically this meant GPG, which works but has it's challenges

^ tools like GPG are incredibly confusing for unfamiliar users, raise the barrier to entry

^ require users to maintain private keys

^ doesn't solve the problem of trust: even if an artifact is signed, how do you know you can trust the signature?

---

[.hide-footer]
![fit](images/sigstore.png)

^ sigstore is a new project by the linux foundation across multiple vendors including google

---

## Understanding sigstore

* Ephemeral keys
* Certificate authority
* Transparency log
* Timestamping service
* OpenID Connect

^ ephemeral keys mean the signing keys are used once and then thrown away, forever. no keys to maintain

^ a certificate authority binds these cryptographic keys to an identity and an artifact

^ every signature is stored in a log that can be searched and can't be tampered with

^ signing certificates are only valid for a short period to prevent reuse

^ oidc, built on the oauth protocol, allows fine-grained identities, e.g. github actions workflows

---

## `sigstore-python`

---

## Improvement:
# Better, more secure build infrastructure

^ there's a lot of different environments and ecosystems upon which software can be built

^ some properties increase security, while others don't

---

[.hide-footer]
![fit](images/slsa.png)

---

## Understanding SLSA ('salsa')

* Security framework
* Checklist of standards and controls
* A series of levels

^ many build environments are working on making it possible to achieve various slsa levels

^ a given build process might produce an artifact at SLSA level 1 (least secure) or higher

^ these levels depend on the properties of the build

^ how do we know?

---

## Improvement:
# Attestations

^ attestations are a way of proving the state of the build process for some piece of software

---

[.hide-footer]
![fit](images/intoto.png)

---

## Understanding in-toto

* A universal standard
* For all ecosystems
* Ensuring integrity of an artifact
* Proof of what was done at each step

^ designed to ensure the integrity of a software product from initiation to end-user-installation

^ by making it transparent what steps were performed, in what order, and by who

---

## Improvement:
# Enforcing security policies for source control

^ above and beyond what your source control repo can provide

---

[.hide-footer]
![fit](images/allstar.png)

---

## Understanding Allstar

* A GitHub app
* Enforces best practices
* Allows you to set policy
* Across an entire organization

^ e.g. branch protection, binary artifacts, outside collaborators, etc

---

## Improvement:
# Vendor neutral collaboration

^ everyone working together across ecosystems and companies

---

[.hide-footer]
![fit](images/ossf.png)

^ new organization as part of the linux foundation

---

## Improvement
# New features for PyPI

^ 2FA mandate, voluntary 2FA requirement

^ Credential-less publication via OIDC

^ PEP 458 & PEP 480

---

# What _else_ can we do to fix this?

---

## Improvement:
# More funding for projects

^ much of the cost for these larger projects is being supported by big vendors

^ but there's likely a need for support in your ecosystem as well

^ financially sponsoring your local software foundation makes things like this possible

---

[.hide-footer]
![fit](images/ossf-members.png)

^ or, become a member of the open ssf foundation

---

## Improvement:
# More users and contributors!

^ This means you!

^ Try this stuff out, tell us how it works for you, share your experience

^ Possibly become a contributor, it's all open source!

---

## Predictions
# My predictions for the next year

^ if you're an open-source software repository or package installer maintainer - brace for interest and funding
^ if you're an open-source maintainer - brace for people asking you to adopt new security practices
^ if you're an open-source consumer - educate yourself

---

## Shoutouts

* William Woodruff & Alex Cameron @ Trail of Bits
* PyCon Staff

^ I also want to give a huge thank-you to the PyCon staff for everything they've dealt with and everything they've done to bring this conference online.

^ They absolutely deserve your thanks as well, be sure to let them know you appreciate all the hard work they're doing.

^ See you next year!

---

[.hide-footer]

# *Thanks!*
## ![](images/twitter-logo.png) @di_codes
