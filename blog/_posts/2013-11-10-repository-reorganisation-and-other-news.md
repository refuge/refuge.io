---
layout: post
title: Repository reorganisation and other news
author: benoitc
tags: refuge
---

Good news, during the next two months I will be able to dedicate more
time to the Refuge project. Which means that a lot of code will be
released. Coffer will be finally released this month as an
easy way to store, sync and share any content in a decentralised
manner.

In the process, I decided to reorganise a little the project and make easier
to track changes in it. The first step is mostly done: the source code
repositories have been redispatched between 3 Github organisations:

- [Refuge attic](https://github.com/refuge-attic): all dead and
  unmaintained codes have been moved there. This is where you will find all
of our temptatives...
- [Refuge incubator](https://github.com/refuge-incubator): All the
  projects of refuge will start here. If a project is considered enough
stable and in phase with the project, it will be moved to the main refuge
organisation
- [Refuge](https://github.com/refuge): The main organisation. All
  maintened refuge products will be found there.

There is still some work in progress in moving the code right now. For
example once the [new refactored
coffer](https://github.com/refuge-incubator/coffer) will be OK in the
incubator, old code in the refuge organisation will be moved to the
attic. Also we will removed dependencies we don't fork (to maintain
specific patches) from the main repository. But so far, most is already
done.

During the month some other changes will happen:

- The website will be moved to a controlled location and replicated to a
  CDN (ie. moved out from github). Same for the documentation.
- The mailing-lists will be also put back in our control
- Mirrors will be setup to fetch the code with git
- And finally a custom tool will be created to replicate and manage
  issues from Github even when github is down

Of course any help is welcome, so feel free to join us on irc or the current
mailing lists.


Enjoy!

-- Benoit Chesneau and the Refuge team.
