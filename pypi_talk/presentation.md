# Software
## _of the_
# Long Now

---

![](images/window.png)

^ physical objects on this time scale

^ started doing software, struggled with the ephemerality of my work

---

![](images/hillis.jpg)

^ Danny Hillis

^ lifetime building supercomputers, more in museums than still running

^ 90s -> 2000s

---

![](images/hillis_bg.jpg)

> “I want to build a clock that ticks once a year. The century hand advances once every one hundred years, and the cuckoo comes out on the millennium. I want the cuckoo to come out every millennium for the next 10,000 years.”
-- Danny Hillis

^ 10000 years is just within the limits of plausability

^ we have found artifacts that are approximately that old, but nothing so complex

^ danny made his dream a reality

---

![](images/prototype_1.jpg)

^ this is the clock that was finished january 31st, 1999

^ it's called "the clock of the long now"

^ five design principles

---

![](images/prototype_1_bg.jpg)

# Longevity

^ 1. accuracy, rust, flooding, looting

---

![](images/prototype_1_bg.jpg)

# Maintainability

^ 2. future generations, minimal tools

^ access to parts

^ hand-wound

^ If there is no attention for long periods of time the Clock uses the energy captured by changes in the temperature between day and night on the mountain top above to power its time-keeping apparatus.

---

![](images/prototype_1_bg.jpg)

# Transparency

^ 3. understandable without stopping, creators will be long gone

---

![](images/prototype_1_bg.jpg)

# Evolvability

^ 4. improve over time

^ for example, the earth is slowing at a noticible but unpredictable rate

^ it should be adjustable if length of day changes without stopping the clock

---

![](images/prototype_1_bg.jpg)

# Scalability

^ 5. prototypes

---

![](images/prototype_1.jpg)

^ this is actually a scale prototype

---

![](images/prototype_2_1.png)

---

![](images/prototype_2_2.png)

---

![](images/prototype_2_3.png)

^ prototype 2, west texas

---

![](images/mt_washington.jpg)

^ mount washington, nevada

^ biggest concerns are earthquakes, changing rotational speed of earth

^ these are geologic, planetary concerns

^ we dont design software to exist at this scale, not even 100-year scale

---

# `$ git blame`

^ oldest code on your laptop

^ how long will it be used

^ oldest thing that you have created

^ code: how long will it be used? docs: how long will it be relevant? talks: when is the last time someone will watch it?

^ we don't want to think about this

---

![](images/logo-large.jpg)

^ the closest i've come is PyPI

^ canonical repository for python packages

^ contributor, maintainer, administrator

---

# `$ pip install ...`

^ PyPI is what picks up the phone at the other end of the line when you pip install something

^ one of the oldest

^ like most languages, this centralized repo didn't exist when python was created

^ guido joke

^ packaging was a solved problem

^ couldn't imagine python on a platform without a package manager

---

![fit](images/pypi_2003.png)

^ 2003: definitely old software

^ prototype, didn't host, still pretty good

---

> “Any sufficiently advanced prototype is indistinguisable from production software.”
-- Me

---

![fit](images/pypi_2007.png)

^ 2007, four years later

---

![fit](images/pypi_2018.png)

^ 2018

---

![fit](images/pypi_2007.png)
![fit](images/pypi_2018.png)

^ eleven years between these two images

^ there is a reason for this

^ unfair to compare visually

---

# ~3k → ~140K

^ what you can't see

^ went from "a" place to "the" place

---

# [fit] 🥚 🐣 🐔

^ chicken/egg

^ web frameworks, testing frameworks

^ there were no tests

---

![fit](images/warehouse.png)

^ rewrite pypi from scratch

^ started in 2015

^ i joined early 2016

^ seemed like it might never be finished

---

![fit](images/mozilla.png)

^ november

^ grant for myself, an infrastructure engineer, designer and project manager to work full time

---

![fit](images/newpypi.png)

^ by april we had launched

^ what we told mozilla

---

![](images/logo-small.png)

^ ulterior motive: turn pypi into software for the long now

^ as it turns out, the same principles for designing a 10000 year clock are generally good principles for designing anything to last a long time

---

![](images/logo-small_bg.png)

# Longevity

^ 1. should always be able to pip-install first module ever uploaded

^ accuracy: it should still install the same code (even if it probably doesn't work)

---

![fit](images/roundup.png)

^ not interesting, aside from the fact that you can still install it with modern tech

---

![](images/logo-small_bg.png)

# Maintainability

^ 2. require as little maintenance as possible

^ doesn't required a lot of my time

^ maintainable by people that aren't me

---

![fit](images/contributors.png)

^ entirely volunteer driven, with the exception of the grant

---

![](images/logo-small_bg.png)

# Transparency

^ 3. code is transparent, but this is not enough

^ documentation helps, but still is not enough, too much "how"

^ need to understand the thoughts/discussions/decisions, the "why"

---

![fit](images/distutils.png)

^ minimize backchannel, record everything

^ thinking of users in the future when making github comments

---

![](images/logo-small_bg.png)

# Evolvability

^ 4.

---

# 100%

^ tests

---

![fit](images/sponsors.png)

^ entirely sponsor-supported

---

![fit](images/stackoverflow.png)

^ using modern frameworks

^ ability to add new features

---

![fit](images/markdown.png)

^ first thing I did

---

![](images/markdown_twitter.png)

^ evolvability begets survivability

---

![](images/logo-small_bg.png)

# Scalability

^ 5. we've already had our prototype, learned from it

^ can it support the growing demands in the next year?

^ in the next decade?

---

![fit](images/fastly.png)

^ one way to ensure pypi can scale: put it behind a CDN

^ if something is going to be viewed twice, put it in the cache

^ lots of extra logic around when to invalidate the cache

^ 2B req/day, 20TB of bandwidth, 2TB storage

^ order of magnitude more

---

![](images/logo-small.png)

^ I'm confident that PyPI will continue to exist for the next ten years

---

![](images/window.png)

^ I like to think back to this window often

^ like the clock of the long now, it helps give me a greater perspective on what I'm building in a less immediate timeframe

---

# Thanks!
