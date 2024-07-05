---
title: Change the modify date of a file using Python (touch)
timestamp: 2024-07-05T16:10:01
author: szabgab
published: true
description: Get the modify time of a file and set all the timestamps of a file.
tags:
    - stat
    - utime
    - getmtime
---

## The 4 dates of a file on ext4

For a long time Unix/Linux filesystems maintained 3 dates for each file. Apparently the `ext4` filesystem has a 4th. We can use the `stat` command to show these dates.

Create a file
```
$ echo hello > file.txt

$ stat file.txt
Access: 2024-07-05 16:03:28.377121409 +0300
Modify: 2024-07-05 16:03:28.377121409 +0300
Change: 2024-07-05 16:03:28.377121409 +0300
 Birth: 2024-07-05 16:03:28.377121409 +0300
```

Changing the meta-data of the file updates the `ctime` field displayed as "Change" here:

```
$ chmod a+x file.txt

$ stat file.txt
Access: 2024-07-05 16:03:28.377121409 +0300
Modify: 2024-07-05 16:03:28.377121409 +0300
Change: 2024-07-05 16:04:02.922123687 +0300
 Birth: 2024-07-05 16:03:28.377121409 +0300
```


Changing the content of the file, eg. adding more content will update the `mtime` field displayed as Modify" and the "ctime" or "Change" field:

```
$ echo world >> file.txt

$ stat file.txt
Access: 2024-07-05 16:03:28.377121409 +0300
Modify: 2024-07-05 16:04:50.697126837 +0300
Change: 2024-07-05 16:04:50.697126837 +0300
 Birth: 2024-07-05 16:03:28.377121409 +0300
```

Reading the content of the file updates the `atime` field displayed as "Access".

```
$ cat file.txt

$ stat file.txt

Access: 2024-07-05 16:06:21.051132794 +0300
Modify: 2024-07-05 16:04:50.697126837 +0300
Change: 2024-07-05 16:04:50.697126837 +0300
 Birth: 2024-07-05 16:03:28.377121409 +0300
```

Finally there is the `touch` command of Unix/Linux that does not change the content of the file, but updates all 3
timestams.

```
$ touch file.txt

$ stat file.txt

Access: 2024-07-05 16:09:02.075143411 +0300
Modify: 2024-07-05 16:09:02.075143411 +0300
Change: 2024-07-05 16:09:02.075143411 +0300
 Birth: 2024-07-05 16:03:28.377121409 +0300

```

## Update timestamps using Python


```
>>> file = "file.txt"
>>> os.utime(file)
```

```
$ stat file.txt

Access: 2024-07-05 16:11:08.352151736 +0300
Modify: 2024-07-05 16:11:08.352151736 +0300
Change: 2024-07-05 16:11:08.352151736 +0300
 Birth: 2024-07-05 16:03:28.377121409 +0300
```


## Get the modify time in Python

```python
import os
print(os.path.getmtime("file.txt"))
```

```
1720185068.3521516
```

## Showing the elapsed time since the file was modified

```python
import os
import time

print(time.time() - os.path.getmtime("file.txt"))
```

```
137.15206933021545
```


