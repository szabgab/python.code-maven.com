---
title: Everything you need to know about docstrings, but never wanted to ask
timestamp: 2026-08-27T10:10:01
author:
published: true
description:
tags:
    - docstring
---

## ABSTRACT

Remember early grade school and those repetitive handwriting drills in exercise books? We grew up and swapped notebooks for a code editor, but the habit stuck. Let's face it: for most developers, writing docstrings is just another programmer drill - something we feel forced to do, even though few remember why. It ends up acting as nothing more than a graphical separator between a function's signature and its implementation.

Many of us live with the mindset that "good code documents itself," making triple quotes feel like a waste of time. The result? We either skip docstrings entirely or generate automated monstrosities that proudly reveal `get_user_id(user)` is meant to... get user id.

Join this session if you dread writing docstrings. I promise that afterwards, you're still allowed to dislike it - but at least doing it will be less painful and far more useful!


## BIO

About [Maria Lowas-Rzechonek](https://www.linkedin.com/in/maria-lowas-rzechonek-1a215150/)

I graduated in philosophy and social science. True to Zed A. Shaw's advice from "Learn Python the Hard Way", I entered the tech world as "an anthropologist with barely enough of the local language to get around and survive". My next step led me to the Django Girls community - first as an attendee, then as a coach, committer and organizer. I have been working as a Python developer since 2016. I was a speaker at DjangoCon Europe 2016, EuroPython 2026 and Pykonik (the Kraków Python community).

In my free time, I’m involved in the extreme sport of mountain hiking with my kids, as well as dancing flamenco.


{% youtube id="6dqmFnMHW-E" file="2026-08-26-everything-you-need-to-know-about-docstrings-with-maria-lowas-rzechonek.mp4" %}

## Notes

* [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
* [PEP 287 - reStructuredText Docstring Format](https://peps.python.org/pep-0287/)
* [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
* [doctest - Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
* [Python Comments and Docstrings](https://zetcode.com/python/comments-docstrings/)
* [Diátaxis A systematic approach to technical documentation authoring.](https://diataxis.fr/)

## Transcript


1
00:00:01.840 --> 00:00:23.989
Gabor Szabo: So, hello and welcome to the Code Maven channel. It's a Code Maven YouTube channel you're going to watch. It's in the video. My name is Gabor Szabo. I am the host of this. I organize events in various topics, like Python, Rust, Perl. We are going to have a PHP, the first PHP session, and other topics, Postgres.

2
00:00:23.990 --> 00:00:27.209
Gabor Szabo: and AI-related presentations,

3
00:00:27.690 --> 00:00:44.000
Gabor Szabo: And with us today is Maria, and you'll say your full name, because I'm not there… I don't dare to try to say it. I'm really happy to have you here and give you the stage in a second.

4
00:00:45.140 --> 00:01:08.019
Gabor Szabo: Those who are here at the present at the live event, or the presentation, feel free to ask me… ask us questions, ask Maria questions in the chat. I will read them out, and after the presentation, as I mentioned earlier, once the recording is finished, feel free to stay around, and then we can have a free chat. That's sort of the privilege of

5
00:01:08.050 --> 00:01:09.890
Gabor Szabo: Being in the…

6
00:01:10.210 --> 00:01:28.039
Gabor Szabo: presentation, and if you're watching it on YouTube, then you will find a link below the video for various things that are mentioned in this presentation and to the future events. So, with that said, Maria, thank you very much again to

7
00:01:28.200 --> 00:01:35.020
Gabor Szabo: agreeing to give this presentation. The stage is yours. Please introduce yourself, and go ahead.

8
00:01:35.640 --> 00:01:54.519
Maria Lowas-Rzechonek: Okay, thank you for having me here. So, my full name is Maria Lowaszechonek. This is kind of the Polish version of half Hungarian, half Czech surname, so it's, like, kind of crazy, I know. And today, I would like to

9
00:01:54.560 --> 00:02:01.290
Maria Lowas-Rzechonek: tell you everything that you need to know about dock strings, but probably you don't even want to ask.

10
00:02:01.900 --> 00:02:20.199
Maria Lowas-Rzechonek: to start… to begin with, I would like to ask a few questions. I know that I won't be able to see the answer, but it's more about having you think about… about the answers… answers. So, first of all, I would like to ask, how many of you believe in self-documenting code?

11
00:02:21.870 --> 00:02:29.340
Maria Lowas-Rzechonek: And, maybe some of you has used this idea of style documenting code as an excuse not to write docstrings.

12
00:02:31.160 --> 00:02:43.600
Maria Lowas-Rzechonek: And maybe some of you end up, like, muttering under the breath some bad words for people who don't write dog strings, or documentation at all.

13
00:02:44.820 --> 00:02:55.690
Maria Lowas-Rzechonek: So, as a developer, we usually have this kind of dual attitude towards documentations, and docstring probably especially.

14
00:02:55.950 --> 00:03:02.239
Maria Lowas-Rzechonek: But… We know they are useful, but we are not very keen on writing them.

15
00:03:02.240 --> 00:03:08.340
Gabor Szabo: So just one comment here, sorry. So once someone commented that self-documenting code includes docstrings.

16
00:03:08.340 --> 00:03:27.290
Maria Lowas-Rzechonek: All right, that's… that's nice. So, when thinking about it, I have this… it reminds me of some kind of manual drill that we used to do in the primary school. I don't know whether it is something done

17
00:03:27.340 --> 00:03:37.770
Maria Lowas-Rzechonek: in other places, but when I was young, we need to do some, like, this, little drawings, little patterns, between lessons,

18
00:03:38.440 --> 00:03:57.009
Maria Lowas-Rzechonek: And they separated one lesson from another. It looked more or less like this, but, this image is quite, like, elaborate. The patterns could be very easy. And actually, also, were great, you could get grades, depending on how,

19
00:03:57.150 --> 00:04:02.330
Maria Lowas-Rzechonek: carefully, and how neat you've done it. So, many people hated it.

20
00:04:02.570 --> 00:04:07.850
Maria Lowas-Rzechonek: And also, as a child, you really didn't understand, what they are for.

21
00:04:08.620 --> 00:04:24.720
Maria Lowas-Rzechonek: And sometimes, maybe the doc strings are just like that. It's just, they are just, like, graphical, really, pattern that separates the function signature from the implementation.

22
00:04:24.860 --> 00:04:30.160
Maria Lowas-Rzechonek: They even are usually, like, colored, for different… on different colors, so,

23
00:04:30.290 --> 00:04:41.319
Maria Lowas-Rzechonek: sometimes they are just like that. And for many of you, for many of us, this seems to be, like, chores that we don't really like.

24
00:04:41.320 --> 00:04:52.730
Maria Lowas-Rzechonek: we know, somehow, know that we should do this, but we… and we might also don't understand, really, what we are for. So, I hope that after this presentation,

25
00:04:53.580 --> 00:05:06.440
Maria Lowas-Rzechonek: I can change at least some of perceptions like this, and maybe to bring more clarity about dock strings, what they can be used for.

26
00:05:07.430 --> 00:05:22.010
Maria Lowas-Rzechonek: But, first of all, I, before that, I would like to say a few words about myself. So, I'm not a person for, to whom writing comes naturally. I am dyslexic, and, writing,

27
00:05:23.080 --> 00:05:30.210
Maria Lowas-Rzechonek: has always been hard and difficult, and took a lot of effort for me. So… yeah, I…

28
00:05:31.130 --> 00:05:34.890
Maria Lowas-Rzechonek: It's just as… Oh, what's, what's this noise?

29
00:05:36.420 --> 00:05:37.750
Maria Lowas-Rzechonek: Someone joined.

30
00:05:38.660 --> 00:05:39.220
Maria Lowas-Rzechonek: Yeah.

31
00:05:39.220 --> 00:05:42.169
Gabor Szabo: I turn off this beep, it's what, when someone is joining.

32
00:05:44.000 --> 00:05:50.040
Maria Lowas-Rzechonek: And then, during my studies, I started… I studied philosophy, and,

33
00:05:50.850 --> 00:06:05.830
Maria Lowas-Rzechonek: It was about, reading very difficult… difficult text, and, looking for some, main idea, main principle underneath the text we are, we are reading.

34
00:06:07.810 --> 00:06:10.999
Maria Lowas-Rzechonek: So, it was also about finding

35
00:06:11.110 --> 00:06:20.130
Maria Lowas-Rzechonek: What's actually underneath the words that can be difficult, that can be hard to understand, and maybe too complex,

36
00:06:20.360 --> 00:06:22.620
Maria Lowas-Rzechonek: For what purpose they are used.

37
00:06:22.730 --> 00:06:35.789
Maria Lowas-Rzechonek: A few years later, I started working as a technical writer, and my task was to put difficult, complex things into very simple language, because documentation

38
00:06:36.060 --> 00:06:54.250
Maria Lowas-Rzechonek: It needs to be, easily accessible, as you don't read it for pleasure, you usually read it, to find something, to find something quickly, and very often there is a time, pressure on you of some sort that you want to do it quickly.

39
00:06:54.250 --> 00:07:00.960
Maria Lowas-Rzechonek: So, as a technical writer, you must always remember that things you're writing should be as easy as possible.

40
00:07:01.070 --> 00:07:13.659
Maria Lowas-Rzechonek: And, afterwards, I started working as a software developer, which I also do now, and I've learned this dual attitude, that on the other hand.

41
00:07:13.810 --> 00:07:27.709
Maria Lowas-Rzechonek: I really like to see good documentation for new things, for libraries, for new code, etc. But on the other hand, when I'm working on the implementation, very often,

42
00:07:29.100 --> 00:07:40.720
Maria Lowas-Rzechonek: Documentation seems something, unnecessary, something that you need to do, but you really prefer to do something else, that you just do…

43
00:07:40.870 --> 00:07:44.089
Maria Lowas-Rzechonek: As quickly as possible, just to have it done.

44
00:07:44.670 --> 00:08:03.840
Maria Lowas-Rzechonek: Yeah, so this is my background, and now I can tell you more about what I want to talk about today. So, first of all, I want to say what are doc strings, and what are… what is their function. Then, I want to say a few words about what to document and what not to document.

45
00:08:05.410 --> 00:08:13.389
Maria Lowas-Rzechonek: I will also… I will also mention the recommended structure for docstrings and popular formats for them.

46
00:08:13.550 --> 00:08:23.589
Maria Lowas-Rzechonek: I would say a few words about language… what language to use, and also just very briefly about tooling we can use to help us.

47
00:08:23.700 --> 00:08:28.890
Maria Lowas-Rzechonek: When preparing to my talk, I use, PEP for…

48
00:08:29.150 --> 00:08:48.359
Maria Lowas-Rzechonek: at least two paps about doc strings, and there were also a few paps about generating documentation from the code. I also used Google's style guide… style guideline for Python, and some blogs, and also my own opinions

49
00:08:48.520 --> 00:08:52.839
Maria Lowas-Rzechonek: and experience that I have because… during my, my work.

50
00:08:54.510 --> 00:09:05.760
Maria Lowas-Rzechonek: Okay, and… S… to begin with, this is the opening paragraphs from PEP 257.

51
00:09:05.770 --> 00:09:24.040
Maria Lowas-Rzechonek: This is the main pep about dog strings, and it says a dog string is a string, literal, that occurs as the first statement in the module function class or method definition, and such a docstring becomes the dunderdog special attribute of that object.

52
00:09:24.070 --> 00:09:40.890
Maria Lowas-Rzechonek: So from that, we can see that docstrings are not just comments, just… they're not just normal comments, they are live objects, and they can be accessed at runtime. We'll see more of that.

53
00:09:40.920 --> 00:10:00.730
Maria Lowas-Rzechonek: What's more, string literals occurring elsewhere in Python code may also act as documentation. They are not recognized by the Python bytecode compiler, and are not accessible as runtime object attributes. So, docstrings have a special,

54
00:10:01.470 --> 00:10:06.220
Maria Lowas-Rzechonek: With a special power, let's say. And it is used

55
00:10:06.430 --> 00:10:12.159
Maria Lowas-Rzechonek: And I will show you in a bit how it is used in some places.

56
00:10:14.690 --> 00:10:21.900
Maria Lowas-Rzechonek: So, let's, let's say something more about the underdog attribute.

57
00:10:21.970 --> 00:10:38.660
Maria Lowas-Rzechonek: let's have this kind of endpoint written as FastAPI. This is very simple documenta- very simple docstrings, maybe not the perfect one, but anyway, we have everything should be, and it looks like this.

58
00:10:38.950 --> 00:10:48.070
Maria Lowas-Rzechonek: Mmm… So, now when we open, Python Intent Pretter, and just, return dunder docs.

59
00:10:48.110 --> 00:11:00.849
Maria Lowas-Rzechonek: We can see this text, but without… with no formatting. But, of course, we can print it, and then we can see it in a proper way, and we can read it and learn something about the function.

60
00:11:01.990 --> 00:11:06.509
Maria Lowas-Rzechonek: But this is with Underdog, so,

61
00:11:06.780 --> 00:11:21.800
Maria Lowas-Rzechonek: Usually, we don't need to use these magic methods and attributes for very simple things. So, in fact, there is the help function, and if you run it on a…

62
00:11:22.360 --> 00:11:40.229
Maria Lowas-Rzechonek: function, you will see more or less what I saw you in a moment from printing it, but if you call help on the module, you will see a short summary of everything that is inside this module.

63
00:11:41.050 --> 00:11:47.499
Maria Lowas-Rzechonek: So, it can be… so, as you see, it can be, helpful, like, in getting to know the new code.

64
00:11:48.770 --> 00:11:55.489
Maria Lowas-Rzechonek: Also, Python, comes with, PyDoc modules, module, and,

65
00:11:56.180 --> 00:12:05.109
Maria Lowas-Rzechonek: It can process the underdog attribute to produce three kinds of output.

66
00:12:05.110 --> 00:12:23.260
Maria Lowas-Rzechonek: The first one is in the console, and the help function use PyDoc, but you can also save the output to the HTML5 file, or serve it from the browser. And here is the sample output.

67
00:12:23.260 --> 00:12:28.839
Maria Lowas-Rzechonek: From, use, generated by,

68
00:12:29.000 --> 00:12:36.349
Maria Lowas-Rzechonek: with a minus B option, the graphical interface is quite…

69
00:12:36.460 --> 00:12:43.619
Maria Lowas-Rzechonek: I don't know, peculiar, I would say, with those crazy colors. It's really very colorful. But,

70
00:12:43.840 --> 00:12:58.189
Maria Lowas-Rzechonek: You, you have all the information about the module, and also about modules, implement, imported, in your, in the code in such a… in this way, so, you have all the information in one place, if you… if you need them.

71
00:12:59.300 --> 00:13:13.440
Maria Lowas-Rzechonek: But, of course, there are some more modern tools, as this is the FastAPI endpoint. FastAPI comes with Swagger-like documentation, and it looks like this.

72
00:13:13.440 --> 00:13:22.110
Maria Lowas-Rzechonek: And as you see, the doc string you use for a description, it is not formatted anyhow, it's just print… it's just put it there.

73
00:13:24.530 --> 00:13:41.669
Maria Lowas-Rzechonek: And, some fun… well, maybe it's not… it's something that is not, that widely known, that, when you have class, and you have class attributes… attributes, you can put, one-line doc string.

74
00:13:41.720 --> 00:13:47.360
Maria Lowas-Rzechonek: Under… after each, attribute, and they are so-called, attribute docstrings.

75
00:13:47.600 --> 00:14:06.309
Maria Lowas-Rzechonek: they are not accessible via, the underdog, but some tools to process documentation, for example, Sphinx, can process them, and here's also the sample output from Sphinx. So you have,

76
00:14:06.990 --> 00:14:19.139
Maria Lowas-Rzechonek: Yeah, so you have some docs… you have docstring, the main docstring, and you also have docstring attributes in the generated documentation.

77
00:14:21.740 --> 00:14:27.190
Maria Lowas-Rzechonek: Okay, so what is the doc string function? I would just, have a sip,

78
00:14:31.990 --> 00:14:38.019
Maria Lowas-Rzechonek: So, the doc string should document the code usage.

79
00:14:38.120 --> 00:14:41.340
Maria Lowas-Rzechonek: And, it is available at runtime.

80
00:14:42.370 --> 00:14:46.979
Maria Lowas-Rzechonek: It can also be used for generating documentation from code.

81
00:14:47.560 --> 00:14:58.279
Maria Lowas-Rzechonek: It provides supports from IDE, because IDE uses, docstrings for indexing, but also provides some tooltips, and things like that.

82
00:14:58.420 --> 00:15:06.920
Maria Lowas-Rzechonek: Also, LLM uses doc strings, and it also… you also need to be careful with that, because

83
00:15:06.990 --> 00:15:23.490
Maria Lowas-Rzechonek: sometimes LLMs can read docstring and believe that it's true, and don't read implementation. And it happened to me that because the docstring was not up to date, LLM

84
00:15:23.540 --> 00:15:29.240
Maria Lowas-Rzechonek: just believe in docstring and done everything as if it was,

85
00:15:29.830 --> 00:15:40.609
Maria Lowas-Rzechonek: Correct. So, of course, it also, we have one of the criticism about dog strings, but you need to keep them up to date. But for me,

86
00:15:42.740 --> 00:15:49.229
Maria Lowas-Rzechonek: Well… If you do it properly, it shouldn't be that much of a problem.

87
00:15:49.700 --> 00:15:52.209
Maria Lowas-Rzechonek: But we'll see it in a bit.

88
00:15:53.280 --> 00:16:00.829
Maria Lowas-Rzechonek: Docstrings can also be treated as a sign of bad code, because if you struggle to write a docstring,

89
00:16:01.150 --> 00:16:06.000
Maria Lowas-Rzechonek: Maybe the separation of concern in your code is not good.

90
00:16:07.230 --> 00:16:19.200
Maria Lowas-Rzechonek: And dock strings can also help, with design, so if you're preparing some code, skeleton for your, solution,

91
00:16:20.030 --> 00:16:37.149
Maria Lowas-Rzechonek: You can put function signature and a very short docstring with, for example, attributes and return types, and it can help you to design all the interaction between different functions and methods properly.

92
00:16:38.980 --> 00:16:42.620
Maria Lowas-Rzechonek: So, what to document and what not to document?

93
00:16:43.380 --> 00:16:46.590
Maria Lowas-Rzechonek: Not each and every function needs a docstring.

94
00:16:49.510 --> 00:17:02.699
Maria Lowas-Rzechonek: There is no value, at least this is my opinion, so, so, yeah, that there is no value if putting docstring everywhere in your code, in every function, in every method,

95
00:17:03.200 --> 00:17:19.940
Maria Lowas-Rzechonek: well, bad dog string is worse than no dog string, so it's better to just delete the dog string and keep it as is. Also, I think that you should be, have this kind of minimalistic approach to dog strings, because really.

96
00:17:21.310 --> 00:17:24.489
Maria Lowas-Rzechonek: They should be up to, up to the point.

97
00:17:24.730 --> 00:17:30.479
Maria Lowas-Rzechonek: And if not necessary, they just should be, shouldn't be there at all.

98
00:17:32.020 --> 00:17:45.029
Maria Lowas-Rzechonek: So what, what things deserve a dog string? Pep257 says about module classes and functions exported by the module.

99
00:17:45.060 --> 00:17:56.090
Maria Lowas-Rzechonek: And, Google, style guide, says also about public IPI, functions, with no trivial logic or long functions.

100
00:17:56.250 --> 00:18:12.830
Maria Lowas-Rzechonek: To this, I would add that if your codebase you are working on is not, for example, modularized appropriately, and maybe it's kind of messy and not really nice, you should also add the

101
00:18:12.830 --> 00:18:19.230
Maria Lowas-Rzechonek: Each, method and function that are used outside of your, component.

102
00:18:19.230 --> 00:18:31.880
Maria Lowas-Rzechonek: It should be covered by these four points, but if they are not, also think about it that, yeah, if it's used in different places in the code, it should be documented.

103
00:18:34.780 --> 00:18:45.529
Maria Lowas-Rzechonek: So, what should be put inside the docstring? Docstrings document code usage, and comments document the implementation.

104
00:18:46.080 --> 00:18:58.079
Maria Lowas-Rzechonek: So you can… you should, keep implementation out of the doc string. The only thing worth, putting there is, is your implementation,

105
00:18:58.360 --> 00:19:11.220
Maria Lowas-Rzechonek: results in some side effects which are not non-trivial, but are important for the person who will use your function. So then you should put it in the doc string.

106
00:19:11.880 --> 00:19:18.760
Maria Lowas-Rzechonek: A docstring, contains all the information needed to use the function. So, when…

107
00:19:19.200 --> 00:19:28.670
Maria Lowas-Rzechonek: to use the function. So, again, it's not about implementation, it's about using it. So, each time you're writing a docstring, you can think about,

108
00:19:28.870 --> 00:19:36.509
Maria Lowas-Rzechonek: Someone who just opened the console, import your function, and want to use it, want to close it,

109
00:19:37.040 --> 00:19:42.709
Maria Lowas-Rzechonek: And they want to know what type of information they would need to do it properly.

110
00:19:43.130 --> 00:19:46.750
Maria Lowas-Rzechonek: This is, this is the information that you should put in the doc string.

111
00:19:47.410 --> 00:19:56.869
Maria Lowas-Rzechonek: Docspring should expand the, the function signature without duplicating, without duplicating it. So…

112
00:19:57.430 --> 00:20:15.060
Maria Lowas-Rzechonek: as I put in the example, in the description to this session, if you have a function getUserID, and you put docstring getUserIdentifier, or something like this, then probably you don't use this… you don't need this docstring at all.

113
00:20:15.080 --> 00:20:28.800
Maria Lowas-Rzechonek: Yeah, so in such things, just keep the doc string, don't use it. One exception here is it is a library, or is it a public API? You generate the documentation from…

114
00:20:29.050 --> 00:20:43.070
Maria Lowas-Rzechonek: I don't know, clients or outside users, then, well, everything should have the description, that's obvious, but if you don't have any kind of this requirement, just keep the doc string.

115
00:20:43.640 --> 00:20:48.900
Maria Lowas-Rzechonek: You should put some extra information in it, and not just rephrase the signature.

116
00:20:50.130 --> 00:20:57.680
Maria Lowas-Rzechonek: Also, like, good, good type-hinted function signature is better than a docstring. So.

117
00:20:57.790 --> 00:21:08.410
Maria Lowas-Rzechonek: If you want to choose where to put your effort, go and do proper type hinting. It'd probably more… be more valuable than a docstring.

118
00:21:11.420 --> 00:21:23.529
Maria Lowas-Rzechonek: about attributes, because, like, when you say… when we say type hints, and we think about, I'm sorry, I'm saying… about arguments and returns of a function.

119
00:21:24.160 --> 00:21:27.630
Maria Lowas-Rzechonek: So, without type hints,

120
00:21:29.140 --> 00:21:33.270
Maria Lowas-Rzechonek: There was this suggestion that you should put it in dog string.

121
00:21:33.480 --> 00:21:38.839
Maria Lowas-Rzechonek: If it's not obvious, because sometimes it's obvious. But with type hints.

122
00:21:40.710 --> 00:21:42.900
Maria Lowas-Rzechonek: You don't need to do it as often.

123
00:21:43.100 --> 00:21:56.979
Maria Lowas-Rzechonek: Because, really, what you need is the type of the arguments and returns, and when it's already in the type hints, maybe you don't need to put it in the doc string.

124
00:21:57.080 --> 00:22:07.690
Maria Lowas-Rzechonek: But if you decide that you want to add some extra information about arguments, for example, or return types, then document all arguments.

125
00:22:07.690 --> 00:22:21.200
Maria Lowas-Rzechonek: don't do things like… that you document only one or two arguments which are more complicated, and the obvious one you… you don't mention. So if you put… if you document arguments.

126
00:22:21.530 --> 00:22:25.330
Maria Lowas-Rzechonek: You argue… you document all the document… all the arguments.

127
00:22:25.490 --> 00:22:27.090
Maria Lowas-Rzechonek: But you don't have to do it.

128
00:22:28.260 --> 00:22:32.840
Maria Lowas-Rzechonek: So try to avoid… try to… not to repeat yourself.

129
00:22:33.230 --> 00:22:46.770
Maria Lowas-Rzechonek: For example, if you have some nice and longer documentation for a module, and then you have a function that,

130
00:22:47.950 --> 00:22:59.029
Maria Lowas-Rzechonek: somehow refer to all this information that you already included, you can just add a short docstring and then, add, for more information, see

131
00:22:59.110 --> 00:23:10.370
Maria Lowas-Rzechonek: this fragment of… this fragment of… the documentation for this fragment of code, but you don't repeat the information, at least not all of them,

132
00:23:10.730 --> 00:23:20.179
Maria Lowas-Rzechonek: Because otherwise, it might be misleading, and also there will be a problem with synchronizing the data, the information between different, doc strings.

133
00:23:21.420 --> 00:23:40.489
Maria Lowas-Rzechonek: And also, don't document the framework or Python, standard library. There is no need for writing docstrings for, dunder init, saying that it, initialized the class object, and I've seen such docstrings.

134
00:23:40.490 --> 00:23:42.410
Maria Lowas-Rzechonek: So,

135
00:23:42.410 --> 00:23:57.749
Maria Lowas-Rzechonek: yeah, don't do it. Also, if you use frameworks, for example, like Django, with class-based views, don't document the default methods for views, for example.

136
00:23:58.180 --> 00:24:09.819
Maria Lowas-Rzechonek: What you… what you can do, or even should do, is if you add some, side effects, you change the behavior of this, the default behavior of this,

137
00:24:09.820 --> 00:24:18.480
Maria Lowas-Rzechonek: Methods, so yes, you should document it, and you should also convey the information whether you extend or override the method.

138
00:24:22.780 --> 00:24:29.139
Maria Lowas-Rzechonek: Okay, so, I've spoke a lot, do you have any questions by now?

139
00:24:34.580 --> 00:24:38.850
Gabor Szabo: It seems that people are silent, but if they have questions, feel free to type it in.

140
00:24:40.680 --> 00:24:53.510
Gabor Szabo: I just wanted to say, by the way, about this question of self-documenting code versus docstrings, is what, you also said at one point, is that,

141
00:24:53.540 --> 00:25:03.489
Gabor Szabo: document… the first line here, the docs document code usage, and comments document the implementation. So, a self-documenting code is for… is…

142
00:25:03.590 --> 00:25:07.370
Gabor Szabo: Is that the… It's for the developers.

143
00:25:08.020 --> 00:25:12.660
Gabor Szabo: For the implementation, and the doc strings are primary for the users.

144
00:25:12.890 --> 00:25:19.420
Gabor Szabo: Yep. Whether they are other dev… who are other developers, of course, but for the users, right? Yeah, right.

145
00:25:19.420 --> 00:25:19.850
Maria Lowas-Rzechonek: so…

146
00:25:19.850 --> 00:25:27.290
Gabor Szabo: So that's also the separation, so… That's why they are not…

147
00:25:29.300 --> 00:25:34.190
Gabor Szabo: at odds, at odds with each other, self-documentation and dock strings.

148
00:25:34.480 --> 00:25:43.330
Gabor Szabo: Oh, there's a comment. Google's type, Sphinx, SpyDoc, all precede type hints, and certainly there are more widespread adoption.

149
00:25:43.700 --> 00:25:54.529
Gabor Szabo: Okay, so they were before that. So the repetition of attribute typing seems like bureaucracy and boilerplate. Are any dog schemes

150
00:25:54.740 --> 00:26:00.420
Gabor Szabo: Our any dog schemes are being updated accordingly.

151
00:26:05.130 --> 00:26:08.000
Gabor Szabo: Not sure I understand… totally understand the question here.

152
00:26:08.410 --> 00:26:09.125
Gabor Szabo: Damn…

153
00:26:14.010 --> 00:26:19.370
Maria Lowas-Rzechonek: Yeah, I also, don't, I don't think I, I understand, well,

154
00:26:19.940 --> 00:26:25.549
Maria Lowas-Rzechonek: Of course, many, like, swagger and things already, like,

155
00:26:26.450 --> 00:26:38.470
Maria Lowas-Rzechonek: Use type hints from the code and put into the documentation, so it's not that important that you document arguments within a docstring.

156
00:26:38.690 --> 00:26:51.079
Maria Lowas-Rzechonek: But sometimes you may want to add some extra information about the arguments, so then you can document it. I don't know whether it's answering this question.

157
00:26:52.490 --> 00:26:58.309
Gabor Szabo: So, I don't think that typings are bureaucracy, it's,

158
00:26:58.340 --> 00:27:16.199
Gabor Szabo: type hints are useful for tools, I mean, pre-AI, okay? It was very useful for tools. With AI, it might be different, but… and the documentation was solely for the users, for people.

159
00:27:16.810 --> 00:27:25.999
Gabor Szabo: And so adding type-ins helped the various tools to verify the code, right? Versus,

160
00:27:26.360 --> 00:27:29.880
Gabor Szabo: The documentation that only helps the user.

161
00:27:30.850 --> 00:27:38.100
Maria Lowas-Rzechonek: And also, if you are, for example, a developer, with type hints, you, you really No…

162
00:27:39.290 --> 00:27:49.119
Maria Lowas-Rzechonek: Well, a user… so a user, yeah, a user and a developer of this, of this, method function, you, you are able to say exactly

163
00:27:49.250 --> 00:27:53.580
Maria Lowas-Rzechonek: What… what input is,

164
00:27:54.860 --> 00:28:05.709
Maria Lowas-Rzechonek: required, right? So you didn't need to guess, or maybe look into the code, where it is used, and how it is used, but you were just this kind of information, so it helped developer.

165
00:28:06.130 --> 00:28:11.150
Gabor Szabo: Yeah, so the… the continuation of this comment, which is, I think, is the… is the

166
00:28:11.620 --> 00:28:18.239
Gabor Szabo: which was, I agree, is that if there is already an attribute list and type in the signature.

167
00:28:18.350 --> 00:28:24.309
Gabor Szabo: Then adding all this to the documentation is not that useful.

168
00:28:24.310 --> 00:28:25.100
Maria Lowas-Rzechonek: Yep.

169
00:28:25.100 --> 00:28:30.410
Gabor Szabo: And so in that direction, I understand… I totally agree, but because we already…

170
00:28:30.540 --> 00:28:40.289
Gabor Szabo: Because we already had documentation, and in the documentation we might explain all these things, before the types… the whole type annotation came.

171
00:28:40.290 --> 00:28:40.880
Maria Lowas-Rzechonek: Yep.

172
00:28:40.880 --> 00:28:49.740
Gabor Szabo: and then people started to type on ad notation. At that point, maybe they should remove the documentation, so you won't have duplication.

173
00:28:49.900 --> 00:28:54.600
Gabor Szabo: Which might lead to, contradictions.

174
00:28:54.600 --> 00:29:06.420
Maria Lowas-Rzechonek: Yeah, well, that… well, that's right, that's right, if you… if you don't need, like, any… to put any extra information about arguments.

175
00:29:06.670 --> 00:29:09.249
Maria Lowas-Rzechonek: You can, like, just skip it.

176
00:29:09.510 --> 00:29:11.700
Maria Lowas-Rzechonek: Yeah, because, like,

177
00:29:12.430 --> 00:29:36.369
Maria Lowas-Rzechonek: I've also seen a lot of documentation like this, that, it's just… the arguments are just listed, and really there are no extra information about them, or the kind of information are really just boulder plate. So, in that way, skip it, remove it. It's useless. It's useless, it's just, messing the code, messing your brain, or… yeah.

178
00:29:36.510 --> 00:29:38.950
Maria Lowas-Rzechonek: Be minimalistic about it.

179
00:29:39.130 --> 00:29:57.730
Gabor Szabo: This also comes… I think it comes also from studies. At least, when I studied long… many, many years ago at the university, that was sort of the requirement, that you write the documentation and you add each variable, each parameter there, and totally useless. But that's how we learned.

180
00:29:58.160 --> 00:30:09.749
Maria Lowas-Rzechonek: Yeah, maybe it was sent quite, like, yeah, like, the drill you, you, you were, like, learning, yeah, but, in real life, no, I would say be minimalistic.

181
00:30:09.750 --> 00:30:20.830
Maria Lowas-Rzechonek: And it also… oh, by the way, I also was to add a comment about outdated docstrings. So, if you really put in the docstring things needed to

182
00:30:21.300 --> 00:30:22.929
Maria Lowas-Rzechonek: use the function.

183
00:30:23.140 --> 00:30:42.480
Maria Lowas-Rzechonek: Then, and maybe arguments, maybe, maybe not, those things don't change that often, or at least they shouldn't change that often, because they are… they are kind of inter… interface, and you can, really think about it. When you're changing the interface, you should…

184
00:30:42.480 --> 00:30:47.320
Maria Lowas-Rzechonek: do it, con… conscious… consciously. So…

185
00:30:48.130 --> 00:31:00.200
Maria Lowas-Rzechonek: If you don't put too much into the docstring, and you don't put docstring everywhere, but only where it's needed, then, like, the burden to… to make them up-to-date won't be that big.

186
00:31:00.690 --> 00:31:01.340
Gabor Szabo: Yeah.

187
00:31:04.160 --> 00:31:05.060
Maria Lowas-Rzechonek: Okay

188
00:31:05.290 --> 00:31:21.929
Maria Lowas-Rzechonek: So, moving on, we are here, so the next point is, the structure. So the main path about documentation, which I already said, is, 257.

189
00:31:22.010 --> 00:31:35.840
Maria Lowas-Rzechonek: And it's not very long, and it doesn't have a lot of details, but it has some kind of guidelines that I think are very reasonable and see no really point why we should not go with them.

190
00:31:35.840 --> 00:31:44.540
Maria Lowas-Rzechonek: So first of all, the basic form, the simplest form of docstring is a one-line docstring, which is just called one-liner.

191
00:31:45.180 --> 00:31:51.190
Maria Lowas-Rzechonek: Mmm… And it should be a sentence in the imperative mode.

192
00:31:51.300 --> 00:31:57.840
Maria Lowas-Rzechonek: It should tell, what the function does, including what it returns.

193
00:31:58.030 --> 00:32:02.050
Maria Lowas-Rzechonek: It should fit in one line, including triple quotes.

194
00:32:02.210 --> 00:32:04.929
Maria Lowas-Rzechonek: And it should end with that period.

195
00:32:05.080 --> 00:32:06.979
Maria Lowas-Rzechonek: And now, again, why are you…

196
00:32:06.980 --> 00:32:08.549
Gabor Szabo: Two triple quotes here.

197
00:32:09.110 --> 00:32:13.590
Maria Lowas-Rzechonek: Well, it's, because, when…

198
00:32:14.800 --> 00:32:27.299
Maria Lowas-Rzechonek: For example, in the future, you would need to expand it to add some more details, then you will just, you know, go to the dot, press two enters, and then you carry on.

199
00:32:27.300 --> 00:32:36.560
Maria Lowas-Rzechonek: So you don't need to bother about changing one quote… single quote to triple quotes, so the convention is that you use triple quotes everywhere.

200
00:32:36.800 --> 00:32:37.530
Gabor Szabo: Okay.

201
00:32:38.540 --> 00:32:52.750
Maria Lowas-Rzechonek: Yeah. And it also, like, as with the type hint, this PEP was written before type hint, so I think that presently it's not that important that you include what it returns. Unless, of course,

202
00:32:53.860 --> 00:33:04.140
Maria Lowas-Rzechonek: You're… you don't using type hints, or, you know, the way you're using the docstring, doesn't convey this, straight… straight away, so then, of course, yes.

203
00:33:04.260 --> 00:33:13.189
Maria Lowas-Rzechonek: And about this imperative mode, so you should say something like, strip white space and remove special characters from the text.

204
00:33:13.680 --> 00:33:20.290
Maria Lowas-Rzechonek: And no, it strips, or the method strips, so no, it's just imperative mode. Do this.

205
00:33:22.090 --> 00:33:31.329
Maria Lowas-Rzechonek: And there's also the multiliner. So the first line, the summary line, is this one-liner from the previous slide.

206
00:33:31.330 --> 00:33:37.399
Gabor Szabo: Sorry, I'm bothering you. There's another comment. I use hash mark

207
00:33:37.610 --> 00:33:46.050
Gabor Szabo: Instead of the triple quotes, is it still recognized by doctors as a docstring, or ignored as a casual comment?

208
00:33:47.250 --> 00:33:58.819
Maria Lowas-Rzechonek: I would say it is ignored. Well, I haven't, like, made the test of it, but I would say that from everything that I know about docstring, it would be just ignore and treated as a comment.

209
00:33:59.320 --> 00:34:02.009
Gabor Szabo: Yeah, that's… that's my thinking also.

210
00:34:03.080 --> 00:34:06.550
Maria Lowas-Rzechonek: So yeah, so you can use it, but it won't be, it won't be,

211
00:34:07.700 --> 00:34:09.799
Gabor Szabo: The hash mark is for comments.

212
00:34:10.409 --> 00:34:16.709
Gabor Szabo: Is… and… and the… the… the… strings?

213
00:34:17.150 --> 00:34:21.029
Gabor Szabo: are… are for documentation. For dock strings, yeah.

214
00:34:23.370 --> 00:34:32.669
Maria Lowas-Rzechonek: So, about multiliners. So, there is a summary line, which is kind of one-liner from the previous slide, then there is the

215
00:34:33.900 --> 00:34:35.400
Maria Lowas-Rzechonek: the entity line?

216
00:34:35.699 --> 00:34:44.740
Maria Lowas-Rzechonek: I don't know why it's not a blank line, and then, there are more details. It is not specified,

217
00:34:45.280 --> 00:34:51.750
Maria Lowas-Rzechonek: in what format? There should be more details. It's, like, open for…

218
00:34:52.570 --> 00:35:01.090
Maria Lowas-Rzechonek: for what's needed in the project. And also, the indentation should be as the opening triple quotes.

219
00:35:01.300 --> 00:35:04.480
Maria Lowas-Rzechonek: And the closing triple quote should be in a separate line.

220
00:35:06.760 --> 00:35:09.590
Maria Lowas-Rzechonek: So, just the exa- like, in this example.

221
00:35:10.760 --> 00:35:12.899
Maria Lowas-Rzechonek: Right. Interesting.

222
00:35:12.900 --> 00:35:18.669
Gabor Szabo: And the opening triple chords… so the first line is on the same line where the opening triple chords.

223
00:35:18.670 --> 00:35:19.250
Maria Lowas-Rzechonek: Yeah.

224
00:35:20.170 --> 00:35:31.070
Maria Lowas-Rzechonek: So you can think about it, like this, that first of all, you write the, one-line, documenta- doc strings, yeah, so…

225
00:35:31.980 --> 00:35:35.579
Maria Lowas-Rzechonek: would go? Okay, I need to go… no.

226
00:35:36.770 --> 00:35:51.299
Maria Lowas-Rzechonek: Here. So, first you line the, write the one-line document doc string, and then if you have some more details to add, you go to the end of the line and press enter and continue. So, it's kind of…

227
00:35:51.450 --> 00:35:54.680
Maria Lowas-Rzechonek: This one liner stays there.

228
00:35:55.750 --> 00:35:59.240
Maria Lowas-Rzechonek: This is at least the way I'm thinking about it.

229
00:36:01.270 --> 00:36:02.110
Maria Lowas-Rzechonek: Okay.

230
00:36:02.160 --> 00:36:13.719
Maria Lowas-Rzechonek: But, so, so, this is, more or less everything that, PEP 2.7 says about the structure of, docstring.

231
00:36:13.720 --> 00:36:22.560
Maria Lowas-Rzechonek: But even in this example, you can see that there is a section keyword argument, because very often we have some kind of extra.

232
00:36:23.530 --> 00:36:33.580
Maria Lowas-Rzechonek: We have this need for extra, sections, sections in the doc string, and for that reason.

233
00:36:34.390 --> 00:36:38.689
Maria Lowas-Rzechonek: With time, several formats for a doc string involves.

234
00:36:38.860 --> 00:36:46.710
Maria Lowas-Rzechonek: And I would say only about those 5, but there are also some others. However.

235
00:36:47.130 --> 00:37:02.859
Maria Lowas-Rzechonek: I think they are not that popular, so I think that those… the first four are most popular, but the… and the docs test, I think it's something interesting which worth mentioning, so… so I also included it in the list.

236
00:37:04.770 --> 00:37:18.959
Maria Lowas-Rzechonek: So first of all, plain text. Plain text, has no redefined formats, apart from what's, like, the separation between the first line and the rest of the docstring.

237
00:37:20.270 --> 00:37:37.739
Maria Lowas-Rzechonek: there is a PEP287 about recommended format, and it says that plain text always will be supported, that this is the basic format, and if you don't have any more requirements, stick with it, it's very good.

238
00:37:38.180 --> 00:37:46.579
Maria Lowas-Rzechonek: Here was, the example of, documentation for Pickle,

239
00:37:47.880 --> 00:37:52.769
Maria Lowas-Rzechonek: it has some section, but they are written, yeah, they are written as a plain text, right? So, so…

240
00:37:53.130 --> 00:37:56.290
Maria Lowas-Rzechonek: What, whatever you need, thing is needed.

241
00:37:57.000 --> 00:37:57.840
Maria Lowas-Rzechonek: But…

242
00:37:58.450 --> 00:38:08.709
Maria Lowas-Rzechonek: Maybe your documentation is more complex, so you need some kind of structure in the docstring. So, there is a restructured text.

243
00:38:08.710 --> 00:38:21.300
Maria Lowas-Rzechonek: And, it is supposed to be easy to read and easy to use, and probably this is right for the basic syntax, but I don't think it's true for

244
00:38:21.340 --> 00:38:40.880
Maria Lowas-Rzechonek: more complex one. So this is a… quite a rich format, and it also… it is also used for writing full documents, full documentations, documentation, so maybe if you have documentation and docstrings, then living in, for example, one project, it makes sense to use, the structured text.

245
00:38:40.920 --> 00:38:49.900
Maria Lowas-Rzechonek: It is recommended by PEP287, and it is also the format that Sphinx prefers.

246
00:38:50.100 --> 00:38:51.230
Maria Lowas-Rzechonek: Mmm…

247
00:38:52.030 --> 00:39:01.339
Maria Lowas-Rzechonek: So, whereas it was chosen, for being easy to read and in the code, it can turn up,

248
00:39:01.570 --> 00:39:20.970
Maria Lowas-Rzechonek: to be quite cubrisson, for example, probably most of us will see something like this, that you have some basic information about the function, and then you have a list of params and returns and types, which is basically very hard to read. So, it's not that

249
00:39:21.950 --> 00:39:24.220
Maria Lowas-Rzechonek: It doesn't live up to the promise.

250
00:39:25.860 --> 00:39:37.960
Maria Lowas-Rzechonek: There is a Google style. I would say this is my favorite one, just to be… to state my opinion clearly, but this is my opinion. You are welcome not to agree.

251
00:39:38.000 --> 00:39:54.100
Maria Lowas-Rzechonek: It is… it has very simple and clean format and minimal structure. So, basically, it's also only about these arcs, returns, rises, where can we also, yields, or, example.

252
00:39:54.480 --> 00:40:04.180
Maria Lowas-Rzechonek: And apart from that, it is the plain text. So it is very, very, really… Clean and simple.

253
00:40:04.200 --> 00:40:20.810
Maria Lowas-Rzechonek: But it structures this docstring in a certain way. Of course, not every section needs to be there. Like, in the docstring, add only a section that is appropriate for this function.

254
00:40:20.830 --> 00:40:27.330
Maria Lowas-Rzechonek: And also, there is an extension to Sphinx, Napoleon, who is able to process this format, so…

255
00:40:28.740 --> 00:40:36.419
Maria Lowas-Rzechonek: One, if you have, like, a kind of requirements to generate documentation from the code, you will be fine.

256
00:40:38.380 --> 00:40:48.089
Maria Lowas-Rzechonek: There is also NumPyDoc, and it is used by NumPy and SciPy. It is based on very structured text.

257
00:40:48.090 --> 00:40:59.919
Maria Lowas-Rzechonek: but has some custom markers, a little bit similar to Google, like node, parameters, attributes, it's called differently, but the idea is mostly very similar.

258
00:41:00.090 --> 00:41:13.000
Maria Lowas-Rzechonek: And NumPyDoc is recommended for a project that requires a complex documentation, so then, yes, you need the structure there, so you can use something more complicated.

259
00:41:13.650 --> 00:41:26.769
Maria Lowas-Rzechonek: And doc test, this is a Python module, and it searches for pieces of text that looks like an interactive Python console, and then executes them and verified the output.

260
00:41:26.940 --> 00:41:42.120
Maria Lowas-Rzechonek: So, it can be helpful for regression tests, but also for keeping documentation up to date. And also, it can be kind of a form of tutorial for how to use the function.

261
00:41:44.960 --> 00:41:51.239
Maria Lowas-Rzechonek: Okay, and this is all about formats, and now, everything, like, how to write.

262
00:41:51.410 --> 00:41:58.310
Maria Lowas-Rzechonek: dog strings, and, like, what language to use. Of course, English, but what kind of English?

263
00:41:58.510 --> 00:42:04.579
Maria Lowas-Rzechonek: So, first of all, correct English. The grammar, punctuation, and spelling should be correct.

264
00:42:04.580 --> 00:42:24.299
Maria Lowas-Rzechonek: So don't, bother too much if someone, like, don't be, annoyed, maybe, when someone will, correct the typo in the doc… in the code review, the typo in the doc string. This is something important, as it's,

265
00:42:25.210 --> 00:42:31.799
Maria Lowas-Rzechonek: It's… We can read text Easy, easier, if the text is correct.

266
00:42:31.840 --> 00:42:38.780
Maria Lowas-Rzechonek: If the text is not correct, if it contains some errors, some mistakes, well, it will,

267
00:42:38.790 --> 00:42:53.079
Maria Lowas-Rzechonek: it will distract us, and we'll think more about the typo or grammar error than about what's written there. So, yeah, it should be correct English.

268
00:42:53.610 --> 00:43:03.099
Maria Lowas-Rzechonek: Also, full sentences are recommended for the same reason. It's easier to read full sentences, and also,

269
00:43:03.270 --> 00:43:09.420
Maria Lowas-Rzechonek: I think that full sentences are less… Ambiguous.

270
00:43:09.620 --> 00:43:24.669
Maria Lowas-Rzechonek: they are more to the point. Basically, docstrings, even… they are kind of documents, and it's good to think about them as a document. A very short one, a very simple one, but a document. So, in a document, you won't use, like.

271
00:43:24.950 --> 00:43:34.240
Maria Lowas-Rzechonek: You would use full sentences. You will not add some, not some, separate words, or some pieces of text, notes.

272
00:43:35.320 --> 00:43:42.030
Maria Lowas-Rzechonek: It is documents, so you should write it properly as a document, although very short.

273
00:43:44.030 --> 00:43:56.300
Maria Lowas-Rzechonek: you should use simple language, because simple language is, again, it's more accessible. We need less, brain power to process it.

274
00:43:56.300 --> 00:44:05.530
Maria Lowas-Rzechonek: And we have more brain capacity for other tasks, so we want the dog string to be easy to read, to understand.

275
00:44:05.890 --> 00:44:14.659
Maria Lowas-Rzechonek: And also, a lot of people using your docstring won't be native speaker of English.

276
00:44:14.960 --> 00:44:23.279
Maria Lowas-Rzechonek: In fact, they might have very basic knowledge of English, so you want to make sure that it's easy to understand.

277
00:44:24.480 --> 00:44:33.430
Maria Lowas-Rzechonek: And also, you can use, simplified grammar. So basically, use present simple.

278
00:44:33.680 --> 00:44:43.290
Maria Lowas-Rzechonek: In most cases. Maybe not… it won't be 100, percent correct.

279
00:44:43.400 --> 00:44:47.219
Maria Lowas-Rzechonek: But it will be much easier to understand.

280
00:44:47.620 --> 00:45:03.789
Maria Lowas-Rzechonek: I would say that you should use other tenses only if it's absolutely needed to understand what's going on, but in most cases, present simple will be enough. And here I can… I want to show you one example, what I've…

281
00:45:03.880 --> 00:45:08.380
Maria Lowas-Rzechonek: put in my previous slides. I will just… should… will go there.

282
00:45:09.700 --> 00:45:15.280
Maria Lowas-Rzechonek: Here. For example, if you have this sentence, we avoid repeating ourselves.

283
00:45:15.530 --> 00:45:27.310
Maria Lowas-Rzechonek: Usually, if you, like, in speaking, or just writing in a document, probably you would say something, we should avoid repeating ourselves.

284
00:45:27.790 --> 00:45:33.940
Maria Lowas-Rzechonek: Or, the second sentence. A doc string contains all the information needed to use the function.

285
00:45:34.010 --> 00:45:45.160
Maria Lowas-Rzechonek: needed to use, yeah. So, it's, again, it's without any need, should, could, will, we just, use a very simple grammar.

286
00:45:45.160 --> 00:46:00.090
Maria Lowas-Rzechonek: And, it is also similar in instruction, in step-by-step instruction, that you should use very simple English, very simple grammar. It's, yeah, it helps in understanding.

287
00:46:00.120 --> 00:46:03.960
Maria Lowas-Rzechonek: What's going on, and don't have any doubts about

288
00:46:05.500 --> 00:46:09.830
Maria Lowas-Rzechonek: Any things that you sh- were not, like, your concern?

289
00:46:10.590 --> 00:46:20.580
Maria Lowas-Rzechonek: Also, use consistent vocabulary, so try always to refer to the same thing, the same action, the same,

290
00:46:22.430 --> 00:46:26.729
Maria Lowas-Rzechonek: Yeah, anything, by the same name.

291
00:46:27.360 --> 00:46:39.539
Maria Lowas-Rzechonek: Because, yeah, then… well, we don't need to bother about being too repetitive, because docstrings are very short, and they are accessed, like, out of the context, so,

292
00:46:39.930 --> 00:46:55.400
Maria Lowas-Rzechonek: using different words just to, have some maybe more fluent language is not important. What we really want to… what we really want is that dock strings should be concise and, not ambivalent.

293
00:46:55.400 --> 00:47:04.610
Maria Lowas-Rzechonek: So, yeah, we always use get or retrieve, we always use test for test, Well,

294
00:47:05.070 --> 00:47:09.499
Maria Lowas-Rzechonek: In this way, it's really easier and faster to read it.

295
00:47:10.790 --> 00:47:17.850
Maria Lowas-Rzechonek: But on the other hand, don't forget about human touch, especially in longer docstring.

296
00:47:18.320 --> 00:47:31.839
Maria Lowas-Rzechonek: very schematical text, and also very often text generated by AI, is very hard to concentrate on. So, if you're really bothered about your readers, not about LLMs.

297
00:47:31.930 --> 00:47:49.200
Maria Lowas-Rzechonek: it shouldn't be generated text. Of course, you can help yourself with the tools, tools are for you, but remember to add this kind of something which will keep the reader interested, focused in the text.

298
00:47:50.420 --> 00:47:58.399
Maria Lowas-Rzechonek: And if you have any doubts, when you think, what really I should put in the doc string, is it enough, is it not enough?

299
00:47:58.400 --> 00:48:11.939
Maria Lowas-Rzechonek: Just, yeah, put yourself in different shoes. So, imagine that you are a developer who just imported the function and wanted to use it, and what kind of information they would, they would need.

300
00:48:13.580 --> 00:48:21.900
Maria Lowas-Rzechonek: Okay, so this is one, section off, gone, and now a few words about, tools. So,

301
00:48:25.480 --> 00:48:45.199
Maria Lowas-Rzechonek: This is something that's good about the doc strings, which might not be as good with self-documenting code, that we have some linters that can help us make sure we use correct formats, etc, etc. There are two main linters, PyDocStyle and PyDocLint.

302
00:48:45.200 --> 00:48:54.600
Maria Lowas-Rzechonek: they focus on slightly different things. PyDoc style is more about formatting, while PyDocLint is more about,

303
00:48:54.840 --> 00:48:58.619
Maria Lowas-Rzechonek: Sections, arguments, etc, etc.

304
00:48:59.300 --> 00:49:17.719
Maria Lowas-Rzechonek: And the, PiDoc style is, currently, deprecated, and roof is, suggested, to use otherwise. And also, roof has many PyDoc lint, rules included, so maybe Roof would be enough.

305
00:49:18.930 --> 00:49:20.060
Maria Lowas-Rzechonek: Also.

306
00:49:20.430 --> 00:49:31.569
Maria Lowas-Rzechonek: you can use… you can add a roof to… to the pre-commit, so it's done automatically, but, I would say,

307
00:49:31.870 --> 00:49:34.760
Maria Lowas-Rzechonek: If you decide to use it,

308
00:49:34.880 --> 00:49:45.470
Maria Lowas-Rzechonek: Think about rules that you want to include, and the one you want to exclude, because the default configuration for roof is very, very strict.

309
00:49:45.530 --> 00:49:53.150
Maria Lowas-Rzechonek: And if you use it like this, without any, any, any changes, then, it will,

310
00:49:53.200 --> 00:50:08.059
Maria Lowas-Rzechonek: it will, tell you that, all the time that this function doesn't have docstring, etc, etc, etc, and this is something that I just say, you should… you don't have to do, you don't need to do, so…

311
00:50:09.120 --> 00:50:18.250
Maria Lowas-Rzechonek: If you want to be, like, really minimalistic and use dock string only when it's needed and not everywhere,

312
00:50:18.710 --> 00:50:31.459
Maria Lowas-Rzechonek: you would need to switch off some rules, some rules, because otherwise, you won't be able to proceed. But it's okay, it's just, do it consciously, and it will be fine.

313
00:50:34.760 --> 00:50:44.680
Maria Lowas-Rzechonek: Okay, and then I added two examples from PyCharm. I know that not everyone is using PyCharm, but I,

314
00:50:45.040 --> 00:50:59.319
Maria Lowas-Rzechonek: I guess in other code editors, probably, we can find similar functionalities. So, in PyCharm, when you click on a name, and then press Ctrl-Q,

315
00:50:59.320 --> 00:51:07.190
Maria Lowas-Rzechonek: Then, you get this kind of small pop-up when you have a function signature, and also a docstring.

316
00:51:07.190 --> 00:51:19.699
Maria Lowas-Rzechonek: If you hit CTRL-Q twice, you would, have the same information in a separate window. For example, if you want to refer to it, like, during,

317
00:51:20.650 --> 00:51:22.629
Maria Lowas-Rzechonek: Writing code or something.

318
00:51:22.740 --> 00:51:42.330
Maria Lowas-Rzechonek: And also, in the project settings, you will have something like integrated tools, or Python integrated tools, where you can choose which docstring format to use, and now you know what the format are about, so you can choose, the format is… there is…

319
00:51:42.630 --> 00:51:44.450
Maria Lowas-Rzechonek: Most convenient for you.

320
00:51:44.680 --> 00:51:55.969
Maria Lowas-Rzechonek: And PyCharm should suggest this format when writing. Also, because, well, I don't have this included in the, in the presentation, but if you use

321
00:51:55.970 --> 00:52:10.719
Maria Lowas-Rzechonek: LLM, well, everyone is using LLMs now, so consider adding some kind of skill or rules, where you state what format you expect from your doc strings, and maybe add some, additional comments,

322
00:52:10.830 --> 00:52:13.729
Maria Lowas-Rzechonek: Which are, like, important for you.

323
00:52:14.900 --> 00:52:21.709
Maria Lowas-Rzechonek: So, so you make sure that, that, agents also will use the proper docstrings for, for your code.

324
00:52:23.000 --> 00:52:26.990
Maria Lowas-Rzechonek: Okay, and that's all from me, and if you have any questions…

325
00:52:27.160 --> 00:52:29.109
Maria Lowas-Rzechonek: I open… I'm open for it.

326
00:52:30.170 --> 00:52:31.080
Gabor Szabo: Well…

327
00:52:31.220 --> 00:52:38.249
Gabor Szabo: Thank you very much. So, if anyone has questions, please write the questions now. I know I have one.

328
00:52:38.430 --> 00:52:49.299
Gabor Szabo: That you sort… partially, talking about now with the IDE, but I was wondering how,

329
00:52:49.430 --> 00:52:58.369
Gabor Szabo: Various other tools, Know which form… how to… how to format your, dog strings.

330
00:52:58.610 --> 00:53:04.830
Gabor Szabo: what kind of formatting it assumes. So, you have your dock strings in one of the formats.

331
00:53:05.390 --> 00:53:10.189
Gabor Szabo: And then you run… let's say you,

332
00:53:10.380 --> 00:53:15.200
Gabor Szabo: published it, on, so it's published on, Read the Docs.

333
00:53:15.880 --> 00:53:22.819
Gabor Szabo: How does it know how to format your code. Does it guess, or is it.

334
00:53:22.820 --> 00:53:30.430
Maria Lowas-Rzechonek: Well, I haven't used Read the Dogs, but I think that they are using things underneath, or something.

335
00:53:31.020 --> 00:53:31.530
Gabor Szabo: So far.

336
00:53:31.530 --> 00:53:32.210
Maria Lowas-Rzechonek: Probably…

337
00:53:32.210 --> 00:53:33.040
Gabor Szabo: nose?

338
00:53:33.360 --> 00:53:38.719
Maria Lowas-Rzechonek: Well, I haven't used things that, well, it's…

339
00:53:40.820 --> 00:53:43.409
Maria Lowas-Rzechonek: There should be a configuration like this.

340
00:53:43.570 --> 00:53:56.230
Maria Lowas-Rzechonek: For sure, for sure, like, Ruth has the configuration when you can specify which format, which docstring format you use, and it, selects, rules that are

341
00:53:59.220 --> 00:54:10.280
Maria Lowas-Rzechonek: good for the format you've chosen, but probably, I would say that, that, for things and for, for other tools, there should be some kind, some sort of

342
00:54:11.660 --> 00:54:12.969
Maria Lowas-Rzechonek: Setting for that.

343
00:54:14.280 --> 00:54:25.390
Gabor Szabo: Yeah, okay. I see that David included a list of the links to the PEPs, and a couple of other things, I think. I will include them

344
00:54:26.370 --> 00:54:31.759
Gabor Szabo: On the website, on the page of this, of this video, which will be linked underneath the video.

345
00:54:33.380 --> 00:54:33.820
Maria Lowas-Rzechonek: Okay, yeah.

346
00:54:33.820 --> 00:54:38.289
Gabor Szabo: Any questions from the… Public? Present here?

347
00:54:39.410 --> 00:54:59.289
Gabor Szabo: If not, then I think we can thank you again. It was very interesting, a couple of things, new things I learned. I love, by the way, doc tests, and I teach it often to students, or show them at least, that it's how useful that can be.

348
00:54:59.530 --> 00:55:03.340
Gabor Szabo: And I learned a couple of things, so thank you very much.

349
00:55:04.020 --> 00:55:06.119
Maria Lowas-Rzechonek: Thank you. I think that someone…

350
00:55:06.420 --> 00:55:07.020
Gabor Szabo: Sorry?

351
00:55:07.200 --> 00:55:11.089
Maria Lowas-Rzechonek: Someone says that the mics are muted, but I think they will be…

352
00:55:11.090 --> 00:55:17.100
Gabor Szabo: Yeah, I will unmute the mix once we finish the video recording.

353
00:55:17.260 --> 00:55:34.190
Gabor Szabo: So, what I still wanted to say is for the people who are watching the video, so please click on the like of the video, follow the channel, and below the video, you will find a link to the various presentations that we are…

354
00:55:34.410 --> 00:55:52.470
Gabor Szabo: going to have, so you can find them there, and you can follow those channels, and that way you can join one of our upcoming sessions. And we'll have a link also how to find Maria after to her LinkedIn page and other stuff.

355
00:55:53.540 --> 00:55:58.210
Gabor Szabo: That's it. Thank you very much, and see you at another event.

356
00:55:58.520 --> 00:55:59.600
Gabor Szabo: Bye-bye!

357
00:55:59.600 --> 00:56:00.930
Maria Lowas-Rzechonek: Bye bye, thank you!

