---
layout: post
title: GeoCouch and Refuge
---

Hello,

Two news about __geocouch__ in [Refuge](http://refuge.io/):

* geocouch has been renamed as [refuge_spatial](https://github.com/refuge/refuge_spatial), and becomes officially a fork of geocouch (if it wasn't already the case ;-) ). The previous geocouch is still available in a different [repository](https://github.com/refuge/geocouch).
* knn query (knn stands for k-nearest-neighbour) ability into refuge_spatial.

knn query gives you the ability to request the n nearest geometries relative to a given query point, with the following parameters:

* `n`: number of geometries being returned
* `q`: the geometry used as reference point
* `spherical=true`: the [Haversine formula](http://en.wikipedia.org/wiki/Haversine_formula) is used to calculate spherical distances for nearest-neighbour-queries. In this case the geometries are expected to use the coordinate system [WGS 84](http://en.wikipedia.org/wiki/WGS_84).

Example: returning 2 nearest geometries to the point `(50,10)` and using spherical distance computation:

    curl -X GET 'http://localhost:5984/places/_design/main/_spatial/points?n=2&q=50,10&spherical=true'

This integration has been adapted from the excellent work done by Tobias Sauerwein (Twitter: [@tsauerwein](https://twitter.com/#!/tsauerwein)) in the branch [knn_1.2.x](https://github.com/tsauerwein/geocouch/tree/knn_1.2.x).

__Have fun!__

Thank you,

Nicolas Dufour <nicolas.dufour@nemoworld.info> (CapNemo)