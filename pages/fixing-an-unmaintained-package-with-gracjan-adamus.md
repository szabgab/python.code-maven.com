---
title: Fixing an unmaintained package, spanning Python, C++, nanobind and Github Actions
timestamp: 2026-08-25T10:30:01
author:
published: true
description:
tags:
---

## DESCRIPTION

[nanobind](https://github.com/wjakob/nanobind) is the official successor to the widely used [pybind11](https://pybind11.readthedocs.io/) library, allowing you to quickly create seamless and maintainable Python bindings for C++ code.

For pybind11, an extension called [pybind11_json](https://github.com/pybind/pybind11_json) was developed to easily pass JSON objects between Python and C++. This package has been used in an open-source project that I contribute to. However, when we decided to migrate to nanobind, we discovered a major issue: the nanobind equivalent - which is even linked directly from the pybind11_json README - did not work at all. 

In this talk, I will share the fun (and not-so-fun) parts of my journey to fix this package. I'll go over what pybind11 is and how nanobind improves it. I'll provide a brief overview of the open-source project I was working on, and explain why we needed JSON interoperability. From there, I’ll dive into the specific bugs, quirks, and issues I encountered while resurrecting nanobind_json. Throughout the whole talk I will showcase necessary examples and code snippets.

## BIO

[Gracjan Adamus](https://www.linkedin.com/in/gracjan-adamus/) is an Applied Computer Science student at AGH University of Kraków. His main interests span GPUs, High-Performance Computing, and open-source software. He is a former Summer Student at the Paul Scherrer Institute and a current Summer Student at CERN. Griger5 @ Github.

{% youtube id="etxnKZVYi1s" file="2026-08-24-fixing-an-unmaintained-package-with-gracjan-adamus.mp4" %}

## Useful links
nanobind_json project repo: https://github.com/Griger5/nanobind_json
nanobind project repo: https://github.com/wjakob/nanobind
nanobind docs: https://nanobind.readthedocs.io/en/latest/
PyPartMC repo: https://github.com/open-atmos/PyPartMC
PyPartMC SoftwareX paper: https://doi.org/10.1016/j.softx.2023.101613

## Transcript

1
00:00:01.730 --> 00:00:22.780
Gabor Szabo: So, hello and welcome to the Code Maven session, or Code Maven channel, or also called the Python Maven session. So, the Code Maven is the general name of this channel and the meetings, and this is the Python subsection, let's say it, let's call it that way. My name is Gabor Szabo, I…

2
00:00:22.780 --> 00:00:42.729
Gabor Szabo: organize these sessions. I usually help companies with development practices. Recently, I started to offer DevRel services to companies, and I also do training, and I'm really happy that you are here, Gracian, for this presentation. I hope I pronounced your name correctly, and if not, then please…

3
00:00:43.400 --> 00:00:58.499
Gabor Szabo: say properly, I would like to give you the option to introduce yourself, tell you about yourself, whatever, give the presentation. As I mentioned, all the people who are here present.

4
00:00:58.820 --> 00:01:11.720
Gabor Szabo: during this session, you're free to ask questions in the chat room. I will try to ask these questions, and I didn't even ask you earlier how long we can expect this presentation to be.

5
00:01:12.520 --> 00:01:21.549
Gracjan Adamus: I think it should not take more than an hour. I would say that maybe 50 minutes, maybe 40, we will see.

6
00:01:21.550 --> 00:01:24.890
Gabor Szabo: Okay, so go ahead, the stage is yours.

7
00:01:25.690 --> 00:01:36.849
Gracjan Adamus: Okay, thank you. Then I will just share my screen, and I have some slides on an introduction about me in a second. First of all, thank you all for joining, and also for inviting me here.

8
00:01:37.160 --> 00:01:50.320
Gracjan Adamus: Today, I'm gonna give a talk about my journey of fixing an unmaintained package, where I, let's say, battled with Python, with C++, Nanobind, and also with GitHub Actions.

9
00:01:50.930 --> 00:01:54.749
Gracjan Adamus: And a small, introduction of me.

10
00:01:54.940 --> 00:02:12.349
Gracjan Adamus: I completed my third year of applied computer science at AGH University of Krakow. I still have one semester left in my bachelor of Studies. I am also the current president of a student scientific club of computer science students at my faculty.

11
00:02:12.630 --> 00:02:24.070
Gracjan Adamus: Last year, I was a summer intern at the Pulcher Institute in Switzerland. This year, I'm a summer student at CERN, and I'm also speaking to you from near Geneva.

12
00:02:24.340 --> 00:02:33.109
Gracjan Adamus: I also worked as a C++ developer, I really liked Moshe, and this picture is what I have on my GitHub as my profile picture.

13
00:02:33.420 --> 00:02:39.179
Gracjan Adamus: I am interested in high-performance computing, GPUs, and all the stuff around it.

14
00:02:39.530 --> 00:02:42.830
Gracjan Adamus: And you can find me on GitHub as Grieger5.

15
00:02:43.160 --> 00:02:46.179
Gracjan Adamus: And I can also mention that for today's talk.

16
00:02:46.350 --> 00:02:53.790
Gracjan Adamus: We will first go through what PyBind11 and NanoBind is, because I will assume that you probably don't know it.

17
00:02:54.380 --> 00:02:58.559
Gracjan Adamus: then I will say, how I got into

18
00:02:58.800 --> 00:03:05.729
Gracjan Adamus: let's say this mess that I had to fix, what kind of project I was making when I,

19
00:03:06.220 --> 00:03:08.620
Gracjan Adamus: came into Denver by JSON stuff.

20
00:03:08.910 --> 00:03:17.410
Gracjan Adamus: And also, at the end, I decided to add a small section on, let's say, a crash course on how to use NanoByte.

21
00:03:17.720 --> 00:03:22.980
Gracjan Adamus: So, let's get started. First, what event is Pinebind11?

22
00:03:23.120 --> 00:03:29.959
Gracjan Adamus: It was created by an associate professor at EPFL called Winsler Jacob. I hope I pronounced it right.

23
00:03:30.200 --> 00:03:39.159
Gracjan Adamus: And it was a header-only library for C++. That exposes the C++ types to Python and vice versa.

24
00:03:39.570 --> 00:03:45.410
Gracjan Adamus: And it is a very convenient wrapper over the typical Python CRP.

25
00:03:46.100 --> 00:03:50.120
Gracjan Adamus: And it has very minimal boilerplate, which we will see later.

26
00:03:51.190 --> 00:04:07.739
Gracjan Adamus: For example, here, you have a comparison between PyByte 11 and another binding library from the Boost organization, and you can see that the file sizes and compilation time are very, very close to each other.

27
00:04:07.750 --> 00:04:20.869
Gracjan Adamus: So, it is not worse, let's say. I think that the smaller the score on the graph, the better, so it is even better than Boost Python, and is very nice to work with.

28
00:04:21.490 --> 00:04:29.670
Gracjan Adamus: And you may ask, does anyone actually use PyBank 11? And yes, quite a lot of people.

29
00:04:29.670 --> 00:04:45.520
Gracjan Adamus: pretty much every major machine learning library is based on PyMind 11, because obviously the computing backend that has to be high performance is written in C++, or CUDA, or something like that, and then Pinebite 11 is used to

30
00:04:45.860 --> 00:04:56.680
Gracjan Adamus: bring that power to Python. You can also find it in Scikit, OpenCV, so image processing library, again, the performance is needed there.

31
00:04:56.850 --> 00:05:02.350
Gracjan Adamus: also just in SciPy, or those two is used in robotics.

32
00:05:03.940 --> 00:05:10.490
Gracjan Adamus: And to give you a comparison of what this minimal boilerplate means.

33
00:05:11.520 --> 00:05:19.520
Gracjan Adamus: Let's say you have a function in C or C++ that just sorts an array. Here, I think it is insertion sort.

34
00:05:19.740 --> 00:05:29.230
Gracjan Adamus: And, well, it's written in C, so it is rather fast, especially compared to knife implementation in Python. So, maybe you would like to use it from Python.

35
00:05:29.710 --> 00:05:37.590
Gracjan Adamus: And if you wanted to do that with the python.edge API, it takes a lot of code, as you can see.

36
00:05:37.830 --> 00:05:43.909
Gracjan Adamus: And you have to do manual parsing of the arguments, go through all of the…

37
00:05:44.110 --> 00:05:46.399
Gracjan Adamus: shoot a whole array.

38
00:05:46.990 --> 00:06:00.239
Gracjan Adamus: You have to then call this function, then again, one after another, assign it to the result. You also have to create the methods, the module, init the module.

39
00:06:00.390 --> 00:06:08.630
Gracjan Adamus: In general, you can see that it's a very, very easy function, and also just one function, and there's already a lot stuff to do.

40
00:06:09.440 --> 00:06:22.220
Gracjan Adamus: With pipend 11, that's all the code you need. Here, I assume that you will use something like a vector, and not just a array, but you can just call the sortC function, and it works.

41
00:06:22.330 --> 00:06:29.249
Gracjan Adamus: And then, from the Department 11 side, that's basically a one-liner to define it.

42
00:06:29.380 --> 00:06:36.049
Gracjan Adamus: And you can also see that Paramount 11 actually infers the types of your functions.

43
00:06:36.160 --> 00:06:43.410
Gracjan Adamus: itself, by clever template metaprogramming. It is a really marvelous piece of code, I have to say.

44
00:06:44.610 --> 00:06:46.690
Gracjan Adamus: But now, what is NanoBind?

45
00:06:46.940 --> 00:06:57.409
Gracjan Adamus: It is also created by the same person, and it was intended to be a successor to PineByte 11. It fully utilizes modern C++ features.

46
00:06:57.650 --> 00:07:03.820
Gracjan Adamus: It compiles much faster, it has smaller binary sizes, and a lower runtime overhead.

47
00:07:04.220 --> 00:07:08.319
Gracjan Adamus: It has a very similar API with some differences that we'll discuss.

48
00:07:08.800 --> 00:07:19.619
Gracjan Adamus: And it was also built on top of a lot of feedback and lessons learned from development of PiMet11, which was also a multi-year effort.

49
00:07:20.780 --> 00:07:24.720
Gracjan Adamus: Here's a comparison from the NanoBind documentation itself.

50
00:07:25.070 --> 00:07:36.060
Gracjan Adamus: Here to explain it, the func under a graph means that it was a function-heavy module, so think of hundreds of functions.

51
00:07:36.160 --> 00:07:42.219
Gracjan Adamus: And class means it was a class-heavy module, so think of hundreds of classes.

52
00:07:42.480 --> 00:08:02.439
Gracjan Adamus: And so, basically, we compare how long it takes to compile, and how big the resultant binary is. And you can see that, in this case, NanoBind basically declassifies everything, it has huge improvements compared to PyBind11, and it fares very, very good compared to Cyton or Boost Python.

53
00:08:04.230 --> 00:08:07.140
Gracjan Adamus: A runtime performance is also compared.

54
00:08:07.380 --> 00:08:24.659
Gracjan Adamus: here you can see that Nanobind actually loses to Cyton when it's a class-heavy module, but it is still better in the function one, and you can also see a huge improvement compared to PyBind 11 when it comes to the class-heavy modules. It's 10 times faster

55
00:08:24.780 --> 00:08:33.240
Gracjan Adamus: at runtime. Obviously, it is not some super huge overhead, but sometimes it will count.

56
00:08:33.750 --> 00:08:49.850
Gracjan Adamus: And you may also wonder, okay, nanobind is cool and all, but are people actually using it and switching to it? And yes, I know of one example. It's JAX from Google. It is a, let's say, machine learning library…

57
00:08:49.990 --> 00:09:02.559
Gracjan Adamus: for accelerated computing that, with one code, enables you to run it on CPUs and GPUs. I think they also mentioned TPUs, but I didn't have the privilege to test it.

58
00:09:02.700 --> 00:09:10.650
Gracjan Adamus: But they started with PowerBend11 and are in the process of switching to Nanobind. So, yes, that is actually happening.

59
00:09:11.810 --> 00:09:16.590
Gracjan Adamus: And now, what is Pimat-relevant JSON, which will be important?

60
00:09:17.090 --> 00:09:31.009
Gracjan Adamus: It is also a header-only library that bridges PyBet11 and Nortman JSON, which, if you don't know, I think it is the most popular C++ library for handling JSON objects.

61
00:09:31.790 --> 00:09:41.039
Gracjan Adamus: It enables automatic conversion between the C++ JSONs to native Python types, like dictionaries, lists, and others.

62
00:09:41.160 --> 00:09:47.590
Gracjan Adamus: And you just have to include one header, and it will work. You don't have to do any other manual work.

63
00:09:48.120 --> 00:09:57.800
Gracjan Adamus: And to give you the example, here you have some functions that takes and returns a JSON structure in C++.

64
00:09:57.930 --> 00:09:59.660
Gracjan Adamus: And there's something to it.

65
00:09:59.890 --> 00:10:06.899
Gracjan Adamus: And we define it in the Pirate 11 module the same way as we do a regular function.

66
00:10:07.020 --> 00:10:09.680
Gracjan Adamus: And it just works in Python.

67
00:10:11.170 --> 00:10:12.719
Gracjan Adamus: So, that's cool.

68
00:10:12.900 --> 00:10:16.780
Gracjan Adamus: That it's so easy. You just drop the header, and it works.

69
00:10:17.680 --> 00:10:21.079
Gracjan Adamus: And does anyone use BibreLab and JSON?

70
00:10:21.430 --> 00:10:27.380
Gracjan Adamus: Well… Yes, but it's certainly not used as widely as Bireend11 itself.

71
00:10:27.620 --> 00:10:34.559
Gracjan Adamus: It is used, for example, by Zeus Python, which is an alternative kernel for the Jupyter notebooks.

72
00:10:34.920 --> 00:10:43.529
Gracjan Adamus: It's also used in the robot operating system, which is, as I said, a package for robotics.

73
00:10:44.030 --> 00:10:54.180
Gracjan Adamus: And it's also used in PipartMC, and I contribute to PipardMC, and that's how I actually came into contact with the PyBite 11 and JSON stuff.

74
00:10:55.280 --> 00:10:58.640
Gracjan Adamus: So, a quick note on paper DNC.

75
00:10:58.990 --> 00:11:08.640
Gracjan Adamus: It's a wrapper for another package that is used for atmospheric aerosol simulation through Monte Carlo simulations.

76
00:11:09.160 --> 00:11:17.880
Gracjan Adamus: It has been developed at the University of Illinois Urbana-Champaign in USA, and AGH University of Krakow here in Poland.

77
00:11:18.290 --> 00:11:23.640
Gracjan Adamus: It has 4 languages in the codebase, those being C, C++, Fortune, and Python.

78
00:11:23.790 --> 00:11:28.839
Gracjan Adamus: It's available on… all, popular platforms.

79
00:11:29.110 --> 00:11:36.770
Gracjan Adamus: And under the hood, it uses PyMite 11 JSON to, let's say, provide a more Pythonic experience.

80
00:11:37.160 --> 00:11:44.530
Gracjan Adamus: Because PartMC itself was intended to be run as a library, to which we would then give

81
00:11:44.640 --> 00:12:00.409
Gracjan Adamus: let's say something akin to configuration files, and so for one simulation, you would have many files and the executable somewhere else, and so with PipartMC, you have this more library approach, and you have everything in code, so…

82
00:12:01.660 --> 00:12:06.189
Gracjan Adamus: It is somewhat, let's say, cleaner, more Pytonic, more maintainable.

83
00:12:07.080 --> 00:12:18.470
Gracjan Adamus: And at some point, we decided to switch to Nanobind, and it was mostly my work, and I can also say that it was a success, and we saw a 4x speedup in the compilation.

84
00:12:19.910 --> 00:12:24.539
Gracjan Adamus: But the switching was not, let's say, a one-day effort.

85
00:12:25.790 --> 00:12:33.780
Gracjan Adamus: Switching just the PyBet 11 code to NanoByte was rather simple, because, as I said, the API is very similar.

86
00:12:34.190 --> 00:12:37.599
Gracjan Adamus: But we needed the alternative to PyMAT11 JSON.

87
00:12:38.290 --> 00:12:46.239
Gracjan Adamus: But, well, it existed. We looked into the repository of 5.11 JSON, and we saw it linked. Great, let's try it.

88
00:12:47.050 --> 00:12:53.890
Gracjan Adamus: But, when we run it, we run into a small error that, it cannot find

89
00:12:54.520 --> 00:12:58.689
Gracjan Adamus: A header for nanobind is not found in the nanobind JSON.

90
00:12:58.940 --> 00:13:13.009
Gracjan Adamus: I looked in the NanoBind repository, and I see that, okay, they changed the header from .hp to .h. So, I just change that, and it should work, right?

91
00:13:14.060 --> 00:13:16.389
Gracjan Adamus: Well, it did not.

92
00:13:16.520 --> 00:13:22.449
Gracjan Adamus: And there were more than 400 lines of very long C++ errors.

93
00:13:23.950 --> 00:13:28.559
Gracjan Adamus: So, I decided to maybe get in touch with the maintainer and mention an issue.

94
00:13:29.100 --> 00:13:38.989
Gracjan Adamus: But unfortunately, on his GitHub, I saw that he just said that his account and his repositories are no longer maintained.

95
00:13:39.320 --> 00:13:44.649
Gracjan Adamus: I think I was doing it sometime after the January 10th, probably, like.

96
00:13:44.900 --> 00:13:51.930
Gracjan Adamus: a couple months. And I tried to contact him on LinkedIn, but unfortunately, I also had no luck there.

97
00:13:52.250 --> 00:13:54.850
Gracjan Adamus: So, I decided to fix it myself.

98
00:13:55.930 --> 00:13:59.349
Gracjan Adamus: And my… let's say, main…

99
00:13:59.920 --> 00:14:03.860
Gracjan Adamus: A course of action was reading one of the errors.

100
00:14:04.390 --> 00:14:08.760
Gracjan Adamus: Which was usually, usually something, something was not found.

101
00:14:09.190 --> 00:14:17.449
Gracjan Adamus: Then I would look through the documentation for both PyMet11 and Nanobind, and see what that was, what it is called now in Nanobind.

102
00:14:17.990 --> 00:14:24.649
Gracjan Adamus: Then change, like, one line, recompile, and hopefully there would be one error less.

103
00:14:25.810 --> 00:14:32.990
Gracjan Adamus: And to give you a couple of examples, for example, in PyBind 11, there was something called Cast.

104
00:14:33.100 --> 00:14:36.379
Gracjan Adamus: And it was a member of the

105
00:14:36.780 --> 00:14:53.489
Gracjan Adamus: most basic class for which all of the Apartment 11 objects then derive, which, as you can see, just holds a reference to a Python object, and it isn't even reference scouting. So it's their very, very basic base class.

106
00:14:53.600 --> 00:15:02.560
Gracjan Adamus: And it was a method in there. So, whenever you wanted to cast a pyramid 11 object to something, you called that method on this object.

107
00:15:02.900 --> 00:15:17.750
Gracjan Adamus: However, in Nanobind, it was changed, and it's a standalone function, to which you, give the object as an argument. So, for example, in every place when there was a custom, I just had to fix this line.

108
00:15:19.940 --> 00:15:23.839
Gracjan Adamus: Another example are functions called load and cast.

109
00:15:23.950 --> 00:15:34.570
Gracjan Adamus: And, that's funny, because discuss and the previous one are completely different functions, and from these names, you probably don't really know

110
00:15:34.750 --> 00:15:40.690
Gracjan Adamus: what… what they do. And even if I show you this, you might not be fully aware.

111
00:15:41.550 --> 00:15:47.670
Gracjan Adamus: But if I show you this… oh, I see, I forgot to change, this part of code.

112
00:15:48.730 --> 00:15:49.610
Gracjan Adamus: Yes.

113
00:15:49.740 --> 00:16:01.420
Gracjan Adamus: But here, on the left, you have the apartment 11 version, on the right, you have the nanobind version, and as you can see, the name is much clearer on the nanobind side, because

114
00:16:01.420 --> 00:16:13.489
Gracjan Adamus: What those functions do is convert an object from Python to the C++, let's say, equivalent, and from C++ to Python equivalent.

115
00:16:13.770 --> 00:16:21.549
Gracjan Adamus: And they are defined in objects called typecasters, Each type has one.

116
00:16:21.750 --> 00:16:34.260
Gracjan Adamus: And they are what is doing the actual casting. And we will see that you can create your own typecaster, and I will show an example of how you can write those two functions.

117
00:16:36.430 --> 00:16:40.709
Gracjan Adamus: To provide, casting for different types.

118
00:16:41.380 --> 00:16:45.370
Gracjan Adamus: And as you can see, the changes are also…

119
00:16:45.490 --> 00:17:00.360
Gracjan Adamus: let's say, in the naming, so that it is more clear what something is actually done. I'm sure that there was probably a lot of confusion with the load and cast, and the second cast, and that was also one of the lessons that we learned from pipe end 11.

120
00:17:01.720 --> 00:17:06.500
Gracjan Adamus: But there were also a couple of other problems, for example, circular references.

121
00:17:07.140 --> 00:17:10.800
Gracjan Adamus: This is a test from, PipartMC.

122
00:17:11.140 --> 00:17:17.789
Gracjan Adamus: Where we basically, make sure that a runtime error will be erased.

123
00:17:18.150 --> 00:17:24.610
Gracjan Adamus: When there is a circular reference in the… Object in the dictionary.

124
00:17:26.400 --> 00:17:31.839
Gracjan Adamus: And thankfully, in PyBind 11 JSON, they already did that.

125
00:17:33.200 --> 00:17:38.830
Gracjan Adamus: And so, I basically just copied their solution to NanoBind JSON.

126
00:17:40.090 --> 00:17:55.959
Gracjan Adamus: Basically, a helper function for converting the Python objects to JSONs gets another argument, which is a set of references to pi objects. So, pi object is from the,

127
00:17:56.480 --> 00:17:59.490
Gracjan Adamus: fundamentalpython.h CRP.

128
00:18:01.020 --> 00:18:08.420
Gracjan Adamus: And so, basically, whenever we are iterating over a list, or over a dictionary, we insert

129
00:18:09.620 --> 00:18:12.630
Gracjan Adamus: That object to the set.

130
00:18:12.740 --> 00:18:16.200
Gracjan Adamus: And we check if it wasn't in the set previously.

131
00:18:16.620 --> 00:18:32.970
Gracjan Adamus: And at the end, after we iterate over everything, we then erase it, because otherwise we would just also throw exception on the same object being twice in a list, and not that the list itself is self-referencing.

132
00:18:33.590 --> 00:18:38.379
Gracjan Adamus: So, that was also a pretty okay fix, because it was already done before.

133
00:18:39.350 --> 00:18:47.459
Gracjan Adamus: So, wow, everything actually works! Piperte MC compiled, all tests were passing.

134
00:18:47.680 --> 00:18:52.510
Gracjan Adamus: So I decided to fork NanoByte JSON and add those changes.

135
00:18:56.030 --> 00:18:57.420
Gracjan Adamus: So, time to fork!

136
00:18:58.200 --> 00:19:01.120
Gracjan Adamus: I go to the NanoBind.json repository.

137
00:19:01.860 --> 00:19:04.700
Gracjan Adamus: And I see that there is already one pull request.

138
00:19:06.620 --> 00:19:13.479
Gracjan Adamus: And it turns out that somebody already fixed all the stuff that I just mentioned.

139
00:19:13.640 --> 00:19:20.619
Gracjan Adamus: or most of the stuff that I just mentioned, and I didn't have to spend so much time on it.

140
00:19:21.890 --> 00:19:25.709
Gracjan Adamus: So, well, now I have the plan. I create the fork.

141
00:19:25.910 --> 00:19:31.799
Gracjan Adamus: And I add the temporary branch with what I already did, just so Piper.mC is working.

142
00:19:32.270 --> 00:19:41.300
Gracjan Adamus: Then I will merge the PR that is already on the original repo, so that we give credit where credit is due, because they did it faster.

143
00:19:41.850 --> 00:19:47.889
Gracjan Adamus: I will adjust it where necessary, because, for example, they didn't handle the circular references.

144
00:19:48.750 --> 00:19:58.010
Gracjan Adamus: I wanted also to write the tests that would cover the same or at least similar scope as the ones in the Department 11 JSON.

145
00:19:58.570 --> 00:20:03.290
Gracjan Adamus: and also add the CI workflow for testing also on different platforms.

146
00:20:04.870 --> 00:20:08.140
Gracjan Adamus: But with the tests, there was a problem.

147
00:20:08.360 --> 00:20:12.279
Gracjan Adamus: There is no embedded interpreter in Nanobyte.

148
00:20:13.050 --> 00:20:16.999
Gracjan Adamus: And to give you an example of what that means.

149
00:20:17.320 --> 00:20:26.880
Gracjan Adamus: Though this is a test from PowerMet11 JSON, and you can see that a scoped interpreter is constructed

150
00:20:28.300 --> 00:20:36.290
Gracjan Adamus: And basically, what PyMet1 allows you to do is actually run an interpreter inside your C++ code.

151
00:20:36.550 --> 00:20:47.540
Gracjan Adamus: And, for example, the line below it, creating a pipeline boot object, was actually going through this interpreter and creating an actual Python object.

152
00:20:48.920 --> 00:21:08.079
Gracjan Adamus: But this feature was deleted from NanoBind, because from the name, you can tell that they want to keep things nano, and get rid of a lot of the bloat. That's also why it's a bit faster, smaller binary sizes. Basically, this was cut off fully intentionally.

153
00:21:08.620 --> 00:21:12.310
Gracjan Adamus: But without it, we can't write the test.

154
00:21:12.450 --> 00:21:15.890
Gracjan Adamus: the same way as they did in PowerPoint 11 JSON.

155
00:21:17.590 --> 00:21:25.909
Gracjan Adamus: Oh yes, this is what I mentioned, that it has been debited and will not be added in the future.

156
00:21:26.850 --> 00:21:35.540
Gracjan Adamus: So, I looked at how NanoBind itself handles testing, and I saw that basically for every kind of test.

157
00:21:35.700 --> 00:21:38.770
Gracjan Adamus: They have a C++ file and a Python file.

158
00:21:39.160 --> 00:21:49.549
Gracjan Adamus: And in the C++ one, they will define some variable, some test function, a function to test, that will also do some checks on its side.

159
00:21:50.050 --> 00:22:04.069
Gracjan Adamus: And also, on the Python side, with PyTest, there will be some kind of test that will also do some checks on the Python side. And so, basically, both sides of code are covered, both languages are covered.

160
00:22:05.100 --> 00:22:11.030
Gracjan Adamus: So I did the same, and wrote the first test with a simple Boolean.

161
00:22:11.800 --> 00:22:26.440
Gracjan Adamus: So I just sent false from C++, and also I assume that I will get false from Python, and on the Python side, it is also very easy. I do two asserts, I send false, should work, right?

162
00:22:27.780 --> 00:22:29.030
Gracjan Adamus: Well, it didn't.

163
00:22:29.320 --> 00:22:39.840
Gracjan Adamus: I mean, sending from JSON, so the test where I send something from C++ works, but the one that receives it from Python does not.

164
00:22:40.780 --> 00:22:44.130
Gracjan Adamus: So, I did a quick debugging.

165
00:22:45.180 --> 00:22:50.869
Gracjan Adamus: Let's check which branch does it enter, and where it actually fails.

166
00:22:52.250 --> 00:22:53.680
Gracjan Adamus: It's not Boolean.

167
00:22:53.980 --> 00:22:58.130
Gracjan Adamus: Okay, so it is… it isn't even a Boolean.

168
00:22:58.680 --> 00:23:03.180
Gracjan Adamus: Well, then let's just dump this JSON and check what is inside.

169
00:23:06.610 --> 00:23:07.730
Gracjan Adamus: Null.

170
00:23:08.210 --> 00:23:10.099
Gracjan Adamus: There is nothing inside.

171
00:23:10.720 --> 00:23:12.910
Gracjan Adamus: And that got me thinking.

172
00:23:13.040 --> 00:23:17.060
Gracjan Adamus: what's going on? Because only that from Python fails.

173
00:23:18.690 --> 00:23:21.490
Gracjan Adamus: BipartMC works fine with my code.

174
00:23:21.600 --> 00:23:25.810
Gracjan Adamus: Even though it sends a lot of JSONs from Python to C++.

175
00:23:26.370 --> 00:23:30.349
Gracjan Adamus: I got null instead of bull, like, there's no object.

176
00:23:31.040 --> 00:23:43.049
Gracjan Adamus: And I also tried to send dictionaries and lists, which are, let's say, more akin to the typical JSON schema, because I thought that maybe just sending a pure bull

177
00:23:43.580 --> 00:23:46.360
Gracjan Adamus: Has something to do with it, but no, they also failed.

178
00:23:46.980 --> 00:23:48.879
Gracjan Adamus: So, what was wrong?

179
00:23:49.670 --> 00:23:58.909
Gracjan Adamus: And then I remembered that PipartMC uses the different branch with my, let's say, quick, improvised changes.

180
00:23:59.120 --> 00:24:03.980
Gracjan Adamus: But here, I am working on the version merge from that other pull request.

181
00:24:05.120 --> 00:24:10.939
Gracjan Adamus: So I started really digging into the code, and trust me, it took me a lot of time.

182
00:24:11.390 --> 00:24:17.259
Gracjan Adamus: I think it was… Multiple hours, for sure.

183
00:24:19.060 --> 00:24:21.529
Gracjan Adamus: But finally, I found the culprit.

184
00:24:23.050 --> 00:24:35.020
Gracjan Adamus: It was in this part of the code. And trust me, I basically went line by line, comparing those two versions, the working one and the crushy one, to find it.

185
00:24:36.230 --> 00:24:43.110
Gracjan Adamus: And, if you think about it, you might see it already where it is, but I will show you.

186
00:24:43.500 --> 00:24:44.529
Gracjan Adamus: It's this.

187
00:24:45.530 --> 00:24:51.310
Gracjan Adamus: As I mentioned before, from Python is a method inside the Typecaster object.

188
00:24:51.960 --> 00:24:55.830
Gracjan Adamus: And, if you look at this code, Basically.

189
00:24:56.360 --> 00:25:03.680
Gracjan Adamus: no information, no object leaves this function other than the returned Boolean.

190
00:25:04.570 --> 00:25:05.660
Gracjan Adamus: Because…

191
00:25:06.080 --> 00:25:15.790
Gracjan Adamus: It should be like this. You should assign to value, which is already defined in this structure as this value field.

192
00:25:16.450 --> 00:25:31.699
Gracjan Adamus: But if we do auto-value, we create a variable with the same name, and because of that, we won't write anything to the actual member field that we want, so when it is read in the future.

193
00:25:31.710 --> 00:25:38.730
Gracjan Adamus: It is null, because we never wrote anything to it, we just assigned to a temporary variable in this function.

194
00:25:39.040 --> 00:25:39.930
Gracjan Adamus: So…

195
00:25:40.760 --> 00:25:52.059
Gracjan Adamus: don't name the variables the same way, or use this, or self, if you're doing it in Python, to avoid errors like this, please. It took me a while.

196
00:25:53.320 --> 00:26:04.360
Gracjan Adamus: But okay, that was working, tests were passing, I wrote the test, as I said, for basically everything, so let's add the CI on GitHub Actions.

197
00:26:05.000 --> 00:26:07.910
Gracjan Adamus: It's a very simple workflow.

198
00:26:08.100 --> 00:26:14.050
Gracjan Adamus: We set up the Python, install PyTest, We configure and build it.

199
00:26:14.050 --> 00:26:16.209
Gabor Szabo: Gracian, Gracian, there is a question here now.

200
00:26:16.210 --> 00:26:17.199
Gracjan Adamus: Yes, yes.

201
00:26:17.200 --> 00:26:21.370
Gabor Szabo: Sorry, did GCC not warn about the name shadowing?

202
00:26:23.370 --> 00:26:24.670
Gracjan Adamus: Ehhh…

203
00:26:25.600 --> 00:26:34.809
Gracjan Adamus: I am not sure, probably if I compiled it with debug flags, then it would show up, but I didn't, because

204
00:26:35.020 --> 00:26:43.770
Gracjan Adamus: I thought that, it's gonna be simpler than that, but then you're a couple hours deep, but yes, that's also,

205
00:26:44.800 --> 00:26:50.800
Gracjan Adamus: a lesson learned for me, that I should always have all debug flags on, yes.

206
00:26:51.740 --> 00:26:53.950
Gracjan Adamus: And warning flags, yes, yes.

207
00:26:57.290 --> 00:27:01.029
Gracjan Adamus: Yes, so where I was, yes, build it with CMake.

208
00:27:01.350 --> 00:27:04.370
Gracjan Adamus: And just run the test with bytest.

209
00:27:05.190 --> 00:27:11.679
Gracjan Adamus: But it wasn't that easy, and I had really several, tries.

210
00:27:11.910 --> 00:27:14.289
Gracjan Adamus: And, tries and errors.

211
00:27:14.920 --> 00:27:18.960
Gracjan Adamus: And it took me 59 commits to get it working.

212
00:27:19.860 --> 00:27:23.519
Gracjan Adamus: So, let's look at some of the failing workflow runs.

213
00:27:24.590 --> 00:27:30.269
Gracjan Adamus: Well, unfortunately, it was a long time ago, and GitHub deletes them.

214
00:27:31.350 --> 00:27:35.890
Gracjan Adamus: So I had to do some reverse engineering.

215
00:27:36.370 --> 00:27:39.689
Gracjan Adamus: To remember what the issue was.

216
00:27:40.470 --> 00:27:43.689
Gracjan Adamus: So, at some point, I got to this.

217
00:27:43.890 --> 00:27:53.039
Gracjan Adamus: that Ubuntu was working correctly, macOS was also passing, but the Windows builds would fail.

218
00:27:53.920 --> 00:27:56.660
Gracjan Adamus: And what were the problems?

219
00:27:56.910 --> 00:28:00.840
Gracjan Adamus: In general, there were also just YAML syntax problems.

220
00:28:01.080 --> 00:28:11.040
Gracjan Adamus: there were also wrong paths, specifically of Windows, because it builds in a different, in a different place.

221
00:28:11.400 --> 00:28:15.690
Gracjan Adamus: I also screwed up installations, in some…

222
00:28:16.080 --> 00:28:19.170
Gracjan Adamus: places, and the Python package was not found.

223
00:28:20.370 --> 00:28:27.209
Gracjan Adamus: But most of the time, most of my time was wasted on this, on Windows.

224
00:28:27.790 --> 00:28:33.470
Gracjan Adamus: Oh, no, sorry, it was also on… it was on every version, sorry, sorry.

225
00:28:33.610 --> 00:28:37.120
Gracjan Adamus: Yes, on Ubuntu, it was…

226
00:28:37.220 --> 00:28:50.940
Gracjan Adamus: undefined symbol error for a PI object vector call. So from this, I already see that it is also something from the python.h… library.

227
00:28:52.390 --> 00:29:04.070
Gracjan Adamus: that something is missing, there must be some mismatch, because, well, it should exist. And you can also see that the newer Python versions actually passed, and only the older ones failed.

228
00:29:04.870 --> 00:29:07.349
Gracjan Adamus: On macOS, everything passed.

229
00:29:07.500 --> 00:29:10.630
Gracjan Adamus: And there was also an error of symbol not found.

230
00:29:10.980 --> 00:29:17.050
Gracjan Adamus: And I also see that it is also from the typical CIP.

231
00:29:18.190 --> 00:29:22.749
Gracjan Adamus: And on Windows, Only the newest Python failed.

232
00:29:22.970 --> 00:29:29.690
Gracjan Adamus: And it was an import error that a dynamically linked library could not be loaded.

233
00:29:30.140 --> 00:29:39.210
Gracjan Adamus: So, on every system, I had a slightly different error, because it was also compiled with a slightly different compiler, the typical for the OS.

234
00:29:39.820 --> 00:29:42.889
Gracjan Adamus: And I had to spend a lot of time debugging that.

235
00:29:43.790 --> 00:29:47.850
Gracjan Adamus: But finally, I found the issue.

236
00:29:48.830 --> 00:29:50.970
Gracjan Adamus: And it was here.

237
00:29:51.490 --> 00:29:55.640
Gabor Szabo: Wait a second, there's another question, though I think I can answer, but did you.

238
00:29:55.640 --> 00:29:56.650
Gracjan Adamus: Yes, yes.

239
00:29:56.650 --> 00:30:05.320
Gabor Szabo: Did you use GitHub Action to test on various systems? Okay, I'm not sure I understand. Various operating systems, right.

240
00:30:05.880 --> 00:30:08.010
Gracjan Adamus: Yes,

241
00:30:08.290 --> 00:30:20.760
Gracjan Adamus: Okay, I do not show it here, but yes, I had the matrix of systems, so it was running on Ubuntu, macOS, Windows, and later, I think I also added Ubuntu ARM.

242
00:30:20.870 --> 00:30:24.250
Gracjan Adamus: And so, it just runs on the GitHub machines.

243
00:30:24.860 --> 00:30:33.049
Gracjan Adamus: And I also built it for the matrix of Python versions that are supported by NanoBind.

244
00:30:34.490 --> 00:30:39.870
Gracjan Adamus: Yes, so it is tested that it works cross-platform, yes, yes.

245
00:30:41.470 --> 00:30:57.519
Gabor Szabo: I also have a question here. I would personally probably do this… this… the first step for me would be setting up the CI, and cleaning up the code to that point, and then starting to make changes.

246
00:30:59.970 --> 00:31:06.169
Gabor Szabo: You may… did most of the work, or all of the work, and then you set it up.

247
00:31:06.170 --> 00:31:07.909
Gracjan Adamus: Yes, yes, yes, true.

248
00:31:07.910 --> 00:31:16.399
Gabor Szabo: Do you think that it would have changed, impacted your… your… the way of your development, if you did it under…

249
00:31:16.670 --> 00:31:18.000
Gabor Szabo: And under order?

250
00:31:18.930 --> 00:31:29.240
Gracjan Adamus: I think the problem here would be that at the start, basically nothing was working. The library wasn't even compiling.

251
00:31:29.350 --> 00:31:36.350
Gracjan Adamus: So, I think, the best course of action would be to get the very, very

252
00:31:36.530 --> 00:31:40.169
Gracjan Adamus: crude, working version, and maybe then write the tests.

253
00:31:40.490 --> 00:31:48.949
Gracjan Adamus: and then add the CI, and then do all of the full development, for example, with the SQL references and stuff like that.

254
00:31:49.960 --> 00:31:59.900
Gracjan Adamus: But in general, yeah, having a CI and test before always helps. That's also why we have the test-driven development.

255
00:31:59.990 --> 00:32:11.389
Gracjan Adamus: I personally never did that, but I can see how that can be very useful and can sometimes help with catching bugs early, yes.

256
00:32:12.770 --> 00:32:13.600
Gabor Szabo: Okay.

257
00:32:14.290 --> 00:32:15.230
Gabor Szabo: Right.

258
00:32:18.300 --> 00:32:25.859
Gracjan Adamus: Okay, we were here. So basically, this is the logs from the GitHub Actions workflow.

259
00:32:26.460 --> 00:32:32.230
Gracjan Adamus: And here, I noticed… that Python, It's found 2 times.

260
00:32:32.590 --> 00:32:34.669
Gracjan Adamus: With two different versions.

261
00:32:35.200 --> 00:32:39.249
Gracjan Adamus: One being 3.13, one being 3.14.

262
00:32:40.050 --> 00:32:44.150
Gracjan Adamus: So, what's the deal here? And then I look at my CMake.

263
00:32:44.750 --> 00:32:46.390
Gracjan Adamus: And I see this.

264
00:32:46.670 --> 00:32:55.100
Gracjan Adamus: I downloaded the Nanobyte and Lockman JSON as they are needed for the tests with fetch content.

265
00:32:56.980 --> 00:33:00.259
Gracjan Adamus: and I do findPackagePython.

266
00:33:00.450 --> 00:33:09.630
Gracjan Adamus: But I do it after I have the libraries already in place in CMake and already built and installed.

267
00:33:10.030 --> 00:33:23.059
Gracjan Adamus: So, basically, I think that it was NanoBind that went looking for Python and found the first version, and only then does MyCMake look for Python.

268
00:33:23.060 --> 00:33:33.650
Gracjan Adamus: and finds a different version. And then, when those two pieces of code want to interact, suddenly there is a mismatch in the Python, and

269
00:33:33.650 --> 00:33:46.970
Gracjan Adamus: it fails with weird errors on all of the systems. So all I had to do was move the last line before fetching those two libraries, and it was working smoothly.

270
00:33:47.800 --> 00:33:50.079
Gracjan Adamus: And here, I can also mention that

271
00:33:51.170 --> 00:34:00.240
Gracjan Adamus: If you don't know, in CMake, you have the fetch content package, which allows you to…

272
00:34:00.470 --> 00:34:13.550
Gracjan Adamus: get external dependencies from inside just the CMake. So, here we get it from GitHub, we can even get it from whatever branch we want by providing the git tag.

273
00:34:13.880 --> 00:34:22.030
Gracjan Adamus: And I think that for small projects, that's a pretty nice way of having it self-contained.

274
00:34:22.429 --> 00:34:26.389
Gracjan Adamus: Instead of having, for example, multiple submodules.

275
00:34:26.610 --> 00:34:32.470
Gracjan Adamus: which maybe are better for bigger projects, but for small, I think that this is a nice approach.

276
00:34:34.250 --> 00:34:36.970
Gracjan Adamus: And so, their package was fixed.

277
00:34:37.429 --> 00:34:42.860
Gracjan Adamus: All the tests we're passing on all the operating systems.

278
00:34:43.600 --> 00:34:50.670
Gracjan Adamus: I also messaged the original creator of Nanobind, and he said that it looked great.

279
00:34:51.080 --> 00:34:58.719
Gracjan Adamus: And I linked my code from inside the official NanoBind documentation, of which I am pretty proud of.

280
00:34:59.180 --> 00:35:02.349
Gracjan Adamus: And also, you can find that repository here.

281
00:35:04.410 --> 00:35:13.370
Gracjan Adamus: I can also say that I added support for ordered JSON, which are also available in the C++ library.

282
00:35:13.720 --> 00:35:21.479
Gracjan Adamus: And this is a screenshot from the Department 11 JSON, that there is an open issue for,

283
00:35:21.610 --> 00:35:23.649
Gracjan Adamus: Now, more than 3 years.

284
00:35:23.790 --> 00:35:34.080
Gracjan Adamus: to add the support, and it was still not done, unfortunately. Although I did create, a couple of weeks ago, a pull request

285
00:35:34.280 --> 00:35:37.329
Gracjan Adamus: Adding that, so maybe it will be merged.

286
00:35:38.560 --> 00:35:55.490
Gracjan Adamus: And, obviously, this is open source, so help wanted, and I welcome any contributions. If you find any bugs, feel free to create an issue or just fix it and do a pull request. I'm sure that there probably are some bugs that I didn't cut.

287
00:35:56.360 --> 00:36:07.960
Gracjan Adamus: this library only supports one JSON library. If you would like to also create bindings for the other ones that I listed, or the other ones that you can find.

288
00:36:08.080 --> 00:36:18.229
Gracjan Adamus: Please do. For example, I know that the SIM.json one is the fastest of all of them, so for example, support for that would be great.

289
00:36:20.050 --> 00:36:30.849
Gracjan Adamus: And, as a bonus, I wanted to do a little nanobind crash course, so we will go through building a very simple Ferris binding.

290
00:36:31.060 --> 00:36:35.769
Gracjan Adamus: Also, how you can expose objects and their properties to Python.

291
00:36:35.950 --> 00:36:43.109
Gracjan Adamus: how to use the STL in C++, and how you can write your own typecuster.

292
00:36:46.230 --> 00:36:49.390
Gracjan Adamus: So, a minimal example is like this.

293
00:36:49.920 --> 00:36:53.389
Gracjan Adamus: We just defined a doc string for the whole module.

294
00:36:54.020 --> 00:37:01.540
Gracjan Adamus: And we defined one standalone function, here we just use lambda, that will just add two numbers.

295
00:37:03.230 --> 00:37:06.880
Gracjan Adamus: The nanobind arg, where we…

296
00:37:07.740 --> 00:37:16.209
Gracjan Adamus: do A and B, is basically creating a keyword argument on the Python side. So, you know, it is more Pythonic.

297
00:37:16.990 --> 00:37:23.119
Gracjan Adamus: And also, at the end, we have a doc string for the function itself.

298
00:37:25.100 --> 00:37:27.170
Gracjan Adamus: to build it in CMake.

299
00:37:27.890 --> 00:37:33.900
Gracjan Adamus: This is also a rather… regular, let's say, CMake boilerplate.

300
00:37:34.040 --> 00:37:51.069
Gracjan Adamus: Here, I also installed NanoBind with fetch content. On the NanoBind documentation, you can find an example of doing it if NanoBind is a Git submodule, and also if it's already installed in the system, so I decided to show you the third way.

301
00:37:52.110 --> 00:38:04.170
Gracjan Adamus: And here you can see that all you have to do is basically call nanobindAddmodule and provide the C++ file where you,

302
00:38:04.480 --> 00:38:05.900
Gracjan Adamus: Define the module.

303
00:38:06.150 --> 00:38:12.750
Gracjan Adamus: And you can also install it like other packages, so it is usable in your current environment.

304
00:38:15.210 --> 00:38:24.429
Gracjan Adamus: I also added pyproject.toml, because, well, if you're creating bindings to Python, you probably want to have it as a Python library.

305
00:38:24.570 --> 00:38:34.709
Gracjan Adamus: It is also very simple, you just need Nanobind and Scikit Build Core, because that is used by Nanobind, that's its dependency.

306
00:38:35.620 --> 00:38:40.149
Gracjan Adamus: And then, to build it and use it, you just do pip install.

307
00:38:40.270 --> 00:38:45.179
Gracjan Adamus: here, where you have the pipe project and CMake files.

308
00:38:45.910 --> 00:38:50.479
Gracjan Adamus: And I also showed using it from the Python terminal.

309
00:38:50.710 --> 00:38:52.729
Gracjan Adamus: It works. Great.

310
00:38:54.330 --> 00:38:55.380
Gracjan Adamus: Now.

311
00:38:55.660 --> 00:39:04.569
Gracjan Adamus: consider a case where you have some classes, and you also want to show them… or use them in Python.

312
00:39:04.990 --> 00:39:15.499
Gracjan Adamus: let's say we have a very simple class counter that just has a value and can increment it. You can set the value, you can read the value.

313
00:39:15.650 --> 00:39:20.570
Gracjan Adamus: And also, when you construct it, you can give it a different start point.

314
00:39:20.910 --> 00:39:22.630
Gracjan Adamus: So it's quite simple.

315
00:39:24.140 --> 00:39:27.409
Gracjan Adamus: Here is how you could wrap it in Nanobyte.

316
00:39:28.170 --> 00:39:33.780
Gracjan Adamus: First, You define the constructor that it takes the int.

317
00:39:33.980 --> 00:39:41.800
Gracjan Adamus: And, you can also set a default value, like we do here, with equals 0 for the start argument.

318
00:39:42.600 --> 00:39:52.859
Gracjan Adamus: Here, I can also mention that the default value in the binding and the default value of the constructor itself are different.

319
00:39:52.930 --> 00:40:06.719
Gracjan Adamus: completely different. They can be… one can be 0, one can be 10. You can specify one and not the other. That's something else, but for creating Pythonic interfaces, that's wood.

320
00:40:07.730 --> 00:40:12.600
Gracjan Adamus: We can wrap any class method the same way.

321
00:40:13.330 --> 00:40:20.189
Gracjan Adamus: So, for example, the increment one, and also the value that returns the value.

322
00:40:20.590 --> 00:40:29.330
Gracjan Adamus: Here you can also see that the Python name does not need to match the method name. We can define it as whatever we want.

323
00:40:30.240 --> 00:40:34.520
Gracjan Adamus: And, what is important, Is we also use…

324
00:40:35.050 --> 00:40:40.149
Gracjan Adamus: Define property read only, and define property read right.

325
00:40:40.620 --> 00:40:51.819
Gracjan Adamus: what that does is that instead of it being a function, a method that you need to call on the Python side, it will be a property.

326
00:40:52.380 --> 00:40:58.399
Gracjan Adamus: which you can see here in the example. We don't need to call value arrow.

327
00:40:58.630 --> 00:41:10.320
Gracjan Adamus: it is a Pythonic object property, so that's nice. And also, as you could guess, read-only means that we get an error when we try to write it.

328
00:41:10.580 --> 00:41:13.840
Gracjan Adamus: Read-write means that we can both read and write to it.

329
00:41:14.590 --> 00:41:30.570
Gracjan Adamus: And you can also define dunder methods from NanoBind. For example, here we do one for the representation, and we turn it into a string, so when we actually print object like that, it has a pretty… it is…

330
00:41:30.710 --> 00:41:32.489
Gracjan Adamus: Printed in a pretty way.

331
00:41:35.350 --> 00:41:38.249
Gracjan Adamus: And, how we can use STL.

332
00:41:38.250 --> 00:41:39.700
Gabor Szabo: I have a question, sorry.

333
00:41:39.700 --> 00:41:40.780
Gracjan Adamus: Yes, yes?

334
00:41:40.780 --> 00:41:48.389
Gabor Szabo: which is, actually not… probably not related to the use. Python allows integers to be arbitrary.

335
00:41:49.280 --> 00:42:02.459
Gabor Szabo: an arbitrary value, so it will just allocate more and more memory as you increment an integer. If you call this function, inside, I think it was defined as an int. It has a…

336
00:42:03.020 --> 00:42:07.110
Gabor Szabo: What happens here if you call, or who is…

337
00:42:07.520 --> 00:42:12.019
Gabor Szabo: Okay, what happens if you call this Python function, right? The one that.

338
00:42:12.480 --> 00:42:16.539
Gabor Szabo: Ozma, with a number that is… doesn't fit ILD.

339
00:42:17.040 --> 00:42:21.750
Gracjan Adamus: Yes. So, I don't remember how exactly it is handled.

340
00:42:21.980 --> 00:42:24.000
Gracjan Adamus: But,

341
00:42:24.850 --> 00:42:36.299
Gracjan Adamus: I think it will just, fail. I'm not sure if there is a different behavior between, for example, unsigned or signed integers.

342
00:42:38.030 --> 00:42:53.699
Gracjan Adamus: that I can't really tell you, I would have to check, nanobind docs to see how they're handled it. But yes, that is an issue, and it is not, for example, somehow expanded under the hood, no. It's handled in some different way.

343
00:42:54.240 --> 00:43:04.789
Gabor Szabo: Yeah, I mean, I mean, from the Python side of view, or from the Python side, you can even call this with a string, you know, Python doesn't care.

344
00:43:04.970 --> 00:43:05.820
Gabor Szabo: Right?

345
00:43:06.110 --> 00:43:22.150
Gracjan Adamus: Yes, yes, yes. But in that case, when coming with a string, NanoBind will show an error that this type cannot be casted to what is needed by the method, by the function.

346
00:43:22.910 --> 00:43:23.760
Gabor Szabo: Okay.

347
00:43:25.590 --> 00:43:32.180
Gracjan Adamus: So, in general, the nanobind bindings should be type-safe, yes.

348
00:43:35.150 --> 00:43:48.990
Gracjan Adamus: And also, NanoBind includes a lot of ready bindings for the STL, so for the libraries, the basic libraries with containers and algorithms for C++.

349
00:43:49.330 --> 00:43:53.309
Gracjan Adamus: And so, you can have vectors, string, lists.

350
00:43:53.440 --> 00:43:55.320
Gracjan Adamus: And a lot of different stuff.

351
00:43:55.800 --> 00:43:57.330
Gracjan Adamus: Ehhh…

352
00:43:57.680 --> 00:44:01.689
Gabor Szabo: Henry, could you remind us what is STL here?

353
00:44:01.690 --> 00:44:05.580
Gracjan Adamus: Yes, yes, yes. STL means Standard Template Library.

354
00:44:06.300 --> 00:44:18.070
Gracjan Adamus: And so, it is a collection of, as I said, containers and algorithms for C++ that use templates, so they are generic and work for a lot of types.

355
00:44:18.320 --> 00:44:25.929
Gracjan Adamus: And without them, C++ would be very much more similar to C and harder to use, yes.

356
00:44:26.310 --> 00:44:31.980
Gracjan Adamus: So, for example, here, we can have a collection of some strings in a vector.

357
00:44:32.470 --> 00:44:43.699
Gracjan Adamus: And I think I have a… no, I forgot to add an example, but we could pass a list of strings on the Python side to it, and it would just work.

358
00:44:43.820 --> 00:44:56.440
Gracjan Adamus: again, without any more manual conversions, because all the stuff that I listed on the site is already done by NanoBind itself, and it will just work as the arguments.

359
00:44:56.650 --> 00:45:10.570
Gracjan Adamus: And it will be, let's say, translated both going to Python and coming from Python. So when we return the vector, it will also be returned as a list on the Python site.

360
00:45:13.720 --> 00:45:23.430
Gracjan Adamus: So, to be honest, most codebases can probably work very well without custom typecasters.

361
00:45:24.140 --> 00:45:28.230
Gracjan Adamus: But nevertheless, we will quickly look at them.

362
00:45:28.970 --> 00:45:30.980
Gracjan Adamus: Here's part of it.

363
00:45:31.280 --> 00:45:40.140
Gracjan Adamus: for stdwell Array, which is one of the STL containers that is not provided by NanoBind, because it is rather

364
00:45:40.510 --> 00:45:41.860
Gracjan Adamus: uncommon.

365
00:45:41.990 --> 00:45:52.520
Gracjan Adamus: But it was used heavily in the Packard MC library, so when we were switching to Nanobyte, we would have to rewrite a lot of functions.

366
00:45:53.090 --> 00:45:58.910
Gracjan Adamus: To use, for example, the vector. So it was much easier to just write a custard.

367
00:46:00.020 --> 00:46:07.710
Gracjan Adamus: And casting it from C++ to the Python object is very easy. We create a… Nano-bind list.

368
00:46:07.910 --> 00:46:15.310
Gracjan Adamus: And we just append all of the elements, and we return it, and on the Python side, we will see it as a list.

369
00:46:16.100 --> 00:46:24.029
Gracjan Adamus: the function to turn it from a Python type to the C++ one is a bit more complex.

370
00:46:24.770 --> 00:46:28.410
Gracjan Adamus: First of all, we have a… Two ifs.

371
00:46:29.550 --> 00:46:40.409
Gracjan Adamus: In one, we check if it is a regular Python list, and in another one, we check if it is an array, so for example, something passed from NumPy.

372
00:46:40.650 --> 00:46:44.099
Gracjan Adamus: But that it is one-dimensional and of that type.

373
00:46:44.710 --> 00:46:57.950
Gracjan Adamus: And in both cases, we have some, let's say, boilerplate for iterating over this object, and assigning all the values to the val array.

374
00:47:02.080 --> 00:47:09.809
Gracjan Adamus: And here I wanted to give a little bit of insight of how it looks in the NanoBind JSON itself.

375
00:47:10.810 --> 00:47:15.220
Gracjan Adamus: This is a helper function.

376
00:47:15.910 --> 00:47:22.690
Gracjan Adamus: that takes some JSON and returns the nanobyte object.

377
00:47:22.990 --> 00:47:25.870
Gracjan Adamus: And it is basically a tree of…

378
00:47:25.990 --> 00:47:40.340
Gracjan Adamus: else if statements, where we check if it's a null, if it's a boolean, so that we can cast it to the correct type, and assign it… and create a correct Python object from it.

379
00:47:40.810 --> 00:47:42.970
Gracjan Adamus: So, it's rather uneventful.

380
00:47:43.730 --> 00:47:51.890
Gracjan Adamus: However… going the way from Python to C++ is a bit more complex.

381
00:47:52.010 --> 00:47:56.259
Gracjan Adamus: Here is a part of it. I mean, it is also mostly else if.

382
00:47:56.410 --> 00:48:01.699
Gracjan Adamus: We also check if it's a bool, then cast to bull, it's an integer, cast to integer.

383
00:48:02.170 --> 00:48:06.560
Gracjan Adamus: But… This is the rest of the function.

384
00:48:07.080 --> 00:48:12.410
Gracjan Adamus: And here you can see that we check if it's a tuple and if it's a list, or if it's a dictionary.

385
00:48:13.020 --> 00:48:19.970
Gracjan Adamus: And we have to do the circular reference check that I already mentioned before.

386
00:48:20.220 --> 00:48:25.370
Gracjan Adamus: To make sure that we don't have, basically an infinite loop and a crash.

387
00:48:26.250 --> 00:48:31.060
Gracjan Adamus: And also, if it's none of those types, we say that

388
00:48:31.350 --> 00:48:36.529
Gracjan Adamus: this was not implemented for the JSON, And we show an error.

389
00:48:38.550 --> 00:48:55.640
Gracjan Adamus: And also, to have easier time using it, there is overload that doesn't take the set of references, and it just creates it inside, so we don't have to do it ourselves at every point where we call that function.

390
00:48:57.880 --> 00:49:01.849
Gracjan Adamus: This is a part that handles

391
00:49:03.080 --> 00:49:07.640
Gracjan Adamus: stuff on the Lockman JSON portion.

392
00:49:07.770 --> 00:49:11.919
Gracjan Adamus: So… Those are serializes.

393
00:49:12.120 --> 00:49:18.370
Gracjan Adamus: serializers for the library, the C++ library itself.

394
00:49:19.550 --> 00:49:32.319
Gracjan Adamus: And you can see that it is also pretty easy, because we have the utility already written. We just cast it from whatever type we have been given to this JSON.

395
00:49:32.530 --> 00:49:48.749
Gracjan Adamus: And this is made as a macro, because there are a lot of nanobind types for which we have to write it, because basically every nanobind type that we receive also has to have a serializer for the JSON library.

396
00:49:48.940 --> 00:49:52.370
Gracjan Adamus: And doing it with macros is just easier.

397
00:49:53.770 --> 00:50:00.529
Gracjan Adamus: And the custer is generally ready. This is also a very simple piece of code.

398
00:50:00.730 --> 00:50:02.629
Gracjan Adamus: We do,

399
00:50:04.270 --> 00:50:17.520
Gracjan Adamus: template specialization for the particular type which we want to do. In this case, it is just a JSON type. And from Python and from C++ functions, also just call our wrappers.

400
00:50:17.720 --> 00:50:20.529
Gracjan Adamus: I mean, our utility functions.

401
00:50:20.880 --> 00:50:25.590
Gracjan Adamus: So, that's basically it, and that works, and that's nice.

402
00:50:26.890 --> 00:50:35.889
Gracjan Adamus: And, a couple quick fun facts behind the scenes when I was doing the presentation, preparing the presentation.

403
00:50:36.390 --> 00:50:41.449
Gracjan Adamus: You could see on the slides that it was…

404
00:50:42.720 --> 00:51:02.609
Gracjan Adamus: the Python 3.13 that was failing on Windows, but previously, I found in the pipelines that it was the only one passing. But suddenly, with seemingly the same code that I was trying to, let's say, reverse engineer.

405
00:51:02.710 --> 00:51:05.760
Gracjan Adamus: It was completely opposite.

406
00:51:06.390 --> 00:51:15.869
Gracjan Adamus: the newest Python was failing, and all the others were passing. So, that also shows you how volatile of an error that was.

407
00:51:16.740 --> 00:51:27.809
Gracjan Adamus: Also, I accidentally created a pull request to the original repository 3 times when I was working on a throwaway branch on my fork.

408
00:51:28.870 --> 00:51:41.920
Gracjan Adamus: And also, because after I fixed everything, I did a pull request to the original tool, so that people can find it, and so there were two pull requests, and I wanted to show that there was one.

409
00:51:42.100 --> 00:51:53.340
Gracjan Adamus: So, I did what every hacker in first grade does, and used InspectElement to just change that to 1, so it looks good for the slides.

410
00:51:54.460 --> 00:52:11.930
Gracjan Adamus: I also used a lot of teammate sessions. If you don't know what it is, basically it allows you to SSH into a running pipeline on the GitHub Action CI, and debug from there, check out what's going on.

411
00:52:11.930 --> 00:52:14.260
Gabor Szabo: What is this? I don't know this one.

412
00:52:14.850 --> 00:52:20.250
Gracjan Adamus: This is something that you can add to your CR workflow.

413
00:52:20.600 --> 00:52:27.359
Gracjan Adamus: which, at some point, it will, let's say, stop executing, and give you an SSH

414
00:52:27.440 --> 00:52:45.179
Gracjan Adamus: I don't know how to say it, key or link, through which you can connect to the machine that was actually running this code. And so with that, you can easily debug stuff on the CI, and, you know, use it as a regular terminal.

415
00:52:45.290 --> 00:53:02.649
Gracjan Adamus: So you can just rerun the test, maybe see some error that was not seen in the logs, or change something. Or, for example, in my case, I spent a lot of time looking where the library was actually installed when I was having the issues with the paths.

416
00:53:02.730 --> 00:53:09.260
Gracjan Adamus: So, that's very nice, but I accidentally left it open for more than 2 hours on the CI.

417
00:53:10.280 --> 00:53:15.810
Gabor Szabo: Okay, so is this… is this a configuration in the… in the GitHub Actions file?

418
00:53:15.810 --> 00:53:21.719
Gracjan Adamus: Yes, yes, yes, you added in the YAML. I think it's, like, 3 lines.

419
00:53:21.840 --> 00:53:28.550
Gracjan Adamus: If you look up teammate session, then I think you should find the repository for it, yes. It's very useful.

420
00:53:29.380 --> 00:53:30.290
Gabor Szabo: Excellent.

421
00:53:31.960 --> 00:53:44.410
Gracjan Adamus: And also, it was my first time actually using Git Cherry Peak, when I was looking at the different commits, trying to see which one was failing the CI in the way that I wanted.

422
00:53:44.780 --> 00:54:03.550
Gracjan Adamus: And I also wanted to once present it as a lightning talk on Tech Talks in Krakow, but my laptop decided to just not work with the HDMI cable, and I couldn't do it. But thanks to that, I turned it into a full-fledged presentation, so…

423
00:54:03.550 --> 00:54:04.950
Gracjan Adamus: That's very good.

424
00:54:05.070 --> 00:54:11.070
Gracjan Adamus: And thank you very much for listening and for inviting me, and I would also like to thank

425
00:54:11.090 --> 00:54:25.779
Gracjan Adamus: the people, the Pipard MC team that got me into the project, and they're also the reason why I got involved with this, and also all the people, connected to NanoBind, PyBand 11, and PyMat11 JSON for doing…

426
00:54:25.820 --> 00:54:32.870
Gracjan Adamus: very, very great software engineering work with their libraries. Thank you.

427
00:54:34.430 --> 00:54:42.330
Gabor Szabo: Thank you very much, Gracian. Any more questions from the audience who is in the chat, or…

428
00:54:42.470 --> 00:54:45.130
Gabor Szabo: Shall we finish this session now?

429
00:54:45.570 --> 00:54:47.400
Gabor Szabo: It seems that,

430
00:54:47.640 --> 00:54:55.939
Gabor Szabo: They are done with their questions for now. So thank you, thank you very much for this presentation, it was very interesting.

431
00:54:57.640 --> 00:55:09.909
Gabor Szabo: Yeah, someone is writing that we are currently using PyBind11 for binding the CERN controls middleware, so this is a very relevant topic. Well, very… I'm very happy that it's relevant for someone.

432
00:55:10.640 --> 00:55:17.490
Gabor Szabo: immediately. So thank you very much, and as I said it, earlier.

433
00:55:18.060 --> 00:55:35.730
Gabor Szabo: We are going to finish now the video recording, so if you are watching the video, then don't forget to like it, and follow the channel, and whatever, and below the video, there's going to be a link to various things that were mentioned in this presentation.

434
00:55:35.730 --> 00:55:44.150
Gabor Szabo: And if you are here in this presentation, then feel free to stay after the presentation, and then we can have a free chat about

435
00:55:44.450 --> 00:55:58.839
Gabor Szabo: anything you like to talk, I will let everyone speak on that occasion. That's the advantage of being in the live present… that's one of the advantages of being here at the live presentation.

436
00:55:58.840 --> 00:56:06.940
Gabor Szabo: So, thank you very much again, and see you in the next time, next video, whatever. Bye-bye.

437
00:56:07.240 --> 00:56:08.120
Gracjan Adamus: Thank you.

