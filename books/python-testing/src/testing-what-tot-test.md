# Testing: What to test?

How would you check that the code works as expected?

In general we can divide the testing into two:

## Happy path

* Valid input
* Valid edge cases (0, -1, empty string, etc.)
* e.g. if you are expecting a number what if you get 0, -1, 131314134141?

## Sad path

* Invalid input?
* If you are expecting a number what if you get the word "zero"?
* If you are expecting a number between 0-255 and you get 256? or -1?
* Broken input (string instead of number, invalid values, too long input, etc.)

* System failure (power failure, network outage, lack of memory, lack of disk, ...)
* Third-party error or failure - How does your system work if the 3rd party API does not respond or returns rubbish?

Also consider non-functional problems:

* Extreme load

