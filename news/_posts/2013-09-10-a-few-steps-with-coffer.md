---
layout: post
title: A few steps with Coffer
author: nrdufour
tags: coffer, tutorial
---

Here is the first of a serie of posts trying to explain what we are trying to do and also how to use it.

The main idea is foster discussions around it and also archive our process if possible.

---

### Coffer?

Coffer is a simple engine (written in erlang) allowing you to store **blobs** (set of bytes) that are uniquely identified and managed by a given storage.

A **storage** is a named space using a particular implementation and a configuration.

So far we carry natively 2 of them: ets based (so in-memory) and local disk (basically maintaining the blobs in a directory tree structure on your disk). The idea is to be able to add more storage implementations (like a S3 based one for example) over time.


### Why?

Well, our main goal is to create a real document-oriented database in which the document is the first class citizen (as it should be). The blob is in fact the document: it's simply a set of bytes with a unique identifier stored in a storage area. Coffer is one step towards Refuge.

### OK so what can I do with it now?

So right now the base code is "stable" enough to start storing blobs (specially using the local disk storage) and being able to retrieve them.

I will come back in details to it in a moment.

### Any limits or caveats?

Yes the current storage implementations expects a unique id in the following format: `type-id` where `type` is usually a hashing method name (like `sha1`) and `id` is the actual content hash (example: `sha1-42654224436`).

To make a long story short: the storages will crash if the given id doesn't carry a `-`.

---

### OK time to dive in

#### Before to start …

Make sure you have erlang at least version R15.

#### Installing it

The best way to install a coffer server (for now) is to retrieve the project `coffer_standalone_server` on [github](http://github.com/refuge/coffer_standalone_server).

    git clone https://github.com/refuge/coffer_standalone_server
    cd coffer_standalone_server
    make
    make rel

#### Starting it

At this point, you should have in `coffer_standalone_server/rel/coffer` a fully compiled and package coffer.

So go in `coffer_standalone_server/rel/coffer` and launch:

    ./bin/coffer start

If you want to stop it:

    ./bin/coffer stop

And if you want to follow the logs and use the erlang shell:

    ./bin/coffer console