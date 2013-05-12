---
layout: post
title: CSV and refuge
---

Hello all,

One of the Refuge goals is to help you process/publish your datasets.
For that reason, Ecsv was created to help you with CSV files.

[Ecsv](https://github.com/refuge/ecsv) is a simple parser that will send the parsed lines to an erlang function.

Example: how to count the lines, just defines the following function:

    MyFun = fun(_NewLine, Counter) ->
        % NewLine contains an array of strings
        Counter + 1.

Then call ecsv with the default state set to `0`:

    {ok, IoDevice} = file:open("/path/to/my.csv", [read]),
    {ok, FinalCounter} = ecsv:process_csv_file_with(IoDevice, MyFun, 0)

`FinalCounter` will have the number of parsed lines.

Take a look at the [README.md](https://github.com/refuge/ecsv/blob/master/README.md) file for more details.

---

The next step will provide a streamlined way to import your csv files without having to specify anything else.

Stay tuned!

~Nicolas (capnemo)
