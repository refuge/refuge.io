---
layout: post
title: New preview of rcouchx
---

rcouchx is a macosx interface for rcouch. Initial version was
segfaulting on some osx systems becausee it didn't find the uri file.

I've updated the code to fix this issue and while I was there I also
updated the rcouch source to generate a full DMG and distribute the
rcouchx application;


![rcouchx DMG screenshot](/img/new-preview-of-rcouchx/screenshot.png)

You can download the binary on github:

[https://github.com/downloads/refuge/rcouch/rcouchx-0.5.2.zip](https://github.com/downloads/refuge/rcouch/rcouchx-0.5.2.zip)

Or build it from the source:

    $ git clone git://github.com/refuge/rcouch.git
    $ cd rcouch && make rcouchdxmg

To only build the application:

    $ cd rcouch && make rcouchx

Then launch `rcouchx.app` .

Enjoy,

- beno&icirc;t
