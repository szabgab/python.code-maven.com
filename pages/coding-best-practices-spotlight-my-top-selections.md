---
title: Coding Best Practices Spotlight - My Top Selections
timestamp: 2026-10-25T22:30:01
author:
published: true
description:
tags:
---


## Description

Coding best practices is a phrase we hear often, but how often do we actually take time to stop and examine the patterns we use every day?
In this short talk, I’ll share a few selected practices and anti-patterns that I came across over the last year. We’ll cover these practices through live coding examples and design tradeoffs, focusing on where things can go wrong, even when they seem right.

## Bio

[Nadav Mary](https://www.linkedin.com/in/nadav-mary/) is a Principal Software Engineer at Palo Alto Networks, where he's been working on diverse challenges across backend, frontend, and infrastructure for the past 10 years.

He's led development efforts across multiple teams, driving improvements in architecture, developer experience, and team collaboration.
Nadav is passionate about clean code, mentoring engineers, and helping others grow into better versions of themselves.
He cares deeply about doing things right and helping others level up.

## Length

30 min

{% youtube id="T_hJzFxVg4Y" file="2026-10-25-coding-best-practices-spotlight-my-top-selections-by-nadav-mary.mp4" %}


## Transcript

1
00:00:01.980 --> 00:00:14.580
Gabor Szabo: So, hello, and welcome to this session. This… if you're watching on YouTube, then it's the Code Maven channel. My name is Gabor Szabo, I organize these events. This time, it's Nadav Marin, who is going to

2
00:00:14.800 --> 00:00:19.140
Gabor Szabo: talk about, some stuff in Python.

3
00:00:19.260 --> 00:00:25.419
Gabor Szabo: He will introduce himself, and they'll introduce his presentation.

4
00:00:25.530 --> 00:00:38.669
Gabor Szabo: If you are here at the event, thank you very much for joining us. Feel free to ask questions. That's the big privilege of being present at the event. And if you're watching on YouTube, then below the video you will find

5
00:00:38.670 --> 00:00:53.409
Gabor Szabo: the like button, and you can follow the channel, and you can also find a link to the future events, and also notes about this event, and links to things about Nadav, so that would be a good idea to follow them there.

6
00:00:53.500 --> 00:01:04.710
Gabor Szabo: With this, let me give the stage to you, Nadav. Thank you very much for agreeing to give this presentation, and really, the stage is yours.

7
00:01:05.830 --> 00:01:10.459
Nadav Mary: Thank you, so let me share my screen. Just let me know that you can see that.

8
00:01:10.460 --> 00:01:11.739
Gabor Szabo: Yes, we can see.

9
00:01:12.110 --> 00:01:12.940
Nadav Mary: Facts?

10
00:01:13.330 --> 00:01:21.380
Nadav Mary: All right, so, hi everyone, and thanks for joining my session. Let me start with a quick question.

11
00:01:22.310 --> 00:01:29.050
Nadav Mary: So actually, now that AI can write the code for us, do we really need to care about

12
00:01:29.280 --> 00:01:36.670
Nadav Mary: coding best practices, Keep the question in mind, and we'll go through that question in this session.

13
00:01:38.560 --> 00:01:52.090
Nadav Mary: Yeah, so for those who don't know me, I'm Nadav Mahri, I'm Principal Software Engineer at Palo Alto Networks. I've been with the company for the last 10 years, going back to my CyberAc days before the acquisition.

14
00:01:52.690 --> 00:02:09.999
Nadav Mary: I love solving design problems, but what I love even more is helping other developers grow. Watching someone from going from, I'll just make it work, to understand why this is the right solution, this is my, really, passion.

15
00:02:10.190 --> 00:02:18.049
Nadav Mary: I'm also known as the clean code guy, or as my teammates put it, the one who actually reads the pull request.

16
00:02:18.250 --> 00:02:29.500
Nadav Mary: And now, seriously, over the last 10 years, I've worked across different teams, different languages, backend and front-end, and reviewed a lot of code.

17
00:02:29.970 --> 00:02:40.949
Nadav Mary: And I've seen the same problem over and over again. Code that works, code that looks reasonable, but code that's built around a design that doesn't quite fit the problem.

18
00:02:41.950 --> 00:02:44.650
Nadav Mary: And you don't always notice it immediately.

19
00:02:44.770 --> 00:02:49.500
Nadav Mary: Usually, you will notice it months later, when simple change becomes

20
00:02:49.620 --> 00:02:59.750
Nadav Mary: Complicated, or when testing becomes painful, or when adding one feature means touching five different areas or classes in the code.

21
00:02:59.920 --> 00:03:18.720
Nadav Mary: And today, nowadays, AI is changing the way we develop software. It can write code incredibly fast, incredibly cheap, generate the entire implementation, suggest design patterns, and produce code that looks clean and well-structured.

22
00:03:18.920 --> 00:03:35.619
Nadav Mary: But here's something that I've been thinking a lot about since the AI came into our life. When AI generates a solution that looks perfectly reasonable, how do we know, actually, if this is the right solution?

23
00:03:36.820 --> 00:03:46.829
Nadav Mary: And this is something that I want us to explore together today. We're going soon to open the IDE and build something together, of course, in Python.

24
00:03:47.800 --> 00:03:59.570
Nadav Mary: And we'll start with a solution that seems perfectly reasonable, and then we'll introduce new requirements, discover some design problems, and see how we can improve the solution.

25
00:04:00.170 --> 00:04:12.389
Nadav Mary: We're going to revisit a few familiar coding practices, and I'm not here to teach you the definitions or anything like that. I guess that most of your… maybe all of you probably have heard about them before.

26
00:04:13.060 --> 00:04:18.100
Nadav Mary: My goal is to sharpen your instinct for when and why to apply them.

27
00:04:18.250 --> 00:04:32.540
Nadav Mary: And hopefully, you will live with a few simple rules of thumb that help you recognize these design problems earlier, whether if the code was written by you, or a teammate, or an AI agent.

28
00:04:32.670 --> 00:04:42.509
Nadav Mary: And I'm not going to reveal the design problems up front, that would be… that will spoil the fun, and we'll discover them together as we code.

29
00:04:42.880 --> 00:04:52.910
Nadav Mary: Yeah, so let's just jump into it and open the idea. I will use a cursor that also will be my assistant and will help me,

30
00:04:53.070 --> 00:04:54.600
Nadav Mary: code.

31
00:04:54.970 --> 00:04:57.760
Nadav Mary: And we're going today to build,

32
00:04:58.030 --> 00:05:16.659
Nadav Mary: a vehicle system, we're going to model a vehicle system, and we're going to start simple, having two different types of vehicles. We'll have the gasoline vehicle, which is run by gas, of course, and the electric vehicle, which is run by electricity, of course.

33
00:05:17.800 --> 00:05:25.090
Nadav Mary: And for our first implementation, I'm going to create a class of vehicles. It's going to be an abstract class.

34
00:05:25.310 --> 00:05:30.389
Nadav Mary: And, our base class will first have

35
00:05:30.550 --> 00:05:33.520
Nadav Mary: With Free Staff 2, and…

36
00:05:33.710 --> 00:05:42.960
Nadav Mary: main members. One would be the year of the vehicle, and the second will be, let's say, the model, and we'll save this,

37
00:05:43.140 --> 00:05:46.080
Nadav Mary: These members, on our class.

38
00:05:46.310 --> 00:05:53.480
Nadav Mary: And then we'll have an abstract method for starting, the, yeah, the, the vehicle.

39
00:05:53.990 --> 00:05:56.170
Nadav Mary: So we'll have the dev start.

40
00:05:56.450 --> 00:06:00.569
Nadav Mary: And this is an abstract method, so it will be implemented by the inheritors.

41
00:06:00.790 --> 00:06:11.159
Nadav Mary: And then we're going to have two different vehicles. As we've said, we'll have the gasoline and the electric vehicle, so let's implement them. So we'll have the gasoline vehicle.

42
00:06:11.310 --> 00:06:21.200
Nadav Mary: And, of course, we'll inherit from vehicle, and the gasoline vehicle will introduce, of course, the year and the model, and also will have the gas level.

43
00:06:21.850 --> 00:06:31.930
Nadav Mary: of the car, of the vehicle, and of course, we'll call Super.na, thanks, for Cursor, for holding the ear and the model, by the base class.

44
00:06:32.130 --> 00:06:38.679
Nadav Mary: And of course, we'll, hold the gas level also on, as a member in our,

45
00:06:38.790 --> 00:06:44.129
Nadav Mary: In the gasoline vehicle, And we'll, of course, have to implement our start method.

46
00:06:44.310 --> 00:06:45.040
Nadav Mary: Oh…

47
00:06:45.550 --> 00:06:59.820
Nadav Mary: Let's say that our implementation, yeah, just will be printing out that we're starting the car, the gasoline vehicle, let's also put over here, starting gasoline vehicle, printing the model and the gas level.

48
00:07:01.040 --> 00:07:04.609
Nadav Mary: And that's… Do just the same for the electric vehicle.

49
00:07:05.570 --> 00:07:15.820
Nadav Mary: And just the same will inherit from the vehicle, and our constructor, this time will get the air and the model just the same, and this time we'll get the battery level.

50
00:07:15.950 --> 00:07:32.129
Nadav Mary: And we'll hold the battery level as the data member in the electric vehicle, and our start method will do pretty much as similar as the gasoline vehicle, and we'll print out the model and the battery level of the electric vehicle.

51
00:07:32.920 --> 00:07:41.600
Nadav Mary: Perfect. And now we can go ahead and create an electric vehicle, and call to start, and when we run that.

52
00:07:41.960 --> 00:07:49.360
Nadav Mary: So we can see down here that we're starting the electric vehicle, and everything works as we, expect.

53
00:07:49.780 --> 00:07:54.100
Nadav Mary: Let's say that we are running the system for a while, for months, for…

54
00:07:54.330 --> 00:07:57.599
Nadav Mary: Whatever time it is. And then,

55
00:07:57.820 --> 00:08:08.470
Nadav Mary: We're getting a new requirement, and we want to support a hybrid vehicle. A hybrid vehicle, of course, that is running both on gas and on electricity.

56
00:08:09.250 --> 00:08:21.009
Nadav Mary: And of course, as good developers who want to perform code reuse, we want to reuse the capabilities that we already implemented in our gasoline and the electric vehicle.

57
00:08:22.060 --> 00:08:32.870
Nadav Mary: And for our implementation, we'd like to create a class, and this will be our first suggestion for creating the Harvard vehicle.

58
00:08:32.870 --> 00:08:44.000
Nadav Mary: And we'll use multiple inheritance, and we'll inherit both from gasoline and the electric vehicle, because we want to reuse the capabilities that these two classes are giving us.

59
00:08:44.330 --> 00:08:55.260
Nadav Mary: And Python also allows us to use multiple inheritance, so there is nothing wrong about about that.

60
00:08:55.730 --> 00:09:03.220
Nadav Mary: And then, for our constructor, of course, we'll hold the air, the model, and both gas and the battery level.

61
00:09:03.320 --> 00:09:10.800
Nadav Mary: And let's start by calling super.init with all the parameters, the year, the model, gas level, and battery level.

62
00:09:10.900 --> 00:09:20.580
Nadav Mary: And also, let's implement our start method. Yeah, start with the hybrid vehicle, and we'll print out the model, the gas level, and the battery.

63
00:09:21.730 --> 00:09:40.680
Nadav Mary: let's go ahead and try to initialize and calling the electric… no, the electric vehicle, sorry, the hybrid vehicle, let's do it again. So, let's initialize the hybrid vehicle, and calling the start method, and then we'll try and drown that for encountering our first issue.

64
00:09:41.780 --> 00:09:56.099
Nadav Mary: And if we're looking closely, so basically we've called in our constructor super.inate, and we can see over here that actually this super.init, as expected, by the way, is calling to gasolinevehicle.init.

65
00:09:56.700 --> 00:10:06.570
Nadav Mary: And this is since our hybrid vehicle is inheriting from gasoline vehicle first, and this is the reason that gasoline vehicle's constructor is being called.

66
00:10:07.510 --> 00:10:21.500
Nadav Mary: And we can see here that it gets less parameters than we're passing over here. We're passing also the battery level, which is not expect… is not accepted by the gasoline vehicles constructor, and this is the reason

67
00:10:21.500 --> 00:10:29.229
Nadav Mary: we're getting that error. And, one solution for that, there are various solutions for this.

68
00:10:30.750 --> 00:10:48.850
Nadav Mary: And we'll go for one solution. This is calling… instead of calling super.init, and we'll talk deeply about that just in a few moments, we'll call explicitly to gasolinevehicle.init as a static call, and this time we'll have to pass self.

69
00:10:48.960 --> 00:10:58.390
Nadav Mary: And of course, we'll call also electric vehicle.init, and we'll call it the gasoline vehicle only with the gas level, so we'll delete the battery level.

70
00:10:59.670 --> 00:11:01.120
Nadav Mary: And pretty much…

71
00:11:02.270 --> 00:11:07.519
Nadav Mary: Let's hope that this is it, and now it will work, so let's go and run the code.

72
00:11:08.010 --> 00:11:13.059
Nadav Mary: And no, it seems that they were still having an issue, and they will dig into it.

73
00:11:13.200 --> 00:11:21.879
Nadav Mary: So we can see that our init function… go and see the status, right? So, our init function calls the gasolinevehicle.init.

74
00:11:22.310 --> 00:11:26.620
Nadav Mary: And then we're having… we're hitting the super.init.

75
00:11:26.720 --> 00:11:33.180
Nadav Mary: And this time we got the electric vehicle that is missing one requirement parameter of the battery level.

76
00:11:33.460 --> 00:11:48.260
Nadav Mary: And then, here, we can say that things are becoming more complicated, because this is something we wouldn't expect when calling super, that suddenly electric vehicles constructor will be called.

77
00:11:48.320 --> 00:12:03.009
Nadav Mary: And the reason for that is a mechanism in, that is, is being applied in Python and in many other languages that is called the Method Resolution Order, MLO.

78
00:12:03.060 --> 00:12:13.499
Nadav Mary: And the MRO is becoming confusing, and something you should be familiar with when dealing, especially with multiple inheritance.

79
00:12:13.620 --> 00:12:22.889
Nadav Mary: Because you might think that calling super.something will… will call your parents, function, but this is not the case.

80
00:12:22.950 --> 00:12:30.340
Nadav Mary: Not necessarily the case when dealing with multiple inheritance. When calling super, what is actually happening is that

81
00:12:30.400 --> 00:12:47.790
Nadav Mary: in Python, in the other languages, Python is building how the method resolution will be ordered. And when dealing with multiple inheritance, the method resolution order will be when we're having the hybrid vehicle, then

82
00:12:47.790 --> 00:12:58.210
Nadav Mary: The first inherited gasoline vehicle, and then the next method resolution order will be taken from the electric vehicle, and then from the base class of the vehicle.

83
00:12:58.330 --> 00:13:01.690
Nadav Mary: So when we hit, GaslonVehicle.innit.

84
00:13:02.000 --> 00:13:07.760
Nadav Mary: And then, when we called super.net from the gasoline vehicle, we actually called for the next

85
00:13:07.830 --> 00:13:24.929
Nadav Mary: method in the… in the order, and super does need in this time, so we started from hybrid vehicle, then we arrived to gasoline vehicle, and the next method will be from the electric vehicle, and not from the vehicle. And this is the confusion, and this is the confusing point.

86
00:13:25.400 --> 00:13:33.589
Nadav Mary: About, calling, super. And this is the reason where we, we reached out from the gasoline vehicle into the electric vehicle.

87
00:13:34.900 --> 00:13:45.300
Nadav Mary: And since we are calling super.init with an ear and a model, and in our case, calling super is actually calling to electric vehicles constructor.

88
00:13:45.640 --> 00:13:59.919
Nadav Mary: This is why we're missing some parameters, as we've said… as being said here in the… in the yellow, that we're missing one required position algorithm, which… which is the battery level, since super.Nate of the gasoline vehicle passes only the air in the model.

89
00:14:00.820 --> 00:14:01.550
Nadav Mary: bomb.

90
00:14:01.590 --> 00:14:12.289
Nadav Mary: And this is… and we can solve this issue just as we've solved the previous problem, so we can explicitly, instead of calling super.

91
00:14:12.290 --> 00:14:25.840
Nadav Mary: We actually wanted the vehicle being called, so we can just explicitly call vehicle.init, and we'll pass here self, both in the gasoline, in the electric vehicle, you know, constructor.

92
00:14:26.030 --> 00:14:41.419
Nadav Mary: And then our problem will be solved. Let's run the code right now and see if everything is fine, and we can see here that we're starting our Harvard vehicle with the gas level and the battery level.

93
00:14:41.600 --> 00:14:59.030
Nadav Mary: And everything is fine, but as we said at the beginning, we want our… we want to make as much reuse of our code as possible, and we can see that our start method doesn't…

94
00:14:59.040 --> 00:15:07.659
Nadav Mary: doesn't reuse the start from the electric and the gasoline vehicle. So let's play a little bit with that and see.

95
00:15:07.660 --> 00:15:12.350
Gabor Szabo: Nadav, sorry, could you change the number so they won't be both 100?

96
00:15:12.840 --> 00:15:13.729
Nadav Mary: Yeah, of course.

97
00:15:14.130 --> 00:15:14.970
Nadav Mary: Of course.

98
00:15:16.110 --> 00:15:27.909
Nadav Mary: So let's say that our… yeah, our battery level is on 50 and 100 for the gas level. Let's run it again, so now we can see the difference. Perfect.

99
00:15:28.230 --> 00:15:32.000
Gabor Szabo: Just to make sure that the numbers are in the correct place, and not… Yeah.

100
00:15:32.180 --> 00:15:34.440
Nadav Mary: Absolutely right. Yeah, yeah.

101
00:15:34.580 --> 00:15:37.810
Nadav Mary: Perfect. So,

102
00:15:37.920 --> 00:15:54.060
Nadav Mary: Yeah, so let's try and perform code reviews in our start method, and we already talked about the MRO and its confusion about how it behaves, so let's first go and call super.start and see,

103
00:15:54.300 --> 00:15:57.270
Nadav Mary: How it goes and what we're getting.

104
00:15:57.990 --> 00:16:02.390
Nadav Mary: So now we can see that we're calling to starting gasoline vehicle.

105
00:16:02.520 --> 00:16:10.249
Nadav Mary: And then we're calling to our starting hybrid vehicle, but we do not call our electric vehicle at all.

106
00:16:10.510 --> 00:16:15.890
Nadav Mary: And as we said, we want to use both of our capabilities from both electric and the gasoline vehicle.

107
00:16:17.390 --> 00:16:34.520
Nadav Mary: And let's take it even farther. We already talked about the MRO, the method, resolution, and order. If we'll go here and replace the way that we are inheriting, so we'll inherit from the electric vehicle and then from the gasoline vehicle, then we'll run our program.

108
00:16:34.740 --> 00:16:45.420
Nadav Mary: So, surprisingly, or maybe now, and not that surprisingly, now that we understand the MRO, we're seeing that we arrived to our electric vehicle start function.

109
00:16:45.560 --> 00:16:54.399
Nadav Mary: And then to the hybrid vehicle. But we didn't get into our gasoline vehicle. So, as we can see here, the,

110
00:16:55.030 --> 00:17:13.379
Nadav Mary: the order that we are inheriting from our electric and the gasoline vehicle actually influences our behavior of the code, and this is something that I think that we wouldn't expect, but in our case, it did influence it.

111
00:17:15.220 --> 00:17:30.399
Nadav Mary: Perfect. So in order to fix that, so we already learned about calling explicitly to gasolineVehicle.it its function, so we could call gasolineVehicle.start, and electric vehicle.start in our start method, and it would solve the problem.

112
00:17:31.420 --> 00:17:41.709
Nadav Mary: But let's learn another technique that we can do over here, and this is calling the super.start, and taking advantage of the MRO,

113
00:17:41.910 --> 00:17:50.229
Nadav Mary: In both of our gasoline and the electric vehicle, and as we've said, since we're calling Super.start, so our first

114
00:17:50.280 --> 00:18:10.279
Nadav Mary: method resolution order will go this time to the electric vehicle start function, and then the super.start over here will go to the next method in the order, and it will go to the gasoline vehicles start method, and then it will print out the gasoline vehicle, then the electric vehicle start, and then we'll see the hybrid vehicle

115
00:18:10.690 --> 00:18:13.139
Nadav Mary: So let's run and say that this is the…

116
00:18:13.290 --> 00:18:29.809
Nadav Mary: the way it behaves, and as we've said, this is our expected behavior, and again, as we've seen before, if I flip again the inheritance order, so our behavior will be changed.

117
00:18:29.900 --> 00:18:42.640
Nadav Mary: Okay, so in the first run, it was the gasoline vehicle that was hit first, then the electric vehicle, and now it was flipped since we have flipped our inheritance order.

118
00:18:42.750 --> 00:18:53.760
Nadav Mary: Alright, so it was pretty, pretty tough, stuff that we've been dealing here, and,

119
00:18:54.100 --> 00:19:10.329
Nadav Mary: you know, when I'm seeing this solution, it feels quite complicated to me, and we've been struggling with having here only four classes in our modeling system, and we already encountered so many issues.

120
00:19:10.420 --> 00:19:14.070
Nadav Mary: So this is a red flag, for me.

121
00:19:14.070 --> 00:19:31.849
Nadav Mary: And also, if I'm taking it a step further, since our… let's take the electric vehicle and our hybrid vehicle, so since the hybrid vehicle is inheriting from electric vehicle, so each new function or capability that will be applied to the electric vehicle

122
00:19:31.880 --> 00:19:50.510
Nadav Mary: will be automatically applied to our hybrid vehicle. So, for example, if we'll have a new… have a new capability of wireless charge for our, for our electric vehicle, and, of course, wireless charge will have to charge our battery level.

123
00:19:50.570 --> 00:20:07.910
Nadav Mary: So this capability will be automatically applied to our hybrid vehicle, and if I'll try to call over here, and the idea already completes what I want to do, and if I'll call in the hybrid vehicle the wireless charge, so

124
00:20:08.100 --> 00:20:21.960
Nadav Mary: And I'll run the program, so you can see that I got this capability automatically into my hybrid vehicle, although it was implemented in my base class of the electric vehicle, but

125
00:20:22.140 --> 00:20:35.820
Nadav Mary: maybe we do not want date capability. Maybe our hybrid vehicle doesn't support, or doesn't support yet, the wireless charge capability. So what we'll do then? Because now we can call this, and it's…

126
00:20:36.110 --> 00:20:49.270
Nadav Mary: you know, kind… kind of will be working, but it's not really what we were intended to do. So, I guess that what we'll do next will be go and…

127
00:20:50.460 --> 00:21:00.510
Nadav Mary: And then override the wireless charge function, and then we'll raise, yeah, a not implemented error, so if developers will go and call wireless charge, so they will encounter

128
00:21:00.660 --> 00:21:04.630
Nadav Mary: That exception, and then they'll know that they shouldn't do that.

129
00:21:05.120 --> 00:21:12.190
Nadav Mary: Yeah, so things becoming really, really smelly in our implementation.

130
00:21:12.340 --> 00:21:15.880
Nadav Mary: Let's stop here for a second and go back to our presentation.

131
00:21:17.480 --> 00:21:28.800
Nadav Mary: Perfect. So, let's talk, and let's talk a little bit more about the download inheritance problem that we just encountered, and in general, about inheritance.

132
00:21:30.070 --> 00:21:40.539
Nadav Mary: So, as we've seen, we've had a vehicle system, we started with a vehicle-based class, then we had the electric and the gasoline vehicle that we're inheriting from the vehicle.

133
00:21:40.560 --> 00:21:54.900
Nadav Mary: And then we added the hybrid vehicle, and we used multiple inheritance in order to achieve our capabilities, and then we encountered the download inheritance. Damode inheritance, basically, you can see it over here in this,

134
00:21:55.080 --> 00:22:01.749
Nadav Mary: In this diagram is when we have one class, the hybrid… in our case, it was the hybrid vehicle, which

135
00:22:02.380 --> 00:22:11.650
Nadav Mary: It inherits both with the… from two classes. In this example, it was the electric vehicle and the gasoline vehicle, and these two classes are inheriting from,

136
00:22:11.940 --> 00:22:28.779
Nadav Mary: the same ancestor. In our case, it's the vehicle, and then we get this shape of a diamond, and this is called the diamond inheritance problem, and we've seen various problems that we had to deal with, whether it's the method resolution.

137
00:22:29.480 --> 00:22:46.859
Nadav Mary: the confusing method resolution order, and also, we can say that we only have here four classes, and we only have a hierarchy tree level of level 2. We have the vehicle, electric gas vehicle, and under them, with the hybrid vehicle, it's a lot of

138
00:22:46.900 --> 00:22:52.749
Nadav Mary: Things that we need to follow in order to understand how, our system,

139
00:22:52.820 --> 00:23:10.819
Nadav Mary: is working, and also what will happen when we'll add more and more vehicle types? What will happen if we'll need to put a new vehicle between, I don't know, our electric vehicle and the hybrid vehicles? We'll need to refactor and change our whole modeling system.

140
00:23:11.100 --> 00:23:21.669
Nadav Mary: Great. So… Let's just take it and see what we can do in order to simplify our implementation.

141
00:23:22.740 --> 00:23:25.810
Nadav Mary: So I'm going back to the… to the IDE.

142
00:23:26.190 --> 00:23:29.959
Nadav Mary: And what we're going to do now is,

143
00:23:30.240 --> 00:23:33.700
Nadav Mary: He's doing a few things in order to flatten down

144
00:23:33.750 --> 00:23:49.480
Nadav Mary: flatten, actually, this inheritance chain. And, first of all, we'll go to the basics, and let's talk about our gasoline and our electric vehicle. So basically, the gasoline and the electric vehicle, they both hold

145
00:23:49.490 --> 00:24:03.410
Nadav Mary: the way that the vehicle is starting, whether by gas or whether by battery. So we're talking about the engine system. So what we're going to do now is instead of holding these capabilities of gas.

146
00:24:03.480 --> 00:24:06.069
Nadav Mary: And watery, and…

147
00:24:06.220 --> 00:24:23.729
Nadav Mary: directly in our vehicles, we're going to take it out into a new modeling hierarchy of engines. So, what I'm going to do is implement the engine class, it's going to be abstract.

148
00:24:24.270 --> 00:24:37.699
Nadav Mary: And we'll have an upset method for the start, to start the engine. Yeah, and then I'm going to have two new engines. I'm going to have the gasoline engine and the electric engine.

149
00:24:37.850 --> 00:24:41.570
Nadav Mary: Okay, so let's start with the gasoline engine, and…

150
00:24:41.880 --> 00:24:47.089
Nadav Mary: And its constructor will hold the gas level.

151
00:24:47.360 --> 00:24:52.769
Nadav Mary: As we've done before, and we're going to replace it, as we've done before in the gasoline vehicle.

152
00:24:52.910 --> 00:24:55.059
Nadav Mary: And we're going to hold the gas level.

153
00:24:55.570 --> 00:25:03.010
Nadav Mary: Inside the gasoline engine, and of course, we'll have to implement the start method, because we're inheriting from the engine.

154
00:25:03.340 --> 00:25:16.610
Nadav Mary: So our start method will simply, yeah, we'll start gasoline engine, and we'll print out the gas level, and we'll do just the same for the electric engine. Thank you, cursor.

155
00:25:16.690 --> 00:25:30.469
Nadav Mary: So we have the electric engine, we have the constructor, and we are holding the battery level in our electric engine, and our start function is starting the electric engine, and we're printing out the battery level.

156
00:25:30.620 --> 00:25:42.020
Nadav Mary: And now we're going to change our gasoline and the electric vehicles. We're not going to hold anymore the gas level itself, but instead we're going to hold and create the engine.

157
00:25:42.110 --> 00:25:56.439
Nadav Mary: of the gas level. So, we're composing, or is in composition of the gas level inside the gas… the gasoline vehicle. So, we're using composition and holding the gasoline engine.

158
00:25:56.480 --> 00:26:15.399
Nadav Mary: And now we'll have also to change our start implementation, and we'll call self.engine.gasLevel, and of course, our start function doesn't have to… maybe, no, let's leave it for now, but we'll call this time to the engine.start.

159
00:26:15.670 --> 00:26:21.200
Nadav Mary: Which will go ahead… will go to the gasoline engine start function.

160
00:26:21.340 --> 00:26:27.159
Nadav Mary: Perfect. And then we'll do the same for the electric vehicle. Instead of holding the battery level over here.

161
00:26:27.290 --> 00:26:38.660
Nadav Mary: We'll hold the electric engine instead, and we'll pass the battery level, and we'll fix our start function, also to call self.engine.start.

162
00:26:38.790 --> 00:26:44.870
Nadav Mary: And, of course, over here, the start function will take the battery level from the engine.

163
00:26:45.000 --> 00:26:53.559
Nadav Mary: And for our wireless charge, so just the same, we'll call self.engine.batteryLevel, and we'll increase it by 10, and…

164
00:26:54.040 --> 00:26:57.970
Nadav Mary: Of course, same for the printing out the battery level.

165
00:26:58.980 --> 00:27:03.490
Nadav Mary: Perfect. Now, we… we've prepared,

166
00:27:03.810 --> 00:27:08.239
Nadav Mary: the field for fixing our hybrid vehicle.

167
00:27:08.350 --> 00:27:16.380
Nadav Mary: So if you are thinking about that, and when thinking about inheritance, you should always keep in mind that,

168
00:27:17.580 --> 00:27:36.889
Nadav Mary: that inheritance is a relationship between two or more classes, and usually if you want to ensure that inheritance fits to your use case, just try and say whether your subclass is a type of the class. So, for example.

169
00:27:36.890 --> 00:27:47.789
Nadav Mary: let's try and put it on our use case. So, hybrid vehicle is a gasoline vehicle and electric vehicle, and in saying that, it doesn't really feel correct, because

170
00:27:47.790 --> 00:27:58.490
Nadav Mary: hybrid vehicle is not a gasoline vehicle, and neither an electric vehicle. They do share some common behaviors, common capabilities, but they don't

171
00:27:58.800 --> 00:28:06.910
Nadav Mary: They're not really the same. They don't share the same… they're not the same identity.

172
00:28:07.010 --> 00:28:23.189
Nadav Mary: But if we're talking about hybrid vehicle and the vehicle, the base class, or base class from the beginning, so we can say that the hybrid vehicle is a vehicle, and it will be absolutely valid. So, let's go ahead and inherit

173
00:28:23.190 --> 00:28:31.399
Nadav Mary: Directly from a vehicle, instead of, inheriting from both electric and And the gasoline vehicle.

174
00:28:31.470 --> 00:28:46.110
Nadav Mary: And now we can do just the same as we've done in our electric and gasoline vehicle, and instead of calling the init functions, we can just go and initialize our gasoline engine, and the electric engine, and

175
00:28:46.110 --> 00:28:54.140
Nadav Mary: Use, as well in our habit vehicle, using composition and holding these engines.

176
00:28:54.190 --> 00:29:01.990
Nadav Mary: in the hybrid vehicle. Then our start function, we don't need to call that anymore, super.start, because

177
00:29:02.150 --> 00:29:14.520
Nadav Mary: Our super.start will go to the vehicle, which is an absolute class that does nothing, so we can simply call self.gasolineEngine.start and self.electricEngine.start.

178
00:29:14.650 --> 00:29:24.759
Nadav Mary: And also, yeah, we can change over here our print in order to print the right… from the right place, the gas level and the battery level.

179
00:29:24.890 --> 00:29:35.529
Nadav Mary: And we don't need anymore this wireless charge, not implemented error, because we do not inherit anymore this function.

180
00:29:35.760 --> 00:29:42.050
Nadav Mary: The wireless charging, because we don't inherit from electric vehicle anymore, so we can just… Delete.

181
00:29:42.240 --> 00:29:50.210
Nadav Mary: And then we can delete the habitvehicle.wirelessChart, because it's not something that exists.

182
00:29:50.360 --> 00:29:53.419
Nadav Mary: On our hybrid vehicle. And…

183
00:29:53.620 --> 00:30:00.150
Nadav Mary: let's just hope that I did everything fine. I'll try to run the program.

184
00:30:00.420 --> 00:30:03.039
Nadav Mary: And it seems like I missed something.

185
00:30:06.920 --> 00:30:08.709
Nadav Mary: Let's see what I've missed…

186
00:30:12.700 --> 00:30:14.170
Nadav Mary: Seems like there is…

187
00:30:17.860 --> 00:30:19.679
Nadav Mary: Yeah, just a second…

188
00:30:33.830 --> 00:30:37.450
Nadav Mary: Inload syntax… deprecated.

189
00:30:38.010 --> 00:30:46.240
Nadav Mary: I think that they just… Have a typo somewhere…

190
00:30:59.330 --> 00:31:03.289
Nadav Mary: If any of you is seeing the typo, just let me know.

191
00:31:12.110 --> 00:31:13.539
Gabor Szabo: Can you show the whole arrow?

192
00:31:15.060 --> 00:31:15.420
Nadav Mary: Sorry.

193
00:31:15.420 --> 00:31:18.120
Gabor Szabo: Can you enlarge the… yeah, that one.

194
00:31:18.640 --> 00:31:23.600
Nadav Mary: Yeah, it seems like… Something's…

195
00:31:25.180 --> 00:31:27.230
Gabor Szabo: Close the editor and open it again.

196
00:31:27.230 --> 00:31:28.660
Nadav Mary: Yeah, let's try that.

197
00:31:30.780 --> 00:31:33.139
Nadav Mary: Let's killer terminal and see…

198
00:31:37.360 --> 00:31:38.740
Nadav Mary: Alright, thank you.

199
00:31:39.920 --> 00:31:43.420
Nadav Mary: Let's see, so our… Yeah.

200
00:31:43.660 --> 00:31:45.660
Nadav Mary: Hybrid vehicle.

201
00:31:46.010 --> 00:31:47.659
Nadav Mary: Don't have them there anymore.

202
00:31:48.060 --> 00:31:49.230
Nadav Mary: Just a second…

203
00:32:03.980 --> 00:32:04.950
Nadav Mary: Hmm.

204
00:32:13.540 --> 00:32:17.520
Gabor Szabo: If you don't initialize the period, then the model won't be assigned.

205
00:32:17.520 --> 00:32:21.329
Nadav Mary: All right, yeah, so I'm missing over here the super domain.

206
00:32:21.550 --> 00:32:33.229
Nadav Mary: And that's it. This was the missing part. We had to call to Super.ignate in order to initialize the year and the model, sorry for that. And now everything works, as we expect.

207
00:32:33.970 --> 00:32:46.160
Nadav Mary: Perfect. Also, yeah, what, assets we can do is… we don't need anymore to call super.star, the electric vehicle in the gasoline vehicle.

208
00:32:46.510 --> 00:33:03.030
Nadav Mary: Because, again, calling super.start just will point to the vehicle, which points to pretty much nothing, because this is an abstract method, we did it only to fix the method resolution order, and do the same here in the gasoline vehicle.

209
00:33:03.410 --> 00:33:09.870
Nadav Mary: And also, we don't need to call explicitly in the electric and the gasoline vehicle.

210
00:33:09.980 --> 00:33:19.089
Nadav Mary: to vehicle local, we can go back and call super.inet, and we'll do the same over here in the electric vehicle.

211
00:33:20.220 --> 00:33:27.570
Nadav Mary: And let's see that everything still works, and yeah, it seems that everything is working, and… And…

212
00:33:27.760 --> 00:33:45.539
Nadav Mary: I feel right now that the implementation, feels, way more predictable and more expected, in… compared to what we did before. Perfect. So let's go back to the presentation.

213
00:33:47.150 --> 00:34:01.450
Nadav Mary: Yeah, so basically what we've done here is using composition for the rest of the inheritance and the damage inheritance issues. So we have created new models for the engine and the electric and the gasoline engine.

214
00:34:01.890 --> 00:34:14.809
Nadav Mary: And then our… for our vehicle modeling, we've used composition also, so our electric vehicle and the gasoline vehicle now use composition in order to hold the electric and the gasoline engines.

215
00:34:15.070 --> 00:34:32.820
Nadav Mary: And our hybrid vehicle, we have flattened our hierarchy tree level, and instead of inheriting gasoline and the electric vehicle, as we've done before, is now inheriting directly from the base vehicle class, and is holding the gasoline and the electric engine.

216
00:34:33.110 --> 00:34:43.400
Nadav Mary: engines. Perfect. So we've talked, pretty much, a lot about inheritance and composition. Let's, I have a question.

217
00:34:43.889 --> 00:34:44.316
Gabor Szabo: But the.

218
00:34:44.530 --> 00:34:45.080
Nadav Mary: Yep.

219
00:34:45.550 --> 00:34:52.050
Gabor Szabo: Have you encountered any case where a diamond inheritance didn't make a problem?

220
00:34:53.749 --> 00:35:12.559
Nadav Mary: Basically, so, this example is taken from a real-world example that I've encountered in my job. Diamond inheritance usually will cause you problems, as we've seen over here.

221
00:35:12.659 --> 00:35:23.199
Nadav Mary: This… there is no… basically, there is not any problem using multiple inheritance, although you should be cautious also about multiple inheritance.

222
00:35:23.309 --> 00:35:40.719
Nadav Mary: But if we're talking about diamond inheritance, so in the end, you'll probably end up dealing with the MRO, the confusing MR role, and also think about it, that in our friendship implementation, we had to call the vehicle.net twice.

223
00:35:40.829 --> 00:35:58.559
Nadav Mary: both from the electric vehicle and the gasoline vehicle, when we initialized the hybrid vehicle. In our case, it didn't cause any problem, because the calling vehicles in it function was pretty much consistent, and it only initialized its members, but

224
00:35:58.609 --> 00:36:13.529
Nadav Mary: But in other cases, you might encounter issues. So, whenever you're dealing with download inheritance, I guess that it's a red flag for your implementation, and you might rethink about your code design.

225
00:36:14.620 --> 00:36:26.550
Gabor Szabo: I think, actually, if it was a real car, then this would… calling the initialization of the vehicle twice would mean… would be like turning the key twice.

226
00:36:27.050 --> 00:36:28.750
Nadav Mary: Yep. Yeah, yeah, that's correct.

227
00:36:28.960 --> 00:36:33.400
Gabor Szabo: These days, no one turns a key, but just pushes the button, but…

228
00:36:33.400 --> 00:36:41.820
Nadav Mary: Yeah, but then you will push the button twice, so it's the same… might be the same problem. Again, maybe pushing the button twice will cause nothing, but a good shot.

229
00:36:42.540 --> 00:36:43.160
Nadav Mary: Lucas.

230
00:36:43.360 --> 00:36:45.200
Nadav Mary: Or maybe turn the car off, absolutely.

231
00:36:45.870 --> 00:36:46.359
Gabor Szabo: Yeah, yeah.

232
00:36:46.360 --> 00:36:57.060
Nadav Mary: Because really, it depends on the implementation, and again, this is something that you wouldn't expect from your code, and this is when things can become worse.

233
00:36:59.380 --> 00:37:00.070
Gabor Szabo: Okay.

234
00:37:01.060 --> 00:37:11.609
Nadav Mary: Perfect. Yeah, so let's talk about, inheritance versus composition. Let's talk about pros and cons, in different aspects. So, when

235
00:37:11.610 --> 00:37:20.160
Nadav Mary: We're talking about the relationship type, so we already touched it, before. So, when talking about inheritance, we're talking about an is,

236
00:37:20.160 --> 00:37:31.989
Nadav Mary: relationship. So, a gasoline vehicle is a vehicle, and our hybrid vehicle, we thought that inheritance would fit, but hybrid vehicle isn't gasoline and electric vehicle.

237
00:37:32.090 --> 00:37:50.450
Nadav Mary: This is why, this is why we had the confusion, and of course, there are various of examples. I don't know, a rectangle is a shape, right? And this may be something that you are, you already heard so many times from your studies.

238
00:37:51.570 --> 00:38:03.550
Nadav Mary: And regarding composition, we're talking about a hash relationship. So, as we've seen, a car has an engine, and this is how you can know that composition will fit into your use case.

239
00:38:03.710 --> 00:38:06.500
Nadav Mary: Regarding, flexibility.

240
00:38:06.750 --> 00:38:17.430
Nadav Mary: So we've seen that inheritance introduced us a strict structure and deep hierarchies, so we're not very flexible when dealing with inheritance.

241
00:38:18.400 --> 00:38:33.129
Nadav Mary: If we want to add more classes to our inheritance chain, it might become difficult, or if we're adding more capabilities, so we're getting that immediately into our subclasses.

242
00:38:34.220 --> 00:38:44.719
Nadav Mary: And we're talking about composition, so we have more modularity, and it's easier to change. We have some modules, and we can plug and play the different classes into

243
00:38:44.720 --> 00:38:56.869
Nadav Mary: Into other classes, as we've seen with the gasoline vehicle, and we used composition to add the gasoline engine, then we had the hybrid vehicle, which also composed the gasoline engine.

244
00:38:56.870 --> 00:39:04.769
Nadav Mary: Or, for example, if we'll have the air conditioning system, so we can have more composition to our vehicles.

245
00:39:05.180 --> 00:39:06.489
Nadav Mary: And so on.

246
00:39:06.670 --> 00:39:20.410
Nadav Mary: Regarding code reusability, so inheritance, as we've seen, it highly encourages code reuse, but it can lead into tight coupling, as we've seen with wireless charging.

247
00:39:20.410 --> 00:39:30.560
Nadav Mary: function that we had to inherit, and there is an exception for our private vehicle when we didn't necessarily wanted this mobility.

248
00:39:31.000 --> 00:39:44.620
Nadav Mary: And regarding composition, it also encourages code reuse, and in this time, we're getting decoupled behavior also. And just a small notice.

249
00:39:44.720 --> 00:39:53.019
Nadav Mary: code… so when we're talking about code reviews, it's not necessarily talking about writing less code. In our new implementation, we have

250
00:39:53.060 --> 00:40:12.849
Nadav Mary: from what I remember, around 20 lines more code than our first implementation, but we're still having code reviews. We're still reusing the start from our volume and the electric engines, so we do have code reviews. We might write a little bit more code.

251
00:40:13.000 --> 00:40:15.969
Nadav Mary: But we are gaining more flexibility

252
00:40:16.290 --> 00:40:19.869
Nadav Mary: and, and the couple, behavior.

253
00:40:20.120 --> 00:40:22.560
Nadav Mary: And… talking about composition.

254
00:40:22.590 --> 00:40:40.449
Nadav Mary: Regarding the MRO, the method resolution order, so when dealing with a diamond inheritance, where we have to deal with confusing MRO, and we had to debug and understand how it works in order to understand what happened.

255
00:40:40.510 --> 00:40:43.940
Nadav Mary: And when talking about composition, it's not,

256
00:40:44.030 --> 00:40:45.980
Nadav Mary: It's not something that we had to deal with.

257
00:40:46.090 --> 00:41:02.050
Nadav Mary: And regarding scalability, so in inheritance, the more inheritance chains that we'll have, the more deep it will be, it will be harder to extend. And in composition, it scales better as the product grows.

258
00:41:03.580 --> 00:41:13.649
Nadav Mary: Basically, that's it, let's sum it up. So, when should we use inheritance, and when should we use composition? So, use inheritance when the objects share both common identity and behavior.

259
00:41:13.660 --> 00:41:33.229
Nadav Mary: So, our confusion at the beginning was that the hybrid and the gasoline and the electric vehicle shared the same behavior of the gas level and the battery level, but it didn't share the common identity, and this is why our first implementation didn't really fit.

260
00:41:33.620 --> 00:41:44.150
Nadav Mary: And use composition when your object needs functionality from another class, but it's not fundamentally the same thing as we've seen.

261
00:41:44.460 --> 00:41:45.260
Nadav Mary: Great.

262
00:41:46.180 --> 00:42:00.089
Nadav Mary: Let's go to the second part. In the second part, we'll not need neither the hybrid vehicle and the wireless chart, so I'll just delete it, so we'll have less code to look at.

263
00:42:00.440 --> 00:42:09.949
Nadav Mary: And let's say that now we want to add a new capability to our vehicle system, and is a capability of creating a report.

264
00:42:09.950 --> 00:42:24.159
Nadav Mary: So let's say that in the base behavior will print out the year and the model, and our inheritors, the gasoline and the electric vehicles, will print out the gas level and the battery level.

265
00:42:24.370 --> 00:42:37.299
Nadav Mary: in each of them. So we'll have a full report with the year, the model, and the specific parts of each, of each vehicle. So, what we can do is creating a function of a create report.

266
00:42:37.690 --> 00:42:44.689
Nadav Mary: And we'll print out the model and the year.

267
00:42:44.750 --> 00:42:58.420
Nadav Mary: And then what we can do is go ahead for our gasoline and the electric vehicles, and we can override, the createReport function.

268
00:42:58.580 --> 00:43:02.510
Nadav Mary: And first, of course, we'll call a super.createReport.

269
00:43:02.660 --> 00:43:14.069
Nadav Mary: And then we'll print out the specific part of the gasoline vehicle, which is the gas level, and we'll do just the same for the electric vehicle.

270
00:43:14.210 --> 00:43:31.050
Nadav Mary: And now one will print out our electric vehicle credit report, and we'll run that. We can see that we have the full report with the model, and the year, and the electric report. The electric vehicle adds its battery level.

271
00:43:31.250 --> 00:43:34.150
Nadav Mary: And when looking at that.

272
00:43:34.150 --> 00:43:48.019
Gabor Szabo: Nadav, sorry, sorry to interrupt you. Sure. There is a question now, could we consider using protocols? Would they add flexibility? Are they as easy to maintain in sort as well as in code?

273
00:43:48.870 --> 00:44:06.060
Nadav Mary: Yes, absolutely, we can use a protocol. I don't want to touch it a lot, but maybe I can share an example later in the chat, but absolutely, you can use a protocol in order to encapsulate some behaviors inside the protocol, and then your

274
00:44:06.060 --> 00:44:23.630
Nadav Mary: letting your inheritors go ahead and implement their specific… the specific behavior that you would like. I didn't want to go into protocols, because it's something that might be more specific to Python, and I wanted to explain

275
00:44:23.630 --> 00:44:31.829
Nadav Mary: the, the basic, patterns, agnostically, but, absolutely, yes. You can, also use, protocols and,

276
00:44:31.840 --> 00:44:37.299
Nadav Mary: Later, I can, I can share in the chat, implementation using protocols.

277
00:44:39.830 --> 00:44:40.510
Gabor Szabo: Thanks.

278
00:44:40.890 --> 00:44:44.200
Nadav Mary: Yes, thank you. Yeah, so,

279
00:44:44.400 --> 00:44:47.870
Nadav Mary: So, let's go back to the Curate report, so…

280
00:44:48.100 --> 00:44:58.469
Nadav Mary: So, we can already see that we're having some issues with that implementation. First of all, our gasoline and electric vehicles

281
00:44:58.600 --> 00:45:09.750
Nadav Mary: must call the super.createReport, because otherwise our… our report will look broken. We'll have only their specific parts, so right now.

282
00:45:10.160 --> 00:45:17.130
Nadav Mary: Our inheritors are controlling the basic behavior, sorry, for the create report.

283
00:45:17.780 --> 00:45:31.979
Nadav Mary: And calling super becomes mandatory, otherwise we're breaking the base behavior, and this also breaks the encapsulation of the base class of how the report will look like.

284
00:45:33.860 --> 00:45:52.699
Nadav Mary: And second of all, and even worse, what if our report, and let's go to the base function, what if our report will be more sophisticated, and not just the first line from the base class, and then second line from the inheritor? What if we'll want

285
00:45:52.710 --> 00:45:55.090
Nadav Mary: I had to create here the header.

286
00:45:55.280 --> 00:46:06.070
Nadav Mary: And then we'll want the body of the report, the specific part, and then in our… let's say even the header, the model is

287
00:46:06.440 --> 00:46:17.949
Nadav Mary: The model, and then in our footer, we'll want to print out our… the ear of the… of the… of the… of the vehicle.

288
00:46:18.160 --> 00:46:22.580
Nadav Mary: In this case, in our implementation, it will never work, because

289
00:46:22.710 --> 00:46:31.780
Nadav Mary: calling super will print out the header and the footer, and just then the specific part of our subclass.

290
00:46:33.380 --> 00:46:37.640
Nadav Mary: And this is where things, again, becomes more complicated.

291
00:46:38.670 --> 00:46:52.419
Nadav Mary: And in order to fix that, what we can do, is using the temp… it's called the template design pattern, in order to simplify our, infra code, our vehicle.

292
00:46:52.520 --> 00:47:02.249
Nadav Mary: code. And the idea is that we let the vehicle base class to define how the report should look like, structurally speaking.

293
00:47:02.700 --> 00:47:11.690
Nadav Mary: And our inheritance, the gasoline and the electric vehicle, will only deal and will add their specific parts to the report.

294
00:47:12.540 --> 00:47:17.790
Nadav Mary: So what we're going to do is keeping our createReport main function.

295
00:47:17.920 --> 00:47:22.609
Nadav Mary: And, our vehicle will call the create a body report.

296
00:47:22.970 --> 00:47:30.730
Nadav Mary: Which will be… which will be an abstract function, an abstract method.

297
00:47:30.870 --> 00:47:37.900
Nadav Mary: It, will be enforced, will be implemented by each inheritor.

298
00:47:38.030 --> 00:47:52.019
Nadav Mary: And then what we'll do is that in our gasoline vehicle and the electric vehicle, instead of overriding the create report, we'll override the create body report, and now we don't have any more to call to super.

299
00:47:52.280 --> 00:48:00.709
Nadav Mary: And then our gas zone vehicle will only have to complete its part, as we've said. And we'll do the same for the electric vehicle.

300
00:48:01.410 --> 00:48:06.249
Nadav Mary: Create a body report, and again, we don't need to call super anymore.

301
00:48:06.450 --> 00:48:19.039
Nadav Mary: And then we… when we run the program, we can see the exact structure that we wanted. We have the header, with the specific part of the vehicle, and then we'll have the footer with the ear.

302
00:48:19.730 --> 00:48:24.419
Nadav Mary: Perfect. And… yeah, let's go to the… back to the presentation.

303
00:48:25.980 --> 00:48:31.289
Nadav Mary: Yeah, so we just encountered what's called the cold super anti-pattern.

304
00:48:32.000 --> 00:48:34.430
Nadav Mary: So what is the cold superante pattern?

305
00:48:34.740 --> 00:48:41.200
Nadav Mary: Called super anti-pattern means when calling super becomes mandatory, when subclasses

306
00:48:41.210 --> 00:48:55.939
Nadav Mary: Must remember, as we've seen, calling super, otherwise our base functionality broke, because we didn't get a full report in our example. And as we've said, it also breaks the encapsulations, because subclasses

307
00:48:55.940 --> 00:49:04.909
Nadav Mary: could control the base behavior, and could, for example, not calling super, and then they could, control of how they report

308
00:49:04.920 --> 00:49:06.240
Nadav Mary: Will look like.

309
00:49:06.650 --> 00:49:20.430
Nadav Mary: And we've simplified that by using the template design pattern, which is a very strong and very good pattern for flexibility in our case. By the way, we could

310
00:49:20.700 --> 00:49:21.780
Nadav Mary: also…

311
00:49:21.910 --> 00:49:34.089
Nadav Mary: if we want even to make a more sophisticated template over here, so we can go ahead and create more abstract functions if we want to create a footer report, which is

312
00:49:34.090 --> 00:49:43.699
Nadav Mary: customed by the inheritors or anything else. We can do it as much as we want, using the template design pattern.

313
00:49:43.950 --> 00:49:58.690
Nadav Mary: And basically, what template design pattern gave us is encapsulating the structure in the base class, so we had the structure of our port in our vehicle.

314
00:49:58.830 --> 00:50:04.619
Nadav Mary: And we let the subclasses only fill their specific parts. In our case, it was the body.

315
00:50:05.040 --> 00:50:10.990
Nadav Mary: And we didn't need to call, to, to super anymore in the, in the subclasses.

316
00:50:11.780 --> 00:50:17.299
Nadav Mary: And the last thing is, when calling super actually becomes anti-pattern.

317
00:50:17.370 --> 00:50:21.290
Nadav Mary: So, in general, there's nothing wrong with a subclass.

318
00:50:21.330 --> 00:50:26.849
Nadav Mary: calling to, to, to super. It's something that,

319
00:50:26.880 --> 00:50:46.250
Nadav Mary: that the language is supporting, and specifically Python, and it's something that you can absolutely and you should use if it's something that you need. But when super becomes a requirement to your functionality, this is when it becomes an anti-pattern, because

320
00:50:46.250 --> 00:50:49.319
Nadav Mary: Calling super is not enforced by the language.

321
00:50:50.020 --> 00:51:01.270
Nadav Mary: And if it's not enforced by the language, so when you're not calling it, you're increasing the risk of mistakes, again, in case that calling super becomes a requirement.

322
00:51:03.440 --> 00:51:21.429
Nadav Mary: Basically, this is it from me, so we talked about… we talked about inheritance, and we talked about the download inheritance issue that we encountered, and we talked about composition, and we compared between inheritance and composition, and we just talked about the cold super anti-pattern.

323
00:51:21.430 --> 00:51:24.569
Nadav Mary: And we solved it using the template design pattern.

324
00:51:24.600 --> 00:51:36.160
Nadav Mary: But more importantly, I want to remind you the question that I asked you at the beginning. So, if AI writes code, do coding best practices still matter? So.

325
00:51:36.240 --> 00:51:49.269
Nadav Mary: I personally believe that coding best practices matter even more than before, because good code is not just code that works, it's code that is designed to evolve.

326
00:51:49.400 --> 00:51:59.070
Nadav Mary: Whether it's inheritance on composition or any other design pattern, the important part is not memorizing the rules. It's understanding when and why you should apply them.

327
00:51:59.100 --> 00:52:10.160
Nadav Mary: AI shifts our job from writing code into judging code. It becomes our assistant. And you cannot judge what you don't understand.

328
00:52:11.380 --> 00:52:15.489
Nadav Mary: That's it. Thank you so much. If you have any questions,

329
00:52:15.560 --> 00:52:35.260
Nadav Mary: I'll look at the chat now, and we can talk about it, and I shared over here my LinkedIn and my email, so you can just go ahead and connect me, and you can send me any message if you have questions afterwards, and I promise that I will answer all of your messages.

330
00:52:35.530 --> 00:52:36.380
Nadav Mary: Thank you.

331
00:52:37.860 --> 00:52:54.189
Gabor Szabo: Well, Nadav, thank you very much for this presentation. As I can see in the chat, there are no other questions, which is a little bit less surprising, because, like, 90% of the people here are from your workplace, so they are sparing the questions for later when they're going to meet you tomorrow.

332
00:52:54.190 --> 00:52:59.590
Gabor Szabo: But, still, if you have… if any of you have questions, then please ask now.

333
00:52:59.590 --> 00:53:04.250
Gabor Szabo: In the chat room,

334
00:53:05.200 --> 00:53:23.350
Gabor Szabo: I was wondering if I have any questions, but we can talk a little bit about the AI, actually, because you are sort of in the position, as I guess, that AI will write your code, and you will still accept the pull request from AI, or whatever way you integrate your code.

335
00:53:23.350 --> 00:53:26.699
Gabor Szabo: And at one point, you might need to read your code.

336
00:53:26.700 --> 00:53:42.710
Gabor Szabo: the code, that's sort of your assumption. As I understand, many people think that that's not going to be the case anymore, that we are just telling the AI to rewrite it, and rewrite it, and improve the

337
00:53:43.070 --> 00:53:48.339
Gabor Szabo: Features of the program without caring what is underneath.

338
00:53:54.200 --> 00:53:59.440
Gabor Szabo: I guess I was just talking, so I can give the opportunity for people to ask questions, but they don't…

339
00:53:59.440 --> 00:54:00.360
Nadav Mary: Yeah, yeah.

340
00:54:00.550 --> 00:54:12.060
Nadav Mary: Yeah, so I personally, see AI as my assistant, and not necessarily owning my engineering decisions.

341
00:54:12.130 --> 00:54:25.309
Nadav Mary: as you can see, it sped up my coding. If I had to write all the code by myself, it would probably take me, in the best case, twice then it took.

342
00:54:25.460 --> 00:54:36.180
Nadav Mary: But still, I'm the one who's responsible… responsible about the code, and I'm the one that's responsible to understand the feature.

343
00:54:36.650 --> 00:54:42.049
Nadav Mary: And the correctness, and understand the future of my product.

344
00:54:42.310 --> 00:54:48.689
Nadav Mary: And this is the reason that, again, coding best practices is important, and building,

345
00:54:49.540 --> 00:54:55.120
Nadav Mary: code in the right way is important, because if we'll not write

346
00:54:55.200 --> 00:55:10.149
Nadav Mary: the code in the correct way, we might deal and let, of course, AI deal with technical debts instead of going forward and building new features and new capabilities to our system.

347
00:55:10.270 --> 00:55:13.179
Nadav Mary: And so this is my two cents about that.

348
00:55:14.050 --> 00:55:20.460
Gabor Szabo: Yeah. By the way, just as a last note, it would be interesting to have a…

349
00:55:21.430 --> 00:55:29.399
Gabor Szabo: presentation, or a series of presentations, or a series of people presenting, how each one of them is using AI to write code.

350
00:55:29.580 --> 00:55:48.060
Gabor Szabo: what are the types of the ways of people? It's just a side note to you, and to all the people here who are here, and all the people watching the video. As I see, there are no questions, so just let me thank you, say thanks again for the presentation.

351
00:55:48.060 --> 00:56:00.540
Gabor Szabo: And for all the people who… Thank you. …who were here, and if you're watching the video, then remember to like the video, and follow the channel, and below the video, you will find links to,

352
00:56:00.540 --> 00:56:11.420
Gabor Szabo: the contact information of Nadav, so you won't have to copy it from the screen. And if you are here, the people who are here, feel free to stay

353
00:56:11.530 --> 00:56:25.979
Gabor Szabo: after the recording is stopped, and we can continue speaking, even though I know that most of you can meet him. You're going to meet tomorrow in the office, but those few people, especially those few people who are not.

354
00:56:26.020 --> 00:56:32.729
Gabor Szabo: You're welcome to stay and chat a little bit more. Thank you very much again, and goodbye!

355
00:56:33.160 --> 00:56:34.040
Nadav Mary: Thank you.



