---
title: "Listing a directory using Python"
timestamp: 2015-02-06T19:30:01
tags:
  - os.listdir
  - sys.argv
  - os.path.join
  - os.path.isdir
  - os.path.isfile
  - os.path.getsize
  - os.stat
published: true
books:
  - python
author: szabgab
archive: true
---


We have seen how to [list a directory using Node.js](/list-content-of-directory-with-nodejs), let's now take a look
at Python.


## List current directory

Given a path to a directory the call to [os.listdir(path)](https://docs.python.org/2/library/os.html#os.listdir) will return the names of the files, directories, symbolic links, etc.
in that directory. In the simple case we can go over the elements using a `for in` loop and print out each one of them:

{% include file="examples/python/ls_plain.py" %}

In order to make the code Python 3 compatible I added `from __future__ import print_function`.
The `path` is hard-code `.` indicating the current directory.

Otherwise the code seems to be straight forward.

## List any directory

In order to make the script more flexible, let's accept an optional(!) directory name on the command line. 

{% include file="examples/python/ls_argv.py" %}

For this we also loaded the `sys` module and looked at the [sys.argv](https://docs.python.org/2/library/sys.html#sys.argv).
This array contains the list of things on the command-line excluding the `python` executable. So the first element (index 0)
of this array is the name of the script, and if the user runs the script with a value on the command line then the length of the
array will be 2 or more.

In this code we have `path = '.'` being the default value of `path`, but if there are two items on the command line,
the script and presumably the path to another directory, then we replace the default value by the value provided on the command line.

The rest of the code is the same.


## Check the inode for further details

In order to provide more information in the directory listing we have to check the inode table of the file.
For this we need the path to the file which the the content of the `path` variable and the name of the file
together. We use the [os.path.join](https://docs.python.org/2/library/os.path.html#os.path.join) method
that can join together two or more pieces of a directory path with the appropriate(!) connecting character.
On Unix/Linux systems this will be a slash `/`, on MS Windows this will be a back-slash `\`
and on other operating systems it might be something else.

```python
    full_path = os.path.join(path, name)
    print(full_path);
```

Then we call the [os.stat](https://docs.python.org/2/library/os.html#os.stat) method with the full path.
It returns an object representing the content of the [inode table](http://en.wikipedia.org/wiki/Inode)
of the give file or directory. This contains all the information about ownership of the file, right various groups
have on the file, timestamps and a few more things.

The `st_size` method of this object returns the size of the file in bytes.

The `inode.st_mode` returns a number representing the rights on this file and the type of this file.
we can use bitwise operations with the appropriate values to know which bit is set.
I wrote a lot more about this in the article about [stat in Node.js](/system-information-about-a-file-or-directory-in-nodejs).

In these two line we check if the given thing is a file or a directory. (We have not dealt with symbolic links
or other things that might be in the filesystem.

```python
    print('  ' + ('f' if inode.st_mode & 0100000 else '-' ))
    print('  ' + ('d' if inode.st_mode & 0040000 else '-' ))
```

In case you are not familiar with this syntax the `A if COND else B` is the ternary operator of Python.

The alternative, and probably much more readable way is to call the
<a  href="https://docs.python.org/2/library/os.path.html#os.path.isdir">os.path.isdir</a>
and [os.path.isfile](https://docs.python.org/2/library/os.path.html#os.path.isfile) for the
appropriate boolean (True or False) value, and to call the
[os.path.getsize](https://docs.python.org/2/library/os.path.html#os.path.getsize) method
to fetch the size of the file.

The full script can be seen here:

{% include file="examples/python/ls.py" %}


## Comments

line 20 gives me an "invalid token" .. specifically the highlighting the 010000 in if stmt.

. I presume its testing whether its a file or directory?
I was doing similar to this getting python to call and run a dir cmd using a bat file.

This way all the code can be contained in the program.
thanks. (Python 3.7, beginner)

---

Do you get a compile time error or a run-time error? If the former, then it might be that the copy-paste inserted some invalid character. Maybe an invalid invisible character.

<hr>

I also had a problem with an invalid token in line 20

and it did not go away until I inserted letter 'o' after the leading zero in these constants

leding zero means OCTAL in C and C++, but it seems that in python one should put 'o' after the leading zero, for octal constants

