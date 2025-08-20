# What is testing?

So what do we really mean when we mean testing?

For every piece of code whether it is a small module or a huge application, you can have the following equation.

```
Fixture + Input = Expected Output
```

## Fixture = environment

Every application works in some environment. For example if we have an application that takes all the CSV files in a given folder,
analyzes them and creates images with png extension for each file, then the starting environment of this application is a folder
with one or more csv files and without and png file.

If the application is a complex system, the environment might include multiple networking elements, servers, databases, ioT devices etc.

If the application is a simple: print the sum of these two numbers, then the environment does not have anything in it. In that case the environment is just the interpreter/compiler.


No matter what, the environment is called by the testing people the "Fixture".

## Input

Once we setup the fixture, we execute the code - the Application Under Test or AUT - and give it some input.

This will generate some kind of a result. Something printed on the screen, a bunch of new file, a change in the database, etc.

## Expected Output

That result should equal to some "Expected Output".

So this is our equation.

```
Fixture + Input = Expected Output
```

