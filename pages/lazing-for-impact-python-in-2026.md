---
title: Lazing for Impact, Python in 2026 with Aekasitt (Sitt) Guruvanich
timestamp: 2026-07-20T14:30:01
author:
published: true
description:
tags:
---


{% youtube id="HxveXb_wd8w" file="2026-07-20-lazing-for-impact-python-in-2026-with-aekasitt-sitt-guruvanich.mp4" %}

## Abstract

Discussing language features, runtime reflections and direction forward in Python the lazy way.

Coming up on 30 years and Python programming language has been growing faster than ever. It has endured many paradigm shifts along the way as well as many competitors for the throne of prototyping king. Unlike its contemporaries which has come and gone, Python is more popular than ever and it topped every popularity chart before agents skewed all datasets. Reflecting on where we had been and where we are going make for a great realignment. Will Python's explicit typing cost its personality or force an evolution rarely seen since Python 2.7?

## Speaker:

* [Aekasitt (Sitt) Guruvanich](https://www.linkedin.com/in/aekasitt-guruvanich-b1bb4b53/)


## Transcript

1
00:00:01.980 --> 00:00:21.609
Gabor Szabo: So hello and welcome to the CodeMaven meeting. My name is Gabor. I'm the organizer of this, and we can get started. I'm really happy to welcome our guest, Sid, from Thailand, who is going to give this presentation now.

2
00:00:21.650 --> 00:00:28.529
Gabor Szabo: The mic is yours. Please introduce yourself. You can pronounce your name much better than I can. So

3
00:00:28.530 --> 00:00:45.689
Gabor Szabo: Go ahead, and people who are here in the meeting, feel free to ask questions, either now or later. Just remember that it's being recorded, it's going to be published, so you can ask also in the chat, and then I can read out the question if you don't want to.

4
00:00:45.700 --> 00:00:49.950
Gabor Szabo: Ask it to… in your voice. Thank you very much.

5
00:00:50.240 --> 00:01:02.499
Aekasitt Guruvanich: I'll go to my site. Alright, thank you everybody for coming by. So my name is Aekaset Guruvanis, but you can just call me Seth just, like, for brevity. So…

6
00:01:03.070 --> 00:01:13.680
Aekasitt Guruvanich: In Thailand, like, we actually have an, we have a Python community here as well that actually does a lot of meetups. We have a lot of, like, expats from the United States, we have a lot of expats from the

7
00:01:13.910 --> 00:01:30.489
Aekasitt Guruvanich: from the European Union, which is why, like, we all have a shared love for, like, Greenland, so the joke is there. That is, like, the Greenland Defense Force thing, like, it's a, it's a thing we do here, it's an inside joke on our side. So I actually, I've been programming since I was 12.

8
00:01:30.850 --> 00:01:41.270
Aekasitt Guruvanich: I do think, like, my primary language right now, we have, like, the lower-level stuff, like, from Rust, and I use Titan as, like, my primary language in my

9
00:01:41.800 --> 00:01:47.659
Aekasitt Guruvanich: Quant… Quant analysis, position in our hedge fund.

10
00:01:47.930 --> 00:02:03.090
Aekasitt Guruvanich: We also do… I also do, like, a block in Thai as well, because I think I'm trying to, like, expand the knowledge base in our language as much as possible, and I think, like, we're lacking a lot, like, a text content on that side, but,

11
00:02:03.430 --> 00:02:09.979
Aekasitt Guruvanich: very happy that you all came and joined us. I did, my… I did my studies in Hong Kong, so…

12
00:02:10.259 --> 00:02:17.369
Aekasitt Guruvanich: If, if any… if anyone has been to Thailand or Hong Kong, like, want to talk to me about that, like, later on, just, ping me.

13
00:02:17.690 --> 00:02:26.359
Aekasitt Guruvanich: So, again, it's just an inside joke, but just to make sure that we don't mispronounce the shark name of Greenland. It is their national animal.

14
00:02:26.470 --> 00:02:32.100
Aekasitt Guruvanich: But it is microcephalus, which means small head, and I'm very, very yeah.

15
00:02:32.610 --> 00:02:34.390
Aekasitt Guruvanich: Objective about that, yes.

16
00:02:34.710 --> 00:02:47.649
Aekasitt Guruvanich: So, we're here to talk about, Python. I've actually given a lot of, like, talk about, like, Python, about packaging, like, using, like, both Poetry and UV, so, like, I've been giving a lot, like, basically Py

17
00:02:47.760 --> 00:02:55.139
Aekasitt Guruvanich: I've also, like, been talking about, like, foreign function interface, like, using Python as well. So, like, I was focused a lot more on, like, using Rust

18
00:02:55.240 --> 00:03:14.379
Aekasitt Guruvanich: As the lower level language on Python packages. But also, I gave a talk about using my PyC to do ahead of time compilation for Python, which means that whatever your normal language Python is, including type annotations and including a few tricks.

19
00:03:15.430 --> 00:03:34.900
Aekasitt Guruvanich: In your sleep, you can actually do ahead of time compilation using Python. And it is, I would say, four to five times faster. And that includes basically writing a web service. And that's something that we can talk about in some other time. But today, we're going to be talking about the GIL, the Global Interpreter Lock.

20
00:03:35.120 --> 00:03:40.390
Aekasitt Guruvanich: types, and, basically, like, what's coming ahead. So, like, we're gonna lace for impact, we're gonna

21
00:03:40.600 --> 00:03:43.749
Aekasitt Guruvanich: Prepare for, like, the next version of Python.

22
00:03:43.870 --> 00:03:49.399
Aekasitt Guruvanich: So, this is, like, a personal announcement, like, but when I talk about, like, heightened packaging.

23
00:03:49.690 --> 00:03:58.219
Aekasitt Guruvanich: I would say, this is something that, like, just happened earlier this year, but I didn't get to brag about it enough, because I also had my daughter earlier this year as well.

24
00:03:58.500 --> 00:04:05.719
Aekasitt Guruvanich: So, yeah, like, in the beginning of, like, 2026, my package got downloaded, like, 2.3 million

25
00:04:05.830 --> 00:04:10.600
Aekasitt Guruvanich: Times around the world, so, like, I see it's a small extension for.

26
00:04:11.060 --> 00:04:12.290
Aekasitt Guruvanich: FastAPI.

27
00:04:12.850 --> 00:04:14.020
Aekasitt Guruvanich: Web framework.

28
00:04:14.180 --> 00:04:27.689
Aekasitt Guruvanich: So, micro web framework, it depends on, like, how you look at it. So, this is something that, like, it's a very, it's a side project for me, but, like, I also, like, take it very seriously as well. I do think, like, Python has, like, the…

29
00:04:28.710 --> 00:04:41.629
Aekasitt Guruvanich: The way… the way that we use Python, and the way we actually have been using Python for almost 30 years now, since, like, 1989, it tells us a lot about, like, basically what are important, and, like, the… why Python won.

30
00:04:41.740 --> 00:04:46.280
Aekasitt Guruvanich: in the metaprogramming battle between the higher level language.

31
00:04:46.640 --> 00:04:50.119
Aekasitt Guruvanich: So, let's talk about the guild first. So, I think, like, everybody

32
00:04:50.380 --> 00:04:55.489
Aekasitt Guruvanich: Knows that, like, you're not a Pythonista, like, unless you complain about the girl.

33
00:04:55.680 --> 00:04:58.430
Aekasitt Guruvanich: I do think that, like, this is something that

34
00:04:58.900 --> 00:05:16.339
Aekasitt Guruvanich: a lot of people have, like, a misunderstanding about it as well, because when you heard about, like, hey, like, the latest version of Python, like, is now, like, free-threading, we kind of expected, like, all of our asynchronous, like, programming to, like, be much faster, or just, like, you know, like, have, like, utilize, like, a lot more.

35
00:05:20.990 --> 00:05:22.799
Gabor Szabo: We have this connection.

36
00:05:23.520 --> 00:05:25.639
Aekasitt Guruvanich: People didn't understand is that like, I think like a

37
00:05:26.000 --> 00:05:28.710
Aekasitt Guruvanich: Your face for us, so, like, am I still coming through?

38
00:05:29.230 --> 00:05:35.880
Gabor Szabo: I think we had this — we got disconnected for a second or two.

39
00:05:36.610 --> 00:05:40.880
Aekasitt Guruvanich: Okay, yeah, so, you're no longer frozen. Should I, I'll repeat.

40
00:05:41.050 --> 00:05:43.389
Gabor Szabo: Yeah, can you start?

41
00:05:45.190 --> 00:05:45.840
Gabor Szabo: River.

42
00:05:45.840 --> 00:05:46.230
Aekasitt Guruvanich: Okay.

43
00:05:46.230 --> 00:05:47.500
Gabor Szabo: A couple of seconds.

44
00:05:47.920 --> 00:05:59.650
Aekasitt Guruvanich: Okay. So, I think, like, you're not, like, a real Pythonista, like, unless you complain about the guild, right? Like, I think, like, people kind of expected, like, the latest versions of Python, like, the one

45
00:05:59.790 --> 00:06:01.260
Aekasitt Guruvanich: as,

46
00:06:01.780 --> 00:06:09.669
Aekasitt Guruvanich: as, like, a feature to be, like, much faster, or, like, this and that? Because, like, we… a lot of us, like, we misunderstand, like, the latest exchange, right?

47
00:06:10.720 --> 00:06:27.600
Aekasitt Guruvanich: Python that has always kind of have like a kind of built in, I would say like a parallelism, but like it had data parallelism, but it did not have the interpreter parallelism. So I think like this is something that people had to like do many workarounds about it. Like for example, like using multi-processing.

48
00:06:27.890 --> 00:06:41.989
Aekasitt Guruvanich: package, like, this, like, in the standard library to spawn a different, like, thread, like, spawn, like, a different process utilizing the other threads. But, like, we, like, it would be much nicer, for not just, like, our, like.

49
00:06:42.140 --> 00:06:46.329
Aekasitt Guruvanich: Little corner of Python as well, but, like, to have, like, a built-in

50
00:06:46.480 --> 00:06:51.700
Aekasitt Guruvanich: free threading in all of our packages, so that I actually would

51
00:06:51.870 --> 00:07:03.249
Aekasitt Guruvanich: have a ripple effect of, like, increasing our, like, scripting and, like, programming the performance. So I think, like, we're just gonna talk about the guild and how

52
00:07:03.650 --> 00:07:10.559
Aekasitt Guruvanich: a lot of these changes are not easily observed. For example, like, when you actually start using the free-threading version of Python.

53
00:07:10.970 --> 00:07:27.299
Aekasitt Guruvanich: you don't see the changes right away, but what, what you're, what you're gonna see a lot more is that, like, if you're using, like, NumPy, or using, like, data frame packages like, Polars and Pandas, those, changes become very, apparent immediately because

54
00:07:27.400 --> 00:07:37.710
Aekasitt Guruvanich: the underlying work of, like, your, libraries, begin to change. And it did not happen right away, but it is slowly happening because, essentially.

55
00:07:37.870 --> 00:07:41.060
Aekasitt Guruvanich: A lot of our…

56
00:07:41.830 --> 00:07:58.809
Aekasitt Guruvanich: free threaded reels are coming out right now. So, at the moment, like, this is a screenshot from last night. So, Thomas Walters, like, he is a, like, a prominent, like, computer scientist, and he gave a talk in PyCon earlier this year, and he talks about, like, 60% of our

57
00:07:59.170 --> 00:08:12.119
Aekasitt Guruvanich: top 360, binary wheels on Python are already, doing it. And now, last night, it was, like, already 60%. So, like, we're… we're moving towards, like, a… having a free-threaded, not just, like, the Python interpreter.

58
00:08:12.120 --> 00:08:22.819
Aekasitt Guruvanich: But also, like, all of the wheels, all the binary wheels that we're coming out with as well, it's gonna be, essentially all free-threaded. And we're not even gonna remember, like, how it was in Python that did not have free-thread

59
00:08:23.080 --> 00:08:25.509
Aekasitt Guruvanich: So that was a that was actually a big deal.

60
00:08:25.770 --> 00:08:26.600
Aekasitt Guruvanich: Oh.

61
00:08:26.760 --> 00:08:42.709
Aekasitt Guruvanich: all I want to, like, basically caution everyone is that, like, yeah, like, when we had the flip the switch moment of, like, basically having free threading in Python, like, the change is not going to become apparent, like, right away. What we had to do was also, like, upgrading, like, a lot of the wheels.

62
00:08:42.880 --> 00:08:47.540
Aekasitt Guruvanich: the binary file and the packages that I see, do not support, like, free-threading web yet.

63
00:08:47.640 --> 00:08:49.969
Aekasitt Guruvanich: So, we can talk about,

64
00:08:50.240 --> 00:08:55.430
Aekasitt Guruvanich: This is gonna be the most controversial topic of, like, Python, which is typing.

65
00:08:55.560 --> 00:09:04.509
Aekasitt Guruvanich: So, I think, like, a lot of people expect, like, higher-level language to not care so much about type, but what people always tend to forget is, like, Python actually is a type language.

66
00:09:04.680 --> 00:09:08.090
Aekasitt Guruvanich: And like we, we do type actually quite well.

67
00:09:08.260 --> 00:09:21.500
Aekasitt Guruvanich: I think, like, the one thing that, like, people, tend to forget is that, like, a lot of, like, Python performers, a lot of, like, Python secret sauce actually come from the lower-level, binaries, like, for example, like, NumPy.

68
00:09:21.550 --> 00:09:30.630
Aekasitt Guruvanich: and, like, XRA and, scientific packages. And those things, like, when we… when we import the result, like, import the,

69
00:09:30.730 --> 00:09:36.320
Aekasitt Guruvanich: calculation. We have to do it, like, using some kind of, typing as well, because

70
00:09:37.240 --> 00:09:42.620
Aekasitt Guruvanich: In a, in a foreign, foreign function interface, like, environment, like, we always have to communicate, like, through types

71
00:09:43.540 --> 00:09:44.530
Aekasitt Guruvanich: And, you know.

72
00:09:45.170 --> 00:10:03.020
Aekasitt Guruvanich: in terms of, like, popularity as well, like, we are beginning to actually see JavaScript drop in terms of, like, popularity, against TypeScript, and TypeScript has become, like, one of the most, like, actively used language on GitHub in, year 2025, but what I want to caution you guys here is that, like,

73
00:10:03.580 --> 00:10:11.809
Aekasitt Guruvanich: Popularity is not, like, it's not the be-all-and-all kind of number, like, the metric that we can look at, because, like, we always, like, look at lies, damn

74
00:10:11.910 --> 00:10:31.240
Aekasitt Guruvanich: When you look at the top programming language on GitHub, on the open source environment, we're not seeing a lot of cloud bot activities. We're not going to see a tag as like, hey, this is a real person repository, or this is a repository made by basically all the AI cloud bots and agents and everything.

75
00:10:31.240 --> 00:10:31.950
Aekasitt Guruvanich: So, like…

76
00:10:31.970 --> 00:10:49.960
Aekasitt Guruvanich: Take it with caution. I would say always compare with the TV Programming Community Index as well, because that way you see that Python is always going to be on top. We had a very high spike during the 2024 and 2025 as well, because those are the years of the

77
00:10:50.440 --> 00:10:53.269
Aekasitt Guruvanich: artificial intelligence repository.

78
00:10:53.990 --> 00:11:06.820
Aekasitt Guruvanich: So, should we all just switch to using TypeScript because, like, it is a… well, it has type in the name, right? I do think, like, Python actually does type, like, way better than TypeScript does, and I think, like, a lot of people

79
00:11:07.210 --> 00:11:09.870
Aekasitt Guruvanich: I'm not making use of it.

80
00:11:09.960 --> 00:11:23.630
Aekasitt Guruvanich: again, like, when I talk about, like, using types, like, way better in Python, I always mention, like, hey, if you actually need, like, performance-critical, like, areas in Python, all you have to do is, like, do your type annotations very well.

81
00:11:23.630 --> 00:11:30.540
Aekasitt Guruvanich: And you can ahead of time compile that part using MyPyC as well. That's actually like a tool that's actually…

82
00:11:30.680 --> 00:11:39.020
Aekasitt Guruvanich: being a sponsor and, like, have long-term support using, from the Python Software Foundation. So I think, like, these are things that we can always, like, bet on.

83
00:11:39.140 --> 00:11:43.850
Aekasitt Guruvanich: I do think, like, Python does do type, better than TypeScript do.

84
00:11:44.170 --> 00:11:56.690
Aekasitt Guruvanich: Because, like, TypeScript does not actually compile your types into anything. TypeScript can only, transfer that back to, like, JavaScript, and, like, run that in, like, a very, constrained environment. So I think, like, this is something, like, we can always make use of.

85
00:11:58.650 --> 00:11:59.390
Aekasitt Guruvanich: So.

86
00:11:59.510 --> 00:12:02.959
Aekasitt Guruvanich: Python actually is dynamic type. We've always had typing.

87
00:12:03.050 --> 00:12:15.680
Aekasitt Guruvanich: And we're gonna get… we're gonna get a lot more tricks and tips at doing this, like, way better in the future. So these are, like, three of, like, the coming-up, proposals in Python.

88
00:12:15.680 --> 00:12:24.749
Aekasitt Guruvanich: which, like, we actually have a PEP called PEP82… 837, type manipulation, which is, it's gonna give us TypeScript-like

89
00:12:25.070 --> 00:12:41.139
Aekasitt Guruvanich: keywords that actually, allow us to do types way better, than we did before as well. So, when I talk about, like, the motivation here, like, people don't actually understand the word, like, metaprogramming too much, but our bread and butter in Python, so, like, for example, like, if you're using

90
00:12:41.920 --> 00:13:01.529
Aekasitt Guruvanich: The bread and butter would actually be borrow, shaker, and others. Those are the newer metaprogramming in the new world. But for us, Pythonista, metaprogramming for us is actually runtime reflection. And nobody else does runtime reflection as good as Python. I know it was actually introduced by the Lisp programmers.

91
00:13:01.870 --> 00:13:10.539
Aekasitt Guruvanich: But actually, I do think that, like, with 30 years of experience, like, almost 30 years of experience, like, Python has been doing, like, runtime reflection really, really well.

92
00:13:10.660 --> 00:13:13.749
Aekasitt Guruvanich: And type is actually only going to improve on this.

93
00:13:14.650 --> 00:13:15.400
Aekasitt Guruvanich: So.

94
00:13:15.880 --> 00:13:21.560
Aekasitt Guruvanich: This is actually, like, one of the keywords introduced by the… The PSF Fellow.

95
00:13:21.790 --> 00:13:25.939
Aekasitt Guruvanich: So type manipulation is actually introduced by Michael Sullivan.

96
00:13:26.840 --> 00:13:32.149
Aekasitt Guruvanich: And we're gonna have, like, certain keywords like this that actually, like, it basically copies, like, what

97
00:13:33.610 --> 00:13:48.399
Aekasitt Guruvanich: What extending and omitting from TypeScript does, which means that when we want to do a type definition in Python, we don't actually have to redo our work from the beginning every single time.

98
00:13:48.790 --> 00:13:53.729
Aekasitt Guruvanich: It means that, like, when we actually have, like, other types, we can, extending on top of that type.

99
00:13:54.160 --> 00:14:01.339
Aekasitt Guruvanich: Using, like, its member and everything. So, this is, one thing that we can actually do using, creating the record.

100
00:14:01.570 --> 00:14:05.109
Aekasitt Guruvanich: And how we do that is we're going to use the keyword pick.

101
00:14:05.410 --> 00:14:13.689
Aekasitt Guruvanich: So we can actually, like, pick, like, certain, certain, type attributes, like, from one type. So the top part right there is actually, like, the…

102
00:14:13.730 --> 00:14:29.680
Aekasitt Guruvanich: how you do PIC in, in TypeScript, and the bottom part is, like, how we… how we can actually do PIC, in, in Python in the future. So this… this one actually is under review at the moment, but I… I do think, like, it… it has a very good chance of, like, actually being merged in.

103
00:14:30.030 --> 00:14:38.310
Aekasitt Guruvanich: So we… as you can see, you can see the… the word, like, new protocol and ITIL, in… in the typing, keyword, right… right there.

104
00:14:39.320 --> 00:14:51.709
Aekasitt Guruvanich: And the next one's actually, like, gonna be omit, right? So, like, now that we can actually, like, do, like, type definition, like, without having to, like, have a separate module file with, like, 200, like, lines of, like, redefinition.

105
00:14:51.910 --> 00:14:56.049
Aekasitt Guruvanich: Creating, like, more vectors, like, more area of, like, actually

106
00:14:56.860 --> 00:15:05.139
Aekasitt Guruvanich: areas of, error-prone, code, we can do that with, like, just, like, using new keywords here, which is the new protocol item is assignable.

107
00:15:06.150 --> 00:15:09.450
Aekasitt Guruvanich: But I do think, like, these two things alone, like, CAIC and O

108
00:15:09.600 --> 00:15:22.669
Aekasitt Guruvanich: selecting attributes, like, from, one, or, like, basically deselecting, like, attributes from one when you're coding, like, a type. It's actually gonna, like, basically, like, make, type programming in, Python, like, type metapro

109
00:15:24.000 --> 00:15:36.469
Aekasitt Guruvanich: And I think this is the last topic that I have right here. Maybe I'm actually, like, speaking a bit too fast, so, like, maybe, like, I don't think it's, like, 15 minutes yet. But yeah. So, the… the last part here is actually,

110
00:15:36.470 --> 00:15:46.280
Aekasitt Guruvanich: It is a performance-focused part of Python. I think that, like, a lot of people, when they use, like, Python, like, as the convention goes, like, we put a lot of our

111
00:15:46.600 --> 00:15:49.900
Aekasitt Guruvanich: Import the statement in the top of the model file.

112
00:15:50.060 --> 00:15:53.460
Aekasitt Guruvanich: Which is, which is, sometimes it can actually

113
00:15:53.670 --> 00:16:10.299
Aekasitt Guruvanich: slow down, like, our app start time. This will obviously, like, affect you more, like, if you actually use, like, a serverless environment, like, to actually do, like, a Python, kind of endpoint, or Python, Python, like, workflow in a Lambda or, like, a serverless environment.

114
00:16:10.330 --> 00:16:13.909
Aekasitt Guruvanich: And in the future, like, I think that we're gonna have, like, two…

115
00:16:14.130 --> 00:16:24.650
Aekasitt Guruvanich: consider about, like, disk performance, like, overhead, like, in a WASM environment as well, like, say, in the WebAssembly, like, environment, which, again, Python actually is, like, very good

116
00:16:25.190 --> 00:16:25.890
Aekasitt Guruvanich: Oh.

117
00:16:26.120 --> 00:16:42.180
Aekasitt Guruvanich: you might have to consider using an explicit key, which is, like, the lazy import. So, it's scheduled for release in this year, in October, and the explicit, lazy import here, from the proposal itself, you already see, like, 70%

118
00:16:42.720 --> 00:16:46.919
Aekasitt Guruvanich: Performance improvement, in terms of, like, up to, startup time.

119
00:16:47.420 --> 00:16:56.879
Aekasitt Guruvanich: I think that, like, if you prefer to actually have, like… once we… when we start having this, like, for a long time, like, we… we now know, like, hey, like, there is no…

120
00:16:57.320 --> 00:17:03.830
Aekasitt Guruvanich: Other reason to actually do… do it the old way, you can also, like, start, activating the flag as well in your…

121
00:17:04.170 --> 00:17:07.790
Aekasitt Guruvanich: Python runtime. I think, like, we can actually accept this in the…

122
00:17:08.160 --> 00:17:15.259
Aekasitt Guruvanich: pyproject.toml file to actually say we always do lazy loading all the time instead of doing it explicitly.

123
00:17:16.220 --> 00:17:30.259
Aekasitt Guruvanich: And, if you want to do it today, you can also use it today. I think, like, we also underestimate, like, how good tooling in Python has become. Like, a lot of the consolidation has been happening, like, using, again, like, Rust.

124
00:17:30.850 --> 00:17:40.439
Aekasitt Guruvanich: If you use UV package manager in Python, you can set up like a virtual environment. You can install the latest beta release of Python 3.15.

125
00:17:40.770 --> 00:17:50.719
Aekasitt Guruvanich: And it's already been supported. This syntax of using explicit lazy loading has already been supported by the formatter and the linter.

126
00:17:50.910 --> 00:17:53.429
Aekasitt Guruvanich: And the language, it's level 4 already, so…

127
00:17:53.820 --> 00:17:55.559
Aekasitt Guruvanich: You can all use it today.

128
00:17:55.960 --> 00:17:59.470
Aekasitt Guruvanich: And that is it. Any question?

129
00:18:07.440 --> 00:18:11.910
Gabor Szabo: Do you actually use this one, this version of Python?

130
00:18:13.740 --> 00:18:15.670
Aekasitt Guruvanich: The the next one? Yes, I do.

131
00:18:16.810 --> 00:18:20.719
Gabor Szabo: For some production use, or development, or how do you use it?

132
00:18:21.930 --> 00:18:23.110
Aekasitt Guruvanich: Right now, like.

133
00:18:23.440 --> 00:18:39.689
Aekasitt Guruvanich: right now, basically, like, I do a lot of, CICD pipeline that actually use, that actually use, like, UV in the pipeline itself. So, like, right now, like, I space, like, a lot of my tech stack to using, like, the… I'm not sure you have heard of, like, JUST,

134
00:18:39.960 --> 00:18:46.040
Aekasitt Guruvanich: it is essentially, like, a ZMake version of, like, using Rust, right? So…

135
00:18:46.040 --> 00:18:46.819
Gabor Szabo: Give me a hand.

136
00:18:47.520 --> 00:19:01.889
Aekasitt Guruvanich: Yeah, so I would use Jest, and instead of, like, writing an Excel script, like, I would, write everything in, like, in Python instead. So, like, I would have, like, basically a process runner, like, a command line runner, like, all in, in Jest. And, like, this whole thing that I, I write

137
00:19:02.030 --> 00:19:11.009
Aekasitt Guruvanich: Gets imported to, like, the CICD pipeline immediately. So, like, I would say, like, hey, like, here's how… here's the first file you look at in my repository, which

138
00:19:11.350 --> 00:19:12.820
Aekasitt Guruvanich: It basically, like.

139
00:19:12.950 --> 00:19:30.840
Aekasitt Guruvanich: if, if, if I do it, like, a project that I know, like, I'm gonna use by myself, like, I would use Tailscript, like, easy, easier, like, kind of integration for, like, setting up something new. But, like, if I know, like, I'm gonna have to, like, share this, like, around, like, with my juniors, right? Like, I would use, I

140
00:19:31.270 --> 00:19:34.499
Aekasitt Guruvanich: And, like, write everything out in Python, because, like, that way.

141
00:19:34.730 --> 00:19:37.939
Aekasitt Guruvanich: Managing, like, a large project with, like, with

142
00:19:38.670 --> 00:19:45.299
Aekasitt Guruvanich: with colleagues and with juniors, like, would be much easier. So, like, I usually be… and I try to basically, like, you know.

143
00:19:45.790 --> 00:19:51.150
Aekasitt Guruvanich: If it's, like, a lazy import, something like this, like, it's actually, like, it shows performance, like.

144
00:19:51.650 --> 00:19:54.490
Aekasitt Guruvanich: The longer, like, my command, like, run it goes through.

145
00:19:56.080 --> 00:19:57.979
Gabor Szabo: Jacob, you wanted to ask something?

146
00:19:59.000 --> 00:20:05.160
Jacob Barhak: Yeah, I'm So, I'm curious about the global interpreter lock.

147
00:20:05.300 --> 00:20:12.310
Jacob Barhak: So, we've been hearing the rumors all the way, all the time, for, like, a year or two or something, and…

148
00:20:12.490 --> 00:20:30.389
Jacob Barhak: I was… I don't know… actually, tell me more about the Global Interpreter Lock, because I'm curious about how it will look like. I do a lot of high-performance computing. The question is, will it help me at all, or do I… will I still have to use all those external libraries, like Dask, Gray, whatever?

149
00:20:32.230 --> 00:20:41.469
Aekasitt Guruvanich: it depends on, like, what you use with it, right? So, like, for example, like, if you're using a… if you're, like, writing down, like, a production-grade, like,

150
00:20:41.990 --> 00:20:43.280
Aekasitt Guruvanich: Yeah.

151
00:20:44.300 --> 00:20:55.909
Aekasitt Guruvanich: if you're using, like, protocol-level, programming, like, I think, like, what you run into, like, immediately is that, like, you do want to, like, basically spread your work into, like, different, different threads.

152
00:20:56.140 --> 00:21:04.340
Aekasitt Guruvanich: And, like, what we had with that is, like, we don't use, like, a, like, setting when you process completely. What we have with that is, like, asynchronous programming.

153
00:21:04.740 --> 00:21:10.080
Aekasitt Guruvanich: And asynchronous programming for Python is not true asynchronous programming.

154
00:21:10.450 --> 00:21:18.160
Aekasitt Guruvanich: So, like, right now, essentially, it's like we're untying the knot of, like, hey, like, all about async threats in Python.

155
00:21:18.330 --> 00:21:21.119
Aekasitt Guruvanich: They all can only use, like, one interpreter lock.

156
00:21:21.600 --> 00:21:29.329
Aekasitt Guruvanich: We're just untying that knot, and we're basically saying, like, okay, like, we're gonna, we're gonna let, we're gonna let each strat have its own.

157
00:21:29.520 --> 00:21:32.129
Aekasitt Guruvanich: And that's all we're doing. So.

158
00:21:32.240 --> 00:21:42.379
Aekasitt Guruvanich: Essentially, you will not feel it immediately because, like, again, like, I think that people always underestimate, like, how fast Python already is.

159
00:21:42.650 --> 00:21:46.630
Aekasitt Guruvanich: It is a slow language when you compare it to the lower level programming.

160
00:21:46.900 --> 00:21:50.800
Aekasitt Guruvanich: But like for a higher level programming, it's always been.

161
00:21:51.010 --> 00:21:53.120
Aekasitt Guruvanich: Fairly optimized, I would say.

162
00:21:53.660 --> 00:21:58.960
Aekasitt Guruvanich: So you're gonna see that in, in the, in the binaries. So this is why I brought this up, like,

163
00:21:59.190 --> 00:22:09.910
Aekasitt Guruvanich: Essentially, it's like, if you're using, free threading, a lot of, like, the underlying, popular wheels in Python, they have to adopt it, and then we feel it.

164
00:22:10.630 --> 00:22:15.260
Aekasitt Guruvanich: So, like, a lot of this, for example, like, I use, Pedantic Call every day.

165
00:22:15.820 --> 00:22:18.210
Aekasitt Guruvanich: Right? I use, like, pedantic cards, like.

166
00:22:18.470 --> 00:22:21.699
Aekasitt Guruvanich: Embedded more type information in my code base.

167
00:22:21.880 --> 00:22:25.790
Aekasitt Guruvanich: And, like, the faster Python decor is, the faster my code base is.

168
00:22:26.240 --> 00:22:27.790
Aekasitt Guruvanich: So, this is how you would view it, right

169
00:22:28.140 --> 00:22:31.410
Aekasitt Guruvanich: But if, if, if your project is like, you know.

170
00:22:31.970 --> 00:22:43.309
Aekasitt Guruvanich: I do have to say, there also is a performance impact as well. Like, some code will get slower, because, like, if we're not, like, if we're not, like, writing complicated, like, complex, like, large code base.

171
00:22:43.340 --> 00:22:54.879
Aekasitt Guruvanich: Like, you know, like there is a, performance cost of like actually having free threading because that means like the, the base interpreter itself also has like do actual like a parallelism now.

172
00:22:54.880 --> 00:23:07.299
Aekasitt Guruvanich: there is an overhead there, but, like, if you're, if you're, like, writing a large, complex project, I think, like, you will see it immediately, like, you will see that, like, there is performance improvement in, in my async code.

173
00:23:08.560 --> 00:23:12.880
Jacob Barhak: Okay, so this is aimed mostly for us in code. Okay, got it.

174
00:23:14.100 --> 00:23:14.630
Aekasitt Guruvanich: Yeah, okay.

175
00:23:14.780 --> 00:23:27.110
Jacob Barhak: Gabor, you… you were asking the same question for a while, Gabor. We've been having the conversation. Perhaps, unless someone else has a question, perhaps you should ask him the AI question?

176
00:23:29.550 --> 00:23:36.570
Gabor Szabo: Well, let's let other people ask questions first about the main topic of this presentation.

177
00:23:39.410 --> 00:23:43.450
Gabor Szabo: Anyone else? There are a couple of more people here.

178
00:23:43.650 --> 00:23:45.660
Gabor Szabo: who might want to ask questions.

179
00:23:50.710 --> 00:23:56.659
Gabor Szabo: No question. Well, go ahead, ask that question, Jacob, if you really want.

180
00:23:56.660 --> 00:24:02.790
Jacob Barhak: It's your question. I'll rephrase his question.

181
00:24:03.170 --> 00:24:13.029
Jacob Barhak: Gabor and I are both trying to figure out what's the place in Python with all this AI coming in, like, the AI wave. It's like one… one…

182
00:24:13.180 --> 00:24:17.849
Jacob Barhak: One language is not enough, and people are using whatever now, so…

183
00:24:18.600 --> 00:24:21.529
Jacob Barhak: We're kind of debating it, like.

184
00:24:21.700 --> 00:24:28.139
Jacob Barhak: What do you think? Like, by the way, Python kind of created AI of today. Think about it.

185
00:24:28.280 --> 00:24:33.500
Jacob Barhak: Like, underneath, it's all Python. So, what do you think, like…

186
00:24:33.930 --> 00:24:40.060
Jacob Barhak: How does Python will shape itself in the future to join this force?

187
00:24:44.180 --> 00:24:58.250
Aekasitt Guruvanich: So, like, let me… let me answer in two ways. Like, basically, I… we did have a conversation, like, with a company that, like, gone full… fully AI, as in, like, they… they're, like, trying to, like, replace their junior, employees with, like, you know, like, a…

188
00:24:58.360 --> 00:25:05.980
Aekasitt Guruvanich: multiplexing of, like, Agentic, like, flow and everything. So, like, that person, like, obviously,

189
00:25:07.150 --> 00:25:21.729
Aekasitt Guruvanich: he, he, he thinks that, like, basically, like, language like Python is gonna die, because, like, you know, like, we don't actually need, like, we don't need easier language for, like, the junior depth anymore, and I completely disagree with him, because, like, you know, I think that, what has proven to, like

190
00:25:21.910 --> 00:25:23.270
Aekasitt Guruvanich: More and more…

191
00:25:23.420 --> 00:25:32.010
Aekasitt Guruvanich: true over time, is that, like, we have layers of, like, abstraction, and the AI is going to be really good at, like, the higher level abstraction.

192
00:25:32.110 --> 00:25:46.940
Aekasitt Guruvanich: And people can focus more on the medium layer of tracking, the protocol level of work, and the kernel level of work, which AI has proven time and time again to just be really bad at, right? I do think that when it comes down to, like, where Python actually lies, it…

193
00:25:47.050 --> 00:25:54.779
Aekasitt Guruvanich: Python has never been… I would say that, like, Python has always been the right mix of no.

194
00:25:55.260 --> 00:25:57.199
Aekasitt Guruvanich: Higher level of traction, because

195
00:25:59.760 --> 00:26:19.400
Aekasitt Guruvanich: We are slow on purpose. We say, hey, if my code is going to only touch the starting point for two seconds, I would rather focus a lot of my implementation time in the protocol of stuff, and then I can actually adapt, make it more versatile, and make new abstraction with Python.

196
00:26:19.420 --> 00:26:25.920
Aekasitt Guruvanich: And we see that. We see, like, Python has, like, the runtime reflection, like, made up it make…

197
00:26:27.390 --> 00:26:44.579
Aekasitt Guruvanich: coding Python, like, really enjoyable, and we get to see newer abstractions, we get to see newer tricks and, tips and tricks in Python first. I do think, like, Python is gonna be the threshold breaker there. Like, where it actually is, like, it means that, like.

198
00:26:45.130 --> 00:27:04.020
Aekasitt Guruvanich: AI is going to be really good at churning out code in Python, like 20,000 lines, and cause the hugest amount of growth as possible. And the people who understood Python as what it's supposed to do are the people who just say, well, I want to have 20 lines of Python here, because I know how to use these packages.

199
00:27:04.550 --> 00:27:10.569
Aekasitt Guruvanich: underlying, connectivity, like, I know where everything is, like, I know why this works.

200
00:27:10.710 --> 00:27:16.189
Aekasitt Guruvanich: And I know why the trade-off here is amazing. I don't even think, like, I've ever had a product

201
00:27:16.550 --> 00:27:17.890
Aekasitt Guruvanich: Productive conversation.

202
00:27:18.210 --> 00:27:31.119
Aekasitt Guruvanich: with my LLMs about trade-offs. I do not think they understand that term fully. They understand the definition of it, but they don't understand the temporal effect of trade-offs.

203
00:27:33.540 --> 00:27:51.160
Jacob Barhak: I agree with you about today. Those things are going fast. The question is like, here, when you actually work on Python, are you using a lot of LLMs to support, to help you in doing this? I assume yes by now, but in the future, will…

204
00:27:51.360 --> 00:27:56.200
Jacob Barhak: PEPs will be added… AI will suggest PEPs and decide on them?

205
00:27:56.460 --> 00:28:07.660
Jacob Barhak: Like, 10 years into the future. This is what I'm trying to think. It's like, where will it go, the Python Foundation? Are we going in the direction that things will be automated more and more?

206
00:28:08.090 --> 00:28:10.090
Jacob Barhak: Or will it be human-centered?

207
00:28:11.060 --> 00:28:15.100
Aekasitt Guruvanich: Okay, so the most controversial thing I said today was about, like, Python and types.

208
00:28:15.370 --> 00:28:24.770
Aekasitt Guruvanich: And the second most controversial thing I'm gonna say today is that, like, we are literally, like, witnessing, like, the… a dumber generation than the last of humans.

209
00:28:26.020 --> 00:28:38.119
Aekasitt Guruvanich: And, like, you know, like, how AI is trained. Like, AI is trained in human data. So, like, I do not agree with you that, basically, we're gonna see, like, a Cameron explosion of, like, AI intelligence. I genuinely think that, like.

210
00:28:38.210 --> 00:28:49.400
Aekasitt Guruvanich: machine intelligence, you know, is gonna be, like, derivative of, like, human intelligence, and I do not see that going up forward forever. Like, we are witnessing one that's going backwards, so, yeah.

211
00:28:49.610 --> 00:28:50.979
Aekasitt Guruvanich: There is a regression.

212
00:28:53.670 --> 00:28:55.419
Gabor Szabo: Okay, okay.

213
00:28:55.420 --> 00:29:00.850
Aekasitt Guruvanich: That was only the second most controversial thing I said today. Again, Python and Type, way more controversial.

214
00:29:01.830 --> 00:29:09.039
Gabor Szabo: Yeah. Okay. Well, thank you very much for the presentation and for the answering these.

215
00:29:09.170 --> 00:29:11.370
Gabor Szabo: worrying questions.

216
00:29:12.130 --> 00:29:23.579
Gabor Szabo: And thank you for everyone who participated. I think it's always nice to have a set of people listening in. And if you are watching the…

217
00:29:23.580 --> 00:29:32.799
Gabor Szabo: the video then please don't forget to like the video and follow the channel and see you at one of our next events

218
00:29:33.290 --> 00:29:34.140
Gabor Szabo: Bye bye.

219
00:29:35.880 --> 00:29:37.199
Aekasitt Guruvanich: Thank you so much for your time.

220
00:29:37.200 --> 00:29:38.709
Gabor Szabo: Thank you very much for your.

