---
title: Python async.io - From zero to hero with Eyal Balla
timestamp: 2025-02-13T13:10:01
author: szabgab
published: true
description:
---


Asyncio is a cool part of python. But what does it do?
It is a way to write async code in Python.

This lecture shows use real world use cases, knowhows and troubleshooting methods for using asyncio in python

[Eyal Balla](https://www.linkedin.com/in/eyal-balla/)


![Eyal Balla](images/eyal-balla.jpeg)


{% youtube id="aNYSG_HcX0g" file="2025-02-12-python-async-io-from-zero-to-hero.mp4" %}


## Transcript

1
00:00:01.740 --> 00:00:30.889
Gabor Szabo: So Hello, and welcome to the Codemavens, Meetup Group and Codemavens Channel. If you're watching it on on Youtube, my name is Gabor Sabo. I usually teach python and rust at companies and also introduce test automation and Ci, and that the area and I also think that sharing knowledge is extremely important among high tech

2
00:00:31.470 --> 00:00:56.010
Gabor Szabo: programmers and and people working in the high tech industry. So that's why I am organizing these these meetings, these presentations. As you can see it's being recorded. It's going to be on Youtube, please, like the video and follow the channel below the video, you will find a link to information about Al and and about the content of this video.

3
00:00:56.130 --> 00:01:03.549
Gabor Szabo: And I would like to welcome everyone who's who joined us in the live meeting, and especially like Eyal, giving us the presentation.

4
00:01:03.820 --> 00:01:11.349
Gabor Szabo: So now it's yours. Please introduce yourself and share the screen as you feel fit and welcome.

5
00:01:12.590 --> 00:01:30.479
Eyal Balla: Thank you. So I'll share the screen. So this is presentation about it's the it's like a take off on a presentation I did like, I think, 2 years ago, or maybe 3 years ago.

6
00:01:33.070 --> 00:01:42.467
Eyal Balla: bit about me. So I've been developing for more than 15 years and working in python like

7
00:01:43.120 --> 00:01:49.530
Eyal Balla: 5 to 10 years. And currently, I lead the data team in scenario.

8
00:01:50.390 --> 00:01:51.629
Eyal Balla: See? That's me.

9
00:01:52.994 --> 00:02:04.040
Eyal Balla: So you can find me in the links, and if you're interested we're also hiring. So you're welcome to try and join. And we're looking for people that

10
00:02:04.520 --> 00:02:08.080
Eyal Balla: working python, and that is their passion.

11
00:02:08.650 --> 00:02:13.000
Eyal Balla: So today, what I'm gonna do is I'm gonna go through

12
00:02:13.340 --> 00:02:29.884
Eyal Balla: a bit about what Asyncayo is and try to give a real world example from things that we do, and then we'll try and talk about some advanced topics regarding Asyncayo. And so that's what we're gonna do.

13
00:02:31.060 --> 00:02:36.420
Eyal Balla: I think it's important that you guys feel free to step in and ask questions if you need

14
00:02:38.620 --> 00:02:45.520
Eyal Balla: and cause there, there's gonna be a bit code and some topics, and maybe

15
00:02:45.730 --> 00:02:52.010
Eyal Balla: hopefully, it's gonna be all clear. But if somebody has any question, then feel free to jump in.

16
00:02:52.550 --> 00:03:00.030
Eyal Balla: So 1st of all, what what is Asyncaio. So Asyncaio is a style of concurrent programming in python.

17
00:03:00.340 --> 00:03:04.660
Eyal Balla: So why do we need it? So you can think of

18
00:03:04.960 --> 00:03:08.569
Eyal Balla: wanting to do multiple things in python at the same time.

19
00:03:08.770 --> 00:03:09.506
Eyal Balla: So

20
00:03:11.140 --> 00:03:19.540
Eyal Balla: a simple way to do it is using a fork right? So you can run multiple python processes at the same time.

21
00:03:20.010 --> 00:03:43.789
Eyal Balla: So the OS handles the concurrency. And you can actually use multi-cores on your machines. And the problem is that you get duplicated memory because each process has its own memory space right? And in order to communicate between the different python processes you need like OS level communications. So pipes and

22
00:03:43.950 --> 00:03:45.463
Eyal Balla: files, and

23
00:03:47.161 --> 00:03:59.079
Eyal Balla: sorry other ways of multi-process communication. So you'd say, Okay, maybe we can do it some some other way. So there's also multi-threading in python.

24
00:03:59.390 --> 00:04:02.710
Eyal Balla: So this is nice. So you can create new thread. And

25
00:04:03.242 --> 00:04:11.339
Eyal Balla: it looks like you can run multiple things at the same time. But then there's Gil. So Gil is the global interpreter lock.

26
00:04:11.878 --> 00:04:17.962
Eyal Balla: I know there's an agenda in python to try and remove it. But for now it's there

27
00:04:19.910 --> 00:04:25.750
Eyal Balla: And Gil prevents multiple commands of python running in the same process at the same time.

28
00:04:25.860 --> 00:04:34.925
Eyal Balla: So always concurrency for threading is done when you do. things like

29
00:04:35.580 --> 00:04:41.672
Eyal Balla: accessing files or network, or anytime they give access from the your

30
00:04:42.660 --> 00:04:46.390
Eyal Balla: python commands into the OS. This is done.

31
00:04:47.221 --> 00:04:59.660
Eyal Balla: There's something you don't do implicitly. You do it. You can't do it explicitly. You can only do it implicitly by accessing something or doing something that requires OS interaction.

32
00:05:00.720 --> 00:05:12.629
Eyal Balla: And there's Asyncayo. So what is Asyncaio? It's an I/O event manager. Okay? And it, helps you manage states. So you can have multiple states of your system

33
00:05:12.750 --> 00:05:24.389
Eyal Balla: on the same thread. And you can actually explicitly manage the context switching. So you can say, I want to work on multiple items. These are the multiple items. And I want to work on them.

34
00:05:24.920 --> 00:05:33.670
Eyal Balla: So if we look at high level at what the options are for multiprocessing. Say, we have like multiprocesses.

35
00:05:33.780 --> 00:05:47.120
Eyal Balla: so you can have concurrency, and you can use all the cpus. But you know you can't run many processes on the same machine, because each uses a full CPU, so maybe

36
00:05:47.740 --> 00:05:52.530
Eyal Balla: one to 10 cpus and processes.

37
00:05:52.800 --> 00:06:01.410
Eyal Balla: And you can use, generally, the the standard library blocking components and synchronization tools.

38
00:06:02.110 --> 00:06:16.011
Eyal Balla: And then if you need something that's maybe a bit higher on the scalability you can use threads so you can. You have a single process, and Gil is protecting you from

39
00:06:16.910 --> 00:06:22.843
Eyal Balla: doing things between threads which which ha! Which touch memory, and

40
00:06:23.670 --> 00:06:34.039
Eyal Balla: in intrusive way. And but the problem is that you let the OS think your code and you can't really

41
00:06:34.792 --> 00:06:36.720
Eyal Balla: control it manually.

42
00:06:37.070 --> 00:06:51.839
Eyal Balla: And then there's asking where you can actually handle multiple thousands of scalable small components you call them quote coroutines and but pro, and and it's in the application level.

43
00:06:51.940 --> 00:06:58.970
Eyal Balla: So this is what we're gonna look at today. And we're gonna see how it's work, how it works and how you can control it.

44
00:07:00.620 --> 00:07:03.188
Eyal Balla: So like every other

45
00:07:04.440 --> 00:07:09.849
Eyal Balla: program in the world, there's the hello world like in for asking Kaya. Right? So there's

46
00:07:12.010 --> 00:07:15.570
Eyal Balla: Let's see. Can you see my cursor, then you can.

47
00:07:16.310 --> 00:07:23.630
Eyal Balla: So there's a a regular hello world. And there's the one with asking Kyle, wait, okay, but

48
00:07:23.900 --> 00:07:29.589
Eyal Balla: this program is not really helpful, right? Because it doesn't show anything that's important for us.

49
00:07:30.210 --> 00:07:50.489
Eyal Balla: So what what do we want to do with? I think in the real world? So we want to use it for handling multiple heavy I/O processes. So like maybe database accesses or multiple web requests or file sharing or accessing many I/O components at the same time.

50
00:07:51.330 --> 00:08:10.769
Eyal Balla: And you can always use as incaio using multi processes. So you can have. maybe in a cloud application. You can have multiple pods right? And but also you can run it on multiple processes and have have the ability to use multiple cpus if needed.

51
00:08:13.430 --> 00:08:14.330
Eyal Balla: But

52
00:08:14.440 --> 00:08:28.290
Eyal Balla: the downside of Asyncago is that it's almost a different programming language. It looks like python, and it the constructs are very much like Python, and you just use like a few more keywords. But

53
00:08:28.810 --> 00:08:36.129
Eyal Balla: it's very different in concept, because each coroutine the functions that you call with the weight

54
00:08:37.038 --> 00:08:45.999
Eyal Balla: they have to be short enough to allow multiple contacts to run together. So you mustn't use

55
00:08:46.528 --> 00:08:56.480
Eyal Balla: long computations. You can't block the event. Queue. Okay, just like in iui application. You don't want the the main loop to be blocked.

56
00:08:56.890 --> 00:09:10.859
Eyal Balla: And also you can't use general purpose OS blocking commands like, create connections for socket, or select or sleep. So you have things that are, I think, ios specific

57
00:09:13.062 --> 00:09:20.630
Eyal Balla: so you even have like different libraries that you can use in Asyncaio. So

58
00:09:21.888 --> 00:09:33.809
Eyal Balla: if you usually use requests, I suggest you try use Httpx. It has a better behavior fast Api over Django and flask.

59
00:09:34.671 --> 00:09:37.929
Eyal Balla: Mpg, instead of psychopg, etcetera.

60
00:09:38.130 --> 00:09:40.760
Eyal Balla: Okay, so

61
00:09:42.130 --> 00:09:55.740
Eyal Balla: if we look at Asyncaio at the main building blocks, what we have is, we have the the main Asyncaio run command. So what it does it receives in a

62
00:09:57.490 --> 00:10:05.362
Eyal Balla: in a sync way, it received in a sync context, it receives a core routine, something that

63
00:10:05.900 --> 00:10:09.830
Eyal Balla: is run on the asicio loop and creates a loop

64
00:10:09.990 --> 00:10:16.710
Eyal Balla: and runs the core routine in it. And usually this is how you do the entry point into Asyncaya context.

65
00:10:17.300 --> 00:10:20.779
Eyal Balla: Okay? And then you have the core routines. This, these look like,

66
00:10:21.330 --> 00:10:26.570
Eyal Balla: I define Async Def and a function. And this creates a core routine.

67
00:10:26.770 --> 00:10:31.479
Eyal Balla: Okay and core routines. You can run either using domain loop

68
00:10:31.600 --> 00:10:38.720
Eyal Balla: or create a Co a context, a task using the Asyncare create task.

69
00:10:39.560 --> 00:10:40.470
Eyal Balla: Okay?

70
00:10:40.740 --> 00:10:49.319
Eyal Balla: And also when you want to wait for something to happen, and you want to release the context. So you run, await.

71
00:10:49.480 --> 00:10:59.880
Eyal Balla: call, wait in the call routine, and then you wait for the you wait. The context itself waits until the Async context is finished

72
00:11:00.260 --> 00:11:04.519
Eyal Balla: and then returns the control to the main loop that calls this.

73
00:11:04.620 --> 00:11:05.430
Eyal Balla: Okay?

74
00:11:06.350 --> 00:11:07.370
Eyal Balla: So

75
00:11:08.022 --> 00:11:21.649
Eyal Balla: I'm gonna show you guys an example of a small program. And so what this does it. This is a synchronous program. It reads from S. 3, and then queries some database. Right?

76
00:11:22.040 --> 00:11:23.960
Eyal Balla: So we have, like a

77
00:11:24.090 --> 00:11:30.433
Eyal Balla: 2 contexts. One. This is the 1st one. This is second one, and they're not.

78
00:11:31.700 --> 00:11:48.750
Eyal Balla: they're not dependent on each other. You can see the it just gets a file, and then just runs a query. And seeing we want to try and do this together because we want to have the context returned with the content itself. But we don't have some kind of connection between the 2 contexts.

79
00:11:49.460 --> 00:11:56.740
Eyal Balla: So what you can do is you can move to Asyncayo, define this as a coroutine using the

80
00:11:57.150 --> 00:11:58.716
Eyal Balla: aio bottle.

81
00:12:00.194 --> 00:12:10.339
Eyal Balla: Async library and using Asynpg use, create, run the create a quoting from the query of the database.

82
00:12:10.660 --> 00:12:21.090
Eyal Balla: and then you can use gather to run the 2 core routines together. Okay, independently, one of each other, one from each other. So when

83
00:12:21.826 --> 00:12:30.723
Eyal Balla: the execution of the query runs the return of the items, and the body and of the file is done. This is done

84
00:12:31.300 --> 00:12:40.689
Eyal Balla: asynchronously, and while waiting for the I/O, the the context is continued to the other con. Other part.

85
00:12:41.160 --> 00:12:42.000
Eyal Balla: Okay.

86
00:12:43.430 --> 00:12:46.690
Eyal Balla: Questions great.

87
00:12:47.450 --> 00:13:16.690
Eyal Balla: So more more options. Also supports context managers. So this is very convenient because you can create. For instance, in this you can create, you look at the the bottom part here I had to connect and then close using finally. But I can also create a context manager from this and open the connection with the context manager exits close the connection. So I don't have to use

88
00:13:16.710 --> 00:13:19.260
Eyal Balla: explicit exception handling.

89
00:13:19.850 --> 00:13:21.320
Eyal Balla: And also

90
00:13:22.012 --> 00:13:33.339
Eyal Balla: I think I supports iterators so you can. use like generator way of controlling small parts of the code

91
00:13:33.848 --> 00:13:43.049
Eyal Balla: one after the other, and using Async interval. So this is these are patents very known in Python, and you can also use them in Async context.

92
00:13:45.200 --> 00:13:50.409
Eyal Balla: So now I want to show you guys, maybe a problem from our day to day work.

93
00:13:50.870 --> 00:13:56.281
Eyal Balla: I'll present the problem first.st So what we want to do is we want to do some

94
00:13:58.582 --> 00:14:21.089
Eyal Balla: in integration which reads data from an external source and then enriches it. Okay, gets information from maybe a database, and then adds to the context from the external source, and then writes the results into our database as entities. Okay? And I think the the main issue here is that maybe

95
00:14:21.659 --> 00:14:28.550
Eyal Balla: we have multiple customers. Some are small, some are large, and customers have maybe

96
00:14:29.200 --> 00:14:44.130
Eyal Balla: tens of thousands of entities. So there's a lot of reading from the external source, and also maybe a lot of writing and reading into the database. So we have a lot of I/O. And this actually fits very well the Asyncaio concepts.

97
00:14:44.460 --> 00:14:48.700
Eyal Balla: Okay, so what do we want to do?

98
00:14:49.388 --> 00:15:01.639
Eyal Balla: We wanna call something once in a while and go over each of the customers, get the information and then update with the enriched information into our database. Okay? So

99
00:15:01.810 --> 00:15:06.059
Eyal Balla: like an even nave implementation would be something like this.

100
00:15:07.620 --> 00:15:13.880
Eyal Balla: You define all the the the bootstraps

101
00:15:14.549 --> 00:15:37.869
Eyal Balla: needed, and then you get the list of customers. And then for each customer, you do the information, the enrichment. So you get the settings and you run the enricher on the information, and then you in per customer. You get the information from the integration system and enrich it and write it into your database. Right?

102
00:15:38.640 --> 00:15:40.020
Eyal Balla: So this is nice.

103
00:15:40.935 --> 00:15:41.740
Eyal Balla: But

104
00:15:42.558 --> 00:15:54.589
Eyal Balla: the problem with that when we look at this. So this runs per per customer. So that means that until one customer is done the other, the next customer doesn't start.

105
00:15:54.770 --> 00:15:59.140
Eyal Balla: Okay? So if we have small customers and large customers, then

106
00:16:00.190 --> 00:16:06.090
Eyal Balla: we have a problem that small customers are impacted by the size of large customers right?

107
00:16:06.910 --> 00:16:17.090
Eyal Balla: And also, once we have something that's bigger than the the total chrome time, then it doesn't actually

108
00:16:17.991 --> 00:16:30.509
Eyal Balla: it's not actually up to the time it's called time. So system is not up to the functionality according to the time constraints that supposed to run through.

109
00:16:32.395 --> 00:16:36.110
Eyal Balla: So what can we do so. I think the 1st thing we can do

110
00:16:36.310 --> 00:16:48.919
Eyal Balla: is separated per customer. So we can have, some kind of injection of the customer id through a queue and have the system run only per customer. So

111
00:16:49.160 --> 00:16:54.019
Eyal Balla: it reads the information from the queue gets the customer id

112
00:16:54.380 --> 00:17:01.040
Eyal Balla: here, and then runs the same thing just for a specific customer.

113
00:17:01.160 --> 00:17:03.090
Eyal Balla: So how does this help? So

114
00:17:03.310 --> 00:17:10.749
Eyal Balla: what we can do now is we can scale out. So we can have multiple instances of this specific code run

115
00:17:12.778 --> 00:17:19.050
Eyal Balla: together each on a different customer, and assuming that they're not dependent then.

116
00:17:19.699 --> 00:17:27.270
Eyal Balla: Small customers are now not impacted by the size of large customers and the number of the the time that you wanna

117
00:17:27.829 --> 00:17:29.460
Eyal Balla: to run. This is.

118
00:17:30.045 --> 00:17:40.390
Eyal Balla: at most, the time of the biggest customer. Right? So you can scale out as much as you want, and the time that this whole process takes is the time of the biggest customer.

119
00:17:41.270 --> 00:17:42.110
Eyal Balla: Okay?

120
00:17:42.890 --> 00:17:49.890
Eyal Balla: So till now we did not touch anything. That's as Asyncare, right? So we just used like a simple

121
00:17:50.600 --> 00:17:56.219
Eyal Balla: design patterns that allow scaling out of of loops.

122
00:17:57.300 --> 00:18:02.860
Eyal Balla: So now let's try and use Asyncayo to improve the performance of this whole loop.

123
00:18:03.030 --> 00:18:05.249
Eyal Balla: So what do we do?

124
00:18:05.887 --> 00:18:09.710
Eyal Balla: We create a core routine and run it, using Asikaya run.

125
00:18:11.583 --> 00:18:17.220
Eyal Balla: This coroutine is very much similar to what we ran before.

126
00:18:19.340 --> 00:18:25.209
Eyal Balla: Except that now when we look at what happens inside the run for customer.

127
00:18:25.450 --> 00:18:27.550
Eyal Balla: this looks a bit different.

128
00:18:27.810 --> 00:18:31.698
Eyal Balla: So what do we do? First, st we create

129
00:18:33.466 --> 00:18:44.300
Eyal Balla: we run through the pages. Okay? And when we want to enrich the items, we create batches of coroutines, and then we run them together.

130
00:18:44.420 --> 00:18:59.979
Eyal Balla: Okay, so here. The coroutines are created according to the number of the integration items, and when you enrich and read the information each each batch of the

131
00:19:00.460 --> 00:19:04.559
Eyal Balla: coroutines runs together so you can wait for

132
00:19:06.570 --> 00:19:11.189
Eyal Balla: So so they happen together and wait only for the I/O for each of the items.

133
00:19:11.760 --> 00:19:12.580
Eyal Balla: Okay,

134
00:19:16.630 --> 00:19:20.870
Naty Harary: Yeah, I have a question, and just should I interrupt you? Mid sentence?

135
00:19:20.870 --> 00:19:21.420
Eyal Balla: Yeah.

136
00:19:22.394 --> 00:19:29.490
Naty Harary: So, as far as I know, in Async I/O, it is enough to mark the function itself. Async.

137
00:19:29.700 --> 00:19:34.740
Naty Harary: you just wait for it. So I'm not really familiar with the syntax like here.

138
00:19:35.258 --> 00:19:40.680
Naty Harary: So why do we need to ask Sync this as well? I'm not really sure I understand.

139
00:19:42.430 --> 00:19:48.560
Eyal Balla: What we're doing here is we wait for for each of the pages. So this is a nastic iterator, right?

140
00:19:48.940 --> 00:19:53.389
Eyal Balla: But this, this is. This is the core routine which returns an sn key iterator.

141
00:19:53.510 --> 00:19:56.173
Eyal Balla: And when when you

142
00:19:57.270 --> 00:20:06.239
Eyal Balla: what each of these pages contains items, so you want to enrich each of the items. So you create core teams for each of the items to be enriched.

143
00:20:06.390 --> 00:20:16.100
Eyal Balla: And when you run them you run them using gathers because we can when you run a weight on something. Okay, this makes the the

144
00:20:16.570 --> 00:20:24.700
Eyal Balla: higher level function. Wait till it's done. Okay, this is a way to synchronize as in context.

145
00:20:25.220 --> 00:20:29.610
Eyal Balla: Okay, so here you synchronize multiple as in context, using gather.

146
00:20:31.990 --> 00:20:41.489
Naty Harary: I see. So you just gather all the chunks that you have, and you create them with the asset iterator rather than just give a big function and just asking on that right? That's.

147
00:20:41.490 --> 00:21:00.950
Eyal Balla: Because you want to split your context into smaller processing units, each of them may be I/O bound so together the I would run together on each of the in parallel. On each of the items.

148
00:21:01.940 --> 00:21:03.429
Naty Harary: Got it. Thank you.

149
00:21:06.130 --> 00:21:07.540
Eyal Balla: Okay. So

150
00:21:08.060 --> 00:21:27.009
Eyal Balla: now, like I said before, so enrichment haps happens in parallel. And but still you can scale out. So you can have the multiple services. And so the total performance here is, not blocked. And also small customers are not impacted by the large customers.

151
00:21:30.120 --> 00:21:34.040
Eyal Balla: Okay. So some other things you should take into consideration.

152
00:21:34.300 --> 00:21:45.839
Eyal Balla: So I think the 1st thing is exception handling. So when you create as in context, you sometimes need to handle exception in the the top level.

153
00:21:46.000 --> 00:22:04.660
Eyal Balla: So when you do that you can register manual exception handler, so you get the the main loop and set the exception handler, and you can handle the main the errors from that are created from each of the tasks

154
00:22:06.276 --> 00:22:16.647
Eyal Balla: separately, because if you don't do that, then the the Asyncaio context would ha would behave

155
00:22:18.610 --> 00:22:27.379
Eyal Balla: it. It would exit on each of the when each when one of the sub core teams throws an exception into the main context.

156
00:22:27.760 --> 00:22:28.620
Eyal Balla: Okay?

157
00:22:28.810 --> 00:22:34.353
Eyal Balla: So sometimes you want to wait, maybe maybe for the last one, or

158
00:22:35.440 --> 00:22:41.499
Eyal Balla: perhaps some other behavior that is specific for your system. And you can do this this way

159
00:22:42.607 --> 00:22:54.359
Eyal Balla: specifically for gather you can have 2 ways to handle exceptions, so you can do it. Inside each of the core routines like we I did before, or you can

160
00:22:54.610 --> 00:23:16.869
Eyal Balla: ask the gather to collect all the exceptions from each of the core routines, and then you can handle errors together. For instance, if you want to have some retry mechanism, then this is a good way to do it. So you gather all the errors, and then you can retry all those that failed, or decide to do whatever you want to do with those that did not succeed.

161
00:23:19.144 --> 00:23:29.915
Eyal Balla: Regarding testing. So I think, if you look at this core routines what I want to test here is I want to test, maybe.

162
00:23:32.830 --> 00:23:40.820
Eyal Balla: functional response. Okay, something like a happy path and maybe an exception to test the raise for status.

163
00:23:42.300 --> 00:23:50.960
Eyal Balla: So the important part is to mark your test as pi test mark asking Kyle, so this allows you to run test in asking context.

164
00:23:51.770 --> 00:23:57.170
Eyal Balla: There's like Htpx gives Htpx mock. So you can use that.

165
00:23:57.300 --> 00:24:04.819
Eyal Balla: And and then you can inject the response. Here, for instance, and test your happy flow.

166
00:24:05.150 --> 00:24:17.508
Eyal Balla: and also you can always use pytest raises like you did before. And assuming you marked as Asyncio, you can. Test the flow of async and

167
00:24:18.130 --> 00:24:19.460
Eyal Balla: exception flow.

168
00:24:19.720 --> 00:24:20.520
Eyal Balla: Okay?

169
00:24:22.605 --> 00:24:23.380
Eyal Balla: Sorry.

170
00:24:24.240 --> 00:24:31.040
Eyal Balla: What you can also do is there's Async mock like a unit test magic mock

171
00:24:32.065 --> 00:24:40.340
Eyal Balla: you can mock coroutines. So here's an example of how you mark a coroutines and test it. So

172
00:24:40.510 --> 00:24:48.583
Eyal Balla: this is something that's nice to know, and I think it's very valuable when you're testing and mocking

173
00:24:50.250 --> 00:24:51.110
Eyal Balla: coroutines

174
00:24:51.798 --> 00:25:02.409
Eyal Balla: I think that today the default patch returns in a Async context, or a mock on a magic mark or an Async mark, according to the

175
00:25:02.938 --> 00:25:09.211
Eyal Balla: type of function that it gets. So if this is the core routine, then this would return.

176
00:25:10.050 --> 00:25:17.320
Eyal Balla: create this as an Async mark, and if not, it be a magic mark according to what is needed.

177
00:25:18.980 --> 00:25:24.740
Eyal Balla: Something else that's very important for developers is the ability to debug.

178
00:25:25.240 --> 00:25:33.950
Eyal Balla: So I think Kyle gives a debug mode when you run with the environment variable. You get

179
00:25:34.473 --> 00:25:43.669
Eyal Balla: also track, trace track trace backs on asking functions when they're not awaited. So you can find out where where this happens, and when

180
00:25:44.410 --> 00:25:57.470
Eyal Balla: and also this monitors thread safety. So when you, behave, something in your system behaves unsafe regarding the different core routines and the memory they touch.

181
00:25:57.900 --> 00:26:08.020
Eyal Balla: So you get errors in your in your logs. And also this helps debugs debug slow core routines. Because.

182
00:26:08.592 --> 00:26:10.857
Eyal Balla: I think Cayo is very

183
00:26:12.057 --> 00:26:24.449
Eyal Balla: very sensitive to having core routines and long coroutines blocking short coroutines. So this actually helps you understand better the flow of your code once you use Async I/O

184
00:26:26.425 --> 00:26:38.450
Eyal Balla: so this is how a slow log look looks like. So if I do something very slow, you'd get like a log, saying, this is this has taken too long. Okay? So you would know that

185
00:26:38.890 --> 00:26:40.749
Eyal Balla: you want to look at dysfunction.

186
00:26:42.468 --> 00:26:46.551
Eyal Balla: Also something you want you might want to consider is

187
00:26:47.599 --> 00:26:52.540
Eyal Balla: having something that solvers running in your context in your services.

188
00:26:53.396 --> 00:27:01.890
Eyal Balla: So aio debug allows you to log slow callbacks inside your production pods.

189
00:27:02.010 --> 00:27:08.362
Eyal Balla: And this you can enable a specific

190
00:27:09.420 --> 00:27:12.209
Eyal Balla: callbacks when this happens. And this is

191
00:27:12.340 --> 00:27:14.906
Eyal Balla: really great, because this has

192
00:27:16.144 --> 00:27:20.340
Eyal Balla: almost no performance impact on the actual services.

193
00:27:20.490 --> 00:27:26.070
Eyal Balla: And it allows you to understand better how your code behaves in production.

194
00:27:27.820 --> 00:27:28.650
Eyal Balla: Okay?

195
00:27:29.270 --> 00:27:30.080
Eyal Balla: Great

196
00:27:31.981 --> 00:27:46.289
Eyal Balla: also, something you can do is you can monitor each of the the the different tasks. There's asking Kyle, get all tasks and

197
00:27:46.770 --> 00:27:50.107
Eyal Balla: current tasks. So you can run

198
00:27:51.380 --> 00:27:56.220
Eyal Balla: a core routine once in a while to understand what is running and

199
00:27:56.340 --> 00:28:00.020
Eyal Balla: and get the stacks and understand the behavior.

200
00:28:00.690 --> 00:28:01.500
Eyal Balla: Okay.

201
00:28:03.120 --> 00:28:11.940
Eyal Balla: So this is about it. So I went over the Asynch concurrent programming framework.

202
00:28:12.702 --> 00:28:27.219
Eyal Balla: I think we saw a real world example and understood a bit how I think I behaves, and something, and why we want we'd want to use it. And also we looked at some debug testing and exceptional handling tools.

203
00:28:27.810 --> 00:28:28.950
Eyal Balla: and that's it.

204
00:28:31.170 --> 00:28:32.000
Eyal Balla: Questions.

205
00:28:36.240 --> 00:28:36.940
lapid: Can I?

206
00:28:39.040 --> 00:28:40.060
lapid: Do you hear me?

207
00:28:40.820 --> 00:28:41.869
Gabor Szabo: Yes, yes, we can hear you.

208
00:28:41.870 --> 00:28:56.800
lapid: Oh, Hi, yeah, Hi, so you touched a little bit on it. But I'm when I'm doing something that I called it like a project that develops into something a little bit bigger. I find myself sometimes I I just get lost.

209
00:28:57.150 --> 00:29:01.299
lapid: Oh, I I can't verify myself that I actually

210
00:29:02.800 --> 00:29:06.060
lapid: control all the coroutines properly, because many times

211
00:29:06.430 --> 00:29:20.690
lapid: queues that feed one another like I have some streaming, and then some queues and something like that. And so you touched a little bit on that, and how you how you monitor that! But can you expand a little bit like how do you deal with that cause. I I just

212
00:29:21.140 --> 00:29:29.730
lapid: afterwards I go back, and I just print constantly, and I check the timing, and I waste a lot of time on that, and I feel like maybe someone more experienced has a better solution.

213
00:29:31.030 --> 00:29:34.775
Eyal Balla: So I think, whe when you

214
00:29:35.460 --> 00:29:41.375
Eyal Balla: the, I think that the 1st thing is to build your software like in

215
00:29:42.340 --> 00:29:44.319
Eyal Balla: even though it's Async.

216
00:29:44.440 --> 00:29:59.850
Eyal Balla: you need to build it like a top down architecture, understanding which parts are calling what other the other parts, and making sure that when you synchronize correctly, then, once you do that, things are easier. I think.

217
00:30:01.503 --> 00:30:12.799
Eyal Balla: So you need so like other others. Other considerations in software development. You need to have a a solid design

218
00:30:13.250 --> 00:30:17.059
Eyal Balla: as a as a beginning, right? And then you can use

219
00:30:17.707 --> 00:30:21.539
Eyal Balla: something like the test monitor right here.

220
00:30:21.650 --> 00:30:26.649
Eyal Balla: So you can add this as something that you can call within your code.

221
00:30:27.310 --> 00:30:35.309
Eyal Balla: And this actually helps you understand the the different core routines that are run at the same time

222
00:30:35.530 --> 00:30:57.230
Eyal Balla: and can help, you understand, together with the slow core routines, understand the impact of each of the the different coroutines running. And when you, I think that when you say I want to understand. So you have some kind of a problem, right? You have, maybe something that doesn't get the ability to run at all.

223
00:30:57.380 --> 00:31:07.317
Eyal Balla: and you don't know why. So the reason to this is probably something is blocking the the main loop right? It's too long. So you'd get

224
00:31:08.220 --> 00:31:17.930
Eyal Balla: messages on the slow callbacks. And then you would see this in the running tests and understand the context of how it ran.

225
00:31:19.290 --> 00:31:21.089
Eyal Balla: So does this make sense.

226
00:31:21.380 --> 00:31:46.119
lapid: Yeah, some something on that on that area. It it's more so that I when the polish gets big enough, I you know, I've designed patterns for code that I know that I follow. That helps me, you know, every time again, to a code that I didn't touch for you, I know, like, okay, this is how I what I do in order to actually add a new feature. But somehow, when I when I develop with, I think.

227
00:31:46.430 --> 00:32:05.980
lapid: unless it's something the whole development many times like, if I want to change some change, something in the future, I find myself having to go very deep into the cold like, I don't mind this, or maybe I just don't know how to do a design partner. Well, and for my expense just affect the stuff that

228
00:32:06.150 --> 00:32:15.399
lapid: change in their behavior from something that's asynchronousy to asynchronically had forced me to change my code way deeper than I wanted.

229
00:32:15.650 --> 00:32:22.590
lapid: So this is what actually, I'm I'm curious about this is like, this is the pendate I experienced.

230
00:32:23.800 --> 00:32:28.240
lapid: did it? Didn't like next like, Are you? Are you?

231
00:32:28.430 --> 00:32:40.939
lapid: The the something changing in the future. I want to add something, and this thing now is let's say I. I have some. I'm scraping some information, and I'm leaving it, and I want to do it in parallel.

232
00:32:41.100 --> 00:32:44.689
lapid: But and I have an existing project that was not

233
00:32:44.840 --> 00:32:54.990
lapid: so so far didn't assume anything that has to be in parallel cause. Cause I I had a different data source that I used before, and it was way, way, way faster. So now.

234
00:32:54.990 --> 00:32:55.840
lapid: so.

235
00:32:56.690 --> 00:33:02.479
Eyal Balla: So I I think what you would do is you would add, maybe an Asyncare context to

236
00:33:02.620 --> 00:33:06.920
Eyal Balla: part of the code right, and then

237
00:33:07.310 --> 00:33:14.299
Eyal Balla: run it, maybe, with Asynchaire run, and the rest would remain synchronous.

238
00:33:14.780 --> 00:33:20.479
Eyal Balla: So you can limit the the extent of what you're looking to.

239
00:33:21.090 --> 00:33:27.019
Eyal Balla: and also, as always be sure to test the specific part

240
00:33:27.350 --> 00:33:32.620
Eyal Balla: as a as as a different, like a different library, that you're calling

241
00:33:33.050 --> 00:33:35.920
Eyal Balla: and and treat it like one

242
00:33:36.190 --> 00:33:44.869
Eyal Balla: so like a different code component, a different part of the code and put it somewhere. That's self-contained

243
00:33:46.018 --> 00:33:48.710
Eyal Balla: and maybe that can help.

244
00:33:49.990 --> 00:34:00.119
lapid: Yeah. So so what you're describing is how I solved it. But I didn't. I was not. Actually. I was asking myself like if I had to go over the project again.

245
00:34:00.440 --> 00:34:06.849
lapid: saying, Oh, maybe in the future some I will have some asynchronic way, some asynchronic part.

246
00:34:07.720 --> 00:34:13.109
lapid: I want to actually prepare my code for the possibility of something as running in Async in the future.

247
00:34:13.980 --> 00:34:17.570
Eyal Balla: So I can tell you that we had.

248
00:34:18.586 --> 00:34:23.349
Eyal Balla: we needed to move from synchronous code to Async code in our company.

249
00:34:23.860 --> 00:34:25.130
Eyal Balla: And this is a

250
00:34:25.620 --> 00:34:31.530
Eyal Balla: this is, quite a big migration, because, as I, as I described in the beginning of the talk.

251
00:34:31.690 --> 00:34:39.639
Eyal Balla: using Asyncahyo is like something very different than the design of a synchronous program.

252
00:34:40.050 --> 00:34:43.910
Eyal Balla: So I don't think I have like a

253
00:34:44.429 --> 00:34:56.759
Eyal Balla: anything that I can say. Well, if you write a synchronous problem, and you want to prepare, do this and that because I think that you need to look at it in a very different way. Writing Async code and sync code.

254
00:34:57.500 --> 00:35:01.580
lapid: Okay. So it sounds like you went through the same problems I had. So.

255
00:35:02.470 --> 00:35:02.940
Eyal Balla: Yeah.

256
00:35:02.940 --> 00:35:04.480
lapid: At least we suffer together.

257
00:35:06.480 --> 00:35:08.990
Eyal Balla: Suffering. Sharing is always good.

258
00:35:08.990 --> 00:35:11.800
lapid: Yeah, yeah, thank you.

259
00:35:12.560 --> 00:35:13.260
Eyal Balla: You're welcome.

260
00:35:15.480 --> 00:35:16.050
Eyal Balla: Anything else.

261
00:35:16.050 --> 00:35:21.090
Naty Harary: Yeah. Yeah, I have a question. I'm using a lot of 3rd party.

262
00:35:21.766 --> 00:35:39.670
Naty Harary: Libraries. Test Api sequel. Alchemy like that. And they sometimes hide the implementation of I think I/O, and I always wondered, because I just believe it works well. Is there any way to worry the event loop. So I know.

263
00:35:39.910 --> 00:35:43.440
Naty Harary: like, what's running right now.

264
00:35:43.810 --> 00:35:48.510
Naty Harary: Is it even possible? Is that something that python hides from us completely?

265
00:35:48.690 --> 00:35:56.280
Eyal Balla: So so this is like a way to query all the tasks that are running in Asyncayo.

266
00:35:56.680 --> 00:35:57.110
Naty Harary: All right.

267
00:35:58.330 --> 00:36:06.459
Eyal Balla: And also there's a library I did not talk about here, and it's called Aio Monitor. So you can look into that, too.

268
00:36:07.030 --> 00:36:08.999
Eyal Balla: And it's very nice.

269
00:36:09.965 --> 00:36:11.860
Eyal Balla: So you can try that, too.

270
00:36:12.550 --> 00:36:15.994
Naty Harary: Alright cool cause you talked about the timing, so I didn't know if

271
00:36:16.470 --> 00:36:19.789
Naty Harary: if there are the concerns but a or mine, too. That's cool.

272
00:36:19.930 --> 00:36:20.890
Naty Harary: We'll check it.

273
00:36:22.530 --> 00:36:23.380
Naty Harary: Thank you.

274
00:36:27.600 --> 00:36:29.680
Eyal Balla: Okay, so I think we're done.

275
00:36:30.493 --> 00:36:46.420
Eyal Balla: Thank you guys for listening. And you can reach me this email or Linkedin. And also there's a Github project with this presentation and all the code samples together.

276
00:36:47.370 --> 00:36:51.650
Eyal Balla: I can. I think I sent it to Gabor last time, but I can send it again.

277
00:36:51.880 --> 00:36:53.749
Eyal Balla: and he can spread it out.

278
00:36:53.970 --> 00:36:58.322
Gabor Szabo: Yes, that would be a good idea. I think I'm going to include it in in the there is this

279
00:36:58.740 --> 00:37:09.540
Gabor Szabo: web page about the the presentation which will be linked from the video. And and then on that page you'll see also, I include these these links as well.

280
00:37:09.810 --> 00:37:12.380
Gabor Szabo: Oh, so your your Linkedin, and your

281
00:37:12.870 --> 00:37:15.660
Gabor Szabo: and the link to your that Github page.

282
00:37:15.950 --> 00:37:16.730
Gabor Szabo: We'll get to.

283
00:37:16.730 --> 00:37:17.390
Eyal Balla: Okay. Great.

284
00:37:17.390 --> 00:37:18.530
Gabor Szabo: Repository.

285
00:37:18.820 --> 00:37:19.959
lapid: It's a nice, clear.

286
00:37:19.960 --> 00:37:22.739
Gabor Szabo: No more questions. Then. Thank you very much.

287
00:37:23.530 --> 00:37:27.019
Gabor Szabo: Yeah, thank you. Everyone for participating. And.

288
00:37:27.020 --> 00:37:28.569
Eyal Balla: I think there's 1 more question.

289
00:37:28.570 --> 00:37:31.890
lapid: Oh, I if I can ask chitchat questions.

290
00:37:32.120 --> 00:37:32.950
Gabor Szabo: You're good. Go ahead.

291
00:37:32.950 --> 00:37:37.289
lapid: So you said you you have a company like what your company does, and

292
00:37:37.430 --> 00:37:39.700
lapid: can you elaborate a little bit for more.

293
00:37:40.840 --> 00:37:43.977
Eyal Balla: Sure. So scenario, we do.

294
00:37:45.833 --> 00:37:55.216
Eyal Balla: we do security for health for healthcare. So we give hospitals tools to understand security posture and

295
00:37:56.927 --> 00:38:03.010
Eyal Balla: and attack detection. So we detect, malicious content and attacks on hospitals.

296
00:38:04.950 --> 00:38:06.262
Eyal Balla: And I think,

297
00:38:07.670 --> 00:38:16.929
Eyal Balla: because hospitals are very sensitive. So we need to handle like a very high scale, we do with with passive network inspection.

298
00:38:17.150 --> 00:38:19.275
Eyal Balla: And so we handle like,

299
00:38:20.770 --> 00:38:30.910
Eyal Balla: quite a lot of information in our cloud. So we need to use tools and also using asyncaio helps us

300
00:38:31.040 --> 00:38:34.540
Eyal Balla: scale out and handle things as we need.

301
00:38:35.900 --> 00:38:37.260
Eyal Balla: I hope that.

302
00:38:38.536 --> 00:38:39.730
lapid: Get answered.

303
00:38:40.010 --> 00:38:46.181
lapid: Yeah, no, I'm just curious, like, it's very. It's very far from my my expertise. I'm a i'm a data scientist. And

304
00:38:46.960 --> 00:38:54.960
lapid: MI came across a sync when some of my project needed some boost.

305
00:38:55.770 --> 00:39:01.929
lapid: And you're looking also for data scientist. I'm not available now. But in about a month or 2.

306
00:39:03.532 --> 00:39:14.997
Eyal Balla: So I think data scientist is not something that we're currently looking for. But you, you could actually look at the company career page. There are several positions, and

307
00:39:16.130 --> 00:39:19.450
Eyal Balla: we're expanding, and it's it's a good time, I think.

308
00:39:20.570 --> 00:39:22.509
Eyal Balla: Alright. Then brush.

309
00:39:24.170 --> 00:39:24.860
lapid: Alright. Thank you.

310
00:39:26.120 --> 00:39:32.120
Gabor Szabo: So. So thank you. Thank you very much. Thank you, Al, for the presentation, and for all the questions people

311
00:39:32.430 --> 00:39:38.840
Gabor Szabo: and everyone who was watching, please again, like the video, as I told you, and follow the Channel.

312
00:39:38.980 --> 00:39:46.519
Gabor Szabo: And if you would like to present at one of our meetings, then please get in touch with me.

313
00:39:46.790 --> 00:39:53.759
Gabor Szabo: I would be happy to to provide the the place for people to to share their their knowledge.

314
00:39:54.540 --> 00:39:55.679
Gabor Szabo: Thank you very much.

315
00:39:56.000 --> 00:39:56.850
Gabor Szabo: Goodbye.

316
00:39:56.850 --> 00:39:57.250
Eyal Balla: Bye-bye.

317
00:39:57.250 --> 00:39:57.590
Dmitry Morgovsky: Sure.

318
00:39:57.590 --> 00:39:58.919
lapid: Bye-bye. Thank you.

319
00:39:59.980 --> 00:40:01.209
Shalaka Deshan: Thank you, anyway.

