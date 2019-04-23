# Title
Swiss Train Deployments

# Description
A Swiss Train deployment is a general-purpose deployment philosophy based on ideas from the Ember.js development process, modern browser releases, and various open-source project releases, such as the Ubuntu project.

In this talk, we'll explore the motivation for a Swiss Train style deployment, the problems which it seeks to solve in existing deployment philosophies, and the core philosophy of a Swiss Train deployment.

# Who and Why (Audience)
This talk is for developers who are responsible for deploying code (not just Python!) to production in a timely manner, while still providing a stable ecosystem for their users.

The only background knowledge required is some amount of experience "deploying" code or releasing applications, whatever that may mean for an individual developer (essentially, this will allow the audience member to better empathize with the inefficiencies of current deployment philosophies (or lack thereof) and highlight the advantage of the proposed philosophy.

After watching this talk, the audience should be able to:
- understand why it is important to have a deployment philosophy
- see the inefficiencies in current deployment philosophies
- present a strong argument for adopting Swiss Train style deployments
- be able to implement the deployment philosophy in their own workflow

# Outline
- Introduction, who am I? (1 min)
- Swiss Train Story (2 min)
- Stability Without Stagnation (4 min)
  - Ship Regularly
  - Have Multiple Speeds
- From Ember to You (6 min)
  - Benefits to Maintainers
  - Benefits to Contributors
  - Benefits to Add-On Authors and Developers
- A Realization (3 min)
- Swiss Train Deployments (6 min)
- Breaking Things (4 min)
- Two simple rules (3 min)
  - Don't make your users run for a release
  - Let them decide how fast to get from A to B
- Thanks (1 min)

# Additional notes

This talk is based on my experiences shipping Python code and the result of my popular blog post on the subject of Swiss Train style deployments: (<https://www.promptworks.com/blog/swiss-train-deployments>).

I talk about Python in some form at least once a month, and some of my previous Python talks have included "Detecting Asteroids with Neural Networks", "wat?  Mind-bending Edge-cases in Python" (PyGotham 2016) and "What Is and What Can Be: An Exploration from `type` to Metaclasses" (PyCon 2016), which was described by one attendee as "the most concise and understandable discussion of metaclasses I've heard" (<https://twitter.com/amylouboyle/status/737707897270865925>).

I have been a professional Python developer for more than ten years and have authored a number of small open-source projects (<https://github.com/di>) including a number of Python packages (<https://pypi.org/user/di/>).

I'm a member of the Python Packaging Working Group, the Python Packaging Authority (<https://github.com/orgs/pypa/people)> and a maintainer of the Warehouse project (<https://pypi.org/>).
