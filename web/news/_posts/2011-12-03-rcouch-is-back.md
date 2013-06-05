---
layout: post
title: RCouch is back
author: benoitc
tags: rcouch
summary: RCouch is again maintained.
---

Hi all,

Sometimes ago we used to maintain rcouch, a static distribution of couchdb using rebar. We skiped this release at some point to focus more on refuge. But today we are putting it back online to allow people to easily install an Apache CouchDB distribution on their system.

Based on the couchdb code it will be tagged from time to time for stability purpose. At some point some support branches may appear.
RCouch differs from Refuge by only focusing on Apache CouchDB. It won't contain any of the refuge features like P2P nodes handling, ... .Internally we are using it to test couchdb and as an example on how to embed couchdb in your own applications.


RCouch features are:

- Apache CouchDB based
- Geocouch integrated
- rebar
- relocatable
- static build
- based on Mozilla Spidermonkey 1.8.5 .
- Fully opensource. All the sources are on refuge GIT repository  (http://github.com/refuge) under Apache License 2.

Enjoy,

- benoît
