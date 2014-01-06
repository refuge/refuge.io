---
layout: post
title: A major upgrade of rcouch on the go
author: benoitc
tags: rcouch, refuge
---

**A major upgrade of [rcouch](http://rcouch.org) is on the go**. I am still
fixing the latest bits but I couldn't resist to share some details of what keep
me busy the last 4 days.

Last year, I decided to merge rcouch 0.7x (current release) in Apache CouchDB.
rcouch has been written/updated over 2 years with the help of Nicolas
(@nrdufour) andothers, adding new features, trying some changes, sometimes
rolling back to an old feature because of some bug discovered, sometimes just
because another way to do the feature was found. At some point some rewrite
happened, merging some changes in an atomic way to become the current rcouch
version.

Currently rcouch contains the following features:

[https://github.com/refuge/rcouch/wiki#changes-from-apache-couchdb](https://github.com/refuge/rcouch/wiki#changes-from-apache-couchdb)

and is based on [Apache CouchDB](http://couchdb.apache.org) 1.3 + some changes.
Last change from couchdb has been backported in may 2013.

Little changes in Apache CouchDB has been added since may 2013, but the merge
couldn't just go in a couchdb branch because of its history. Because of these
changes that happened over 2 years.. I wanted to clean the code a little, remove some
optimisations from it to avoid conflicts with the merge of some  bigcouch
features etc. 

So at the end of the year 2013, I deciced to start a new branch from current
couchdb 1.6 and then apply on it all the changes from rcouch one by one. In the
process I also decided to clean a little the build to use shared
libraries as well and improve some features like the view changes. This work
will be put in a couchdb branch and will be the base for the futur rcouch
release.

*Because Rcouch won't disappear with the merge in couchdb.* 

On the contrary, more than a bleeding edge Apache CouchDB distribution, it will
be the base for **a complete standalone product** shipped by the refuge project and
will work with the platform released sometimes this month. I will provide more
details soon.

I was too tired to really start last year and the work really started on last
friday. The changes in the couchdb branch will be done tomorrow. This branch
will become **rcouch 1.0.0**. After that the work on rcouch 2 will start. One of
the resolution I took for this year is to be more verbose, so I and other will
keep you updated more often about what happen in refuge with a weekly blog
post.

Hopefully you will enjoy what is coming.

- benoit
