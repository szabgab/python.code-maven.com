---
title: Reducing your memory footprint by 75% with 6 lines with Tomer Brisker
timestamp: 2025-02-26T08:30:01
author: szabgab
published: true
description:
---

{% youtube id="VYSxuicxulE" file="2025-02-25-reducing-your-memory-footprint-by-75-percent-with-6-lines.mp4" %}


While profiling a slow process I stumbled upon a surprising way to reduce our memory consumption. This talk will present some useful profiling tools, and an important thing to know when using AbstractBaseClass extensively.
In this session, we will dive into the realm of Python optimization, as we cover some essential profiling tools designed to identify and resolve performance bottlenecks in your code. We'll navigate through practical examples, showcasing how these tools can provide invaluable insights into your application's memory and CPU usage patterns.
Furthermore, we'll delve into some nuances of AbstractBaseClass usage, and its implications on speed and memory management in Python applications.
Whether you're a seasoned developer or just starting your journey with Python, this session offers some practical strategies to optimize Python programs effectively.


![Tomer Brisker](images/tomer-brisker.jpeg)


## Transcript

1
00:00:02.250 --> 00:00:29.170
Gabor Szabo: Hi, and welcome to the Codeme events, meetings and the Codeme events channel. If you're watching it on Youtube, my name is Gabor Sabo. I usually teach python and rust and help companies with these 2 languages mostly. And I also organize these events because I really like the idea of sharing knowledge, I mean receiving knowledge from other people like this time, Toma.

2
00:00:29.330 --> 00:00:49.120
Gabor Szabo: and from around the world. So that's a good good idea, I think. And that's it. If you're watching the Youtube, then then please, like the video and those who follow the channel and thanks everyone who arrived to this meeting, and especially Tomer, for giving us the presentation. Now it's your turn.

3
00:00:49.510 --> 00:00:52.949
Gabor Szabo: So welcome to introduce yourself. And yeah.

4
00:00:53.120 --> 00:00:56.100
Tomer Brisker: Thank you. Let me share my screen.

5
00:00:58.800 --> 00:01:00.990
Tomer Brisker: Okay, can you see it?

6
00:01:01.920 --> 00:01:02.670
Gabor Szabo: Yes.

7
00:01:03.060 --> 00:01:03.920
Tomer Brisker: Excellent.

8
00:01:05.334 --> 00:01:09.469
Tomer Brisker: Okay, so 1st of all, I have to make a confession.

9
00:01:09.770 --> 00:01:14.040
Tomer Brisker: It wasn't 6 lines of code. It was actually 7 lines of code.

10
00:01:14.460 --> 00:01:28.110
Tomer Brisker: And I guess you're all pretty wondering, curious what these lines of code were. So here they are. Okay. Okay. It was 8 lines of code. If you count the space in between the functions.

11
00:01:28.660 --> 00:01:39.080
Tomer Brisker: and we'll dive into what exactly these lines of code mean a bit later, and why these allowed us to save so much memory.

12
00:01:39.220 --> 00:01:41.780
Tomer Brisker: But 1st of all, just so, you believe me.

13
00:01:41.930 --> 00:01:47.609
Tomer Brisker: this is for a memory usage graph in production. When we deployed this fix.

14
00:01:47.770 --> 00:02:01.359
Tomer Brisker: As you can see, the deployment was around 5 10 Pm. Which is a great time to deploy fixes. If I remember correctly, this was the Thursday, which is the end of the week for Israel, perfect time for deploying to production.

15
00:02:01.870 --> 00:02:13.220
Tomer Brisker: But 1st of all, do we have anyone in the call who happens to be a Us. Citizen or has to file us. Tax supports.

16
00:02:18.200 --> 00:02:21.170
Tomer Brisker: feel free to wave, or something.

17
00:02:21.860 --> 00:02:24.939
Tomer Brisker: If there are, I guess I guess not.

18
00:02:25.090 --> 00:02:31.839
Tomer Brisker: Well, if you were, I guess this would probably look pretty familiar to you.

19
00:02:31.950 --> 00:02:43.169
Tomer Brisker: So for those of you who don't know practically all us citizens are required to file tax supports annually for the Irs

20
00:02:43.440 --> 00:02:47.260
Tomer Brisker: for the income taxes. This is a

21
00:02:47.360 --> 00:02:52.590
Tomer Brisker: pretty painful process. It requires filling out a lot of obscure forms.

22
00:02:53.093 --> 00:03:17.609
Tomer Brisker: And if you make some mistakes on it, you can find yourself in jail. So most people either pay one of the existing companies who provide services for filing tech supports or pay an accountant to do the tax reports for them. So Hi! My name is Tomer. I'm the tech lead at. We are fixing the issue of Irs tech support filing.

23
00:03:18.833 --> 00:03:27.250
Tomer Brisker: We are developing a simple to use application that allows users to file their taxes seamlessly with the irs.

24
00:03:27.793 --> 00:03:48.870
Tomer Brisker: Usually takes most users around half an hour to do their taxes. Which is pretty awesome compared to what it normally takes, which is many hours and oh, and we don't charge them nearly as much as an accountant or one of the existing providers charge for this.

25
00:03:49.694 --> 00:04:01.029
Tomer Brisker: If I look a bit tired in the recording. I'm going to let you guess which one of these are to blame today. Him she's on the left.

26
00:04:01.935 --> 00:04:04.964
Tomer Brisker: She's 6 months old.

27
00:04:05.810 --> 00:04:11.380
Tomer Brisker: I live with my partner and 2 kids and give a time, which is a suburb of Tel Aviv

28
00:04:12.070 --> 00:04:18.920
Tomer Brisker: and our dog but I I guess you're not here to hear about me and my life.

29
00:04:19.149 --> 00:04:22.340
Tomer Brisker: You're here to hear about performance in Python.

30
00:04:23.170 --> 00:04:25.279
Tomer Brisker: So let's dive in.

31
00:04:25.420 --> 00:04:30.670
Tomer Brisker: Our story begins when we noticed there's some

32
00:04:30.830 --> 00:04:35.610
Tomer Brisker: certain action in our system that's taking quite a long time to complete

33
00:04:36.321 --> 00:04:41.589
Tomer Brisker: in fact, we even got some reports from users, complaining that they were hitting timeouts

34
00:04:41.740 --> 00:04:45.890
Tomer Brisker: when they were running this specific action within the system.

35
00:04:46.710 --> 00:05:01.249
Tomer Brisker: and I was assigned to this task, started digging in, and I managed to produce it locally. I created a nice little script that created the exact conditions of the users that were timing out

36
00:05:01.800 --> 00:05:09.590
Tomer Brisker: and the 1st step was to see how long it actually takes. And yeah, it was actually pretty slow.

37
00:05:09.690 --> 00:05:20.060
Tomer Brisker: Python comes with a couple of built in modules in the Standard Library that are pretty nice when you're timing things those time and those time it

38
00:05:20.599 --> 00:05:25.270
Tomer Brisker: I will leave feeding the exact documentations of them to the listener.

39
00:05:26.530 --> 00:05:27.429
Tomer Brisker: But

40
00:05:28.480 --> 00:05:54.030
Tomer Brisker: we actually have. It's it's very useful. If you know what you're looking for. For example, if there's a specific method that you know, is slow, and you want to measure some change that you make to it, and you want to see the impact of it. This is very useful. We even have a little wrapper method that allows us to easily measure the timings for various functions that we call

41
00:05:54.405 --> 00:06:02.299
Tomer Brisker: but what do we do if we're not sure where the slowness is coming from this specific action in the system.

42
00:06:02.470 --> 00:06:16.779
Tomer Brisker: This was a pretty complex section. It involved calling several different services, a lot of methods, so it's pretty difficult if you don't know what where the slowness is coming from.

43
00:06:18.680 --> 00:06:23.669
Tomer Brisker: So this is what profilers were invented for

44
00:06:24.368 --> 00:06:31.150
Tomer Brisker: profiler. There's a TV series called the Profiler. We're not going to talk about it. I have no idea what it's about.

45
00:06:31.430 --> 00:06:35.990
Tomer Brisker: but profilers generally come into different varieties.

46
00:06:36.560 --> 00:07:03.049
Tomer Brisker: They are. There are that we will mention that as we go, the 1st variety is deterministic profilers. These are profilers, that essentially every time you make a method call. They register that method call. They write down the start time, and once that method returns they write down the end time. Python, like standard library has a nice one called C profile.

47
00:07:03.330 --> 00:07:24.280
Tomer Brisker: It gives you a context manager. Basically, you wrap the code that you want to measure with the context manager. Then call whatever slow function you want to profile and save the statistics to a file. And see profile will actually take care of going over all of the method calls within that function.

48
00:07:24.410 --> 00:07:30.459
Tomer Brisker: measuring how long they take, how much, how many times each method is called, etc.

49
00:07:30.560 --> 00:07:41.699
Tomer Brisker: And it saves all of these statistics into a file which can be used can be read using a module called pstats.

50
00:07:41.810 --> 00:08:05.169
Tomer Brisker: Pstats allows you reading these files. And just so, there's a lot of information here. You can see we'll dive into it a little bit to understand what this table is about. So 1st of all, on the right, we can see the file, name, line number and function name, pretty basic. So you know what we're calling here

51
00:08:05.260 --> 00:08:18.769
Tomer Brisker: on the left hand side, we can see the number of calls to each function, as you can see. The 1st 3 here were called just once. This is actually the script that I was using to de- debug this issue.

52
00:08:19.561 --> 00:08:29.669
Tomer Brisker: The second column. Here is total time, which is the time that was spent within this specific method in total all of the times that it was called.

53
00:08:29.840 --> 00:08:39.579
Tomer Brisker: and those cumulative time which is basically the time that was spent within this method and any other method that was called from within that method.

54
00:08:40.289 --> 00:08:40.799
Tomer Brisker: and

55
00:08:41.130 --> 00:08:53.159
Tomer Brisker: something stood out pretty quickly to me out of 12 seconds. Runtime, in total. About 6 seconds or half the runtime was spent in one specific method.

56
00:08:53.955 --> 00:08:59.914
Tomer Brisker: And this method is ABC surplus check. Interesting. Okay?

57
00:09:00.620 --> 00:09:13.350
Tomer Brisker: let's see. And even more interesting is the number of times. This was called so in 12 seconds. We actually called this method 175,000 times.

58
00:09:13.410 --> 00:09:40.590
Tomer Brisker: That's the number on the right. And if those a slash, and another number here, that means that this method was calling another, it was calling itself recursively. So in this case we were calling ABC. Subtract check a bit over 3 million times. So about 20 times for every single call that we were making to subclass check, it was actually making about 20 different calls on average.

59
00:09:41.633 --> 00:09:53.739
Tomer Brisker: Okay, pretty interesting. But still, I'm not quite sure why we're calling this method so many times, or why is it taking so long when this method is being called.

60
00:09:53.920 --> 00:10:04.660
Tomer Brisker: And that's what the second type of profilers is really useful for identifying the second type of profilers is statistical profilers.

61
00:10:04.720 --> 00:10:21.380
Tomer Brisker: These are profilers that basically take a snapshot of your python call stack, or in any other language, the call stack. Every certain interval. Usually this is done. Every few milliseconds, the shorter the interval.

62
00:10:21.380 --> 00:10:37.109
Tomer Brisker: obviously the higher the impact it has on performance. On the other hand, if you set too long of an interval you might miss very quick method calls return within the interval, and they won't actually be registered when running the profile.

63
00:10:37.190 --> 00:10:44.800
Tomer Brisker: and a very common way of looking at statistical profiles is using a tool called flame charts.

64
00:10:45.400 --> 00:11:06.120
Tomer Brisker: The way that flame charts work. Basically, you have 2 axes here. The x-axis is the time. So the bigger the block is on the X-axis. That means the longer time that was spent within that specific block, and the Y-axis is the stack.

65
00:11:06.420 --> 00:11:26.929
Tomer Brisker: So you can see the actual call stack of every single method. And you can see why it was being called. Well, the call was coming from. See the bigger ones, the smaller ones. And then that's very helpful. When you need to debug and identify why, a certain method is being called a lot of times.

66
00:11:27.900 --> 00:11:31.660
Tomer Brisker: So I used one of these statistical profilers

67
00:11:31.990 --> 00:11:54.509
Tomer Brisker: specifically, one called pyspy. There's multiple different profilers available for python, and each language has its own ecosystem of profilers. I'm just showing the ones that I used in this case, but there are various other tools that are useful, and they're all good in their own fields.

68
00:11:55.047 --> 00:12:02.359
Tomer Brisker: So I run a statistical profile of pispy on this web producer that I created.

69
00:12:02.490 --> 00:12:10.869
Tomer Brisker: And hmm, yeah, okay, this is fine. This is fine. I can deal with that.

70
00:12:11.030 --> 00:12:20.069
Tomer Brisker: as you can see, a flame chart when you have a very complex operation, can be very, very, very difficult to read.

71
00:12:20.650 --> 00:12:27.250
Tomer Brisker: Sometimes there's something that stands out, you see, a very big block that's taking a very long time to call.

72
00:12:27.380 --> 00:12:52.389
Tomer Brisker: and you can identify the bottleneck pretty quickly from looking at this. But other cases everything is on fire, and you don't really know what's going on. Specifically, in this case we were seeing a certain method call being called 3 million times, which makes sense that it would be very difficult to identify all of these different calls within the flame chart.

73
00:12:52.640 --> 00:12:57.119
Tomer Brisker: and for that there was a nice tool called Sandwich.

74
00:12:57.330 --> 00:13:02.459
Tomer Brisker: Not that kind of sandwich. There's a tool called speed scope, and it has a

75
00:13:02.670 --> 00:13:05.350
Tomer Brisker: way of showing flame charges.

76
00:13:05.460 --> 00:13:18.199
Tomer Brisker: playing charts in a different way, which is, they call it sandwich. Basically on the left hand side, we can see all of the different method calls within our application within the run that was profiled.

77
00:13:18.560 --> 00:13:27.659
Tomer Brisker: And we can solve this list by the total time and by the self time. This is the same, by the way, as we saw previously total time, and

78
00:13:27.790 --> 00:13:33.126
Tomer Brisker: the cumulative time with in the c profile

79
00:13:33.860 --> 00:13:36.710
Tomer Brisker: And then once you click on one of these

80
00:13:37.000 --> 00:13:42.490
Tomer Brisker: you can see on the right hand side those 2 parts, those the callers and the callees.

81
00:13:42.500 --> 00:14:09.719
Tomer Brisker: The top half shows you where this method was being called from. So, for example, in this case we can see subtest check was mostly called from instance check, and some other internal methods. Also. Here we can see. Instance, check was being called from various other methods. And here the X-axis actually shows the time. That's cumulative by the specific

82
00:14:09.810 --> 00:14:29.109
Tomer Brisker: method. So this isn't a single call. This is the total of the times that it was called from here, and obviously I can show the internals of our system. But you can see that there were several places that we were calling. Instance check, pretty commonly leading to most of

83
00:14:29.170 --> 00:14:41.379
Tomer Brisker: the load. On this method, and on the left, you can see again. This was about 8 seconds in this test run. So quite a long time

84
00:14:41.480 --> 00:14:44.690
Tomer Brisker: from the overall. Time.

85
00:14:45.310 --> 00:14:50.109
Tomer Brisker: Okay, so instance, check subclass check.

86
00:14:50.290 --> 00:15:05.529
Tomer Brisker: This is like built in python stuff, right? And it's not something in our code base. What what should I do about it? It's pretty odd, I don't know. Let's, I guess, ask Dr. Google.

87
00:15:06.302 --> 00:15:16.930
Tomer Brisker: and turns out there's an open issue about ABC subclass check, which has a very poor performance. And I think a memory leak. Hmm!

88
00:15:17.610 --> 00:15:18.680
Tomer Brisker: More league.

89
00:15:19.030 --> 00:15:20.260
Tomer Brisker: Interesting.

90
00:15:21.537 --> 00:15:25.922
Tomer Brisker: Memories. Memory is pretty expensive.

91
00:15:26.940 --> 00:15:35.520
Tomer Brisker: and turns out I'm pretty bad at counting. So there's not actually 2 kinds of profilers, those 3 kinds of profilers.

92
00:15:35.710 --> 00:15:41.029
Tomer Brisker: There's also memory profilers besides the runtime profilers.

93
00:15:41.170 --> 00:16:10.060
Tomer Brisker: memory. Obviously it's expensive. If you need to use and allocate a lot of it, but it's also expensive in terms of performance, because if the python runtime runs out of memory, it has to make system calls to allocate additional memory to the python program. The garbage collector also has to go over all of the memory and clean up unused memory. So the more memory. You allocate the slow, the garbage collection will be

94
00:16:10.120 --> 00:16:38.349
Tomer Brisker: so. These tools, the memory profilers, allow us to identify issues with our memory allocations. Sometimes our program can be very fast. But allocates a very large amount of memory. Just recently we had a case, actually, where a certain process was crashing, and we were seeing pods being killed. So out of memory killed

95
00:16:38.380 --> 00:16:45.739
Tomer Brisker: basically in Kubernetes, when you allocate a certain amount of memory to a process.

96
00:16:45.930 --> 00:17:15.490
Tomer Brisker: if you over, if the process runs over the memory. The Kubernetes controller will kill it. So it doesn't starve out other processes. And in this specific case memory was running out so quickly that it wasn't even sending telemetry data to Prometheus. And we used actually a memory profiler to identify where exactly this memory was being allocated so rapidly that it was killing our pods.

97
00:17:16.339 --> 00:17:34.970
Tomer Brisker: So let's talk about memory profile as a bit. There's a really nice one for Python called memory. It gives you some nice runtime statistics on your program. In this case this is a reproducer script that I was using.

98
00:17:34.970 --> 00:17:51.320
Tomer Brisker: We can see that we actually had about 11 million object allocations during the script. You can notice that the runtime here is a bit longer than the 12 seconds that it took when running with just c profile. And that's because

99
00:17:51.330 --> 00:17:57.990
Tomer Brisker: every single memory allocation that the program does. There's some overhead to it when you're profiling it.

100
00:17:58.010 --> 00:18:04.920
Tomer Brisker: So the Runtime was a bit slower here, and we were allocating nearly 2 GB of memory.

101
00:18:07.340 --> 00:18:10.049
Tomer Brisker: When running this this process.

102
00:18:10.410 --> 00:18:23.900
Tomer Brisker: and it also gives you information like which python memory allocator was being used. Number of frames. That's the number of samples that it was taking. This is also statistical profilers.

103
00:18:25.123 --> 00:18:33.740
Tomer Brisker: And it also shows us a nice flame chart like we saw before. But, unlike the runtime profilers.

104
00:18:33.760 --> 00:18:59.500
Tomer Brisker: this flame chart, the X-axis, is actually the size of the memory allocated, so the wider the block is, that means that the memory allocated within this block was higher. And also we can see specific statistics for a certain method call. For example, in this case we were allocating 82 MB of memory and 2 and a half

105
00:18:59.520 --> 00:19:05.030
Tomer Brisker: a thousand objects were being allocated in a single call to subtrust check.

106
00:19:09.150 --> 00:19:11.982
Tomer Brisker: Okay, so let's go back to the bug.

107
00:19:13.050 --> 00:19:20.099
Tomer Brisker: ABC, subtest check has very poor performance. I think. Memory leak. It's open since May 2022.

108
00:19:20.350 --> 00:19:24.630
Tomer Brisker: Anybody in the audience maybe knows who Samuel Colvin is

109
00:19:26.440 --> 00:19:32.050
Tomer Brisker: feel free to unmute. If you do anyone.

110
00:19:32.150 --> 00:19:48.209
Tomer Brisker: Samuel Corvin, that's the guy behind pydantic Pydantic is a very popular data validation Library for python. He opened this issue almost 3 years ago, and it's still open. So

111
00:19:48.856 --> 00:19:53.720
Tomer Brisker: well, I guess case closed. Python is a slow language.

112
00:19:53.940 --> 00:20:09.769
Tomer Brisker: There's nothing to do about it. We have to rewrite our application completely, using go rust elixir. I don't know what are the cool kids using today, Gabbo, I know you do rust a lot. So I guess rewrite right?

113
00:20:10.990 --> 00:20:16.260
Tomer Brisker: No, I could just decide. This is a case of

114
00:20:16.470 --> 00:20:26.119
Tomer Brisker: language limitations. We have to cope with it, and that's it. But they decided to dig in a little bit deeper and try to figure out if there's something we can do to resolve the issue

115
00:20:26.310 --> 00:20:35.859
Tomer Brisker: and to dig in a little bit deeper. We need to discuss ABC a bit, not the TV network abstract based classes

116
00:20:36.280 --> 00:20:41.090
Tomer Brisker: for those of you who are not familiar with abstract based classes.

117
00:20:41.677 --> 00:20:47.099
Tomer Brisker: Which, as we mentioned, have a fairly poor performance for the subclass check.

118
00:20:47.806 --> 00:20:54.949
Tomer Brisker: Abstract-based classes, is a mechanism in Python that allows us to define an abstract class

119
00:20:55.260 --> 00:21:14.820
Tomer Brisker: which allows us to define certain methods. We require any class that is subclassing from that class to do. We require these methods. So if we try to subclass it, and we don't implement these specific methods, the methods. The interpreter will yell at us saying, Hey.

120
00:21:14.930 --> 00:21:19.040
Tomer Brisker: this class has to implement a certain method.

121
00:21:19.701 --> 00:21:34.009
Tomer Brisker: Usually we use subclass ABC's as makes sense, basically defining a specific interface. We want to implement. But they have an interesting idea that is registering virtual subclasses.

122
00:21:34.662 --> 00:21:38.999
Tomer Brisker: Which is, for example, let's say you have a

123
00:21:39.180 --> 00:21:50.129
Tomer Brisker: base class that you've defined, and you want one of the built-in types of python to be a subclass of that. Obviously, you can't

124
00:21:50.380 --> 00:21:54.520
Tomer Brisker: have int subclassing something else right?

125
00:21:55.065 --> 00:22:09.930
Tomer Brisker: And the ABC. Class, or ABC Meta subclass ABC Meta class. Sorry ABC. Meta Meta class allows us to register various other classes as virtual subclasses of the base class.

126
00:22:09.950 --> 00:22:33.360
Tomer Brisker: This is also useful. If you have a class that implements multiple interfaces, let's say you have a class that implements iterable and implements hashable and implements. I don't know sortable, say, and a few others. Obviously, you don't want to have to declare all of these. When you create a class.

127
00:22:33.860 --> 00:22:50.000
Tomer Brisker: you can just register this class as a virtual subclass. And that means that if you look at the method, resolution, or the Mlo. Of a specific object of that class, you won't see these classes as their parent.

128
00:22:50.150 --> 00:23:15.209
Tomer Brisker: That's by the way, the way usually subclass check works. It checks the method, resolution order, and to see if the parent class is there? But since we have to, we allow registering subclasses virtually to classes that aren't the actual parents, there's a specific implementation within ABC. Matter for subclass check and

129
00:23:15.270 --> 00:23:21.079
Tomer Brisker: instance check that allows support for this specific use case.

130
00:23:21.390 --> 00:23:46.080
Tomer Brisker: So just to better understand this use case, let's say we have this class here we have a base class which is an abstract base class. We have class A class B inheriting from that base class, and we have a virtual subclass which isn't inheriting from the base class, but it's registered as a subclass of this base class, and so forth. We have a virtual subclass, a etc, etc.

131
00:23:46.867 --> 00:23:54.869
Tomer Brisker: Let's say we have an object, and we want to check if that object is a subclass or an instance of base class.

132
00:23:55.358 --> 00:24:02.720
Tomer Brisker: In this case we would. Let's say, this object is of type, virtual, subclass, A, we would need to check

133
00:24:02.910 --> 00:24:04.010
Tomer Brisker: the whole

134
00:24:04.160 --> 00:24:25.339
Tomer Brisker: inheritance tree for base class to identify if this class was registered to any of the classes within that inheritance tree. So this calculation is pretty complex. There's also potentially an issue with a bad implementation of

135
00:24:25.420 --> 00:24:53.739
Tomer Brisker: caching within the implementation of abstract base class. But normally this isn't a big issue, because you wouldn't have that many classes inheriting from a single base class, maybe 2, 3, 1020. Usually it's not noticeable. But, as I mentioned, we're dealing with tax reports and tax filing for the Us. Irs.

136
00:24:53.890 --> 00:25:23.869
Tomer Brisker: There's thousands of different forms that the user needs to fill in. Think of the number of states. Each State has its own forms. Each form is composed of multiple different parts, and you can pretty quickly guess the rough number of classes that we have in our system to enable this fairly complex calculation, which has led us to this issue because of the

137
00:25:23.930 --> 00:25:32.029
Tomer Brisker: very large inheritance that we have from our base class that we use for the calculation.

138
00:25:32.380 --> 00:25:49.000
Tomer Brisker: And that's why going back to the solution. This solution worked. Let's look at it a bit more in depth. Obviously, we're using type definitions. We are not barbarians. Previously I was dropping them just to make it easier to look.

139
00:25:49.550 --> 00:26:11.719
Tomer Brisker: But this is very, very straightforward. Those is subclass. And is this instance, and what they do is they go to type. Type is the base class for all classes in case you're not familiar with it, and they call subclass check or instance check on type directly by default. When you call is instance, or is subclass.

140
00:26:11.990 --> 00:26:39.610
Tomer Brisker: The way it works is, it goes to the class that is on the right hand side of the of the second parameter, basically of the function call, and it checks the Meta class for that class looking for subclass check or instance check depending on which method you called, and then it goes up the method resolution order until it finds the implementation. In case of

141
00:26:39.700 --> 00:27:02.590
Tomer Brisker: an abstract base class, it would go to abstract based class ABC subclass check. But here, what we do is we basically bypass the ABC methods and go directly to the source type subclass check, which is the default implementation used by python for any types that aren't abstract based classes.

142
00:27:03.150 --> 00:27:15.699
Tomer Brisker: And then all we had to do in our code base. It's a very simple change. Use is subclass form, first, st subclass instead of using the default, python implementation.

143
00:27:15.800 --> 00:27:35.569
Tomer Brisker: checking. If it's a subclass of the base model. And the reason this worked is because we didn't really care about the virtual subclass aspect of ABC. In our case we were just checking. If a certain object is or isn't, a subclass of our base model.

144
00:27:35.670 --> 00:27:44.720
Tomer Brisker: This wouldn't work, obviously, if we were actually registering our objects into the base model instead of directly inheriting from it.

145
00:27:44.850 --> 00:27:47.290
Tomer Brisker: But in our case this was good enough.

146
00:27:47.520 --> 00:27:57.079
Tomer Brisker: and, as you can see, there's another very nice added benefit to profiling. It lets you add nice statistics to your pull requests.

147
00:27:57.812 --> 00:28:08.119
Tomer Brisker: For example, Runtime went down from 33 seconds to 26 seconds. Memory usage went was improved by 50%, etc, etc.

148
00:28:08.120 --> 00:28:31.359
Tomer Brisker: Actually, I didn't even have to implement this in all of the places. I only had to switch to using the 1st subclass in very specific places I identified, using profiling as being the most common places that this was being called from, and this already gave me a very significant improvement.

149
00:28:31.360 --> 00:28:56.700
Tomer Brisker: And when we actually deployed, this fix turns out that the impact was even higher than the specific use case that I was profiling because this had impact across the system, it could significantly, as you can see here, reduced our memory load. It also improved the system runtime in general, and also the system load. Time was drastically reduced.

150
00:28:56.960 --> 00:29:08.460
Tomer Brisker: making our deployments much faster and saving a lot of costs, questions anybody.

151
00:29:11.030 --> 00:29:16.439
Gabor Szabo: And 1st of all, thanks, thanks for the presentation. Can you go back? 1, 1 slide.

152
00:29:16.880 --> 00:29:17.540
Tomer Brisker: Yes.

153
00:29:17.680 --> 00:29:20.002
Gabor Szabo: What is this? Bump? The hunter.

154
00:29:20.848 --> 00:29:37.821
Tomer Brisker: That's a good question. Actually, that's we're using warning updates. So basically, we spun up a few pods, switched over to them, then spun up a few more pods and it these are

155
00:29:39.060 --> 00:29:56.730
Tomer Brisker: These are. This is the time when there were still some of the older pods running in parallel with the new pods that were using less memory. So this is the 1st drop is when we killed the 1st batch of the old pods, and the second drop is when we killed the second batch.

156
00:29:57.290 --> 00:29:57.870
Gabor Szabo: Hmm!

157
00:30:00.030 --> 00:30:05.289
Gabor Szabo: But why did this? I still don't understand why it went up, but it go up again.

158
00:30:05.554 --> 00:30:10.840
Tomer Brisker: So we started a few pods, killed a few, and then started a bunch more and then killed the rest.

159
00:30:11.010 --> 00:30:11.490
Tomer Brisker: Oh.

160
00:30:11.490 --> 00:30:12.060
Gabor Szabo: Okay.

161
00:30:12.280 --> 00:30:18.859
Tomer Brisker: Oh, man, this is just a loading of the the new ports! While the all the ones were still running.

162
00:30:19.650 --> 00:30:20.610
Gabor Szabo: Okay. Nice.

163
00:30:24.700 --> 00:30:26.580
Tomer Brisker: Any other questions. Anybody?

164
00:30:29.900 --> 00:30:31.789
Tomer Brisker: Okay, thank you very much.

165
00:30:32.380 --> 00:30:39.630
Gabor Szabo: No, it seems so. Thank you. Thank you for giving this presentation and everyone for being here listening.

166
00:30:40.250 --> 00:30:41.120
Gabor Szabo: And

167
00:30:42.190 --> 00:30:49.600
Gabor Szabo: I'm going to stop the video. But please remember to like the video and follow the channel and see you next time, Toya.

168
00:30:50.180 --> 00:30:52.370
Tomer Brisker: Bye, bye, thanks for having me Nobel.

169
00:30:52.370 --> 00:30:53.150
Gabor Szabo: Bye-bye.

