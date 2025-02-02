---
title: "Python Programming Bootcamp for Scientists"
timestamp: 2020-08-11T16:20:01
tags:
  - Bootcamp
published: true
author: szabgab
types:
  - screencast
description: "Introduction to programming in Python for people with not or very limited programming background who would like to use this for scientific computations."
archive: true
show_related: false
---


People studying Chemistry, Biology, Physics, Life Sciences and a whole lot of other sciences will have a lot of need in processing and analyzing the data they collected.
This involves a lot of manual work, but plenty of this can be automated. There are many ready-made applications that can handle some of the computations, but there are even
more that need special treatment.

This course was designed to be given at the [Weizmann Institute of Science](https://www.weizmann.ac.il/) in Rehovot, Israel.
It includes a basic Python course with specific extensions for scientific computational needs. It also touches other areas of
programming that can help scientists to use software the best possible way they can.

The recordings include clarifying questions and the solution of the exercises by [Nóra Doleschall](https://www.linkedin.com/in/nora-doleschall/).

The slides used during the recording are available [here](/slides/python).

<h3>Projects</h2>

At the end of the Bootcamp each student is required to work on a project of their own. After they are done with the project some of them agreed to have video recording in which they
explain their project and we discuss the code. These videos are here for your enjoyment and to give inspiration of what you can do after the bootcamp.

* [Basic modification of Biological data frames using Pandas](/bootcamp-shelley-klompus) by Shelley Klompus
* [Managing jobs in a PBS cluster using Python](/managing-jobs-in-a-pbs-cluster) by Oz Mendelsohn
* [Command line accounting in Python](/command-line-accounting-in-python) by Olga Tapinova
* [Getting started with Git and GitHub](/getting-started-with-git-and-github-on-windows) with Olga Tapinova
* [Fixing elevation data in gpx file](https://he.code-maven.com/fixing-elevation-data-in-gpx-file) by Nathan Weinstein (Hebrew)
* [Getting started with Git and GitHub](https://he.code-maven.com/creating-project-on-github) with Nathan Weinstein (Hebrew)
<!--
* <a href=""></a>
-->


<h3>What to watch and in which order to watch?</h3>

The videos are in the order we recorded them. They are more-or-less along the lines of the chapters, except at the beginning where some chapters are split into multiple videos and some
videos contain parts from multiple chapters.

* There are timestamps on this page pointing you where each sections starts.
* Many sections contain discussions about solving the exercises. I think they can be very useful after you solved the respective exercise, but you can learn the material without them too.
* Part 40 is towards the end, but it can give you a lot of background about programming so you might want to watch it early.
* The Tk video (Part 30) is extra, you don't necessarily need it to complete the course.
* The PyCharm chapter is Part 34, but you might want to watch it earlier, maybe as soon as after Part 10, and then switch to use PyCharm instead of Notepad++
* The Jupyter notebook is Part 42, you might want to watch it earlier. Maybe before SciPy in Part 37.


## Videos


* [Part 1](/programming-bootcamp-for-scientists-1) (27:51 min)
        <ul>
* 00:00 Introduction to the Bootcamp.
* 01:37 Nóra Doleschall introduces herself and her background in programming.
* 02:47 Overview of the Bootcamp. (Programming Python, Computer architecture, Version Control System)
* 08:04 About [Code-Maven](/), all the [slides](/slides), the [Python slides](/slides/python).
* 09:38 Showing the Windows command line and the file explorer
* 15:20 Keyboard shortcuts for the slides
* 16:48 Keyboard shortcuts on YouTube
* 17:37 Start talking about the slides
* 17:55 What is Python?
* 20:14 What is needed to write a program?
* 24:08 The source code of Python
* 26:00 Open Source
        </ul>
        
* [Part 2](/programming-bootcamp-for-scientists-2) (50:12 min)
        <ul>
* 00:00 The beginning of the "First steps" chapter.
* 00:55 Python 2 vs. Python 3 - Why is it important to know about Python 2.
* 04:00 Installing Python.
* 04:10 Linux
* 05:17 Apple Mac OSX [Homebrew](https://brew.sh/)
* 06:38 MS Windows [Anaconda](https://www.anaconda.com/products/individual) 64 bit vs 32 bit.
* 12:57 Verify the installation in Anaconda Prompt. Configure the color of the window.
* 17:26 Editor, IDE for Python
* 19:56 Documentation of Python, search engines, Stack Overflow
* 23:45 Program types
* 28:13 Python on the command line
* 29:53 Hello World! - Writing our first program in Python.
* 36:00 TAB completion on the Windows command line.
* 37:40 Windows file explorer - make the file extensions and the hidden files visible.
* 41:00 File extensions and Syntax highlighting in Notepad++.
* 43:50 How to download all the examples from GitHub
* 47:00 Comments
* 48:45 Variables
* 49:53 Exercise: Hello World
        </ul>
        
* [Part 3](/programming-bootcamp-for-scientists-3) (49:29 min)
        <ul>
* 00:00 More in the "First steps" chapter
* 00:47 Nóra had a couple of questions:
* &nbsp;&nbsp;&nbsp;&nbsp; Should we use Atom as an editor?
* &nbsp;&nbsp;&nbsp;&nbsp; Should we use Python downloaded from Python.org?
* &nbsp;&nbsp;&nbsp;&nbsp; What if we have two installations of Python on our computer?
* &nbsp;&nbsp;&nbsp;&nbsp; What other editors and programming environments to use?
* 11:20 Asking questions?
* 12:15 What is programming?
* 18:05 What are the programming languages?
* 22:05 Let's eat grandpa! Words and punctuation matter!
* 22:35 Literals, Value Types - The consistency of single- and double-quotes.
* 30:20 Running the script using a relative path. Showing exceptions (runtime errors) and how to try to understand them.
* 34:00 How to search for explanation about an exception. How to interpret what we see in StackOverflow.
* 39:30 The type system in Python and other languages.
* 40:50 The floating point error
* 43:40 Value Types in Numpy, Binary (base 2) representation of numbers.
        </ul>
        
* [Part 4](/programming-bootcamp-for-scientists-4) (10.01 min)
        <ul>
* 00:00 The end of the "First steps" chapter.
* 01:20 Variables. Assignment. Multiplying numbers.
* 03:20 Multiply two string. (Ctrl-g is used in many editors to go to a line-number)
* 05:50 Adding numbers together.
* 06:10 Adding strings together. (concatenation)
* 08:23 Exercises: Calculations
        </ul>
        
* [Part 5](/programming-bootcamp-for-scientists-5) (43:33 min)
        <ul>
* 00:00 Keyboard shortcuts for the slides
* 01:25 Reviewing the exercises from the previous chapter. Talking about operator precedence.
* 04:09 The math module of Python. Attributes and methods.
* 09:45 The Python interactive shell (REPL).
* 19:40 The beginning of the "Second steps" chapter up till "Conditional main".
* 19:55 Modules - the sys module, getsizeof.
* 30:00 The main function, indentation.
* 35:25 Can a function be named the same name as an already existing function?
* 37:10 Indentation
* 38:36 Conditional main (dunderscore) (error correction: those are quotations around "__main_"_ not parentheses.)
        </ul>
        
* [Part 6](/programming-bootcamp-for-scientists-6) (1:00:37 min)
        <ul>
* 00:00 "Second steps" starting at Input/Output till the exercises.
* 00:00 Input - Output I/O
* 05:23 print in Python 2
* 08:12 print in Python 3
* 13:00 from __future__ import print_function
* 14:57 Exception: SyntaxError: Missing parentheses in call
* 15:50 Prompting for user input in Python 2 (raw_input)
* 19:20 Prompting for user input in Python 3 (input)
* 26:01 Prompting in both Python 2 and Python 3.
* 28:45 Add numbers entered by the user.
* 32:30 How can I check if a string can be converted to a number?
* 37:26 Nóra pointing out the error in the previous example. Oups.
* 38:23 Converting string to int
* 41:49 Conditionals: if, else, elif
* 53:20 Ternary operator (Conditional Operator)
* 56:00 Case and switch in Python.
* 56:30 Exercises: Rectangle, Circle, Calculator
* 57:40 Learning Python the Hard way.
        </ul>
        
* [Part 7](/programming-bootcamp-for-scientists-7) (44:19 min)
        <ul>
* 00:00 Review of the previous chapter, answering questions raised during the previous video.
* 00:50 Power of. About forgetting language constructs.
* 02:50 Check if a string can be converted to a float.
* 07:45 Solution of the area of rectangle exercise.
* 13:57 Solution of calculator exercise.
* 20:10 Command line arguments
* 32:10 Command line arguments - len
* 34:00 Showing [PyPi](https://pypi.org/)
* 35:03 Command line and exit. Usage. Exit code.
* 41:25 Continuous Integration systems.
* 43:20 Exercises: Rectangle, Calculator.
        </ul>
        
* [Part 8](/programming-bootcamp-for-scientists-8) (55:40 min)
        <ul>
* 00:00 Solutions of the Rectangle and Calculator exercises.
* 03:30 Solution of Calculator with eval and why not to use eval.
* 08:25 Compilation vs. Interpretation
* 16:00 Is Python compiled or interpreted?
* 20:50 Flake 8 static code analysis (linter).
* 22:10 Numbers chapter
* 25:10 Operators for Numbers
* 30:08 Integer division and the __future__
* 30:50 Pseudo Random numbers (uniform distribution)
* 35:38 Fixed Random numbers (seed)
* 37:56 Rolling dice - randrange
* 40:41 Random choice
* 41:40 built-in method
* 45:19 Exception: TypeError: 'module' object is not callable
* 48:30 Exception: AttributeError: module 'random' has no attribute
* 52:28 Exercises: Number guessing game; Fruit salad
        </ul>
        
* [Part 9](/programming-bootcamp-for-scientists-9) (51:25 min)
        <ul>
* 00:00 Intro to this video
* 02:10 How to get MS Windows not to close the cmd when the program ends?
* 04:00 Associate file extension with a program in MS Windows
* 09:30 Solution of Number guessing game level 0.
* 13:38 Solution of Fruit Salad.
* 19:05 Comparison and Boolean
* 20:30 Comparison operators
* 20:40 Compare numbers, compare strings (ASCII, Unicode)
* 24:35 Do NOT Compare different types!
* 28:03 Complex if statement with boolean operators (and, or, not)
* 31:14 Boolean truth tables
* 32:08 Boolean values: True and False
* 35:00 Flag
* 37:15 Toggle
* 38:10 Short circuit
* 42:10 Does this value count as True or False?
* 43:15 True and False values in Python
* 43:58 Incorrect use of conditions
* 45:49 "False" is True
* 48:02 What is the type of True and False?
* 49:10 Exercises: compare numbers; compare strings
        </ul>
        
* [Part 10](/programming-bootcamp-for-scientists-10) (1:18:52 min)
        <ul>
* 00:00 Solution to compare numbers
* 03:57 Solution to compare strings
* 08:00 Nóra explains her solutions using functions
* 13:10 Refactoring
* 19:27 Start the chapter Strings
* 19:38 Single quoted and double quoted strings
* 21:19 Triple quoted strings (multiline strings)
* 21:47 What would you do if you wanted to print a quote character? Escaping quotes. \n, \t
* 26:43 Is it OK to TABs instead of spaces for indenting Python code? Indentation examples. Notepad++ show whitespaces.
* 35:13 String length (len)
* 35:36 String repetition and concatenation
* 37:18 A character in a string.
* 38:00 Is a string a list? No, it's a Sequence.
* 39:00 String slice (instead of substr)
* 41:58 Change a string - Strings are immutable
* 44:20 String copy
* 47:05 String functions and methods (len, upper, lower)
* 49:30 All the built-in functions of Python
* 50:29 index and rindex in string
* 58:24 When the string is not found we get an exception. How can we prevent it?
* 59:16 find in string
* 1:00:39 in string
* 1:03:51 Encodings: ASCII, Windows-1255, Unicode
* 1:09:32 raw strings
* 1:14:42 ord
* 1:16:16 chr - number to character
* 1:16:45 Exercises
        </ul>
        
* [Part 11](/programming-bootcamp-for-scientists-11) (1:02:56 min)
        <ul>
* 00:00 Solving the exercise: one string in another string.
* 04:32 Solving the exercise: compare strings. Including Nóra finding a bug in my solution and fixing it.
* 12:27 Solving the exercise: ASCII CLI.
* 13:00 Loops chapter
* 14:23 for-in and while loops.
* 15:49 for-in loop on strings.
* 18:17 for-in loop on lists.
* 19:33 for-in loop on range.
* 22:58 for-in loop with early end using break.
* 26:08 for-in loop skipping parts using continue
* 28:06 for-in loop with break and continue.
* 30:58 while loop.
* 32:30 Infinite while loop.
* 34:25 while with complex expression.
* 35:28 while with break
* 38:34 De Morgan's law
* 40:25 while True
* 42:12 Duplicate input call.
* 45:11 Eliminate duplicate input call.
* 46:05 do while loop.
* 47:30 while with many continue calls.
* 50:28 Exit vs. return vs. break and continue.
* 52:25 Exercises.
        </ul>
        
* [Part 12](/programming-bootcamp-for-scientists-12) (51:31 min)
        <ul>
* 00:00 Nóra solves the exercises of the Loop chapter.
* 02:00 Solution for exercise: Print all the locations in a string
* 16:27 Solution for exercise: Number guessing game.
* 40:40 Solution for exercise: Count unique characters. (also using sets)
* 45:10 What is the difference between == and the "is" operator?
        </ul>
        
* [Part 13](/programming-bootcamp-for-scientists-13) (20:38 min)
        <ul>
* 00:00 Nóra solves the rest of the levels of the number guessing game in the Loops chapter.
        </ul>
        
* [Part 14](/programming-bootcamp-for-scientists-14) (1:01:23 min)
        <ul>
* 00:00 Intro.
* 01:14 Formatted Printing.
* 01:48 format - sprintf
* 08:31 Examples using format - indexing
* 09:00 Examples using format with names
* 09:36 Format columns
* 15:00 Examples using format - alignment
* 16:18 Format - string
* 17:15 Format characters and types.
* 18:05 Format floating point numbers.
* 18:46 f-strings (formatted string literals).
* 21:01 raw f-strings.
* 22:40 What would you use in a GUI? - Templates.
* 
* 25:02 First part of the List chapter.
* 29:00 Access single element of a list, access sublist (slice) of a list.
* 31:26 List slice with steps.
* 33:52 Change the content of a list.
* 37:25 Change with steps.
* 38:44 List assignment and list copy. (shallow copy, deep copy)
* 48:51 join
* 51:30 join list of numbers (also show map, str, and list comprehension)
* 56:59 split (divide strings, separate parts of a string).
        </ul>
        
* [Part 15](/programming-bootcamp-for-scientists-15) (32:56 min)
        <ul>
* 00:00 Lists chapter from split till first exercises.
* 00:50 for loop on lists (for in)
* 02:25 in list (in)
* 03:00 Where is the element in the list  (index)
* 05:25 Index improved
* 06:30 insert element into list (insert)
* 08:25 append element to the end of a list (append)
* 08:45 remove element from list by value. (remove)
* 10:15 remove element from list by location (by index) (pop)
* 11:35 Why is it called pop?  (Discussing queues FIFO and stacks LIFO)
* 14:24 Remove first element of a list (shift, pop(0))
* 15:20 Remove several elements, a sublist, from a list.
* 16:48 Use a list as a queue.
* 20:27 Use deque from collections to be a queue.
* 23:20 Use a list as a stack.
* 24:50 Use deque from collections to be a stack.
* 25:30 Exercise: Queue
* 27:00 Exercise: Stack (Reverse Polish Calculator)
* 31:15 Exercise: MasterMind
        </ul>
        
* [Part 16](/programming-bootcamp-for-scientists-16) (24:13 min)
        <ul>
* 00:00 Nóra solving the exercises in the middle of the Lists chapter
* 01:00 Solution: Queue
* 07:10 Solution: Stack (Reverse Polish Calculator)
* 16:35 Solution: MasterMind
        </ul>
        
* [Part 17](/programming-bootcamp-for-scientists-17) (37:38 min)
        <ul>
* 00:00 The second part of the Lists chapter.
* 01:10 About debugging
* 06:20 sort
* 07:30 sort numbers
* 08:57 sort mixed list
* 09:37 sort (key)
* 11:05 sort with sorted
* 14:15 range
* 15:56 Looping over index
* 18:25 Enumerate lists (go over lists using index-value pairs)
* 19:57 List operators
* 22:11 List of lists
* 24:36 List assignment
* 26:30 Tuples
* 28:00 Sort Tuples
* 30:00 Exercise: color selector menu
* 32:22 Exercise: count digits
* 33:15 Exercise: create list
* 34:00 Exercise: count words
* 34:47 Exercise: check if number is prime
* 35:00 Exercise: DNA sequencing
        </ul>
        
* [Part 18](/programming-bootcamp-for-scientists-18) (1:25:42 min)
        <ul>
* 00:00 Reviewing the exercises at the end of the lists chapter.
* 01:23 Solution: color selector menu
* 24:45 Solution: count digits
* 28:55 Solution: create list (also using sets)
* 41:00 Solution: count words
* 45:12 Discussing Algorithm complexity.
* 53:40 Solution: check if a number is prime
* 1:08:20 Solution: DNA sequencing
        </ul>
        
* [Part 19](/programming-bootcamp-for-scientists-19) (1:02:22 min)
        <ul>
* 00:00 The Files chapter
* 00:45 File types: Text vs. Binary - Images, Excel files, text files
* 04:15 Open vs. Read vs. Load
* 06:15 Binary files: Images
* 10:50 Reading an Excel file
* 14:49 Open and read file (easy but not recommended)
* 20:45 Open and read file using "with" (recommended)
* 23:14 Read file remove newlines
* 27:22 Filename on the command line
* 28:00 Filehandle with return
* 33:29 Read all the lines into a list
* 35:45 Read all the characters of a file into a single string (slurp)
* 37:00 Not existing file
* 37:50 Open file exception handling
* 40:00 Exception hierarchy of Python
* 43:05 Open many files - exception handling
* 46:47 Writing to a file
* 48:23 Append to a file
* 51:30 Binary mode
* 53:57 Does the file exist? Is it a file?
* 50:50 Direct access of a line in a file
* 57:50 Exercise: count numbers
* 58:20 Exercise: strip newlines
* 58:35 Exercise: color selector
* 59:12 Exercise: ROT13
* 01:01:05 Exercise: combine lists
        </ul>
        
* [Part 20](/programming-bootcamp-for-scientists-20) (1:08:14 min)
        <ul>
* 00:00 The solutions for the exercises in the files chapter
* 01:20 Solution: count numbers
* 05:30 Solution: strip newlines
* 06:17 Solution: color selector and fixing an interesting bug.
* 17:10 Solution: ROT13, discussing open with r+, and how filehandle works.
* 27:25 Solution: combine lists, trying various solutions, including one using sets and one using tuples. Sorting using lambda function.
* 1:04:10 Exercise: print lines with Report
* 1:06:30 return from a function can return a value
        </ul>
        
* [Part 21](/programming-bootcamp-for-scientists-21) (52:04 min)
        <ul>
* 00:00 Dictionaries
* 00:40 Windows: mapping file extensions (.py) to an action in Windows File Explorer; The "where" command of Windows.
* 05:15 What is a Dictionary? ( Hash, Mapcar)
* 06:40 When to use Dictionaries?
* 07:31 Create dictionary
* 10:05 Dictionary keys
* 10:48 Loop over keys()
* 11:26 Loop using items()
* 12:25 Dictionary values()
* 12:50 Not existing key
* 13:15 Get key - get()
* 16:20 Does the key exist? (in)
* 17:05 How can you search among the values? Does the value exist? - values()
* 19:00 How dictionaries work? What is hashing?
* 23:25 Delete key (del, pop)
* 25:25 List of dictionaries
* 29:35 In the lambda/map case we did not use key= while in the sort-case we did. Why?
* 31:35 Shared dictionary - skipped
* 31:55 tuples as dictionary keys
* 32:35 numbers as dictionary keys
* 32:45 Sort dictionary by value
* 38:00 So at the end, are the keys kept in order in the dictionary or not?
* 40:42 A few more words about hashing. Hashing algorithms: (md5, sha1). Comparing files.
* 42:55 Dictionaries vs. lists.
* 43:40 Exercise: count characters
* 44:20 Exercise: count words
* 44:50 Exercise: count words from a file
* 45:10 Apache log
* 47:13 Exercise: combine lists again
* 47:33 Exercise: counting DNA bases
* 48:03 Exercise: count Amino Acids
* 48:19 Exercise: List of dictionaries
* 50:00 Exercise: Dictionary of dictionaries
* 50:40 Exercise: Age limit with dictionaries
        </ul>
        
* [Part 22](/programming-bootcamp-for-scientists-22) (42:42 min)
        <ul>
* 00:00 Nóra solving the exercises from the Dictionaries chapter
* 01:00 Solution: count characters
* 05:30 Looking for defaultdict solution
* 08:20 Solution: count characters from a file
* 20:25 Solution: count words
* 20:50 Solution: count words from a file
* 28:00 Comparing the solutions using two lists with the solution using a dictionary. Discussing complexity again.
* 33:45 Solution: Apache log - how to use split()
* 40:57 Solution: combine lists (combine files)
        </ul>
        
* [Part 23](/programming-bootcamp-for-scientists-23) (38:55 min)
        <ul>
* 00:00 Nóra solving the exercises from the Dictionaries chapter
* 00:25 Solution: DNA base counter
* 04:00 Solution: count Amino Acids
* 15:35 Solution: List of dictionaries, the csv module
* 24:05 Solution: Dictionary of dictionaries
* 26:45 Solution: Age limit with dictionaries
* 30:35 Y2K bug, Bug 2000, Year 2038 problem
        </ul>
        
* [Part 24](/programming-bootcamp-for-scientists-24) (16:12 min)
        <ul>
* 00:00 The sets chapter
* 02:45 Creating a set
* 05:00 Creating and empty set.
* 05:25 Adding element to a set. (add)
* 06:00 Merging one set into another set. (update)
* 09:23 intersection
* 10:38 subset
* 11:05 symmetric difference
* 11:40 union
* 12:44 What is the difference between union and update?
* 13:20 relative complement
        </ul>
        
* [Part 25](/programming-bootcamp-for-scientists-25) (1:17:23 min)
        <ul>
* 00:00 The Functions chapter
* 00:40 Why use functions?
* 04:33 Defining simple function
* 08:28 Functions - pass parameters by position.
* 10:11 Functions - pass parameters by name.
* 11:43 Mixing positional and named parameters.
* 15:20 Default values, optional parameters
* 19:18 Several defaults, using names
* 21:04 Arbitrary number of arguments *
* 26:45 Fixed parameters come before the others.
* 28:00 Arbitrary key-value pairs in parameters **
* 30:50 Extra key-value pairs in parameters
* 31:10 Every parameter option
* 32:11 Duplicate declaration of functions
* 38:03 Recursive functions (recursive factorial)
* 46:00 Recursive Fibonacci function
* 49:30 Non-recursive Fibonacci
* 51:50 Unbound recursion
* 53:18 Variable assignment and change - immutable, mutable
* 55:35 Parameter passing of functions
* 1:00:20 Function documentation
* 1:01:17 Copy-paste code
* 1:07:00 Exercises
* 1:07:24 Returning multiple values from a function
* 1:13:00 Exercise: Merge and Bubble sort
* 1:15:23 Exercise: Refactor earlier solutions to use functions.
        </ul>
        
* [Part 26](/programming-bootcamp-for-scientists-26) (58:03 min)
        <ul>
* 00:00 Solutions for the exercises in the Functions chapter
* 00:40 Solution: Function returning Statistics
* 04:30 The _ placeholder variable
* 07:25 Solution: Recursive function to show dependency tree
* 12:03 Solution: Tower of Hanoi - skipping
* 12:20 Solution: Bubble sort (sort-of)
* 31:50 Solution: Merge sort
        </ul>
        
* [Part 27](/programming-bootcamp-for-scientists-27) (50:39 min)
        <ul>
* 00:00 The Modules chapter
* 00:30 Goals of having modules
* 04:00 Before modules (a function in a single-file program)
* 04:34 Creating modules: Separating the above program in to module and executable. (import, from)
* 05:40 How does Python find the module to be loaded?
* 07:56 Importing and aliasing module name (as)
* 11:25 path to load modules from - the module search path
* 12:30 sys.path the module search path
* 13:45 Flat project directory structure
* 14:39 Relative paths (Why is the directory called 'bin'?
* 16:30 Absolute path and why it is not a good practice
* 18:45 Back to the relative path and explaining how it works (os.path.join, os.path.abspath, os.path.dirname, __file__)
* 24:13 Mentioning modules in directory hierarchy (submodules) but not showing them. Since then, there is already a slide with that example.
* 24:46 Python modules are compiles .pyc files, __pycache__ directory.
* 28:30 Caching
* 30:40 How "import" and "from" work?
* 31:20 Runtime loading of modules
* 33:30 When you import a module, will Python find it eventually?
* 35:13 Conditional loading of modules
* 37:18 Duplicate importing of functions (pylint)
* 40:50 Script or library (script or module) (__name__, __main__)
* 47:00 Import the same module multiple times
* 48:14 Exercises: Convert the earlier solutions to be modules and programs.
        </ul>
        
* [Part 28](/programming-bootcamp-for-scientists-28) (28:01 min)
        <ul>
* 00:00 CSV
* 00:40 Reading CSV in the naive way (split)
* 04:20 What is sys.stderr.write ? (Standard Output, Standard Error)
* 09:50 CSV with quotes and with newlines
* 12:35 Reading CSV file using the csv module (reader, delimiter)
* 17:40 Report when there is an error in the CSV file (strict mode)
* 19:24 CSV to dictionary (DictReader)
* 24:15 CSV Attributes
* 25:30 CSV dialects
* 27:00 Exercise: CSV
        </ul>
        
* [Part 29](/programming-bootcamp-for-scientists-29) (27:51 min)
        <ul>
* 00:00 Excel files
* 00:44 Spreadsheets in general
* 01:35 Python Excel
* 03:12 Created an Excel file from scratch (openpyxl)
* 06:55 Installing a module using pip
* 10:10 Worksheets in Excel
* 12:55 Color Selector
* 14:35 Add expression to Excel
* 17:25 Number series and chart
* 23:35 Read Excel file
* 25:32 Update Excel file
* 26:35 Exercises
        </ul>
        
* [Part 30](/programming-bootcamp-for-scientists-30) (1:08:29 min)
        <ul>
* 00:00 Python Tk for GUI
* 00:45 Python Tk Demo
* 07:00 Simple File dialog
* 09:50 GUI Toolkits
* 12:18 Installation
* 12:45 Documentation
* 13:30 Button (main loop, event loop)
* 17:43 Button with action
* 21:50 Label
* 22:38 Label - font size and color
* 24:00 Keybinding
* 25:57 Entry (one-line text entry)
* 27:03 Entry for passwords and other secrets (hidden text)
* 27:27 Checkbox (Checkbutton) (BooleanVar)
* 31:33 Radiobutton  (IntVar)
* 34:13 Listbox
* 36:31 Listbox Multiple choice
* 37:45 Menu and Menubar
* 43:33 Text widget
* 45:26 Dialogs (File selector)
* 46:40 Messagebox
* 50:12 Combobox
* 51:33 OptionMenu
* 51:47 Scale (Horizontal and Vertical)
* 52:35 Progressbar
* 52:50 Frame
* 54:14 Runner
* 56:01 Runner with threads
* 58:00 Exercises
* 1:01:20 Configuring Windows not to show the cmd window when running a Tk-based application.
* 1:04:30 Update the Text widget in the Demo
        </ul>
        
* [Part 31](/programming-bootcamp-for-scientists-31) (1:00:58 min)
        <ul>
* 00:00 Regular Expressions (part I)
* 01:10 What are regexes?
* 03:40 What are Regular Expressions good for?
* 07:35 Examples
* 09:50 Where can I use Regexes?
* 12:10 grep
* 15:49 Regexes first match
* 19:30 Match numbers
* 21:30 What happens if there are multiple hits, multiple matches?
* 22:40 Why did we match the first set of digits and how to convince it to match the other set of digits?
* 23:58 Capture (group, groups)
* 25:45 How can you match parentheses? (remove the special meaning of the parentheses)
* 28:30 Capture more (multiple pair of parentheses)
* 31:08 Capture even more (parentheses inside parentheses)
* 31:40 findall
* 34:05 findall with capture
* 35:50 findall with capture more than one pair of parentheses
* 37:13 Any Character (dot)
* 40:50 Match a dot
* 41:21 Character Classes
* 45:05 Common Character Classes
* 49:46 Match digits
* 52:35 Match Word characters
* 53:38 Negated character classes
* 55:54 Optional character (the ? quantifier)
* 57:24 0 or more (the * quantifier)
* 58:34 Quantifiers
        </ul>
        
* [Part 32](/programming-bootcamp-for-scientists-32) (1:31:51 min)
        <ul>
* 00:00 Regular Expressions (part II)
* 00:35 Quantifier limit
* 03:39 Quantifiers on character classes
* 05:35 Greedy Quantifiers
* 09:16 Minimal quantifiers
* 13:35 Anchors
* 18:10 Anchors - edge of word
* 24:47 Match ISBN numbers
* 30:53 Matching a section (minimal match, negated character class)
* 35:04 DOTALL (single line)
* 37:55 MULTILINE
* 42:15 Two regex with logical or
* 43:20 Alternatives |
* 43:57 Grouping and Alternatives
* 45:02 Regex internal variables
* 52:00 Regex to match DNA
* 56:40 IGNORECASE
* 56:54 VERBOSE
* 1:00:20 Substitution
* 1:05:35 Fixing dates
* 1:10:10 Double the numbers (duplicate)
* 1:13:37 Remove spaces
* 1:14:00 Replace string in Assembly code
* 1:23:56 Split with regex
* 1:26:20 Exercises
        </ul>
        
* [Part 33](/programming-bootcamp-for-scientists-33) (1:00:17 min)
        <ul>
* 00:00 Solutions of exercises in Regular Expressions
* 01:50 Solutions for Regexes Part 1
* 03:17 Using global and how to avoid it. Moving everything inside functions.
* 09:13 Solutions for Regexes Part 1 (continue)
* 24:54 Solutions for Regexes Part 2 (matching decimal, hexadecimal numbers)
* 28:20 compile regex
* 30:35 Solutions for Regexes Part 2 (matching negative, floating point, octal and binary numbers) a negative look-behind!
* 42:00 Solution: Sorting SNMP numbers; Parse hours log file and create report
* 44:40 Solution: Parse config INI files.
* 54:00 Solution: Replace Python
* 55:05 Solution: Match phone numbers
        </ul>
        
* [Part 34](/programming-bootcamp-for-scientists-34) (1:00:34 min)
        <ul>
* 00:00 PyCharm
* 01:15 Download and Install PyCharm
* 02:27 What is PyCharm and why would you want to use it?
* 04:00 Projects (.idea dir)
* 07:33 Configuring the correct Python installation, Python interpreter
* 13:33 Installing Python packages using PyCharm
* 15:08 Opening file
* 15:50 PEP 8 complaining
* 18:05 requirements.txt and PyCharm offering to install dependencies
* 19:20 Edit file, Run program
* 20:15 Terminal in PyCharm
* 20:32 Open a second file, Run program
* 25:10 Locate and open a file with Ctrl-Shift-N
* 29:55 How to pass command line argument to a program in PyCharm?
* 31:25 Debugging (unconditional breakpoint)
* 33:45 Step into
* 35:45 Step out
* 36:55 Step over
* 41:00 Conditional breakpoint
* 44:20 Set environment variables
* 52:37 Terminal
* 52:50 Console (Interactive shell; IPython)
* 53:10 TODO
* 54:20 Refactoring: Rename variable
* 57:15 Refactoring: Extract method
        </ul>
        
* [Part 35](/programming-bootcamp-for-scientists-35) (47:13 min)
        <ul>
* 00:00 Standard module (standard packages) (slides changed a lot since video recording)
* 00:42 Some standard packages
* 02:58 sys
* 05:14 Writing to the standard error (stderr) and command line redirection
* 10:13 Current directory (getcwd, pwd, chdir)
* 14:30 OS dir (mkdir, mkdirs, remove, rmdir)
* 17:35 python which OS are we running on (os, platform)
* 18:22 Get process ID
* 21:08 OS path  (basename, dirname, abspath)
* 23:28 Traverse directory tree - list directories recursively (walk)
* 24:32 os.path.join
* 24:58 Directory listing (listdir)
* 26:10 Listing specific files using glob
* 27:15 External command with system
* 28:38 subprocess
* 29:13 time
* 32:55 sleep in Python
* 33:38 back to subprocess
* 37:09 subprocess in the background
* 38:15 Accessing the system environment variables from Python
* 38:59 shutil (copy, copytree, move, rmtree)
* 39:23 timer
* 39:41 Current date and time datetime now
* 40:51 Converting string to datetime
* 44:03 datetime arithmetics (elapsed time, timedelta)
* 45:17 Rounding datetime object to nearest second
        </ul>
        
* [Part 36](/programming-bootcamp-for-scientists-36) (35:00 min)
        <ul>
* 00:00 Testing Demo - What is testing? Why would you want to write tests?
* 04:36 How do you test your code?
* 05:20 What is testing?
* 07:06 Testing tools (testing packages)
* 07:14 Testing Demo methodology
* 08:05 AUT - Application Under Test
* 09:54 Use the module
* 10:40 doctest
* 14:40 doctest with failure
* 18:12 Unittest with success
* 23:07 Unittest with failure
* 25:54 pytest using classes
* 27:30 pytest using classes with failure
* 28:38 pytest without classes
* 29:06 pytest run doctest
* 29:28 pytest run unittest
* 29:55 Exercise: anagram
* 31:23 Exercise: Write test for your previous solutions
        </ul>
        
* [Part 37](/programming-bootcamp-for-scientists-37) (19:53 min)
        <ul>
* 00:00 SciPy - for Scientific Computing in Python
* 01:20 SciPy
* 01:45 BioPython
* 01:57 NumPy
* 02:28 Pandas
* 03:00 Matplotlib, Seaborn, Bokeh
* 04:03 SciKit-Learn
* 04:32 TensorFlow
* 04:50 Keras - Trying to explain Deep learning
* 08:27 Orange
* 09:09 Airflow and Luigi
* 10:43 Explanation about GPU, about clusters, and about the cloud
* 17:38 Octave and why Open Source can be better than Matlab
        </ul>
        
* [Part 38](/programming-bootcamp-for-scientists-38) (37:04 min)
        <ul>
* 00:00 Biology
* 00:50 BioPython
* 02:20 BioPython Background; FASTA file format
* 04:42 BioPython sequences (Seq)
* 07:45 NCBI
* 09:15 Read FASTA, GenBank files, download file using the requests module
* 18:15 Search for nucleotides on NCBI
* 28:30 Download nucleotides from NCBI
* 33:14 Chemistry
        </ul>
        
* [Part 39](/programming-bootcamp-for-scientists-39) (42:46 min)
        <ul>
* 00:00 Numpy
* 00:44 What is Numpy?
* 00:55 Numpy vector
* 06:19 2D arrays
* 07:28 Set dtype
* 08:27 Ones and Zeros
* 10:10 Random array
* 12:12 Array dtype changes by division (int to float)
* 12:40 Transpose
* 13:00 Reference and not a copy
* 13:45 Copy array
* 14:02 Element-wise operations on Arrays
* 14:50 multiply, matmul, dot for vectors and matrices.
* 17:43 Casting - converting from strings to integers. (astype)
* 18:40 Indexing 1d array
* 19:26 Slice is a reference, copy
* 19:55 abs value on a Numpy array
* 22:17 Logical not on a Numpy array
* 23:36 Vectorize a function
* 27:36 Filtering array (selecting some of the values from an array)
* 33:00 Some statistics (sum, mean, std, var)
* 33:35 Serialization (saving an array to a file)
* 35:37 Load from Matlab file to a Numpy array
* 37:24 Save a Numpy array as a Matlab file
* 37:49 Horizontal stack vectors (hstack)
* 38:31 Append or Vertical stack vectors and matrices (vstack)
* 38:50 uint, int - showing data overflow
        </ul>
        
* [Part 40](/programming-bootcamp-for-scientists-40) (1:11:05 min)
        <ul>
* 00:00 [Programming intro](https://code-maven.com/slides/programming/)
* 02:00 Types of Software
* 08:18 Computer Hardware Architecture
* 24:27 Connectors
* 26:32 bits and bytes (somewhere else)
* 26:52 Year 2000 (Y2K) (see part 23) 
* 27:17 Year 2038 problem (see part 23)
* 27:23 Incorrect floating point number representation (somewhere else)
* 27:47 Operating Systems
* 31:55 Programming paradigms
* 38:55 Different OOP systems
* 40:11 Compiled vs. Interpreted languages (elsewhere)
* 40:20 Open Source
* 52:47 Version Control
* 57:00 Software Testing
* 59:14 ASCII - Unicode (see part 9 and 10)
* 59:17 Complexity (see part 18 and 22)
* 59:32 What is the Internet
* 1:03:56 What is the Cloud?
* 1:04:45 Software Development methods
        </ul>
        
* [Part 41](/programming-bootcamp-for-scientists-41) (1:01:53 min)
        <ul>
* 00:00 Pandas - Python Data Analysis Library
* 01:10 Datasets in use (Planets, Stack Overflow Survey data)
* 05:48 Read CSV file into DataFrame
* 11:05 DataFrame Statistics
* 14:35 Show first and last rows
* 15:37 DataFrame select columns
* 17:37 DataFrame select rows (iloc)
* 18:37 DataFrame select rows and columns
* 19:05 DataFrame filter rows by size
* 20:25 DataFrame filter rows by value
* 21:17 Filter elementwise boolean and
* 23:34 sort (sort_values)
* 24:09 loc vs. iloc
* 28:03 Add calculated column, remove, delete (drop) column
* 30:11 Calculation (gravitational force)
* 36:03 Read CSV set index column
* 36:50 Count values
* 38:35 Select top items (head, tail)
* 40:24 Pandas Show histogram
* 42:13 Pandas read selected columns
* 44:30 Read files in chunks
* 49:24 Combine columns using any function (apply, vectorize)
* 51:24 Read Excel files (read_excel) (to_excel)
* 52:00 Create Excel file for experiment with random data
* 55:14 Calculate Genome metrics
* 57:25 Exercise: Pandas (incl. Kaggle)
        </ul>
        
* [Part 42](programming-bootcamp-for-scientists-42) (1:02:39 min)
        <ul>
* 00:00 Jupyter notebook
* 01:27 Installing Jupyter
* 02:20 Launching Jupyter notebook
* 05:45 Create a new notebook
* 07:00 Rename notebook
* 09:25 Two modes of work
* 14:40 Show the help by pressing h in command mode.
* 15:20 a, b to add a box above and below
* 16:45 The format of the notebook files, JSON
* 24:10 JSON format
* 25:28 Intellisense, TAB completition
* 26:14 Starting Jupyter notebook from the command line
* 26:53 add.ipynb
* 28:32 planets.ipynb (Markdown)
* 31:00 How can we see when a piece of code is running? (The star)
* 33:40 Seaborn (sns) example
* 36:09 SatckOverflow (skipping)
* 37:54 scipy.ipynb (showing and changing an image)
* 45:08 Create random image 
* 45:43 Load image using OpenCV
* 52:10 Do you usually use multiple editors or just a single editor?
* 54:45 IPy widgets
        </ul>
        
<!--
* [Part 43](/programming-boootcamp-for-scientists-44) ( min)
        <ul>
* 00:00
* 
        </ul>
        
-->
* ...

