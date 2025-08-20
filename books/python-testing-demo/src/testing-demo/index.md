# Why Testing?

(Automated) testing is probably one of the most overlooked technique in the programming world.

Traditionally in the software development industry we had a clear separation between "programmers" or "coders" or "software engineers" on one hand
and "qa people" or "testers" on the other hand. The latter would do the manual testing, the Quality Assurance of the product.

Traditionally the company and thus the programmers relied on the QA people to find the bugs and to ensure high quality.

This approach was never really good, but today it totally breaks down for a variety of reasons in a number of cases.

## Growing complexity

While the application growth and has more and more complex feature the time and manpower allocated for manual QA stays constant or growth at a much slower pace.
That means that even if we have infrequent releases the QA team doing manual testing cannot check all the features and all the possibilities for every release.
So traditionally companies only verified the new features and an a subset of all the other features that were deemed to be important.

As the gap between complexity of the application and the available time to check everything grows so does the uncertainty in the quality of the software.
Bugs start to fall into the gap and programmers start to fear the release more and more.

## Fast-paced development with frequent releases - CI/CD Continuous Integration / Continuous Delivery

In the age of fast-paced development when the release cycles aren't measured in months and not even in days, but in hours or minutes, there is no time for a separate, manual QA process.
You must automate the testing and verification process. Computers are much better at boring repetitive tasks than humans.

## Academia

If you are a student you don't have the luxury of having a people do QA for you. In fact you might be the person doing manual QA for the projects of your professor. I teach Python programming to biology and in general life-sciences students. Some of them will end up writing lots of software to support their research and thesis. They don't have a separate QA department that would check the applications they wrote. They have to do it themselves. Are they interested wasting time on checking the same thing repeatedly? Not likely.

## Open Source

Most of the Open Source developers work on their project in their spare time. They don't have any means to pay someone to do quality assurance for them. They are also not very interested in doing manual QA themselves nor they want to fix the same bug twice. Besides, as they are not getting paid to write that software one of the main value they can back for their investment is the respect of others. They won't get much respect for a buggy and unreliable software. So Open Source developers tend to write a lot of automated tests. Certainly a lot more than in a corporation.
This is true even for the same person in the two different situations. I know a number of people who write lots of tests for their Open Source projects, but almost none at work.




