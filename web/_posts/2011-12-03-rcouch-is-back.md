---
layout: post
title: RCouch is back
---

Hi all,

Sometimes ago we used to maintain rcouch, a static distribution ofcouchdb using rebar. We skipoed this release at some point to focus more onrefuge. But today we are putting it back online to allow people toeasily install an Apache CouchDB distribution on their system.

Based on the couchdb code it will be tagged from time to time for stabilitypurpose. At some point some support branches may appear.
RCouch differs from refuge by only focusing on Apache CouchDB. It won't contain any of the refuge features like P2P nodes handling, ... .Internally we are using it to test couchdb and as an example on how toembed couchdb in your own applications.


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