---
layout: post
title: View changes since...
---

Quite happy,

After a couple of days to figure how the code of the map/reduce engine was organized. Another days passed to think how adding a btree by sequence to a view group with the help of [@davisp](https://github.com/davisp), I finally have a working patch. It's now possible to **get all changes in a view since**... Tommorrow , I will plug it to the `_changes` feed.

Code is available in [refuge](https://github.com/refuge/couch_mrview/tree/btree_byseq).

Here is a quick example on how to use it:

    (refuge@127.0.0.1)3> F = fun(KV, Acc) -> {ok, [KV|Acc]} end. 
    #Fun<erl_eval.12.111823515>
    (refuge@127.0.0.1)4> 
    (refuge@127.0.0.1)4> couch_mrview:view_changes_since(Db, DDoc, <<"all">>, 9990, F).   
    [info] [<0.220.0>] Opening index for db: testdb idx: _design/test sig: "85b8fa1e39dc7fbe8b11b729b319c6bf"
    {ok,[{10000,{<<"72f9250618e65adc8cf4552758fff137">>,0}},
         {9999,{<<"72f9250618e65adc8cf4552758ffe85d">>,0}},
         {9998,{<<"72f9250618e65adc8cf4552758ffdbcf">>,0}},
         {9997,{<<"72f9250618e65adc8cf4552758ffd65e">>,0}},
         {9996,{<<"72f9250618e65adc8cf4552758ffd611">>,0}},
         {9995,{<<"72f9250618e65adc8cf4552758ffd045">>,0}},
         {9994,{<<"72f9250618e65adc8cf4552758ffc982">>,0}},
         {9993,{<<"72f9250618e65adc8cf4552758ffbfdb">>,0}},
         {9992,{<<"72f9250618e65adc8cf4552758ffb1fc">>,0}},
         {9991,{<<"72f9250618e65adc8cf4552758ffae18">>,0}}]}
    (refuge@127.0.0.1)5>   
    (refuge@127.0.0.1)5> couch_mrview:view_changes_since(Db, DDoc, <<"all">>, 10000, F).    
    {ok,[]}
    (refuge@127.0.0.1)7> couch_mrview:view_changes_since(Db, DDoc, <<"all">>, 10000, F).   
    {ok,[{10002,{<<"31b0c9f8353b6b3e2a86c23d2c000a78">>,0}}]}

enjoy.

- benoît