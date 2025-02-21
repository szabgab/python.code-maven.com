---
title: Simulations for the Mathematically Challenged with Miki Tebeka
timestamp: 2025-02-21T07:30:01
author: szabgab
published: true
description:
tags:
    - Python
---

Question: What are the odds that in a class of 23 students, two have the same birthday?
We'll solve this question and others, using only a `for` loop and a random number generator.

In this talk, we'll see how to use Monte Carlo simulations to solve various problems that might intimidate you due to lack of match skills.

[source code](https://github.com/tebeka/talks/tree/master/pyweb-sim)

![](images/miki-tebeka.png)


{% youtube id="CzcxJjpUEmc" file="2025-02-20-simulations-for-the-mathematically-challenged.mp4" %}


## Transcript

1
00:00:02.020 --> 00:00:20.500
Gabor Szabo: So Hi, and welcome to the Codemaven Meetup Group and to the Codemaven Youtube Channel. In case you are watching this in Youtube, my name is Gabor. I provide the training services in python and rust and help companies get start using these languages.

2
00:00:20.740 --> 00:00:28.840
Gabor Szabo: And I also think that it's important to share knowledge among people. So that's why I'm organizing these events, these meetings.

3
00:00:29.820 --> 00:00:40.000
Gabor Szabo: So I would like to welcome everyone who joined us at this meeting, and especially Mickey, for agreeing to give this presentation, and that's it. The floor is yours, Mickey.

4
00:00:40.694 --> 00:00:44.060
Miki Tebeka: Hi, everyone. I am going to share my screen.

5
00:00:44.390 --> 00:00:48.980
Miki Tebeka: Then we will start sure.

6
00:00:50.920 --> 00:00:51.690
Miki Tebeka: Okay.

7
00:00:52.080 --> 00:01:03.720
Miki Tebeka: so we are going to talk about what I call simulations for the mathematically challenged. And this is about the tool called simulation. How you can solve various problems.

8
00:01:03.720 --> 00:01:06.970
Gabor Szabo: Sorry. Just just one thing. Can can you move the.

9
00:01:07.230 --> 00:01:07.910
Miki Tebeka: Oh, there!

10
00:01:07.910 --> 00:01:09.300
Gabor Szabo: This again, I'll do this.

11
00:01:10.010 --> 00:01:11.290
Gabor Szabo: Yeah, thanks.

12
00:01:11.290 --> 00:01:17.899
Miki Tebeka: Moved. Okay, sorry. Okay. So my name is Mickey. I've been a professional developer

13
00:01:18.210 --> 00:01:25.368
Miki Tebeka: 37 years. Now. Give or take work mostly with python and go

14
00:01:26.200 --> 00:01:31.599
Miki Tebeka: I teach. I consult, I write books, I do videos. I

15
00:01:31.870 --> 00:01:46.060
Miki Tebeka: enjoy myself in a very geeky way. And and this is a tool that I used in a couple of occasions. I think it's very simple, but not a lot of people aware of that

16
00:01:46.580 --> 00:01:51.379
Miki Tebeka: and it starts usually with the problem that you have usually a data related problem.

17
00:01:53.670 --> 00:01:58.850
Miki Tebeka: You have a cash. You want to know what are the odds that given that

18
00:01:59.080 --> 00:02:10.100
Miki Tebeka: amount of cache hits. What's the average latency? Other questions that usually involve statistics or probability.

19
00:02:10.680 --> 00:02:16.470
Miki Tebeka: And and then you said, Okay, you know, I'll we're all gigs. Right? So we go and hit the books.

20
00:02:17.910 --> 00:02:23.169
Miki Tebeka: But then you start seeing all these kinds of equations.

21
00:02:23.290 --> 00:02:28.480
Miki Tebeka: and usually around that time. I say, you know what. Maybe this problem is, not that important.

22
00:02:28.670 --> 00:02:30.920
Miki Tebeka: And I'll I'll move to do something.

23
00:02:31.680 --> 00:02:37.979
Miki Tebeka: And what I wanted to show you is basically that if you can write a follow up.

24
00:02:38.110 --> 00:02:39.529
Miki Tebeka: you can do statistics.

25
00:02:40.040 --> 00:02:46.170
Miki Tebeka: and that's it. You don't need more than that. You need the follow up, and you need random.

26
00:02:46.530 --> 00:02:55.529
Miki Tebeka: and these are the only 2 tools that you need in order to work. By the way, I'm going to show code, and if you have questions, feel free to ask

27
00:02:58.270 --> 00:03:12.519
Miki Tebeka: if you don't understand the code, if you want to learn about other things. So what are we going to do is we're going to talk about these 5 problems. So we're going to talk about the game of Qatar. And what are the best tiles going to calculate pipe

28
00:03:12.800 --> 00:03:17.480
Miki Tebeka: randomly, which sounds weird. But it's it's another

29
00:03:18.120 --> 00:03:23.610
Miki Tebeka: interesting uses for simulations. We're going to solve the birthday problem.

30
00:03:23.830 --> 00:03:31.290
Miki Tebeka: Given 23 people, I think. What's what are those the 2 people in say in this group has

31
00:03:32.900 --> 00:03:55.700
Miki Tebeka: the same birthday? We're going to see if person is sick, or what are the odds? That person is sick or not given a test that says that he is sick. And we're going to talk about the Monty Hall problem which is philosophically, it's a statistically interesting, but also a very philosophical question, not a philosopher. So you can discuss it later and see what's going on.

32
00:03:56.150 --> 00:04:02.910
Miki Tebeka: So let's start with Catan. Right? So in Catan we have these tiles, and every tile has a number on it.

33
00:04:03.290 --> 00:04:06.159
Miki Tebeka: and then you throw a couple of dices.

34
00:04:06.370 --> 00:04:13.100
Miki Tebeka: and if the number of the dices matches the number of your tile, then you can do things in the game.

35
00:04:13.290 --> 00:04:20.110
Miki Tebeka: So at the beginning you can pick out where you want to put your places, and it's up to you to decide.

36
00:04:20.269 --> 00:04:26.870
Miki Tebeka: Which tile do you want? And you want to know, you know, which tiles are going to get the most hits. What are the probability

37
00:04:27.060 --> 00:04:28.349
Miki Tebeka: of of doing that?

38
00:04:29.890 --> 00:04:30.850
Miki Tebeka: So

39
00:04:33.760 --> 00:04:39.109
Miki Tebeka: This is this is that. Yes, and I'm old. I'm using vim.

40
00:04:39.440 --> 00:04:54.299
Miki Tebeka: Sue, me later. But I think the code is clear enough. So basically, what we're going to do is we're going to do a dice wall, which is basically just a random number between one and 6. This is coming from there.

41
00:04:54.510 --> 00:05:03.489
Miki Tebeka: And then what we're going to do is we run a simulation. So what we're going? We're going to run a lot of dice roll. So I'm going to do a million

42
00:05:05.690 --> 00:05:07.109
Miki Tebeka: vice vers,

43
00:05:08.070 --> 00:05:21.110
Miki Tebeka: And every time I'm going to do 2 dice rows, right? So I get a number. And I'm updating some kind of counter right? We have counter from collections. This is a special data structure that basically stores

44
00:05:21.520 --> 00:05:29.950
Miki Tebeka: how much data we have per count.

45
00:05:30.090 --> 00:05:35.210
Miki Tebeka: And then I'm going over all the numbers right. The minimal

46
00:05:35.680 --> 00:05:48.199
Miki Tebeka: number that you can get with rolling 2 dices is 2, 2 ones and maximum. One is 12, but the range is half open. So we're not going to get there. I'm going to show the fraction

47
00:05:49.340 --> 00:05:53.260
Miki Tebeka: how many? Hey?

48
00:05:54.170 --> 00:05:57.799
Miki Tebeka: This number of the total counts, and I'm going to print it up.

49
00:05:57.920 --> 00:06:15.039
Miki Tebeka: That's that's the code that I'm going to do. And then, if you're going to do pythonpy, you're going to see now, we get probabilities right? And you see that unsurprisingly 7

50
00:06:15.290 --> 00:06:34.940
Miki Tebeka: has the best percentage to to get roll of 2 dices. And you can do the what I call the hard way, which is just, you know, doing all the combinations of all the dice rolls, and then calculate how many there are. But for me as a programmer. This is much easier.

51
00:06:35.610 --> 00:06:39.139
Miki Tebeka: Why, they just write some code. This is like 20 lines of code.

52
00:06:39.370 --> 00:06:45.859
Miki Tebeka: pretty simple. And now I have it. So this is the basic of simulation. We basically

53
00:06:47.220 --> 00:06:54.540
Miki Tebeka: create scenarios using some kind of randomness in scenario. And then we are going to

54
00:06:55.030 --> 00:07:04.519
Miki Tebeka: calculate some statistics about what happened on every scenario, and finally display the result. And this is known as a simulation or Monte Carlo simulation

55
00:07:04.710 --> 00:07:05.669
Miki Tebeka: for what we

56
00:07:08.870 --> 00:07:10.259
Miki Tebeka: questions about this one

57
00:07:16.070 --> 00:07:17.270
Miki Tebeka: no questions.

58
00:07:17.570 --> 00:07:21.660
Miki Tebeka: Alright. By the way, if you ask questions, just open the mic and ask questions, cause

59
00:07:22.140 --> 00:07:26.409
Miki Tebeka: it's hard for me to focus both on the code and on on the zoom screen.

60
00:07:26.960 --> 00:07:34.329
Miki Tebeka: Okay, the next thing we're going to do it's pretty interesting. We're going to calculate pi again randomly.

61
00:07:34.830 --> 00:07:35.890
Miki Tebeka: So

62
00:07:36.820 --> 00:07:42.999
Miki Tebeka: what the way we're going to do it is, we're going to say, let's take a circle which has a radius of one.

63
00:07:43.810 --> 00:07:48.237
Miki Tebeka: And now we're going to concentrate only on top right

64
00:07:48.990 --> 00:07:57.920
Miki Tebeka: square, which is the bonding square for this circle, and we're going to start getting random dots

65
00:07:58.290 --> 00:08:02.520
Miki Tebeka: if the dot falls in the circle, I'm going to paint them as

66
00:08:03.110 --> 00:08:08.290
Miki Tebeka: green, and if it falls outside of the circle, I'm going to paint them as red.

67
00:08:08.860 --> 00:08:16.689
Miki Tebeka: Okay? So once I've done it enough times I can calculate what is the ratio between the green dots and the red dots.

68
00:08:17.180 --> 00:08:21.580
Miki Tebeka: and this ratio is quarter of a pipe.

69
00:08:24.010 --> 00:08:28.210
Miki Tebeka: right? Because the the area of the

70
00:08:30.090 --> 00:08:32.335
Miki Tebeka: the way of the circle is

71
00:08:33.780 --> 00:08:37.330
Miki Tebeka: pi r squared. But r is one. So it's just pi.

72
00:08:37.840 --> 00:08:42.050
Miki Tebeka: so basically, the amount of dust that falls inside the circle should be pi.

73
00:08:42.320 --> 00:08:50.420
Miki Tebeka: but we we doing it only on a quarter of a circle. This is a quarter of a pi, and we are going to get the number pi.

74
00:08:50.800 --> 00:08:56.720
Miki Tebeka: So this is pi, dot, PP. 1,

75
00:08:57.840 --> 00:09:13.699
Miki Tebeka: so again, we we're going to import this time uniform from random, and then sq, and this is going to run for a bit. So I'm going to display display progress bar with something called Tqdm.

76
00:09:15.030 --> 00:09:22.700
Miki Tebeka: and then the radius of is one, and we have n, which is the number of iterations which is a hundred 1 million.

77
00:09:23.370 --> 00:09:35.250
Miki Tebeka: and inner, is the number of points that are inside the circle, which I'm going to do with to start with 0, right? So I'm getting X and Y, which is uniform between 0 and one.

78
00:09:35.960 --> 00:09:42.390
Miki Tebeka: And then, if the point falls inside the circle, I'm just going to increment inner.

79
00:09:43.700 --> 00:09:46.760
Miki Tebeka: So this is how many points fell inside the signal.

80
00:09:48.670 --> 00:10:01.319
Miki Tebeka: Now the ratio is inner divided by N. And as we said, this is quarter of a pi, so we need to print out 4 times this ratio to get to the number of pi

81
00:10:07.660 --> 00:10:14.720
Miki Tebeka: and you know what I'm going to also run the time command to show you how much time it took. So this is, this is a hundred 1 million

82
00:10:15.110 --> 00:10:19.840
Miki Tebeka: Ron's so it's going to take a little bit of fine.

83
00:10:20.300 --> 00:10:21.420
Miki Tebeka: And

84
00:10:23.110 --> 00:10:30.290
Miki Tebeka: and it's a good thing in the winter, because it also warms up your CPU, so you can warm yourself without using the A/C.

85
00:10:35.020 --> 00:10:43.789
Miki Tebeka: I said. Tqdm, which shows the progress bar is really nice, especially if you have long running processes, you know, if your process is actually running or it's not stuck.

86
00:10:43.930 --> 00:10:45.236
Miki Tebeka: So we're

87
00:10:46.570 --> 00:10:56.980
Miki Tebeka: So it's been done. And and we see that we got a 3.1 4.

88
00:10:57.380 --> 00:11:04.729
Miki Tebeka: Yeah, which is close enough to pie. And it took us about 41 seconds to run.

89
00:11:06.320 --> 00:11:12.810
Miki Tebeka: Now, one thing that can help you with simulations is pip pi-pipe.

90
00:11:12.980 --> 00:11:24.209
Miki Tebeka: So if you're not familiar, the python we are using is called C. Python. It's python written in C. There are other pythons, such as Jython, which is Python, written in Java.

91
00:11:24.530 --> 00:11:30.700
Miki Tebeka: and several others, and micropython for micro devices, and there is pi pi.

92
00:11:30.970 --> 00:11:39.090
Miki Tebeka: which is a python written in Python, and it has several optimizations that are not in C. Python.

93
00:11:39.330 --> 00:11:48.439
Miki Tebeka: especially a git compiler, though from 3 13 and up we have an experimental git compiler in C title which should bring it.

94
00:11:49.475 --> 00:11:54.449
Miki Tebeka: and if I'm going to run a pi po eye on that thing.

95
00:11:54.640 --> 00:11:56.969
Miki Tebeka: you're going to see the difference.

96
00:11:57.100 --> 00:12:05.319
Miki Tebeka: Right? No, forgot the time. Command like. You see, this is

97
00:12:05.520 --> 00:12:12.520
Miki Tebeka: 3.5 seconds, so more than 10 times faster on these calculations. So I'm not going to. I'm not saying.

98
00:12:13.420 --> 00:12:22.700
Miki Tebeka: Use pi for everything. There are some compatibility issues with, especially external libraries and maybe other things, and it's not

99
00:12:22.890 --> 00:12:30.900
Miki Tebeka: on par with python. Currently, I think they're on they're on on 3, 10,

100
00:12:31.160 --> 00:12:36.990
Miki Tebeka: equivalent to 3, 10. And right now in Python we are in 3 13. So they take some time

101
00:12:37.400 --> 00:12:40.189
Miki Tebeka: they're building up, and then they close it.

102
00:12:40.690 --> 00:12:48.000
Miki Tebeka: But it's a it's a nice tool to know and and work with questions about this one.

103
00:12:56.360 --> 00:12:59.850
Gabor Szabo: It's not about this one. And and probably it's not

104
00:13:00.490 --> 00:13:13.559
Gabor Szabo: relevant to this, this presentation. But maybe it's for another time is how come actually, this pi can be pi can be so much faster. I would really like to understand this.

105
00:13:13.560 --> 00:13:29.079
Miki Tebeka: The the current. C. Python itself does not do any optimization. So if you look at the C compiler, it has tons of optimization loop, unrolling, constant folding, a lot of many things that the python temperature is not doing at all.

106
00:13:29.784 --> 00:13:40.270
Miki Tebeka: And the other thing is that there is a technology called jit, which is just in time compilation, which means that you run the code. Once in python.

107
00:13:40.430 --> 00:13:45.080
Miki Tebeka: you see what happens there and then you generate specific machine code.

108
00:13:45.230 --> 00:13:52.810
Miki Tebeka: And next time you call the function, it is actually, not the python function. It's called, but the

109
00:13:53.160 --> 00:14:03.310
Miki Tebeka: optimized generated machine code for that. And this is something that Nodejs and other dynamic languages are using, including Java.

110
00:14:03.590 --> 00:14:08.849
Miki Tebeka: to make things faster. And Pypi has pipi. Sorry. Pi Pi has a

111
00:14:09.040 --> 00:14:12.810
Miki Tebeka: a very good git compiler that has been developed for a lot of years.

112
00:14:13.449 --> 00:14:21.089
Miki Tebeka: And that's why it's faster. Basically, pi is written in Python, but eventually generates a

113
00:14:21.520 --> 00:14:28.779
Miki Tebeka: and executable in machine code. So it is pretty fast in this case.

114
00:14:32.600 --> 00:14:34.444
Miki Tebeka: Okay, so

115
00:14:35.730 --> 00:14:43.390
Miki Tebeka: someone joked that, you know, this is every time they go on a Zoom Meeting. That's what comes to their mind right? This is very similar to

116
00:14:43.630 --> 00:14:55.150
Miki Tebeka: to Zoom, and the idea is, and this is known as the birthday problem. Given a group of people.

117
00:14:55.500 --> 00:15:00.259
Miki Tebeka: what are the odds that 2 people have the same birthday?

118
00:15:00.800 --> 00:15:01.740
Miki Tebeka: And

119
00:15:08.330 --> 00:15:10.020
Miki Tebeka: if a

120
00:15:11.310 --> 00:15:19.429
Miki Tebeka: what I pick up as a group. Size is 23 people. So I would like you to just take a guess

121
00:15:19.730 --> 00:15:24.659
Miki Tebeka: like we have a group of 23 people. What are the odds that 2 people have the same birthday?

122
00:15:24.930 --> 00:15:35.990
Miki Tebeka: Yeah. So around the birthday. So I'm going to basically say that I'm not looking at dates. I'm looking at day of year. So we have 365 days per year. So

123
00:15:36.480 --> 00:15:41.359
Miki Tebeka: a random date is basically a number between one and 365. That's

124
00:15:41.590 --> 00:15:50.350
Miki Tebeka: how many days we have in here. And now what I'm saying is given a groups of a given size. Are there any duplicates in the group?

125
00:15:50.770 --> 00:16:00.790
Miki Tebeka: Alright? So basically I creating a set and then going over the numbers generating around the birthday. And then, if it's already. If you already seen this birthday.

126
00:16:01.290 --> 00:16:06.209
Miki Tebeka: we say there is a duplication, so at least 2 people have the same birthday in that group.

127
00:16:06.350 --> 00:16:16.929
Miki Tebeka: otherwise we add it to the group and return. And finally, if you're out of the follow, we say, no, there are no duplicates in this group. So basically, we draw a group of

128
00:16:17.140 --> 00:16:18.390
Miki Tebeka: random numbers.

129
00:16:19.026 --> 00:16:24.570
Miki Tebeka: Between one and 365, and say, is there an overlap here somewhere?

130
00:16:26.440 --> 00:16:38.710
Miki Tebeka: Alright? And now we start again. The simulation. So simulation now is going to run over a million. We're going to do it 1 million times. The group size is 23. And again, none of the applications is

131
00:16:38.900 --> 00:16:48.529
Miki Tebeka: 0 to begin with. And then we run the simulation. And if there is a duplication, we say, Okay, let's increment duplication.

132
00:16:48.640 --> 00:16:54.299
Miki Tebeka: Finally, we are printing what the fraction is from the total.

133
00:16:55.750 --> 00:16:58.950
Miki Tebeka: Okay, so remember the number you guessed.

134
00:17:09.520 --> 00:17:12.040
Miki Tebeka: anyone guessed 50%.

135
00:17:15.579 --> 00:17:18.080
Miki Tebeka: Right? This is seems pretty high right.

136
00:17:18.319 --> 00:17:24.920
Miki Tebeka: And this is something that happens with statistics and probabilities a lot of time. This is not intuitive.

137
00:17:25.069 --> 00:17:33.850
Miki Tebeka: A lot of times we think that we know the answer, and we say, you know, there are a lot of days, only 23 people. How comes? But

138
00:17:34.070 --> 00:17:41.780
Miki Tebeka: if you do it and you do the statistical computation, you'll get exactly the same thing. That's that's the idea. But

139
00:17:42.430 --> 00:17:48.739
Miki Tebeka: again, this is a a more complicated the

140
00:17:49.250 --> 00:17:53.420
Miki Tebeka: computation. And for me, as a developer. This is pretty easy.

141
00:17:53.760 --> 00:17:55.630
Miki Tebeka: you know a follow up around them.

142
00:17:56.360 --> 00:17:57.329
Miki Tebeka: I'm done with.

143
00:18:01.430 --> 00:18:10.880
Gabor Szabo: Yeah, it's nice. What would be interesting, I think, is to see if you take 2 people, 3 people and so on. Up to 365 people.

144
00:18:11.340 --> 00:18:15.830
Gabor Szabo: and for each number to see this, the probability and then graph.

145
00:18:16.185 --> 00:18:27.929
Miki Tebeka: Pretty sure there is. If you go on the web. This is a really known problem. People have done it already. There's a. You can probably see the graph for that.

146
00:18:29.194 --> 00:18:37.129
Miki Tebeka: But this is not exactly true. Right? This is a joke right?

147
00:18:37.280 --> 00:18:46.709
Miki Tebeka: And the chances of a piece of bread falling on the on butter side down is directly proportional to the cost of the carpet, like it's not 50 50.

148
00:18:47.040 --> 00:18:49.360
Miki Tebeka: This is correlations to Mr. Murphy.

149
00:18:49.580 --> 00:18:50.490
Miki Tebeka: Oh.

150
00:18:50.730 --> 00:19:02.460
Miki Tebeka: and the thing is that not everybody is born or does not an average distribution on the days that you are born, especially if you're born on March 29, th

151
00:19:03.080 --> 00:19:09.370
Miki Tebeka: right? This is reducing the odds that you're going to have someone with the same birthday.

152
00:19:12.510 --> 00:19:13.389
Miki Tebeka: So

153
00:19:17.110 --> 00:19:32.149
Miki Tebeka: we. We have a model, and there's a saying, by George, Box, which I really believe that all models are wrong. But some are useful right? So it needs to be interesting enough, or or the answer should be interesting enough, but not to

154
00:19:34.740 --> 00:19:35.405
Miki Tebeka: to

155
00:19:38.780 --> 00:19:45.018
Miki Tebeka: to give you a useful answer. But you can have a model. So I actually took some data from

156
00:19:45.590 --> 00:19:48.589
Miki Tebeka: for about birthdays in general.

157
00:19:49.030 --> 00:19:53.730
Miki Tebeka: Right? So no, this is

158
00:19:55.770 --> 00:20:06.170
Miki Tebeka: us both. Right? So the the Csv file gives you. What is the birthday? Per file? Oh, this is a windows. New lines. Yay,

159
00:20:07.250 --> 00:20:08.130
Miki Tebeka: so

160
00:20:09.380 --> 00:20:14.699
Miki Tebeka: We have a year, month, day of birth, day of the week, and and how many birth there were

161
00:20:15.070 --> 00:20:17.320
Miki Tebeka: per every one of them.

162
00:20:17.941 --> 00:20:24.589
Miki Tebeka: And then what I'm going to do is I'm going to do actually weighted probabilities.

163
00:20:24.910 --> 00:20:28.047
Miki Tebeka: meaning it's not that every day has the

164
00:20:29.080 --> 00:20:41.680
Miki Tebeka: the same probability. But I'm going to use these frequencies to do that. And here I'm going to switch over to tools from the scientific python side of things.

165
00:20:42.410 --> 00:20:45.390
Miki Tebeka: And these tools are pandas and numpy.

166
00:20:46.170 --> 00:21:04.579
Miki Tebeka: And I'm using pandas. If you're not familiar with pandas, and this may be a topic for a different talk, or probably already done it before. Then, this is a really really great library for working with data. I'm using it to load the Csv

167
00:21:06.360 --> 00:21:15.900
Miki Tebeka: so basically, I'm loading the birthdays from this Csv file, and I'm I'm and

168
00:21:18.510 --> 00:21:20.829
Miki Tebeka: converting things to daytime.

169
00:21:20.980 --> 00:21:25.829
Miki Tebeka: And then I'm saying that the the birthday is the day and the month.

170
00:21:27.370 --> 00:21:36.752
Miki Tebeka: and then I'm doing what is known as a group by to get all of the people that were born on the same day in the month

171
00:21:38.260 --> 00:21:45.690
Miki Tebeka: divided by the total number of probabilities, and then return the index and the values am.

172
00:21:46.010 --> 00:21:52.929
Miki Tebeka: So once I have that I can do something else I'm going to use now. Numpy

173
00:21:53.320 --> 00:21:59.770
Miki Tebeka: numpy has a random choice. Basically choice says, pick things from from a group.

174
00:22:00.274 --> 00:22:10.019
Miki Tebeka: But and if you don't say anything, it's it's going to give an equal probability to everything. But you can provide the size and the probabilities.

175
00:22:10.230 --> 00:22:18.226
Miki Tebeka: and then it is going to do a weighted probability meaning there's a bigger chance. If if people are more people are born on.

176
00:22:19.980 --> 00:22:24.335
Miki Tebeka: What is that? September 9, let's say then,

177
00:22:24.950 --> 00:22:30.960
Miki Tebeka: there is a bigger chance. It's going to pick. September 9 versus February 29, th

178
00:22:31.430 --> 00:22:36.951
Miki Tebeka: let's say, or other day, April 26. For some reason I don't know why

179
00:22:37.570 --> 00:22:42.380
Miki Tebeka: people don't like their birthday, they think, or July, July 4.th

180
00:22:43.140 --> 00:22:46.209
Miki Tebeka: I don't know why they have lessened.

181
00:22:46.480 --> 00:22:53.181
Miki Tebeka: Okay, so I'm loading the birthdays from from the Csv file. I'm doing

182
00:22:56.150 --> 00:23:04.390
Miki Tebeka: And again, no 100,000 this time. Simulations. The group size is 23, and

183
00:23:04.550 --> 00:23:10.139
Miki Tebeka: duplicate is 0. And again, I'm doing the same same. Follow up. And again the same thing the time

184
00:23:10.290 --> 00:23:11.440
Miki Tebeka: I'm doing here.

185
00:23:17.470 --> 00:23:22.520
Miki Tebeka: And if I'm running this one we got the same number.

186
00:23:23.640 --> 00:23:33.690
Miki Tebeka: But this is rounding up. Pretty sure if I'm going to show more digits after the decimal. It is going to show more. You're going to see the difference. But the idea is that

187
00:23:34.725 --> 00:23:38.680
Miki Tebeka: we we added more. We made our model more accurate.

188
00:23:38.790 --> 00:23:42.699
Miki Tebeka: but the inner, the even the inaccurate model, was good enough.

189
00:23:42.850 --> 00:23:48.714
Miki Tebeka: right? It was good enough, and that's what saying that all models are wrong, but some are useful.

190
00:23:49.760 --> 00:23:59.990
Miki Tebeka: you don't have to have exact distribution of exact information about your data to gain some insights which are correct from the data. And a lot of time.

191
00:24:00.420 --> 00:24:02.260
Miki Tebeka: you can do approximations.

192
00:24:02.910 --> 00:24:09.580
Miki Tebeka: And statistically, it's still good Facebook questions.

193
00:24:16.730 --> 00:24:17.690
Miki Tebeka: No question.

194
00:24:18.270 --> 00:24:25.577
Miki Tebeka: Okay, so this is about

195
00:24:26.270 --> 00:24:32.039
Miki Tebeka: a question that actually, they they gave to doctors. They said that there is a test for disease

196
00:24:32.370 --> 00:24:42.200
Miki Tebeka: that has 5% false positives, meaning that in 5% of the people. The test will tell you that you're sick, even though you're not sick.

197
00:24:42.530 --> 00:24:44.750
Miki Tebeka: This is what is known as a false positive.

198
00:24:45.320 --> 00:24:51.000
Miki Tebeka: and he says that it knows that the disease strikes about one person in a thousand in the population.

199
00:24:52.330 --> 00:24:55.103
Miki Tebeka: Okay, they said, okay, now we we're taking

200
00:24:55.970 --> 00:25:08.399
Miki Tebeka: a random test. We take a random person from the street, we make the we make the test, and the test says this person is sick. What is the actual probability that this patient is really sick.

201
00:25:09.550 --> 00:25:11.930
Miki Tebeka: Okay? And think about that.

202
00:25:12.388 --> 00:25:18.140
Miki Tebeka: With Covid, for example. Right they swap you for Covid and says you have Covid. Now

203
00:25:18.430 --> 00:25:38.570
Miki Tebeka: you're home. You're not allowed to go out sometimes, you know, for other diseases. It might say that the doctor says, Okay, you're sick now you need a treatment, maybe a violent treatment, maybe something which costs a lot of money. So they ask his doctors to see if they're actually basing their decisions on something which makes sense or not.

204
00:25:38.690 --> 00:25:43.869
Miki Tebeka: Right. So talking about true positives, right? So

205
00:25:44.450 --> 00:25:50.620
Miki Tebeka: if I predicted that the person is sick and they're actually sick. This is what known as a true positive.

206
00:25:51.430 --> 00:25:57.499
Miki Tebeka: We talked about false positive, which is person, is said to be sick, but they are actually healthy.

207
00:25:59.040 --> 00:26:03.640
Miki Tebeka: and we also have false negative saying, this is now

208
00:26:03.860 --> 00:26:06.710
Miki Tebeka: person who is sick, and we said that they're healthy.

209
00:26:06.920 --> 00:26:15.630
Miki Tebeka: and we have a true negative, which is a healthy person, and that says they are healthy. Right? Remember, positive is sick, negative, healthy.

210
00:26:16.180 --> 00:26:19.649
Miki Tebeka: That's it. This thing is known as a confusion matrix.

211
00:26:19.910 --> 00:26:25.470
Miki Tebeka: And on the confusion matrix, you can do a lot of

212
00:26:25.910 --> 00:26:29.789
Miki Tebeka: calculations. When you measure your models.

213
00:26:30.060 --> 00:26:43.740
Miki Tebeka: especially prediction models, you start with the confusion matrix and then say, what is the percent of true positive, can I? There's precision, recall, and and several other things that come to mind.

214
00:26:44.070 --> 00:26:51.570
Miki Tebeka: I call it the. I think the name confusion. Matrix is also very good, because

215
00:26:51.760 --> 00:26:55.139
Miki Tebeka: I always get confused by that. I need to go back and think about

216
00:26:56.000 --> 00:26:58.449
Miki Tebeka: what every term is saying. But we do that.

217
00:26:58.600 --> 00:27:04.280
Miki Tebeka: So let's have a look at the signal. Okay, so

218
00:27:07.510 --> 00:27:10.059
Miki Tebeka: I have a function for warning. So

219
00:27:10.560 --> 00:27:14.720
Miki Tebeka: I want to say that one in

220
00:27:15.310 --> 00:27:27.320
Miki Tebeka: a thousand. Right? They said, one in a thousand is sick. So basically what they're saying, I'm drawing a number between one and N, and if this number is one, and I can pick any number between. N. So 17

221
00:27:27.780 --> 00:27:31.560
Miki Tebeka: 3, any number will will work. I just need

222
00:27:31.730 --> 00:27:34.390
Miki Tebeka: that one in Ni will happen.

223
00:27:36.230 --> 00:27:43.460
Miki Tebeka: And now, I'm I'm going to say, like this. There is a person.

224
00:27:44.190 --> 00:27:56.340
Miki Tebeka: and if the person is sick we are going to say that the person is sick. This is not specified in the question in the equation, but this is the assumption, the assumption that there are no false negatives.

225
00:27:56.680 --> 00:27:58.850
Miki Tebeka: They're only false, positive.

226
00:27:59.020 --> 00:28:06.990
Miki Tebeka: So if you are doing that, and they say if it, the disease is.

227
00:28:07.220 --> 00:28:27.909
Miki Tebeka: we say we have a 5% false positive. So in one. In 20 cases this test is also going to say true. So if the person is sick, the test is going to say, for sure you're sick. If you're healthy, there's 1 in 5%, one in 5, 1 in 20. Sorry chance that you're the test will still say that you're sick, even though you're healthy.

228
00:28:30.070 --> 00:28:35.889
Miki Tebeka: So now, number of sick people and number of people who are diagnosed as sick are both starting at 0.

229
00:28:36.150 --> 00:28:40.569
Miki Tebeka: And now we are running a million simulations

230
00:28:40.720 --> 00:28:47.079
Miki Tebeka: for every one of them. We are picking a person at random, so the chances of the person being sick

231
00:28:47.240 --> 00:28:57.279
Miki Tebeka: like we said, Here, and the disease strikes 1 1 of every 1,000 people in the population.

232
00:28:57.390 --> 00:29:01.800
Miki Tebeka: Right? So there's a 1 in a thousand chance that this person is sick.

233
00:29:02.450 --> 00:29:06.310
Miki Tebeka: and if the person is sick, then we increment the number of sick.

234
00:29:06.440 --> 00:29:10.619
Miki Tebeka: and then we do the diagonals for the person, and if

235
00:29:11.990 --> 00:29:14.820
Miki Tebeka: we diagnose the person is sick, we increment the number of.

236
00:29:14.970 --> 00:29:18.160
Miki Tebeka: But okay.

237
00:29:18.760 --> 00:29:26.069
Miki Tebeka: So now we have the number of people who are actually sick. And I know people who were diagnosed as sick. And we are going to

238
00:29:27.110 --> 00:29:31.512
Miki Tebeka: print out this frequency that says,

239
00:29:33.000 --> 00:29:38.800
Miki Tebeka: what are the percentage of people who are actually sick from the people who are diagnosed as sick.

240
00:29:41.160 --> 00:29:42.610
Miki Tebeka: Anyone care to guess

241
00:29:51.340 --> 00:29:54.650
Miki Tebeka: 2%. See, you are good.

242
00:29:57.160 --> 00:30:02.210
Miki Tebeka: Okay? So a lot of people are saying, you know, this is

243
00:30:02.340 --> 00:30:04.820
Miki Tebeka: what right? The the test is

244
00:30:05.020 --> 00:30:15.159
Miki Tebeka: only 5% false, positive. How come? So 95%. It's okay. But still only 2% of the people are sick.

245
00:30:15.530 --> 00:30:17.620
Miki Tebeka: So and and think about that.

246
00:30:19.520 --> 00:30:24.550
Miki Tebeka: yeah, 1% per divide 5%. That's 2%

247
00:30:25.490 --> 00:30:26.240
Miki Tebeka: So

248
00:30:29.630 --> 00:30:50.819
Miki Tebeka: if you come to think about that, that has a lot of implications. This is, again, this intuition that we have that is usually wrong when it comes to these things. And the 3rd thing that they give this test to a lot of doctors. Most of them get it wrong. And then it means that they're actually basing treatments and other things on something which is

249
00:30:51.220 --> 00:30:52.330
Miki Tebeka: not correct.

250
00:30:53.535 --> 00:30:57.430
Miki Tebeka: So maybe they should run a simulation

251
00:30:57.600 --> 00:31:00.239
Miki Tebeka: and get some understanding of what's going on.

252
00:31:01.920 --> 00:31:02.710
Miki Tebeka: Alright.

253
00:31:03.700 --> 00:31:11.480
Miki Tebeka: The last one that one is known as the Monty Hall problem. And we are

254
00:31:11.970 --> 00:31:14.529
Miki Tebeka: okay. Well, we have a lot of time.

255
00:31:14.860 --> 00:31:24.710
Miki Tebeka: I'll start speaking. No so the Monty Hall problem says, you're in a game show, and you have 3 doors.

256
00:31:24.990 --> 00:31:30.829
Miki Tebeka: and the host says, you know, behind 2 doors there are goats.

257
00:31:31.030 --> 00:31:36.710
Miki Tebeka: and behind and the 3rd door. There is a car that you can win.

258
00:31:37.980 --> 00:31:43.140
Miki Tebeka: and it says, Pick a door, 1, 2, or 3, and you pick a door. Let's say I picked one.

259
00:31:43.270 --> 00:31:50.730
Miki Tebeka: And now the host says, Okay, he goes on to another door. Let's say this time door number 2 opens the door and shows you a goat.

260
00:31:50.990 --> 00:31:53.920
Miki Tebeka: And now, he says, do you want to keep

261
00:31:54.530 --> 00:31:58.800
Miki Tebeka: your original door, or do you want to switch to the second one?

262
00:32:02.050 --> 00:32:14.090
Miki Tebeka: Right? So you have a strategy now to say, now I pick door number one. I'm going to stay with door number one, or after they show me the door with the goat. I want to change my my answer, and I actually go on to pick door number 3.

263
00:32:14.660 --> 00:32:19.359
Miki Tebeka: So what is the strategy? What is the good strategy to work in this case.

264
00:32:19.660 --> 00:32:24.539
Miki Tebeka: Too late, is it? On, on one or 2?

265
00:32:25.203 --> 00:32:35.650
Miki Tebeka: So again, we are going to simulate right? So a random door is around the manager now

266
00:32:36.020 --> 00:32:45.589
Miki Tebeka: and here. What we're doing is that we pick, we say, does staying with the door wins the game right? So we

267
00:32:46.133 --> 00:32:49.850
Miki Tebeka: we pick a 1 door which the car is

268
00:32:51.282 --> 00:32:57.270
Miki Tebeka: under the door, and then we pick another door, which is the door that the player picked.

269
00:32:57.890 --> 00:33:03.619
Miki Tebeka: Now, if the if it is the same door, it means that the player who says I'm going to stay

270
00:33:03.720 --> 00:33:06.080
Miki Tebeka: is going to win the game.

271
00:33:07.580 --> 00:33:14.870
Miki Tebeka: Okay? So I'm just saying, if the color is equal to the player door, then, meaning that the stay strategy wins.

272
00:33:15.240 --> 00:33:17.310
Miki Tebeka: And now I'm going to

273
00:33:18.660 --> 00:33:26.040
Miki Tebeka: to do a million simulations. I'm going to say that these are the number of wins that the stay strategy have.

274
00:33:26.160 --> 00:33:31.619
Miki Tebeka: and these are the 9 number of wins that the switch strategy had.

275
00:33:31.880 --> 00:33:38.980
Miki Tebeka: And I'm going to run the simulation, and then, if stay wins the game, I'm incrementing the stays. Otherwise

276
00:33:39.620 --> 00:33:43.610
Miki Tebeka: I'm going to increment the wins, and then I

277
00:33:44.710 --> 00:33:53.400
Miki Tebeka: divide them by N. So what is the fraction of the one? And I'm printing out? What is the fraction of times we want with staying, and what is the fraction of

278
00:33:53.980 --> 00:33:58.640
Miki Tebeka: things that, and we did by switching

279
00:34:04.620 --> 00:34:10.360
Miki Tebeka: any guesses which strategy is better.

280
00:34:20.120 --> 00:34:25.560
Miki Tebeka: So if you switch door, you have twice as much chances of winning.

281
00:34:25.980 --> 00:34:30.609
Miki Tebeka: Then then stay.

282
00:34:30.900 --> 00:34:35.659
Miki Tebeka: And and this is really counterintuitive. Because why?

283
00:34:36.440 --> 00:34:45.299
Miki Tebeka: Right? I picked the door at one dome. There could be a car under it. The fact that someone showed me another door that I didn't pick as a goat in it shouldn't change that.

284
00:34:45.790 --> 00:34:47.720
Miki Tebeka: But it actually does.

285
00:34:47.920 --> 00:34:56.590
Miki Tebeka: And there's a lot of debate. If you Google, the multi-hole problem with statistics, there's a lot of debate about

286
00:34:56.710 --> 00:34:59.999
Miki Tebeka: what? What does it mean? And and

287
00:35:00.260 --> 00:35:10.629
Miki Tebeka: are these calculations okay or not. For me. Yeah, it's I have a strategy now. So if I see a goat, they pick the other door. And that's it.

288
00:35:14.370 --> 00:35:18.649
Miki Tebeka: Okay? So you can read more on Wikipedia, on the Monty Hall problem and it.

289
00:35:19.582 --> 00:35:25.739
Miki Tebeka: so that's that's basically these are the 4 cases. And I hope I convince you that

290
00:35:26.660 --> 00:35:30.299
Miki Tebeka: when you have these questions don't don't shy away because you don't know the map

291
00:35:30.470 --> 00:35:40.719
Miki Tebeka: because you don't know how to figure out statistics, and a lot of time will also help you, because a lot of time, our intuition, when it comes to statistics and probabilities, is usually wrong.

292
00:35:41.280 --> 00:35:50.400
Miki Tebeka: We, we, as people, have good intuition about small numbers when it comes to large numbers, we are really

293
00:35:51.569 --> 00:35:53.129
Miki Tebeka: very bad at that.

294
00:35:53.827 --> 00:36:04.760
Miki Tebeka: There, there's 1 statistic and and nothing tallible says that every time he works with statistics he need to turn off this part of the brain that says, I know what I'm doing, and just pass the numbers

295
00:36:05.050 --> 00:36:17.420
Miki Tebeka: right? So if you want to learn more, there is a great talk by Jake Vanderplass is an astrophysicist who's heavily involved in scientific python community.

296
00:36:17.850 --> 00:36:35.519
Miki Tebeka: and he has that's where that's where I started, and he shows some other simulations and how to do statistics. You can read more about the multicolor simulation in in Wikipedia. By the way, I think even in Google sheets and and excel, you can run

297
00:36:36.570 --> 00:36:42.519
Miki Tebeka: Monte Carlo simulations, which is pretty awesome, or in excel

298
00:36:46.570 --> 00:36:50.369
Miki Tebeka: in in excel. Now we have python in excel. Right? So this is

299
00:36:50.760 --> 00:36:54.949
Miki Tebeka: great, and there's a library called Simpy.

300
00:36:55.100 --> 00:37:10.809
Miki Tebeka: If you want to do what is known as a discrete simulation. And Simpa, basically for every tick tell, you tell you process to do something, and then you can simulate cars going and people crossing the road and cell phone towers, and a lot of, and a lot of other things.

301
00:37:14.760 --> 00:37:23.070
Miki Tebeka: Zia, I'm not sure what your name is. But, he said, the simulation will not help you if the problem is not well specified, and that that is true.

302
00:37:23.360 --> 00:37:30.109
Miki Tebeka: Right. So you need a good definition of the problem before you start. If you have a vague definition of the problem, then

303
00:37:30.650 --> 00:37:31.560
Miki Tebeka: now

304
00:37:40.240 --> 00:37:48.350
Miki Tebeka: you, you can think about it any way you want. I'm not sure why you're saying that the Monty Hall problem is not fully defined, but we can talk about it later.

305
00:37:50.230 --> 00:37:52.989
Miki Tebeka: Because this is just about picking a strategy to win.

306
00:37:53.100 --> 00:37:55.940
Miki Tebeka: And I think the the switch one is is a winning strategy.

307
00:37:58.290 --> 00:38:03.219
Miki Tebeka: That's it. All of this code is in my github

308
00:38:03.490 --> 00:38:11.880
Miki Tebeka: talks repo, so you can look at the code there. All all the things that that they have there.

309
00:38:13.050 --> 00:38:20.920
Miki Tebeka: I wrote a book on Python with quizzes, if you want to to buy it, and if you have questions, that's a good time to ask them. Not

310
00:38:28.840 --> 00:38:30.660
Miki Tebeka: no question. Gabor.

311
00:38:30.970 --> 00:38:36.500
Gabor Szabo: Well, I don't have any question either. Now. I already asked the ones I had.

312
00:38:36.620 --> 00:38:40.469
Gabor Szabo: I just want to thank you and thank everyone who who joined us.

313
00:38:41.320 --> 00:38:42.590
Gabor Szabo: And

314
00:38:44.080 --> 00:38:56.819
Gabor Szabo: if you are watching the video and you reach this point, then please remember to like the video and follow the channel. And under the video you will find a link to where you will have the link to this Github page.

315
00:38:56.930 --> 00:39:05.280
Gabor Szabo: To this Github Repo, and you will be able to also find find Mickey. I guess you also.

316
00:39:05.730 --> 00:39:06.530
Miki Tebeka: Yeah, yeah, sure.

317
00:39:06.530 --> 00:39:07.200
Gabor Szabo: Share your link.

318
00:39:07.200 --> 00:39:09.780
Miki Tebeka: If you have any questions I will answer.

319
00:39:11.540 --> 00:39:15.230
Gabor Szabo: Okay, so thank you very much.

320
00:39:15.510 --> 00:39:16.870
Miki Tebeka: So more for organizing this.

321
00:39:17.710 --> 00:39:21.050
Gabor Szabo: You're welcome, and I hope to see you in other presentations.

322
00:39:21.050 --> 00:39:22.110
Miki Tebeka: Awesome. Thank you.

323
00:39:22.110 --> 00:39:22.770
Gabor Szabo: Bye, bye.

