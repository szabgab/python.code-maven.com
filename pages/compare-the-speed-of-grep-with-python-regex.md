---
title: "Compare the speed of grep with Python regexes"
timestamp: 2020-07-01T08:30:01
tags:
  - grep
  - Python
  - re
  - time
published: true
author: szabgab
archive: true
show_related: true
---


At one of my client we had a Bash script that grepped a huge log file 20 times in order to generate a report.
It created a lot of load on the server as <b>grep</b> was reading the entire file 20 times.

As we were converting our Shell scripts to Python anyway I thought I could rewrite it in Python and go over the file
once instead of 20 times and use the Regex engine of Python to extract the same information.

The Python version should be faster as we all know file I/O is way more expensive than in-memory operations.

After starting conversion it turned out to be incorrect. Our code became way slower. Let's see a simulation of it.


## Generate the big log file

In order to make it easy to reproduce the case I created a script that could create a big text file.

{% include file="examples/python/create-big-file.py" %}

We can run it like this, indicating the name of the file we would like to create,
the number of rows and the length of rows.

```
python create-big-file.py FILENAME NUMBER-OF-ROWS LENGTH-OF-ROWS
```

It will create a file full of the character "x", with a single "y" somewhere.

I think this is going to be good enough for our simple example.

## Using grep

In the original shell script we had some 20 different calls to <b>grep</b>,
but to make it simpler I made this shell script with that runs the same regex multiple times.

{% include file="examples/grep_speed.sh" %}

You can pass the name of the data file and the number of time you'd like to run <b>grep</b>.

## Grep with Python regexes

I have an implementation in Python as well.

{% include file="examples/grep_speed.py" %}

I know in the simple case of finding a single "y" character I could use the
<a href="https://code-maven.com/slides/python/index-in-string"><b>index</b></a> method
or the <a href="https://code-maven.com/slides/python/find-in-string"><b>find</b></a> method
and thous would be probably faster, but in our cases we really had more complex regexes.


## Comparing the speed

```
python create-big-file.py a.txt 100000 50
```

Verify the file:

```
$ wc a.txt
 1000000  1000000 51000000 a.txt
```

```
# grep y a.txt
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxyx
```

```
$ time bash examples/grep_speed.sh a.txt 20

real  0m0.227s
user  0m0.055s
sys   0m0.172s
```


```
$ time python examples/grep_speed.py a.txt 20

real  0m9.509s
user  0m9.477s
sys   0m0.032s
```


<b>grep</b> is about 50 times faster than Python even though <b>grep</b> had to read the file 20 time while Python only read it once.


## More complex grep

In the previous case we used a very simple regex, now let's change it to use a slightly more complex expression
in which we are not only looking for a single character, but we also want to make sure it is between two
identical characters.

{% include file="examples/grep_speed_oxo.sh" %}

## More complex python

{% include file="examples/grep_speed_oxo.py" %}

You can try it yourself:

```
grep '\(.\)y\1' a.txt
```


## Comparing the speed of the more complex examples

```
$ time bash examples/grep_speed_oxo.sh a.txt 20

real   0m0.196s
user   0m0.035s
sys    0m0.161s
```


```
$ time python examples/grep_speed_oxo.py a.txt 20

real   0m25.067s
user   0m24.972s
sys    0m0.016s
```

The speed of <b>grep</b> did not change, but Python became even slower. This time grep is more than a 100 times faster than Python.

## Version information

```
$ python -V
Python 3.8.2
```

```
$ grep -V
grep (GNU grep) 3.4
```


## Other cases

The results are consistent with what I saw during my work, but I wonder what would be the results if the file was larger than the available memory in my computer.

## Conclusion

<b>grep</b> is so much faster than the regex engine of Python that even reading the whole file several times does not matter.

Or I made a mistake somewhere that impacts the results.

Oh and one more thing, I also create a [Perl](https://perlmaven.com/) version of the code and
[Perl is much faster than Python](https://perlmaven.com/compare-the-speed-of-perl-and-python-regex)
even though it is also slower than the <b>grep</b> code.

