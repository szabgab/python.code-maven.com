---
title: Unit testing in the age of AI
timestamp: 2026-11-10T15:30:01
author:
published: true
description:
tags:
---

## Desciption

Automated unit testing has become the norm in the software industry, but it can be done well and it can be done poorly. We'll start with an overview of what unit tests are good for, continue with some important do's and don'ts of unit testing, and then address the questions on everyone's minds these days: How has GenAI affected unit testing, and how should we be thinking about unit tests in the age of AI?

## Bio

[Jason Elbaum](https://www.linkedin.com/in/jasonelbaum/)

Currently a senior software engineer at Fullpath, where we build AI-based solutions for car dealerships, I've previously worked at Google, Motorola, Facebook, and elsewhere. I've been writing code for 45 years since I was a kid, and unit tests for 25 years, and I have some strong opinions about them.

## Length

60 min


{% youtube id="ayUw8qMPtiM" file="2026-11-10-unit-testing-in-the-age-of-ai-with-jason-elbaum.mp4" %}


## Transcript

1
00:00:02.070 --> 00:00:14.139
Gabor Szabo: So, hello, and welcome to this session of the Code Maven session, or Python Maven session in this case, even though, as I understand, this session is going to be mostly

2
00:00:14.140 --> 00:00:22.480
Gabor Szabo: language agnostic. My name is Gabor Szabo, I organize these sessions. If you are watching on YouTube, then,

3
00:00:22.490 --> 00:00:29.090
Gabor Szabo: Please like the video and follow the channel, and below the video, you are going to find a link to the future events.

4
00:00:29.140 --> 00:00:47.680
Gabor Szabo: And a link to various notes about this presentation, maybe even the slides, and definitely to the profile of Jason, so you can find him. And I would like to thank Jason for going to… for giving this presentation, agreeing to give this presentation.

5
00:00:47.780 --> 00:00:51.580
Gabor Szabo: And to everyone who is here in the meeting.

6
00:00:51.800 --> 00:01:02.140
Gabor Szabo: you have the opportunity to ask questions, and, let's, go for this. So, Jason, the stage is yours.

7
00:01:02.500 --> 00:01:03.129
Gabor Szabo: Go ahead.

8
00:01:03.130 --> 00:01:05.190
Jason Elbaum: That's what I was… that's what I was afraid of.

9
00:01:06.210 --> 00:01:14.019
Jason Elbaum: of… So, hi, my name is Jason Elbaum. I'm a long-time software engineer.

10
00:01:14.230 --> 00:01:26.809
Jason Elbaum: I've, I was mentioning before, we started that I've been writing code since 1980, believe it or not. So, I've seen a lot of changes in our field, in our industry.

11
00:01:26.950 --> 00:01:28.530
Jason Elbaum: But I don't think…

12
00:01:28.790 --> 00:01:37.899
Jason Elbaum: I'd be hard-pressed to come up with any which have been as dramatic or as rapid as what we've seen in the last couple of years with generative AI.

13
00:01:38.150 --> 00:01:41.799
Jason Elbaum: Maybe the switch to the internet? I don't know.

14
00:01:41.890 --> 00:01:59.880
Jason Elbaum: But it's, it's pretty, pretty, pretty stunning, and I think we're all trying to figure out, how to be effective, and, how to work, well, and how, what kind of, what, which of our long-standing practices, are going to change, which are going to stay the same.

15
00:02:00.030 --> 00:02:15.580
Jason Elbaum: And I'm not gonna claim that I have any, definitive answers here. I'm trying to figure things out just as much as anybody else is, and I follow people online who have very, very widely different opinions on how to develop software with AI, and

16
00:02:15.750 --> 00:02:17.720
Jason Elbaum: And that's fine, so,

17
00:02:17.830 --> 00:02:27.369
Jason Elbaum: You know, take my advice or don't. That's whatever works for you, ultimately. It's, I guess, what my next slide says, if I can switch to it.

18
00:02:28.390 --> 00:02:32.609
Jason Elbaum: No, why am I not switching? Oh, there we go. Yes, your mileage may vary.

19
00:02:33.390 --> 00:02:43.950
Jason Elbaum: So I… my… I work for a company called Full Path. We are a Jerusalem-based software startup.

20
00:02:44.050 --> 00:02:52.159
Jason Elbaum: In the, automotive retail industry, we, we built an AI platform for car dealerships.

21
00:02:52.300 --> 00:03:03.749
Jason Elbaum: To help them organize their customer data and their inventory data, and improve their ability to sell vehicles and make connections with their customers.

22
00:03:03.760 --> 00:03:14.629
Jason Elbaum: We have over 3,000 dealers in North America, and we were just acquired a few months ago by Cox Automotive, which is one of the largest players in the automotive software

23
00:03:14.780 --> 00:03:16.870
Jason Elbaum: space. So,

24
00:03:17.040 --> 00:03:24.210
Jason Elbaum: That's why a lot of my metaphors and examples in this presentation will be related to vehicles.

25
00:03:24.600 --> 00:03:33.610
Jason Elbaum: Okay, so I'm going to talk again. My topic is unit testing in the age of AI.

26
00:03:33.770 --> 00:03:41.419
Jason Elbaum: And I was gonna also mention, I've actually been writing unit tests For about 25 years?

27
00:03:43.500 --> 00:04:01.900
Jason Elbaum: And so I've seen a lot of them, and I've made a lot of mistakes, so a lot of my advice in general about unit testing is born of experience. But again, what works for me might not work for you the same way. But this, I think, is pretty clear. What I'm calling the first axiom of developer testing.

28
00:04:02.180 --> 00:04:04.280
Jason Elbaum: Developers hate writing tests.

29
00:04:05.150 --> 00:04:09.669
Jason Elbaum: And, I put a little asterisk here.

30
00:04:10.140 --> 00:04:28.030
Jason Elbaum: Okay, most, most developers… I actually am one of those who actually generally likes writing tests, at least to some extent, but I think it's a pretty, pretty clear rule that, you know, we want to write code that does things. We want to develop systems, we want to build products.

31
00:04:28.310 --> 00:04:32.570
Jason Elbaum: A test is something we have to do, not because we like to do it, but because…

32
00:04:33.070 --> 00:04:36.729
Jason Elbaum: You know, because we need to, or because it helps us in other ways.

33
00:04:37.340 --> 00:04:53.950
Jason Elbaum: And so I'm going to give you the 2024 version of this rule. Developers hit by writing tests, and if I got, you know, a code review, I got a PR pull request review from some developer, and often it would look like this. Got lots of production code.

34
00:04:54.320 --> 00:04:57.290
Jason Elbaum: And… the test code is crickets.

35
00:04:57.960 --> 00:05:05.040
Jason Elbaum: And I would very, very quickly shot off a little comment that says, please add tests.

36
00:05:05.680 --> 00:05:07.330
Jason Elbaum: Alright, we need tests.

37
00:05:08.350 --> 00:05:17.070
Jason Elbaum: This has been updated. We now have the 2026 version, in which we have a little production code, and loads of test code!

38
00:05:17.590 --> 00:05:24.390
Jason Elbaum: We have more test code than production code, maybe several times more lines of tests than production code.

39
00:05:24.530 --> 00:05:31.979
Jason Elbaum: And my standard comment has changed, and now it's become, hey, too many tests here, can we,

40
00:05:32.250 --> 00:05:34.380
Jason Elbaum: Can we… can we pull back a little bit?

41
00:05:34.550 --> 00:05:38.060
Jason Elbaum: And what's interesting, of course, is that

42
00:05:38.280 --> 00:05:45.670
Jason Elbaum: One thing hasn't changed between two years ago and now, and that's that developers still hate writing tests.

43
00:05:46.100 --> 00:05:56.620
Jason Elbaum: The difference is that in 2024, developers weren't writing tests, or didn't like to. 2026 developers still aren't writing tests. The AI, of course, is writing the tests.

44
00:05:59.610 --> 00:06:08.789
Jason Elbaum: So, that's just a little, you know, starting point here. So now we'll move on to the second axiom of developer testing.

45
00:06:09.260 --> 00:06:11.920
Jason Elbaum: Developers hate reading tests.

46
00:06:12.830 --> 00:06:15.219
Jason Elbaum: You think writing tests is…

47
00:06:15.580 --> 00:06:20.710
Jason Elbaum: dull, and that's really why people say they hate writing tests. It's boring, it's… you know, just…

48
00:06:20.830 --> 00:06:26.350
Jason Elbaum: It's formulaic, it's boilerplate. The Elbras hate reading tests even more than they hate writing tests.

49
00:06:26.970 --> 00:06:32.810
Jason Elbaum: And this, yes, this applies to all developers, even developers who like writing tests I hate reading tests.

50
00:06:33.180 --> 00:06:39.219
Jason Elbaum: I'm willing to go out on a limb on that, on that, on that claim.

51
00:06:41.340 --> 00:06:59.509
Jason Elbaum: And so that means that when we're looking at code reviews, right, if we're talking about a code review, and I'm sitting down with a code review, and the PR has production code, and it's got test code, and very commonly, the reviewer would look at the production code and throw all kinds of comments on it, and pick apart the,

52
00:06:59.510 --> 00:07:04.390
Jason Elbaum: The style, and the details, and the comments, and the whatever, and the test code.

53
00:07:04.630 --> 00:07:11.980
Jason Elbaum: They would stamp… oh, okay, approved. Just, you know, test code, no comments on the test code. It's test code. You don't have to review the test code, right?

54
00:07:12.310 --> 00:07:17.790
Jason Elbaum: And the 2026 version…

55
00:07:18.590 --> 00:07:36.569
Jason Elbaum: is exactly the same, pretty much, okay? Even when the code is written, PR is written by AI, those of us who are still reviewing AI code, and I know that there are people who don't, and people who do, but if you're still reviewing your AI code, chances are you're reviewing the production code, and chances are you're still rubber-stamping the test code.

56
00:07:36.950 --> 00:07:39.210
Jason Elbaum: Because, you know, it's test code.

57
00:07:39.600 --> 00:07:41.249
Jason Elbaum: How important can it be?

58
00:07:42.490 --> 00:07:45.450
Jason Elbaum: So, that's a bit of background here.

59
00:07:47.140 --> 00:08:01.050
Jason Elbaum: And so I want to look at two questions here. One is, how has AI affected testing? And then, how should AI affect testing? And again, I'm going to repeat myself and say that I don't have

60
00:08:01.330 --> 00:08:05.790
Jason Elbaum: definitive answers here, and I think anybody who says that they do,

61
00:08:05.970 --> 00:08:07.650
Jason Elbaum: Take them with a grain of salt.

62
00:08:07.780 --> 00:08:11.050
Jason Elbaum: We're all figuring this out, and it's… Just…

63
00:08:11.170 --> 00:08:15.350
Jason Elbaum: how things are going to look at 5, 10 years from now, I don't think anybody can dearly tell you.

64
00:08:16.160 --> 00:08:17.500
Jason Elbaum: So,

65
00:08:17.930 --> 00:08:32.030
Jason Elbaum: First, the first approach is, since developers hate writing tests, let's let the AI do it. The AI is now our test-writing slave to do all the boring parts. And in fact, when we started first working with GenAI coding.

66
00:08:32.070 --> 00:08:46.390
Jason Elbaum: you know, whatever, a year, a couple years ago, a year and a half ago, whenever it was. I remember some people were saying, well, I don't think I trust the AI, and then, if you remember, the models were a lot, you know, were not nearly as good then, and they would often write

67
00:08:46.420 --> 00:08:59.980
Jason Elbaum: code that just was… didn't work. It was just really bad stuff coming out. And people say, well, I don't trust the AI to write the production code, but, you know, let's have to write the test code? That's the boring… that's the stuff I don't want to write. The AI can write the test code.

68
00:09:00.090 --> 00:09:02.150
Jason Elbaum: And my reaction at the time was.

69
00:09:02.520 --> 00:09:09.840
Jason Elbaum: On the contrary, if I've written the test code, then I'll trust the AI to write the production code, because then at least I know it works.

70
00:09:10.870 --> 00:09:17.050
Jason Elbaum: If the AI has written the test code, I'm not sure. So…

71
00:09:17.230 --> 00:09:23.859
Jason Elbaum: how has AI affected testing? The result of, let's have the AI write all the tests, is we got many more tests.

72
00:09:24.400 --> 00:09:32.619
Jason Elbaum: You know, because obviously, you know, stuff that people hate to do and that's boring, we don't do a lot of it. Maybe we don't do enough of it, but the AI doesn't care. It's not… doesn't get bored.

73
00:09:32.950 --> 00:09:36.160
Jason Elbaum: We have higher test coverage, I think that's pretty clear.

74
00:09:36.460 --> 00:09:38.550
Jason Elbaum: But this all comes at a cost.

75
00:09:38.910 --> 00:09:46.800
Jason Elbaum: What is the cost? Again, we'll talk about… a bit more about that a bit later, but… but we have the…

76
00:09:47.030 --> 00:09:50.970
Jason Elbaum: test… AI test code isn't… isn't free.

77
00:09:51.510 --> 00:09:56.439
Jason Elbaum: So we'll get… There's such, again, things to think about.

78
00:09:56.910 --> 00:10:08.219
Jason Elbaum: So now there… I have two approaches to Agentic coding, and I think most people who've been following this discussion are familiar with it. There's what we call agent-assisted coding.

79
00:10:08.260 --> 00:10:14.860
Jason Elbaum: Where you're the software engineer, you're in charge of the system, and you work with the AI to

80
00:10:14.860 --> 00:10:28.280
Jason Elbaum: craft the code, to give it a task, and you review the code, and you make sure that it meets all these quality criteria, but the engineer, the human software developer, is in charge, or is responsible, ultimately, for the results.

81
00:10:28.800 --> 00:10:35.509
Jason Elbaum: collaborates with AI is just… it's a collaborative process. It's, it's like pair programming with…

82
00:10:35.640 --> 00:10:37.840
Jason Elbaum: A, a non-human being.

83
00:10:38.220 --> 00:10:46.150
Jason Elbaum: It's up to you, and you're responsible, and if something goes wrong at the end, you know, your job is on the line, not the AI's.

84
00:10:46.640 --> 00:10:50.419
Jason Elbaum: And then there's what we call vibe coding.

85
00:10:50.500 --> 00:11:10.489
Jason Elbaum: Vibecoding says, hey, I trust the AI, don't you? If, I've got a robot that does things for me, what do I need to bother for? I don't need to look at the code, I don't need to read the code, I tell the AI what to do, and it builds me a system, and magically, I have working code, and I can read a book, or take a nap.

86
00:11:14.020 --> 00:11:22.639
Jason Elbaum: And actually, to be fair, there are people that I trust and rely on and have a lot of respect for in the industry.

87
00:11:22.800 --> 00:11:25.010
Jason Elbaum: Who take both of these approaches.

88
00:11:25.040 --> 00:11:43.469
Jason Elbaum: I'm still on, version 1. I'm still here, okay? I'm still, on the, I'm responsible for the code, even if I use the AI as a tool, like other tools I use, like a compiler, or a, static analysis, or a debugger, the AI is a tool, and I'm driving.

89
00:11:43.470 --> 00:11:56.759
Jason Elbaum: But there are people I know, including some very senior, experienced, people, who say, no, no, no, this time has come not to read code anymore. So if that's where you are.

90
00:11:56.820 --> 00:12:00.320
Jason Elbaum: More power to you, I'm not there, and I will say that right now.

91
00:12:00.820 --> 00:12:06.810
Jason Elbaum: I'm gonna go back to the basics a bit and talk about Testing, code testing.

92
00:12:08.010 --> 00:12:17.079
Jason Elbaum: how do we know that our code works? We write some code, how do we know that it works? And here I'm open if any of… I don't know what… I don't know how, how,

93
00:12:17.440 --> 00:12:24.660
Jason Elbaum: how active you guys want to be, but if you want to give me… throw out some answers for me, I'm… I'm happy to get some feedback from the community here.

94
00:12:25.180 --> 00:12:27.540
Jason Elbaum: How do we know our code works when we write some code?

95
00:12:30.020 --> 00:12:33.650
Jason Elbaum: Nobody answers, then I'll just plow through and give my own answers, so…

96
00:12:36.680 --> 00:12:40.240
Jason Elbaum: Alright, that's fine. So how do I know our code works?

97
00:12:40.670 --> 00:12:45.159
Jason Elbaum: And then why do we need unit tests? How do we know our code works? I mean…

98
00:12:45.660 --> 00:13:00.500
Jason Elbaum: Yeah, I've… Jim says I always try to put smoke tests in my build. I have databases to support regression tests, so… so tests is obviously the kind of answer that this presentation is hinting at, how we know our code works. But tests are not the only way we know our code works.

99
00:13:00.950 --> 00:13:05.340
Jason Elbaum: I've written, I've developed some code, how do I know it works?

100
00:13:05.660 --> 00:13:24.779
Jason Elbaum: First thing is that I wrote it, deliberately. So I designed something and developed it in a way that, in my head, intellectually, I think will work, right? So I use my mind to think that it worked, number one. Number two, we can review code, we can look at code and read it and think, does this make sense? Will this work?

101
00:13:25.080 --> 00:13:35.870
Jason Elbaum: Number 3, we can write tests, like we said, or those unit tests or other kinds of regression tests to test… to run our code, but we don't need to write tests

102
00:13:35.940 --> 00:13:51.430
Jason Elbaum: to run our code. We can just run the code! And this is what we used to do in the old days. Before about the year 2000, hardly anybody in the software business was writing automated tests. We wrote code, and then we ran it, and we saw if it worked.

103
00:13:51.830 --> 00:13:55.580
Jason Elbaum: And if it didn't work, we fixed it and ran it again.

104
00:13:55.750 --> 00:13:59.140
Jason Elbaum: So yes, you run your code to see if it works.

105
00:13:59.260 --> 00:14:16.739
Jason Elbaum: What other ways can we know our code works? We can have static analysis tools to check for common errors. We have compilers that check for tight mismatches, and we have checks for memory leaks and overflows and all kinds of things.

106
00:14:16.760 --> 00:14:21.870
Jason Elbaum: We have other tools that we use to check the code quality.

107
00:14:21.920 --> 00:14:29.290
Jason Elbaum: So, tests are not the only way we know our code works. They're one of the ways, one of the tools that we use to know our code works.

108
00:14:29.780 --> 00:14:33.580
Jason Elbaum: They might be the most important, I'm not sure, they might be.

109
00:14:33.790 --> 00:14:35.629
Jason Elbaum: But they're certainly not the only.

110
00:14:36.180 --> 00:14:38.880
Jason Elbaum: Was that a hand? I don't know what… I heard it shine.

111
00:14:39.260 --> 00:14:40.459
Jason Elbaum: That means something?

112
00:14:41.100 --> 00:14:48.869
Gabor Szabo: That means that I forgot to turn off the thing that beeps when Someone joins or leaves.

113
00:14:48.870 --> 00:14:49.240
Jason Elbaum: Okay.

114
00:14:49.240 --> 00:14:50.670
Gabor Szabo: about it, I'm going to turn it off.

115
00:14:50.670 --> 00:14:53.219
Jason Elbaum: No problem. No problem. All right.

116
00:14:53.790 --> 00:14:57.689
Jason Elbaum: So, so I'm gonna talk a bit about why… what unit tests are good for.

117
00:14:57.910 --> 00:15:03.539
Jason Elbaum: Okay, then we can discuss how that applies to AI, right?

118
00:15:03.770 --> 00:15:21.230
Jason Elbaum: So I'm going to start with correctness. This is probably the most obvious thing, the reason we write unit tests, to make sure the code works. We write a test, the test says this is what code's supposed to do, and it works. Make sure it meets its requirements. Well, okay, that maybe is the same thing in different words, but the point is that code… code works because

119
00:15:21.230 --> 00:15:29.889
Jason Elbaum: it's supposed to do something, and we're testing it against some kind of requirements. It could be a document, it could be something verbal, but some specifications of what it's supposed to do.

120
00:15:29.890 --> 00:15:43.250
Jason Elbaum: We want to check edge cases, error scenarios, kinds of things that may be hard to see from reading the code. You might not notice it, or just running the code, you might not encounter these situations, but in a unit test, we can create a

121
00:15:43.250 --> 00:15:59.980
Jason Elbaum: A scenario where something fails and tests it. Avoid regressions. So our test works… our code works today, but I change it tomorrow. Is it still working? If I have a test suite, I can run the test again and make sure I haven't broken anything. So that's correctness. Category 1.

122
00:16:00.790 --> 00:16:11.940
Jason Elbaum: Agility. Everyone talks about agile software, nobody really knows what it means, but if it means one thing, it means that we want to be able to make changes to our code, quickly.

123
00:16:11.940 --> 00:16:23.990
Jason Elbaum: And reliably. And so if we have unit tests, we know that if something… we break something, and we make a change to our code, if it breaks something, we're going to find out right away, and… and we can adjust, we can change our approach.

124
00:16:23.990 --> 00:16:33.690
Jason Elbaum: We can confidently change our system, we can roll back with source control, roll the code back to a known good state when the tests were passing, and then think again.

125
00:16:33.690 --> 00:16:41.110
Jason Elbaum: And it gives us scaffolding for refactoring. We want to make a big change to a system, to the structure of our code.

126
00:16:41.110 --> 00:16:54.939
Jason Elbaum: In the old days, we would do it, and we would hope we didn't break anything. But if we have unit tests that test that the code still works, we can change a whole bunch of things behind the scenes in the implementation, in the code structure, and we can see that our tests still run.

127
00:16:55.260 --> 00:17:02.209
Jason Elbaum: That all helps us move faster, make changes faster, push out new features or functionality faster.

128
00:17:02.270 --> 00:17:21.219
Jason Elbaum: And also, I mentioned this, encouraging clean interfaces. If you want to test your code, it helps… it's easier to test code that's designed, that's structured cleanly. It gives you a nice, simple way to take a class and put some inputs in and check some outputs. That's easier to do when your code is clearly structured.

129
00:17:21.760 --> 00:17:25.700
Jason Elbaum: My third category here, why we have unit tests.

130
00:17:25.980 --> 00:17:37.549
Jason Elbaum: Communication. A test is a demonstration of the code's intended usage. You're not sure what this code's supposed to do? Look at the test, and here's an example. It's an executable documentation.

131
00:17:37.570 --> 00:17:44.340
Jason Elbaum: of the interface and expected behavior. In that sense, it's sort of a contract. You look at the code, and this is, again.

132
00:17:44.360 --> 00:17:58.139
Jason Elbaum: The test tells you what the code is supposed to do, and it helps coordinate with other developers. They're reading the code. Sometimes reading the code is hard to understand how it's meant to be used, but you can look at a test, and the test shows you how this is how you use the code.

133
00:17:58.450 --> 00:18:00.740
Jason Elbaum: This is communication. Communication.

134
00:18:02.650 --> 00:18:06.940
Jason Elbaum: So, as a summary, we write tests to make the code better.

135
00:18:07.220 --> 00:18:17.200
Jason Elbaum: Better means different things. Better means higher quality and more reliable. Better means easier to read, easier to understand.

136
00:18:17.370 --> 00:18:28.860
Jason Elbaum: These are all easier to modify and change. The tests are an engineering tool from that perspective. They're an engineering tool, artifact, whatever you want to call it, technique.

137
00:18:29.010 --> 00:18:34.369
Jason Elbaum: To make the code better. If your tests aren't making the code better, you're doing it wrong.

138
00:18:35.430 --> 00:18:50.959
Jason Elbaum: Right? We don't need lots and lots of tests just because someone in management or somebody in the AI engine, whatever, said, hey, let's write some tests. The tests are there to help us, to help us develop software, develop software better, faster, etc.

139
00:18:53.800 --> 00:19:05.340
Jason Elbaum: And so here's my, my, my, bold assertion here. First corollary of gen AI-based testing. If you're vibe coding, you don't need tests.

140
00:19:06.650 --> 00:19:10.160
Jason Elbaum: What do I mean by that?

141
00:19:10.640 --> 00:19:16.900
Jason Elbaum: If your approach to your AI is, I trust the AI to write the code to develop the system.

142
00:19:18.310 --> 00:19:23.630
Jason Elbaum: then… It's really hard for me to fig- find any of these

143
00:19:24.370 --> 00:19:28.570
Jason Elbaum: Any of these items that are relevant anymore.

144
00:19:28.970 --> 00:19:47.080
Jason Elbaum: I trust the AI to make sure the code works and meets its requirements. I trust the AI to make changes to the code. Whenever I say I want this new feature, it does it. AI moves as fast as I can, certainly. Communication, who am I communicating with?

145
00:19:49.230 --> 00:19:50.100
Jason Elbaum: Right?

146
00:19:52.000 --> 00:19:54.530
Jason Elbaum: Now, maybe I've overstated this a bit.

147
00:19:55.940 --> 00:19:57.930
Jason Elbaum: Maybe I've overstated this a bit.

148
00:19:59.060 --> 00:20:00.830
Jason Elbaum: But I'm not sure that I have.

149
00:20:01.810 --> 00:20:05.710
Jason Elbaum: I don't know if anybody has any, pushback here, but,

150
00:20:07.110 --> 00:20:11.440
Jason Elbaum: I mean, just, you know, what's this… before we started, was the…

151
00:20:11.620 --> 00:20:14.060
Jason Elbaum: I remember, yeah, sorry.

152
00:20:14.060 --> 00:20:16.260
Gabor Szabo: Yeah, I definitely, I mean…

153
00:20:16.870 --> 00:20:35.739
Gabor Szabo: I don't think that's the case, but I'm curious how you're going on, because that's sort of the extreme part of… I mean, I can see where you say that, okay, if I totally, 100% trust that it does work perfectly, then you might be right, but I think

154
00:20:36.920 --> 00:20:37.770
Gabor Szabo: That is… that's…

155
00:20:37.770 --> 00:20:54.340
Jason Elbaum: That's exactly what I'm saying, right? If your approach to the AI is, you know, my AI does whatever it wants, and it's, you know, I tell it what to do when it does it, and I never look at the code, I don't care what's in the code, it's hard for me to see.

156
00:20:54.840 --> 00:20:57.750
Jason Elbaum: Unless the AI needs those tests.

157
00:20:58.070 --> 00:21:10.490
Jason Elbaum: for its own use, and I don't know enough about how the code engines work for that, I don't know whether that's the case or not, but I can't see what value those tests have to me.

158
00:21:10.740 --> 00:21:25.040
Gabor Szabo: I… well, my view would be the regression part. So, I asked the AI to do something, it implemented it. On one hand, I trust that it does, but I still do some…

159
00:21:25.200 --> 00:21:42.850
Gabor Szabo: let's say, manual testing, or whatever, or I just give it to the clients, and the clients say everything is fine, except this part, this doesn't work perfectly. And now I'm icing the AI webcoding, telling it, okay, now fix that part.

160
00:21:43.120 --> 00:21:51.090
Gabor Szabo: But, how can I know afterwards that it didn't break other parts? That,

161
00:21:51.090 --> 00:21:54.689
Jason Elbaum: But how can you know beforehand that it didn't break anything?

162
00:21:55.020 --> 00:21:55.390
Gabor Szabo: Tori?

163
00:21:55.390 --> 00:21:56.440
Jason Elbaum: you know…

164
00:21:57.120 --> 00:22:01.810
Jason Elbaum: I say, okay, how can you know… how can you know in the first place that it was all working?

165
00:22:02.320 --> 00:22:18.030
Gabor Szabo: No, what I'm saying is that if I manually tested it, or I assumed that it's working, and gave it to the clients, and the clients were happy up till one point when they've said, okay, now it just took some money from my bank account, and where is it?

166
00:22:19.930 --> 00:22:35.829
Gabor Szabo: So, and at that point, you say, okay, now I want to make sure that all the parts that are… that were working so far will keep working, while I tell the AI vibe coding, okay, to fix the part that wasn't perfect.

167
00:22:36.670 --> 00:22:47.139
Jason Elbaum: So let's say I accept your argument. How do you know that all of those parts that you care are working, how do you know they were all tested in the first place?

168
00:22:47.990 --> 00:22:49.870
Jason Elbaum: If you're not looking at the code.

169
00:22:53.110 --> 00:22:57.299
Gabor Szabo: Good question. I might ask the AI to, I don't know, do…

170
00:22:58.790 --> 00:23:02.600
Gabor Szabo: Run test coverage for on itself.

171
00:23:02.840 --> 00:23:14.960
Gabor Szabo: I can ask it to run mutation tests later on to see if the test coverage is… how fake is that?

172
00:23:15.420 --> 00:23:18.059
Gabor Szabo: Or how real their test coverage is.

173
00:23:18.840 --> 00:23:19.460
Jason Elbaum: Right.

174
00:23:21.150 --> 00:23:29.340
Jason Elbaum: Yeah, okay, I mean, again, I'm not… like I said, I may have overstated the claim, but I think I'm… it'll be a little clearer, maybe, why I'm saying it this way.

175
00:23:29.340 --> 00:23:29.890
Gabor Szabo: Yeah, go ahead.

176
00:23:29.890 --> 00:23:31.480
Jason Elbaum: Yeah.

177
00:23:32.460 --> 00:23:37.730
Jason Elbaum: And if not, if you're not vibe coding, then,

178
00:23:38.070 --> 00:23:45.559
Jason Elbaum: then you still need good tests, like we… just like we did before, because ultimately, like I said, you are the developer responsible for the code.

179
00:23:45.680 --> 00:23:48.129
Jason Elbaum: And for the quality and all that, and…

180
00:23:48.430 --> 00:23:59.960
Jason Elbaum: I don't think we have better ways to get there than alluded to, you know, all those benefits I listed earlier of tests. I don't think we have better ways to achieve them than a test suite.

181
00:24:00.160 --> 00:24:05.649
Jason Elbaum: So if you're not all in for vibe coding, then I certainly say that we need… we need good tests.

182
00:24:06.790 --> 00:24:12.209
Gabor Szabo: There is a comment that WAP coders are allowed to look at the code when they feel like it.

183
00:24:12.370 --> 00:24:13.609
Gabor Szabo: So, the thing here…

184
00:24:15.390 --> 00:24:15.770
Jason Elbaum: Yes.

185
00:24:15.770 --> 00:24:16.880
Gabor Szabo: Okay. The thing that.

186
00:24:16.880 --> 00:24:18.960
Jason Elbaum: Obviously, we're… yeah.

187
00:24:19.480 --> 00:24:29.889
Gabor Szabo: The thing I said that was… that sort of came from what I actually told you before the video started, that I'm teaching people who don't know how to code.

188
00:24:30.020 --> 00:24:36.959
Gabor Szabo: Right. And they are just VIP coding, basically, even though I'm teaching them some syntax, but

189
00:24:37.450 --> 00:24:42.369
Gabor Szabo: In reality, most of them are just vibe coding.

190
00:24:42.720 --> 00:24:50.710
Gabor Szabo: So there's no… for them, there's no value in looking at the code, because they don't know what to see there, what to look there.

191
00:24:51.970 --> 00:24:54.960
Jason Elbaum: Yeah, I hear you. That's interesting. Again, we're gonna…

192
00:24:55.100 --> 00:25:05.490
Jason Elbaum: we're gonna know better, I think, several years from now, how, which approaches, really, are sustainable in the long term, and I, you know, I don't have an answer for that yet, but,

193
00:25:06.440 --> 00:25:12.539
Jason Elbaum: It's interesting. So, I want to talk a bit… a bit more specifically about unit testing.

194
00:25:12.930 --> 00:25:20.810
Jason Elbaum: And this is, you know, when I'm talking unit testing in general, I'm not… now I'm out of the context of AI specifically.

195
00:25:20.930 --> 00:25:24.179
Jason Elbaum: When I talk about… when I say unit testing, what's a unit?

196
00:25:24.680 --> 00:25:35.049
Jason Elbaum: Right? Is it a unit? Is it a method, a class, a component, a subsystem? What do we mean by unit? And this has often been

197
00:25:35.580 --> 00:25:46.369
Jason Elbaum: the, subject of a lot of misunderstanding, in my opinion. And a unit, as I see it, and this is, again, I'm only giving my perspective here.

198
00:25:46.860 --> 00:25:53.079
Jason Elbaum: A unit… the unit for unit testing is a unit of functionality. It's a unit of behavior.

199
00:25:53.710 --> 00:25:55.870
Jason Elbaum: With a stable interface.

200
00:25:56.040 --> 00:26:05.820
Jason Elbaum: Right? A unit is not a little chunk of code that we're testing. A unit is a piece of our requirements. It's something the code has to do.

201
00:26:06.130 --> 00:26:11.019
Jason Elbaum: It's a feature, if you want to call it that, some kind of externally observable behavior.

202
00:26:11.480 --> 00:26:30.499
Jason Elbaum: And ideally, a unit… a unit test should be specified in the business domain, or at least the domain of the client code. Sometimes the code you're implementing might be an internal module somewhere, but we want to define its specification. It's a unit of behavior in terms of

203
00:26:30.800 --> 00:26:34.019
Jason Elbaum: The code that is using it, the code that's calling it.

204
00:26:36.080 --> 00:26:46.260
Jason Elbaum: And finally, we should… we don't want to be unit testing something that's dependent on slow or fragile resources, because this is,

205
00:26:46.570 --> 00:26:53.059
Jason Elbaum: Gets back to what… what unit tests… distinction between unit tests and, and, and system tests, integration tests.

206
00:26:53.200 --> 00:26:57.220
Jason Elbaum: But, instead of a stable interface.

207
00:26:57.690 --> 00:27:04.300
Jason Elbaum: When I say a stable interface, I'm using a lot of very vague terminology here, because some of these are just…

208
00:27:04.580 --> 00:27:20.670
Jason Elbaum: vague, like most things in software. They're guidelines and principles, and there aren't any hard and fast rules, but if I'm implementing, I don't know, an API, then I can be writing tests against the, the class

209
00:27:20.890 --> 00:27:40.449
Jason Elbaum: you know, the service class that supports that API. It could be writing tests against… if I have a service, I don't know, a utility class that performs a certain function in my system, I could be writing tests against that. But the point is that I'm writing tests against the code… a piece of code, a unit of code that I expect to be stable, it's got external

210
00:27:40.560 --> 00:27:47.110
Jason Elbaum: code that depends on it, that expects some level of stability in its interface.

211
00:27:47.440 --> 00:28:04.860
Jason Elbaum: And, when we say stable, everything in software changes, nothing is fixed in stone, otherwise it wouldn't be software, be hardware, for example. But, so sometimes we have a process of designing, discovering, figuring out what our stable interfaces are going to look like.

212
00:28:05.000 --> 00:28:15.940
Jason Elbaum: And that will change, but really, ideally, we want to be writing tests against something which is not going to change very much, because we want to be able to change the code that's behind it.

213
00:28:16.260 --> 00:28:22.230
Jason Elbaum: And we can't do that if we have to change the tests at the same time. Can't do it reliably, at least.

214
00:28:22.880 --> 00:28:26.489
Jason Elbaum: So I'm distinguishing unit tests with

215
00:28:26.900 --> 00:28:33.980
Jason Elbaum: Larger-scale testing, end-to-end testing, unit integration testing, These are all…

216
00:28:34.760 --> 00:28:43.770
Jason Elbaum: Again, things that are often hard to define exactly what the definition is, but the point is that these are tests that integrate

217
00:28:43.980 --> 00:28:57.789
Jason Elbaum: pieces of software that are larger, often they're, are less stable, they might be running over a network or through a database. They're slower to execute, they have a lot of dependencies. It can be really…

218
00:28:57.800 --> 00:29:10.100
Jason Elbaum: difficult and expensive to build and to run some of these integration tests. And for some systems that really need the reliability, that's fine. They can be important to have.

219
00:29:10.270 --> 00:29:15.350
Jason Elbaum: In my experience, they're often not worth the, the, the effort.

220
00:29:15.490 --> 00:29:31.580
Jason Elbaum: But it really depends. The big difference if you're writing, I don't know, a video game versus if you're writing, I don't know, a nuclear power plant regulator. So, different types of software have different levels of

221
00:29:31.810 --> 00:29:34.939
Jason Elbaum: Of quality and reliability requirements.

222
00:29:37.240 --> 00:29:48.740
Jason Elbaum: But usually, if I'm writing, you know, code within my company, and I'm collaborating with another team, and we can talk to each other and make sure the components work, collaborate with each other correctly, and if something breaks, we fix it.

223
00:29:49.140 --> 00:29:56.310
Jason Elbaum: The integration tests are perhaps less, less important, because, you know, if something breaks, we'll see it pretty soon.

224
00:29:57.340 --> 00:30:01.499
Jason Elbaum: That's just a side. How many tests…

225
00:30:01.990 --> 00:30:13.129
Jason Elbaum: Talked a bit… talked before about having too many tests. Some of these slogans come from the extreme programming movement. Kent Beck was one of the big names there.

226
00:30:13.620 --> 00:30:15.999
Jason Elbaum: Test everything that could possibly break.

227
00:30:16.310 --> 00:30:19.639
Jason Elbaum: Write tests until fear is transformed into boredom.

228
00:30:19.840 --> 00:30:26.850
Jason Elbaum: And the point here is, yes, you should test things that you're… test something if you're afraid it will break. If you're afraid it is broken or will break.

229
00:30:26.980 --> 00:30:30.560
Jason Elbaum: You don't write tests for things that you're pretty confident in.

230
00:30:31.000 --> 00:30:43.430
Jason Elbaum: I don't write tests for every line of code. I don't think that 100% coverage is an important or meaningful, testing goal. I need to test things

231
00:30:43.460 --> 00:30:52.619
Jason Elbaum: that I'm worried about. There's things that, code that's… maybe seems a little fragile, or, or has… the logic is a little complicated.

232
00:30:52.670 --> 00:30:55.639
Jason Elbaum: I don't need to set, I don't know.

233
00:30:55.880 --> 00:30:59.900
Jason Elbaum: set a variable in one place and test that it's set in another place. That's…

234
00:31:00.300 --> 00:31:03.289
Jason Elbaum: That's just testing that my programming language works, for example.

235
00:31:03.570 --> 00:31:09.760
Jason Elbaum: And, this is an old… I get paid for code that works, not for tests.

236
00:31:09.880 --> 00:31:14.290
Jason Elbaum: So my philosophy is to test as little as possible to reach a given level of confidence.

237
00:31:14.820 --> 00:31:17.110
Jason Elbaum: And there are a few important things in this statement.

238
00:31:17.800 --> 00:31:20.509
Jason Elbaum: One is the,

239
00:31:20.720 --> 00:31:35.959
Jason Elbaum: the, the, the, what's it called? What you call the business side of it, right? Our business is developing software. We write tests as a tool, like I said earlier, we write tests to help us write better code. We don't write tests for the fun of it, we don't write tests because we have nothing else to do.

240
00:31:36.110 --> 00:31:55.700
Jason Elbaum: We write tests to reach a level of confidence. We have a certain level of confidence that our code works. And like I said, different types of software systems might need different levels of confidence. If I'm right, whatever, a medical device, I want to have a very high level of confidence in its reliability, versus, like I said, you know.

241
00:31:55.790 --> 00:32:05.259
Jason Elbaum: whatever, an online quiz, for example, right? So that level of confidence is something which is adjustable.

242
00:32:05.360 --> 00:32:08.840
Jason Elbaum: And ultimately, everything is a matter of trade-offs.

243
00:32:09.220 --> 00:32:14.179
Jason Elbaum: We're trading off a certain level of… an additional level of confidence versus…

244
00:32:14.360 --> 00:32:18.689
Jason Elbaum: The cost and effort of writing and maintaining tests.

245
00:32:19.780 --> 00:32:23.399
Jason Elbaum: What makes a unit test good?

246
00:32:23.680 --> 00:32:32.449
Jason Elbaum: Readability. I'm gonna say more about readability, but a test should be short, should be obvious, should be linear, should be really easy to read.

247
00:32:32.480 --> 00:32:46.100
Jason Elbaum: a unit test, look at it, and you should understand what it does line by line, step by step. Minimal amount of setup in order to make the test case, viable. Test should be well-named,

248
00:32:47.020 --> 00:33:02.520
Jason Elbaum: We call that robustness. Tests to be fast. Why do tests have to be fast? Because we want to run them a lot. Every time we change the code, we want to run our tests, so we want them to run really fast. They should be independent of each other. I shouldn't have one change in one test that breaks another test.

249
00:33:02.630 --> 00:33:04.210
Jason Elbaum: deterministic…

250
00:33:04.390 --> 00:33:12.020
Jason Elbaum: I want to know that if a test fails, something has gone wrong with my code. A test shouldn't fail because a resource isn't available, or…

251
00:33:12.130 --> 00:33:17.419
Jason Elbaum: Or because, I don't know, the weather has changed, or it's the wrong day of the week.

252
00:33:17.580 --> 00:33:24.229
Jason Elbaum: Failure messages from our tests should be clear and easy, obvious to understand what went wrong when they fail.

253
00:33:24.780 --> 00:33:28.559
Jason Elbaum: Functionality. Our tests, again, I said this earlier, is to test

254
00:33:28.590 --> 00:33:47.059
Jason Elbaum: But domain-level behavior, externally visible behavior, what the code is supposed to do, not the implementation details, not which function was called, or how many methods were run, or what the name of some unit is. Tests should test that our code works, that it does something.

255
00:33:47.240 --> 00:33:49.820
Jason Elbaum: Have assertions that are specific.

256
00:33:49.940 --> 00:34:00.150
Jason Elbaum: Tests should be observed to fail. This is something we often miss, especially with the AI tests, right? You write a test, how do you know… and this is something I haven't said yet, but…

257
00:34:00.620 --> 00:34:06.259
Jason Elbaum: We talked about how we know our code works. I asked you that question earlier. How do we know our tests work?

258
00:34:07.480 --> 00:34:09.450
Jason Elbaum: How do I know that the tests are right?

259
00:34:10.860 --> 00:34:20.149
Jason Elbaum: So I gave you a list of ways we know that our code works, and one of them is writing tests, maybe the most important one. But we don't write tests to check that our tests work.

260
00:34:20.360 --> 00:34:22.330
Jason Elbaum: So, how do we know that our tests are right?

261
00:34:22.710 --> 00:34:25.030
Gabor Szabo: That's what mutation tests are for.

262
00:34:25.810 --> 00:34:32.310
Jason Elbaum: Okay, mutation test is one approach. You try to break the code and see that the code breaks, right?

263
00:34:32.310 --> 00:34:42.980
Gabor Szabo: Yeah, you change something in the code, and you're expecting your tests to fail. If the tests don't fail, then that part is not covered, or…

264
00:34:43.110 --> 00:34:46.029
Gabor Szabo: The test is not actually verifying that something.

265
00:34:46.480 --> 00:34:57.310
Jason Elbaum: Right, so then I wrote here, observed to fail, and that can happen even before you have mutation tests, even before you have code, right? You can write the test, and before you've implemented

266
00:34:57.420 --> 00:35:02.299
Jason Elbaum: The feature, or the code, or the behavior that the test is testing, you want to see that the test fails.

267
00:35:02.800 --> 00:35:08.780
Jason Elbaum: Because if the test passes before you've written the implementation, then your test isn't very useful.

268
00:35:09.100 --> 00:35:14.740
Jason Elbaum: Your test is testing something else, or maybe the feature already exists and you didn't realize it, I don't know.

269
00:35:15.080 --> 00:35:22.449
Jason Elbaum: So a test has to be observed to fail under some conditions… under some conditions in which the code is not working right.

270
00:35:24.420 --> 00:35:34.810
Jason Elbaum: And what else? Right. And test code structure should not be coupled with the code structure, and this is a very common mistake, a mistake I used to make.

271
00:35:34.930 --> 00:35:47.170
Jason Elbaum: And a lot of organizations make this mistake, and a lot of AI tests make this mistake, and what they do is they write… they act… write tests as if the unit they're testing is a class.

272
00:35:47.400 --> 00:36:04.969
Jason Elbaum: And they write… they take a class, and they write a test class that parallels the code, the code class. And they have a class of production code and a class of tests, and each test tests some behavior of that class. Very nice, it seems very modular and very object-oriented.

273
00:36:05.000 --> 00:36:08.570
Jason Elbaum: Until you get to the point where you want to refactor your code.

274
00:36:08.650 --> 00:36:17.999
Jason Elbaum: And you decide that this class, that's not the right class, that class should be something else entirely, that class should be restructured and broken up and redesigned, and now…

275
00:36:19.280 --> 00:36:34.190
Jason Elbaum: all these tests are useless, because they're not testing this class anymore, this class doesn't exist, or doesn't do the same thing it did before, and so I have to rewrite all the tests to align with the code I just rewrote. Now I'm rewriting the code, and rewriting the test at the same time.

276
00:36:34.930 --> 00:36:37.429
Jason Elbaum: So how do I know that I haven't broken the code?

277
00:36:37.640 --> 00:36:39.599
Jason Elbaum: when I've rewritten the code.

278
00:36:39.760 --> 00:36:42.049
Jason Elbaum: Because I can't run these tests on that code anymore.

279
00:36:42.640 --> 00:36:56.449
Jason Elbaum: Am I being clear? Right? If I rewrite my… restructure my code, and my test is linked to the structure of that code, I can't run these tests anymore. The tests are all failing because they're testing code that doesn't exist anymore.

280
00:36:56.940 --> 00:37:04.699
Jason Elbaum: So, I rewrote the code, I rewrote the tests, I've rewritten them both. The code is no longer a scaffolding for refactoring. It's not…

281
00:37:04.820 --> 00:37:10.489
Jason Elbaum: Guaranteeing that I haven't… it's not protecting me against regressions.

282
00:37:10.880 --> 00:37:14.360
Jason Elbaum: Because it's… the tests are changing the tests.

283
00:37:14.910 --> 00:37:16.300
Jason Elbaum: So that's a big one.

284
00:37:16.820 --> 00:37:19.900
Jason Elbaum: And maybe underappreciated, I think.

285
00:37:21.620 --> 00:37:25.350
Jason Elbaum: So here's a… another audacious claim.

286
00:37:26.210 --> 00:37:31.199
Jason Elbaum: I'm going to argue that readability is more important for test code than for production code.

287
00:37:32.280 --> 00:37:46.339
Jason Elbaum: And people, like I said before, often spend a lot of time reviewing their production code to make sure the code makes sense, it's readable, it's clear, it's clean, it's whatever you want to call it, and the test code gets rubber stamped. But I'm going to say that it's more important to be able to read the test code, and why is that?

288
00:37:47.360 --> 00:37:50.779
Jason Elbaum: So production code, the main job of our production code is to

289
00:37:51.110 --> 00:37:56.590
Jason Elbaum: You know, implement a functioning system, to behave, to do things, to run software.

290
00:37:56.640 --> 00:38:15.939
Jason Elbaum: If we have production code that's unreadable, maybe because I wrote it when I was tired, or maybe because the AI wrote it and I can't read its code, I don't know. Unreadable production code is a problem. It's a real problem, it's hard to maintain, but it still has clear business value, because it's doing something in the real world. It's running our software.

291
00:38:16.800 --> 00:38:25.139
Jason Elbaum: Test code, the main job of test code is to prove that the production code works, to prove to developers that the production code works.

292
00:38:25.750 --> 00:38:28.849
Jason Elbaum: How do we know?

293
00:38:29.240 --> 00:38:42.160
Jason Elbaum: from the test code that the production code works, because we can look at the code and see this is testing something, behavior, that the production code is supposed to do. If I can't read the test code and understand what the test code is testing.

294
00:38:42.670 --> 00:38:44.960
Jason Elbaum: Then it hasn't even done its main job.

295
00:38:46.080 --> 00:38:48.919
Jason Elbaum: It's… it's… it's not useful at all.

296
00:38:49.320 --> 00:38:54.929
Jason Elbaum: It's doing something, it's testing something, maybe. It's got assertions.

297
00:38:55.370 --> 00:38:59.620
Jason Elbaum: But what is the testing? If I can't understand what that code, the test code is doing.

298
00:38:59.960 --> 00:39:01.650
Jason Elbaum: It's… it's useless.

299
00:39:03.740 --> 00:39:04.250
Gabor Szabo: I see…

300
00:39:04.250 --> 00:39:04.860
Jason Elbaum: No value.

301
00:39:04.860 --> 00:39:11.910
Gabor Szabo: So I think one of the best examples for this would be, for me at least, is if you have duplicate tests.

302
00:39:12.260 --> 00:39:17.739
Gabor Szabo: And because you don't… can't read them, you don't notice that they are duplicated, so…

303
00:39:17.740 --> 00:39:19.740
Jason Elbaum: Yeah, that happens, sure.

304
00:39:19.870 --> 00:39:20.310
Gabor Szabo: Yeah.

305
00:39:20.310 --> 00:39:26.289
Jason Elbaum: Duplicate tests, or we have tests that have assertions that don't actually check anything.

306
00:39:26.360 --> 00:39:28.110
Jason Elbaum: That happens too.

307
00:39:28.130 --> 00:39:47.249
Jason Elbaum: We have… we have tests that are testing the wrong thing. They've got to set up a whole bunch of things, and they call a bunch of methods, and they do a whole lot of… and… okay, and I have a test case where the name is, I don't know, retrieves, vehicle from inventory and checks against database and updates, notification log.

308
00:39:47.710 --> 00:39:55.300
Jason Elbaum: Is that what it's supposed to do? Is that what the… does the test actually checking that? Is that what the test is really… the coding test is really doing?

309
00:39:55.670 --> 00:40:00.820
Jason Elbaum: Unless I could, again, read the test code very clearly and easily and obviously.

310
00:40:01.120 --> 00:40:04.120
Jason Elbaum: And know that it's doing what it says it's doing.

311
00:40:04.400 --> 00:40:08.159
Jason Elbaum: I… that test isn't… isn't helping. It's not valuable.

312
00:40:09.370 --> 00:40:13.660
Jason Elbaum: And again, unreadable test code has costs.

313
00:40:13.760 --> 00:40:20.339
Jason Elbaum: It costs… first of all, it has to be implemented, so that costs something, whether it's implemented by humans or by AI tokens.

314
00:40:20.730 --> 00:40:32.210
Jason Elbaum: comprehension. We read those tests to understand what the code does. The AI reads those tests to understand what the code does. It spends our token budget reading those tests that are not actually

315
00:40:32.210 --> 00:40:42.670
Jason Elbaum: useful, because we just said they're unreadable, they're… or maybe they're hard to read, maybe the AI can figure it out, but it's… it's expending effort to read these tests.

316
00:40:42.840 --> 00:41:02.189
Jason Elbaum: These tests have to be maintained somehow. I have to go back someday and fix these tests. If something breaks, right? I break a test, I made a change, I break one of these tests, I can spend a crazy amount of time from experience trying to figure out what this test is even doing to know whether… have I broken something that's real? Have I broken something that wasn't working in the first place?

317
00:41:04.100 --> 00:41:19.440
Jason Elbaum: We pay for execution, right? We run these tests every time we push more code. We're paying for that, the resources to run the tests. They delay our process, our continue our integration, our deployment process.

318
00:41:19.490 --> 00:41:27.359
Jason Elbaum: By running these tests, and finally, they give us false confidence, because we think that our code is tested, but in fact.

319
00:41:27.490 --> 00:41:29.510
Jason Elbaum: Our code is tested by tests that…

320
00:41:29.630 --> 00:41:32.429
Jason Elbaum: Nobody can understand, and nobody even knows if they're correct.

321
00:41:33.760 --> 00:41:37.230
Jason Elbaum: So, I'm gonna say that unreadable test code

322
00:41:37.640 --> 00:41:42.549
Jason Elbaum: actually has negative net business value. It costs more

323
00:41:42.700 --> 00:41:46.300
Jason Elbaum: To us, then it value adds to the system.

324
00:41:52.000 --> 00:42:09.149
Gabor Szabo: I just recently heard about the expense of AI, or the cost of AI, or the cost of… the cost increase that now people see with AI, and the comment was that actually about one-third of the extra… of the cost

325
00:42:09.260 --> 00:42:17.909
Gabor Szabo: is running the tests on GitHub Actions, or wherever you run them, because AI writes so much tests.

326
00:42:18.130 --> 00:42:23.159
Gabor Szabo: And it runs all the time when AI is running.

327
00:42:23.740 --> 00:42:31.130
Gabor Szabo: And the cost of running all these tests on GitHub Actions, or whatever.

328
00:42:31.630 --> 00:42:34.790
Gabor Szabo: It's about one-third of the expenses.

329
00:42:36.990 --> 00:42:52.490
Jason Elbaum: And I'm gonna argue that, you know, whatever, I mean, I don't know if that… whether we have… if you, if you, I don't know, you write a… you write a class, let's say, you write a few tests that cover the main scenarios of that class, and some of the error cases, for example.

330
00:42:52.490 --> 00:43:02.100
Jason Elbaum: Right? And now your test… your class is tested, and you feel comfortable enough with it. The AI writes the code, and it gives you, I don't know, a dozen or two dozen, who knows how many test cases.

331
00:43:02.640 --> 00:43:07.859
Jason Elbaum: But is the code 2 or 3 times more reliable for that?

332
00:43:08.430 --> 00:43:25.119
Jason Elbaum: It's a cost-benefit question here, and everything in engineering is about engineering trade-offs, and, you know, very few things come for free. So this is, this is, again, this is part of what I'm arguing here.

333
00:43:26.130 --> 00:43:28.810
Jason Elbaum: Test code has to be readable.

334
00:43:29.010 --> 00:43:34.039
Jason Elbaum: So, now, going back to what I was saying before, if humans never read your tests.

335
00:43:35.520 --> 00:43:37.519
Jason Elbaum: You might as well be vibe coding.

336
00:43:37.960 --> 00:43:42.299
Jason Elbaum: If all your tests are written by the AI, and you never look at them.

337
00:43:43.310 --> 00:43:52.139
Jason Elbaum: How do you know they're adding value to their system? To your system? How do you know they're testing anything of significance? How do you know that they're correct in the first place?

338
00:43:55.670 --> 00:44:06.139
Jason Elbaum: So, again, I said earlier on that I'm still on the side that says that, you know, code matters, and that I'm responsible as a developer for making sure the code is correct.

339
00:44:06.140 --> 00:44:19.780
Jason Elbaum: And this is part of the reason that nobody… if I… the AI writes the tests, writes the code, and it writes the tests, and I've never seen… never looked at them, and can't understand them if I tried to, even.

340
00:44:20.330 --> 00:44:24.009
Jason Elbaum: Then, you know, Why am I in the loop?

341
00:44:24.690 --> 00:44:25.560
Jason Elbaum: Right?

342
00:44:29.770 --> 00:44:41.599
Jason Elbaum: So I… I don't know if I need to go. I have got a whole section here about specific test, structures and scenarios and techniques, with code examples.

343
00:44:43.530 --> 00:44:54.239
Jason Elbaum: I don't know if that's the interesting part here. I could go into it, I could not, but I just wanted to talk about this slide, at least, right? Common testing anti-patterns. And again, this is my opinion here, and

344
00:44:54.280 --> 00:45:09.430
Jason Elbaum: You're welcome to disagree, but these are things that I have run into in my experience, which I think are the wrong way to write tests. Some of them are, I mentioned earlier, one test class per production class, the test structure, the codes, the,

345
00:45:09.480 --> 00:45:15.920
Jason Elbaum: Class structure of your test is coupled tightly with the production code structure, so that you can't change one without changing the other.

346
00:45:15.980 --> 00:45:21.740
Jason Elbaum: long test scenarios. You have a single test class, function, test method that

347
00:45:21.990 --> 00:45:38.559
Jason Elbaum: make some… make some, changes, and run some assertions, and make some more changes, and run some more… and you have a very long test, and then it's just… it's just hard to understand what's going on. It's hard to read. If it fails, it's hard to figure out what the… what the, state was supposed to be, where it failed, and why it's failing.

348
00:45:39.170 --> 00:45:47.730
Jason Elbaum: a test couple implementation details of your code, so that if I change, like I said, a method name or something, I'm breaking a test, even though the code still works.

349
00:45:48.000 --> 00:45:52.420
Jason Elbaum: Test names that are unclear. Excessive use of mock objects.

350
00:45:52.540 --> 00:46:02.770
Jason Elbaum: We've mentioned that earlier, but mock objects are very useful when they're necessary, and they're very problematic when they're not.

351
00:46:03.490 --> 00:46:12.849
Jason Elbaum: Duplicated tests. AI does this, from my experience, a lot. It implements something new, it writes more tests. It doesn't check, well, do these tests already exist somewhere?

352
00:46:13.050 --> 00:46:29.329
Jason Elbaum: It'll write tests that guard against impossible scenarios. It's writing a test for some code that accepts, I don't know, an integer input. It writes some tests that it will break if it's a… if it's a text, if it's a word, if it's not an integer, or whatever it is. I'm thinking, okay.

353
00:46:29.360 --> 00:46:35.709
Jason Elbaum: The test is there, but I know that's never gonna get a word. It's always getting an integer. This test is useless.

354
00:46:37.760 --> 00:46:55.539
Jason Elbaum: irrelevant assertions, it's, you know, we can assert, but an assertion, a test assert that, I don't know, that we got a response, but is it the right response? We don't bother to check that, for example. Or all kinds of tests that look like they've got the coverage, they're running the code, but they aren't actually checking that it's working correctly.

355
00:46:55.540 --> 00:47:03.090
Jason Elbaum: Modifying the code and its tests at the same time. I mentioned that, and the AI, again, in my experience, does this if you don't tell it not to.

356
00:47:03.150 --> 00:47:13.589
Jason Elbaum: And sometimes we forget. We write, we write tests for the, the interesting stuff, but we don't check, is it… what if it's empty? What if it's null? What if it's… I don't know. Okay, so…

357
00:47:13.950 --> 00:47:17.039
Jason Elbaum: We have to… we have to cover… cover edge cases, too.

358
00:47:17.260 --> 00:47:20.579
Jason Elbaum: At least if they're, you know, reasonable edge cases.

359
00:47:21.490 --> 00:47:25.640
Jason Elbaum: AI-generated testing, in my experience, do these things… do this stuff all the time.

360
00:47:26.610 --> 00:47:33.220
Jason Elbaum: So, a compromise approach. Is there a middle way between pure vibe coding

361
00:47:33.320 --> 00:47:47.789
Jason Elbaum: And reading every line of the code and every line of the tests. And again, I'm just… I'm still experimenting here myself. I did an experiment a few weeks ago when I tried to do… I don't know if anybody here has ever done a TDD, test-driven development, where…

362
00:47:47.970 --> 00:47:52.150
Jason Elbaum: You write in very small increments of cycles of

363
00:47:52.300 --> 00:48:00.319
Jason Elbaum: test first, and implementation, refactoring, test, etc. I did an experiment with AI a few weeks back, and

364
00:48:00.820 --> 00:48:14.300
Jason Elbaum: And it worked on some level, but it was excruciatingly slow, because every time the AI starts a new cycle of something, it has to read the code again, and understand it again, and churn and churn and churn, and it was just tremendously difficult.

365
00:48:14.470 --> 00:48:21.459
Jason Elbaum: But, there is what's called acceptance test-driven development, often ATDD.

366
00:48:21.920 --> 00:48:27.509
Jason Elbaum: An acceptance test is, in a sense, an executable specification of your… for your code.

367
00:48:27.780 --> 00:48:30.360
Jason Elbaum: It's a test, it's a, it's code.

368
00:48:30.530 --> 00:48:47.259
Jason Elbaum: Right? But it's code that essentially encapsulates the specification, the requirement of our system, of our task. And this acceptance test can serve as a sort of verifiable human-AI interface.

369
00:48:47.350 --> 00:49:00.540
Jason Elbaum: between us, you know, we create the specification, we say this is what we want the code to do, the AI does the implementation, and we have this layer of tests that is our interface.

370
00:49:00.740 --> 00:49:03.999
Jason Elbaum: In a sense, and the loop kind of looks like this.

371
00:49:04.230 --> 00:49:19.820
Jason Elbaum: And I have the human's job in orange, and the agents in purple, right? Step one, describe the behavior to implement. I'm starting a new task. I write some description of what the code has to do.

372
00:49:20.460 --> 00:49:21.270
Jason Elbaum: Right.

373
00:49:21.680 --> 00:49:30.629
Jason Elbaum: I read what the code has to do, and I specify acceptance criteria. This task will be complete when the following things are working, when, I don't know.

374
00:49:30.630 --> 00:49:42.990
Jason Elbaum: The user can open a new, whatever it is, a new agent on, you know, specify what it means for the code to be working when the functionality is complete on this task.

375
00:49:43.010 --> 00:49:48.220
Jason Elbaum: And if there are any non-functional requirements for performance or security, whatever they are.

376
00:49:48.590 --> 00:49:50.579
Jason Elbaum: And then we tell the agent.

377
00:49:50.670 --> 00:50:09.859
Jason Elbaum: I want you to write a set of acceptance tests. They're gonna fail now, because there's no code yet. I want to write a failing acceptance tests that validate this behavior that we have just specified. Without writing production code now, we're just writing tests. At this point, I want the agent to write acceptance tests that

378
00:50:09.920 --> 00:50:16.230
Jason Elbaum: basically a test suite that describes what I just told it I want, the code to do.

379
00:50:16.460 --> 00:50:20.399
Jason Elbaum: And then I wanted to run the test and show that they're… that they fail.

380
00:50:23.110 --> 00:50:32.660
Jason Elbaum: Okay, I will look at that essay? I'll try to look at that essay. There are loads and loads of articles and essays out there, and

381
00:50:33.730 --> 00:50:36.220
Jason Elbaum: Sorry, can you still see my screen?

382
00:50:38.850 --> 00:50:39.360
Jason Elbaum: Hello?

383
00:50:39.360 --> 00:50:41.209
Gabor Szabo: See this slide? The ATDD?

384
00:50:41.210 --> 00:50:55.320
Jason Elbaum: fine. And then tell it to wait for the… for me to review and approve the test suite, and say, okay, we agree that this test suite specifies the correct behavior of the code.

385
00:50:55.510 --> 00:51:03.600
Jason Elbaum: And then, the agent goes off and implements the code, writes all the production code for all those tests.

386
00:51:03.770 --> 00:51:18.400
Jason Elbaum: And I tell it to do its refactoring, so it would meet the code quality rules, or our coding standards, and etc. Not modifying any test code at this point. It wrote the test suite first, now it's writing the production code.

387
00:51:18.630 --> 00:51:24.009
Jason Elbaum: And then it comes back to me for approval of the implementation.

388
00:51:24.490 --> 00:51:28.429
Jason Elbaum: So I've been… been working with this lately.

389
00:51:28.580 --> 00:51:40.850
Jason Elbaum: And I've got, again, a little instructions to my agent to describe this process. And I… so far, I think it's working reasonably well.

390
00:51:41.330 --> 00:51:44.739
Jason Elbaum: A lot depends, I think, on the size of the tasks.

391
00:51:45.150 --> 00:51:49.519
Jason Elbaum: If he, you know, he tried to do… bite off too much at once.

392
00:51:49.780 --> 00:52:02.180
Jason Elbaum: Then you're gonna have trouble, first of all, specifying the specs in a complete way, and by the time you get a complete test suite that covers all the scenarios, it might…

393
00:52:02.320 --> 00:52:05.769
Jason Elbaum: It might be a very, very long feedback loop.

394
00:52:05.890 --> 00:52:12.760
Jason Elbaum: So there's a… again, there's a lot of engineering judgment here, and everybody… I think.

395
00:52:12.960 --> 00:52:15.899
Jason Elbaum: Is trying to figure out how to do this stuff.

396
00:52:16.250 --> 00:52:24.429
Jason Elbaum: Right, okay, I, november 3rd article, okay. There's so many articles out there.

397
00:52:24.590 --> 00:52:26.330
Jason Elbaum: Everyone's got an opinion.

398
00:52:27.150 --> 00:52:38.359
Jason Elbaum: So I've, I, again, in my experience so far, and everything I say here is tentative, and everything I say here is… is so far, and in my experience, and your mileage may vary.

399
00:52:38.460 --> 00:52:48.979
Jason Elbaum: But in my experience, ATDD is… gives us a balance between the human and the loop, human oversight and guidance, and the coding by the agent.

400
00:52:49.090 --> 00:52:54.940
Jason Elbaum: And, and without, without,

401
00:52:55.520 --> 00:53:01.790
Jason Elbaum: Too much, churn and, and, and, I don't know.

402
00:53:01.970 --> 00:53:21.219
Jason Elbaum: It's, again, I am… this is a suggestion. A lot of people that, again, a lot of people that I… that I respect, are supporting this and arguing for this approach. I've only started trying it recently, so my opinion is preliminary, and you are welcome.

403
00:53:21.290 --> 00:53:22.450
Jason Elbaum: To your own.

404
00:53:22.900 --> 00:53:31.179
Jason Elbaum: So again, I have a lot of code here, I have a bunch of slides with code. I don't think that's really interesting. If anyone wants to look at code.

405
00:53:31.360 --> 00:53:33.859
Jason Elbaum: We could do that, but,

406
00:53:33.990 --> 00:53:36.949
Jason Elbaum: I'm happy to skip all the COVID here.

407
00:53:37.350 --> 00:53:43.260
Jason Elbaum: Because I don't think it's the interesting things as… That's way too much code.

408
00:53:43.610 --> 00:53:59.869
Jason Elbaum: So I was just gonna say, so these are some things, some instructions, some of the rules that I have in… for my agent, what I tell it about how I want the tests to work. And I find it very helpful, I find, it's a… because, again, often I think the stuff that… the tests that AIs write, by default.

409
00:54:00.020 --> 00:54:19.150
Jason Elbaum: are not always that great, maybe because the tests that, you know, in the corpus of, of open source code, maybe the tests aren't that great, I don't know. So I tell it to write one scenario per test, follow patterns, structure tests similar to existing tests in the code.

410
00:54:19.290 --> 00:54:23.879
Jason Elbaum: Name variables clearly. Minimal amount of setup in each test.

411
00:54:24.050 --> 00:54:32.619
Jason Elbaum: Linear tests… I'm not going to go through all the details here, but functionality, not implementation, observable behavior.

412
00:54:32.750 --> 00:54:40.269
Jason Elbaum: Don't test… Logging or monitoring, unless that's, you know, the purpose of the code you're writing.

413
00:54:40.400 --> 00:54:45.299
Jason Elbaum: Refactoring while the test remains static.

414
00:54:45.660 --> 00:54:53.700
Jason Elbaum: Avoid mock objects unless they're actually necessary. Drive the code through its public interface.

415
00:54:53.870 --> 00:55:09.850
Jason Elbaum: and prefer other ways, a stub or a fake, some way to… basically, I like to think of a mock as a last resort here, because a mock essentially is testing the implementation, testing that a particular method was called, or a particular

416
00:55:09.850 --> 00:55:17.220
Jason Elbaum: method was called a certain number of times in a certain order, you're tinning down the implementation rather than testing the behavior.

417
00:55:17.620 --> 00:55:21.720
Jason Elbaum: So, my summary here…

418
00:55:22.130 --> 00:55:29.699
Jason Elbaum: good unit tests can make your code more reliable, more maintainable, and more agile, and I think, again, I think this can apply in the context of AI.

419
00:55:30.240 --> 00:55:38.180
Jason Elbaum: Bad unit tests can absolutely make your code less reliable, less maintainable, and less agile.

420
00:55:38.220 --> 00:55:52.069
Jason Elbaum: And I don't think that we're getting value from the GenAI clogging up our codebase with tests that are… that don't… that don't have as much

421
00:55:52.370 --> 00:55:56.580
Jason Elbaum: don't have enough value to justify their expense, that's…

422
00:55:58.990 --> 00:56:08.959
Jason Elbaum: That's where I am. The same goes for AI in general. Good AI practices can make the good things we do as software engineers even better. Bad AI practices can make the bad things we do even worse.

423
00:56:11.780 --> 00:56:16.349
Jason Elbaum: And maybe I'll just close with this. A few things that keep me up at night, aside from stargazing.

424
00:56:16.730 --> 00:56:20.309
Jason Elbaum: Engineers love writing code.

425
00:56:20.520 --> 00:56:33.729
Jason Elbaum: And I don't think most of us love reading code, and I definitely wonder… we don't know where industry is going, where our job profession is going. Are people going to want to go into the software business if they're not

426
00:56:34.000 --> 00:56:38.990
Jason Elbaum: you know, solving problems with code the same way we're used to doing? I wonder.

427
00:56:39.400 --> 00:56:47.659
Jason Elbaum: All successful, complex software systems start as simple software systems. I think this is a universal rule.

428
00:56:47.880 --> 00:56:50.360
Jason Elbaum: And

429
00:56:50.740 --> 00:57:01.919
Jason Elbaum: all the attempts I've seen so far to tell an AI, go, go build me an Office suite of, suite of office tools from scratch.

430
00:57:01.960 --> 00:57:13.910
Jason Elbaum: those things aren't happening, and they aren't working. Software grows organically and incrementally and iteratively by adding value piece by piece, and

431
00:57:14.010 --> 00:57:20.159
Jason Elbaum: And I don't think that's going to change whether the code is being written by humans or by other software, so…

432
00:57:22.150 --> 00:57:23.390
Jason Elbaum: That's where I am.

433
00:57:28.800 --> 00:57:30.950
Jason Elbaum: Okay, I haven't followed all the comments.

434
00:57:31.810 --> 00:57:35.300
Gabor Szabo: There were tons of comments,

435
00:57:36.560 --> 00:57:41.229
Gabor Szabo: it was interesting, but I guess people didn't want to interrupt you, so…

436
00:57:41.340 --> 00:57:45.209
Gabor Szabo: It's fine, if you'd like to look at them and,

437
00:57:46.830 --> 00:57:53.520
Jason Elbaum: Let's see, let me just, yeah, flip through the comments a bit,

438
00:57:55.090 --> 00:58:04.989
Jason Elbaum: Yeah, tests are things that don't matter and will always pass. Yeah, we have definitely had… those are some of our… our… our less useful tests.

439
00:58:05.220 --> 00:58:20.680
Jason Elbaum: Jim says, my current workflow, my tests run on cloud dev servers and Codex PR review dev servers, which don't… I don't get charged for. Okay. My smoke tests run on Google Cloud Build servers, which cost me pennies per month. My regression tests are Cloud Runner server jobs, with tiny incremental costs.

440
00:58:20.930 --> 00:58:25.229
Jason Elbaum: Someone told me to avoid GitHub Actions many months ago, and I took their advice. All right, well,

441
00:58:25.570 --> 00:58:27.090
Jason Elbaum: I…

442
00:58:27.320 --> 00:58:35.650
Jason Elbaum: I work for a company, and I don't decide where our tests run, so that's… that's out of my hands in my case, but

443
00:58:35.860 --> 00:58:42.530
Jason Elbaum: Yeah, so certainly a lot of this definitely depends on how much things cost. You know,

444
00:58:44.450 --> 00:58:54.859
Jason Elbaum: If you solve a problem, solve a problem with a mock, now you have two mocks. I think the line, the original line may have been, now that you have two problems, but, yeah. Okay, that's an old joke,

445
00:58:55.000 --> 00:58:58.039
Jason Elbaum: I think it used to be said about Pearl, right? If,

446
00:58:58.530 --> 00:59:02.360
Jason Elbaum: Try to solve a problem with Pearl, now I have two problems? I don't know.

447
00:59:02.360 --> 00:59:03.419
Gabor Szabo: regex, I think it'.

448
00:59:03.420 --> 00:59:06.170
Jason Elbaum: Regx's, that's right, it was, regexes, yes.

449
00:59:06.450 --> 00:59:18.549
Jason Elbaum: Tdd is better starting on a freshly new app. It's hard, but not impossible, to shoehorn it into an existing codebase which wasn't built on it. There's some truth to that, but usually even existing codebases, you're often writing a lot of new code.

450
00:59:18.620 --> 00:59:28.509
Jason Elbaum: And you can be working in TDD on the new code, even if the old code is legacy. But yeah, there are different ways to do it.

451
00:59:28.610 --> 00:59:32.789
Jason Elbaum: And, I think TDD, as

452
00:59:32.900 --> 00:59:44.549
Jason Elbaum: as conventionally understood, is basically a human process for helping us understand the code, and improve it, and, and, and,

453
00:59:44.650 --> 00:59:55.219
Jason Elbaum: incrementally change or modify, build our code, and I'm not sure that that's… the same process is really useful the way that GenAI agents work.

454
00:59:55.540 --> 01:00:12.019
Jason Elbaum: But I know that some people have been trying TDD on, GenAI and, claimed that they've found, ways that they find useful to work with it. So, I see, I think there's a webinar… I saw a webinar advertised some later this week that I might try to attend.

455
01:00:12.050 --> 01:00:23.190
Jason Elbaum: So, yeah, people have lots of… everybody, there… I don't know how many millions of people writing software in the world, and I don't know how many of them are currently trying to figure out how to use AI effectively, and how many different opinions they have.

456
01:00:23.270 --> 01:00:27.979
Jason Elbaum: There are lots and lots of things going on, and that's… on the one hand, that's great, but on the other hand, it's…

457
01:00:28.140 --> 01:00:38.179
Jason Elbaum: We used to have something we called best practices. I'm not sure that term is really meaningful anymore. After the last year, nobody knows what best practices are for Gen AI anymore.

458
01:00:38.720 --> 01:00:42.139
Jason Elbaum: Human loop fallacy, I will try to look at that essay.

459
01:00:42.470 --> 01:00:47.930
Jason Elbaum: My debugger looks at tracebacks in the logs. I don't mind if there's a test of logging.

460
01:00:48.060 --> 01:01:04.890
Jason Elbaum: As long as it's not mocked away from being a real test. Now, I have written tests of logging in the past. I'm not saying it's always wrong, but sometimes when I tell the AI, hey, make sure that this gets logged, it says, oh, I'll make sure that it logs… that it gets logged. How do I make sure that it gets logged? I gotta write a test to make sure it's done, right?

461
01:01:05.010 --> 01:01:11.269
Jason Elbaum: And it just keeps adding tests for things because I mention them, or, whatever, you know. So,

462
01:01:11.620 --> 01:01:13.070
Jason Elbaum: Yeah.

463
01:01:13.240 --> 01:01:28.250
Jason Elbaum: So legacy code basically heavily intertwined writing TDT tests for new code can be hard, absolutely, and there's a whole book about it, I don't know if you've heard Michael Feathers working with legacy code, and I'm looking this way because it's on my bookshelf behind me.

464
01:01:28.320 --> 01:01:33.309
Jason Elbaum: He wrote a book. We're working effectively with Legacy Code, he wrote a book once on…

465
01:01:33.520 --> 01:01:42.100
Jason Elbaum: how to start adding tests into legacy codebases, that don't have them. So that might be worth looking at if those are the kinds of things you're trying to do.

466
01:01:43.730 --> 01:01:45.949
Jason Elbaum: No, anything else?

467
01:01:48.500 --> 01:01:50.970
Gabor Szabo: It seems.

468
01:01:50.970 --> 01:01:56.400
Jim Salsman: Yeah, I'll just… I'll just add that in the age of AI,

469
01:01:57.070 --> 01:02:00.730
Jim Salsman: I've taken a different perspective on TDD.

470
01:02:01.100 --> 01:02:07.879
Jim Salsman: I love the idea of it, and I have benefited from it and enjoyed it immensely in many cases.

471
01:02:07.990 --> 01:02:17.699
Jim Salsman: But… These days, I find myself asking the AI to just keep a detailed specification checklist.

472
01:02:18.130 --> 01:02:20.780
Jim Salsman: Or similar kinds of documents?

473
01:02:20.930 --> 01:02:27.640
Jim Salsman: And, relying less on writing TDD tests, because I just…

474
01:02:28.350 --> 01:02:31.170
Jim Salsman: It just seems like the kind of thing that's…

475
01:02:31.430 --> 01:02:39.030
Jim Salsman: a lot of effort for an incremental value that might not be there. I feel the same way about it as,

476
01:02:39.310 --> 01:02:41.649
Jim Salsman: as I do about,

477
01:02:42.560 --> 01:02:56.360
Jim Salsman: type annotations, when I'm talking to the TypeScript guys, you know, it's like, yeah, there's a value in them, they'll save you time on a certain set of bugs, those bugs are maybe about 10% of all the universe of bugs, and…

478
01:02:56.360 --> 01:03:04.659
Jim Salsman: you're not likely to encounter them when you're using AI these days, so I'm not into type annotations the way…

479
01:03:04.700 --> 01:03:07.719
Jim Salsman: A lot of people are, so I'll just leave it at that.

480
01:03:11.390 --> 01:03:21.550
Jason Elbaum: Yeah, I mean, a lot of… I mean, actually, this is just completely, completely orthogonal direction, but if you look at, you know, job listings, job ads.

481
01:03:21.550 --> 01:03:35.749
Jason Elbaum: And you know, lots and lots of Java listeners will say, we want somebody with 5 years of experience in, I don't know, in Java, or in Python with FastAPI, or whatever it is, in some specific technology language, and thinking.

482
01:03:36.180 --> 01:03:53.419
Jason Elbaum: maybe a few years ago, you wanted to hire someone who already knew your language and environment. We're already in code and AI now. The AI knows the languages. I can figure this out without having 10 years of experience in Python. That's what I have the computer for, so it seems like,

483
01:03:53.680 --> 01:04:01.820
Jason Elbaum: A lot of things are gonna have to change about how we think about our work and our jobs and our responsibilities, and… I don't know.

484
01:04:02.580 --> 01:04:04.840
Jason Elbaum: It's, yeah.

485
01:04:05.180 --> 01:04:07.769
Gabor Szabo: That, that seems to be true, yeah.

486
01:04:08.030 --> 01:04:11.020
Gabor Szabo: Thank you very much,

487
01:04:11.020 --> 01:04:17.569
Jim Salsman: Can I just, before we close, can I point out David in chat mentioned something that I think is worth repeating?

488
01:04:17.840 --> 01:04:22.249
Jim Salsman: Trying to find it now, I remember reading it,

489
01:04:23.270 --> 01:04:27.850
Jim Salsman: Yeah, write tests against the specification.

490
01:04:28.500 --> 01:04:43.459
Jim Salsman: those tests are going to be consequential at their unit tests. I think that's going to be my prompt that I'm going to try to clear out my 400 unit tests. I'm going to tell it, okay, keep the tests that test things that are consequential, not

491
01:04:43.660 --> 01:04:54.979
Jim Salsman: incidental, and are somehow related to either the specification or its underlying infrastructure, its necessary infrastructure. So anyway, thanks again.

492
01:04:54.980 --> 01:05:09.410
Jason Elbaum: That's sort of what I was getting at about the ATDD approach, and saying, you know, we want… thinking in terms of what is our external requirements of this code. Those are the things we want to focus on making sure they're tested.

493
01:05:09.510 --> 01:05:14.120
Jason Elbaum: And I have sometimes told my AI, like, when it's… I got a big, you know, whatever.

494
01:05:14.250 --> 01:05:23.440
Jason Elbaum: per code review with a crazy number of tests, and I say, okay, look at those tests, tell me if any of them are overlapping. Tell me if any of them…

495
01:05:23.440 --> 01:05:34.790
Jason Elbaum: are, are, are covering, scenarios that are highly unlikely, or whatever, that kind of thing. Just give us kind of guidelines of the kinds of tests that I think are lower value.

496
01:05:34.910 --> 01:05:46.130
Jason Elbaum: If any of them certainly are testing, internals or implementation details rather than, the external, behavioral interface. And,

497
01:05:46.240 --> 01:05:53.329
Jason Elbaum: Try to winnow down the test to the ones that really do add, add value and confidence.

498
01:05:53.450 --> 01:05:57.639
Jason Elbaum: That the code is correct and working, so… yeah.

499
01:05:59.340 --> 01:06:02.140
dn: Is my sound working, Gabor?

500
01:06:02.340 --> 01:06:03.520
Jason Elbaum: Yes, I hear you.

501
01:06:04.290 --> 01:06:09.650
dn: Oh, good. Managed to fix the problem. Yeah, thank you for comments, Jim.

502
01:06:10.080 --> 01:06:19.619
dn: Yeah, Jason, the ATDD… I like the idea, and it comes back to the comment in the text.

503
01:06:20.010 --> 01:06:21.000
dn: that…

504
01:06:21.170 --> 01:06:30.010
dn: we can check our code. If we write a function which opens a file and reads it in, you know, let's say config data.

505
01:06:30.270 --> 01:06:34.249
dn: We can test that that works. That's trivial.

506
01:06:35.310 --> 01:06:39.150
dn: But I think, as you… you're pointing out there, that

507
01:06:39.360 --> 01:06:48.269
dn: If we do that today, and then we write the same test on a different system, but the same functionality tomorrow, we're spinning our wheels, we're wasting a lot of time.

508
01:06:49.130 --> 01:06:57.880
dn: So that's point number one, make the tests worth doing, and then perhaps get into the software reuse scenario.

509
01:06:58.550 --> 01:07:08.060
dn: But the HTTD starts off higher, because whilst we can test our code, Who has tested the specification?

510
01:07:09.290 --> 01:07:18.930
dn: We're being asked to write software which performs a function, but who has tested that that specification is both accurate and complete?

511
01:07:19.540 --> 01:07:32.239
dn: And we've all written systems where we've been given a spec, we implement the spec, and then the very first user who's actually on the front line.

512
01:07:32.370 --> 01:07:48.809
dn: who tries it says, but hang on a minute, that's not how I do my job, right? Now, that's not a… that's not a fault of the code, right? This is one of our frustrations. We've done exactly what we've been asked to do, whether we wrote tests for our code or not.

513
01:07:48.940 --> 01:07:55.490
dn: It was, to a degree, a waste of time, because the specification was incorrect in the first place.

514
01:07:56.370 --> 01:08:01.930
dn: So… I keep asking this question, how do we test the specification?

515
01:08:02.610 --> 01:08:03.260
dn: And…

516
01:08:03.260 --> 01:08:04.230
Jason Elbaum: To, you know…

517
01:08:04.230 --> 01:08:18.839
dn: So, you know, your ATDD, that's where, to me, that's where it comes in, because the first question I ask, you know, is, if we're talking about a bank account, am I allowed to take money out of the bank account

518
01:08:18.979 --> 01:08:35.169
dn: that is a higher amount than the balance that I had, right? Am I allowed to overdraw my account? And if that's not in the specification, it's an error in the specification, not an error in the implementation, not an error in the code.

519
01:08:35.560 --> 01:08:43.460
dn: So, how do we figure that out as early as possible? So, to me, that's the value of your ATD suggestion.

520
01:08:44.500 --> 01:08:47.660
dn: And… and the ally to that is…

521
01:08:48.010 --> 01:08:53.500
dn: I find… I agree with you, I enjoy writing the code, I enjoy solving the problem.

522
01:08:54.609 --> 01:09:02.379
dn: And the problem is… sorry, that… that… I enjoy solving the problem. The issue to me is that

523
01:09:02.670 --> 01:09:08.600
dn: Writing the tests requires a different way of thinking, a different mode of thinking.

524
01:09:09.430 --> 01:09:25.629
dn: And so, trying to write one test, and then writing some code which implements the test, so the red-green, and then coming back and writing another little test, and writing another little bit of code red-green. To me, I'm switching between

525
01:09:25.819 --> 01:09:27.319
dn: modes of thought.

526
01:09:27.510 --> 01:09:37.970
dn: So, ATDD allows me to say, right, let's test the spec, and let's write a whole series of acceptance tests, and let's just work in test mode.

527
01:09:38.189 --> 01:09:44.510
dn: For the entire time, and obviously there's some decomposition of the larger problem going on here.

528
01:09:45.540 --> 01:09:49.290
dn: And THEN come back and start writing the code.

529
01:09:50.210 --> 01:09:50.930
dn: Nope.

530
01:09:51.100 --> 01:09:57.620
dn: that's not… that's not going to meet with approval from the purest TDD people, but…

531
01:09:58.290 --> 01:10:00.660
dn: I've spoken enough, care to comment?

532
01:10:01.610 --> 01:10:07.310
Jason Elbaum: No, actually, I have a lot of… a number of comments on that. First, I mean, the first thing you're… you're getting at is

533
01:10:07.540 --> 01:10:10.839
Jason Elbaum: is really a broader question, right? We've been talking about

534
01:10:11.410 --> 01:10:27.749
Jason Elbaum: you know, implementing code, implementing tests, you're talking about implementing the right thing, right? Which, in some sense, is the more important question, right? And I always say that my job is not to write code, my job is to solve problems for customers or for users.

535
01:10:27.850 --> 01:10:35.660
Jason Elbaum: as, you know, software is there not… and I did once, I had a job once where

536
01:10:35.660 --> 01:10:48.920
Jason Elbaum: I got a… we were given… the software developers were given a spec, like a 200… 200 or 300 page long spec of a system, and basically told, here, implement this.

537
01:10:48.920 --> 01:11:08.240
Jason Elbaum: And I felt like a, you know, a cog in a machine. That's not the kind of code I want to write. I want to, like I said, I want to solve interesting problems for people, and part of my job is understanding that we're building the right thing, and pushing back, and saying, hey, you know, Mr. Product Person.

538
01:11:08.260 --> 01:11:18.649
Jason Elbaum: Does this make sense? Do you understand the ramifications of this? Is this really what the user wants? Is he going to expect, what happens in such and such a scenario?

539
01:11:18.730 --> 01:11:37.629
Jason Elbaum: So, yeah, I don't think my job as a software developer is to do whatever my manager or my product develop… my product manager says. It's… it's to, you know, to do the… something that makes sense and to collaborate. It's a collaborative process. And really what the Agile

540
01:11:37.870 --> 01:11:43.240
Jason Elbaum: Software movement has… if it stands for one thing, then it's…

541
01:11:43.360 --> 01:11:58.910
Jason Elbaum: It's, they say, people over processes, first of all, and and feedback loops, right? You put a little something out there, and make sure it works, and people are happy with it, and then you build on that.

542
01:11:58.910 --> 01:12:07.469
Jason Elbaum: And that isn't… we do that partly because software is complicated, and we have to build it piece by piece. But the main… the more important reason we do that

543
01:12:07.470 --> 01:12:23.989
Jason Elbaum: It's because life is complicated, and people are complicated, and we can't just put a finished product in front of… you know, we spent… the old days, some company would invest a couple years building a piece of software, and then shrink-wrap it, and send it out to the stores, and people would encounter it for the first time.

544
01:12:24.000 --> 01:12:41.739
Jason Elbaum: And now we can push out little pieces of functionality, every day, or every week, or every hour, depending on how we work. And we get the feedback, we can find out if it's what people want, if it's what people expect. If it breaks something else, we can get that fast feedback loop.

545
01:12:41.920 --> 01:12:57.609
Jason Elbaum: And, Gen AI, in some sense, by being able to build more code faster, pushes us to enlarge those feedback loops in a way that I think isn't always healthy for the, for the,

546
01:12:57.820 --> 01:13:05.710
Jason Elbaum: The coherence, the product coherence of our systems, because it encourages us to just do more and more work before we have a chance to check whether it's the right work.

547
01:13:06.360 --> 01:13:11.790
Jason Elbaum: Did I answer any of your… Comments?

548
01:13:15.480 --> 01:13:25.289
dn: Yes, thank you. You're quite right, and it depends on whether we are iterating on an existing system or whether we're on a greenfield system.

549
01:13:25.420 --> 01:13:26.930
dn: Something brand new.

550
01:13:27.770 --> 01:13:43.870
Jason Elbaum: And it also depends on whether or not you're, you're, you know, you're a bank. If you're a bank, then you have certain things that are not negotiable, or you're a healthcare product, and you have, regulatory requirements, and you cannot push your code if it doesn't follow the rules. You know, so there…

551
01:13:43.870 --> 01:13:50.530
Jason Elbaum: There are different, different, different environments and different regulations, and, you know, Security, and all kinds of…

552
01:13:50.570 --> 01:13:58.120
Jason Elbaum: Things that we have to make sure work, and we can't just, play around with it and hope. So, yeah.

553
01:14:12.250 --> 01:14:13.060
Gabor Szabo: Meh.

554
01:14:13.060 --> 01:14:33.029
Jason Elbaum: Oh, right, and about, right, about the spec being right. Yeah, the other thing I was going to say, the spec, it's very, very unusual, in my experience, at least, that we treat the spec as this… this super big, you know, massive document that comes in as a block, and now we say implement. That's… and again, I had that happen to me once, and it really was not a pleasant experience. It was a case where they had a…

555
01:14:33.240 --> 01:14:46.980
Jason Elbaum: a product which was going through another iteration after it was… it was a lot of experience. They, you know, had architects there who knew this really well, and they said, this is how this is supposed to look. But usually, we work in smaller cycles and increments than that, and so we can…

556
01:14:46.980 --> 01:14:58.680
Jason Elbaum: Specify a task where the spec of that task is… we work to sit with product, we work it out to discuss what makes sense, and when we try it, and we get put in front of the users, and then they tell us if they think it makes sense.

557
01:14:59.200 --> 01:15:01.159
Jason Elbaum: Like I said, it's all about feedback loops.

558
01:15:06.050 --> 01:15:07.100
Jason Elbaum: Yeah, sorry.

559
01:15:07.130 --> 01:15:14.230
dn: Yeah, yeah, and that… that makes sense, you know, that phrase, makes sense, is… is effectively the acceptance test.

560
01:15:14.540 --> 01:15:21.199
dn: Right? This is what you've asked for, you said it makes sense, and this is what we've delivered. Do the two match up?

561
01:15:22.590 --> 01:15:39.059
Jason Elbaum: And if you're a mega company and you have billions of users, then your make sense is gonna be how many, you know, what your logs say, how many people are using the new feature, how much buy-in it's getting, how much revenue it's bringing in. You might not be getting feedback from individual users, but it all depends on your scale, but, yeah.

562
01:15:50.470 --> 01:15:58.070
Gabor Szabo: every time I'm opening my mouth to say that we are done, then people start speaking, which is fine. I'm just not sure.

563
01:15:58.310 --> 01:15:59.420
Gabor Szabo: What to do?

564
01:15:59.710 --> 01:16:05.789
Gabor Szabo: But it seems that we reached some… End of the conversation.

565
01:16:05.900 --> 01:16:09.980
Gabor Szabo: Or at least the part that we do on the… in the video.

566
01:16:10.220 --> 01:16:17.519
Gabor Szabo: While recording, so… thank you very much for this presentation, and for answering the questions or the comments.

567
01:16:17.720 --> 01:16:21.080
Gabor Szabo: It was really, really good. Thank you very much.

568
01:16:21.770 --> 01:16:29.079
Jason Elbaum: I hope it was, helpful, and sometimes provocative, and, I don't know, whether you agree or disagree, it's up to you.

569
01:16:29.420 --> 01:16:32.140
Gabor Szabo: Yeah, yeah, sure. And thanks everyone who

570
01:16:32.540 --> 01:16:46.790
Gabor Szabo: who was present and commented and asked questions. And for everyone who was watching on YouTube, please like the video and follow the channel. And below the video, you are going to find links for future events, and to…

571
01:16:47.020 --> 01:16:52.300
Gabor Szabo: Notes about this video, so check them out.

572
01:16:52.630 --> 01:17:04.469
Gabor Szabo: And I think that's it. People who are here, you can stay on after we stop the recording, and we can keep on chatting, and that's it.

573
01:17:04.470 --> 01:17:20.830
Gabor Szabo: And see you at the next event. I'll share the link to the various events we have. I'm going to share it again in the chat, just to make sure, but you'll also see it below the video, people on YouTube. So thank you very much, and bye-bye.

