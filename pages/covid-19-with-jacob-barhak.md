---
title: The Reference Model for COVID-19 attempts to explain USA data with Jacob Barhak
timestamp: 2025-01-28T08:30:01
author: szabgab
published: true
description:
tags:
    - Python
---


Speaker: [Jacob Barhak](https://sites.google.com/view/jacob-barhak/home)

{% youtube id="Ea_e6xI48Ik" file="2025-01-27-the-reference-model-for-covid-19-attempts-to-explain-usa-data-with-jacob-barhak.mp4" %}


The Reference Model for disease progression was initially a diabetes model. It used the approach of assembling models and validating them against different populations from clinical trials.

The model performs simulation at the individual level while modeling entire populations using the MIcro-Simulation Tool (MIST), employing High Performance Computing (HPC), and using machine learning techniques to combine models.

The Reference Model technology was transformed to model COVID-19 near the start of the epidemic. The model is now composed of multiple models from multiple contributors that represent different phenomena: It includes infectiousness models, transmission models, human response / behavior models, hospitalization models, mortality models, and observation models. Some of those models were calculated at different scales including cell scale, organ scale, individual scale, and population scale.

The Reference Model has therefore reached the achievement of being the first known multi-scale ensemble model for COVID-19. This project is ongoing and this presentation is constantly updated for each venue. To access the most recent publication please use [this link](https://www.clinicalunitmapping.com/show/COVID19_Ensemble_Latest.html)

## Bio:

Jacob Barhak is an independent Computational Disease Modeler focusing on machine comprehension of clinical data. The Reference Model for disease progression is patented technology that was self developed by Dr. Barhak. The Reference model is the most validated Diabetes model known worldwide and also the first COVID-19 multi-scale ensemble model. His efforts also include standardizing clinical data through ClinicalUnitMapping.com and he is the developer of the Micro Simulation Tool (MIST). Dr. Barhak has a diverse international background in engineering and computing science. He is active within the python community and organizes the Austin Evening of Python Coding meetup. For additional information [please visit](https://sites.google.com/view/jacob-barhak/home)

![](images/jacob-barhak.jpg)


[Lessons Learned from Modeling COVID-19: Steps to Take at the Start of the Next Pandemic[v1]](https://www.preprints.org/manuscript/202411.2193/v1)


## Transcript


WEBVTT

1
00:00:02.260 --> 00:00:20.330
Gabor Szabo: Hello, and welcome to the Code Maven Channel on Youtube and our meeting. Thank you for everyone who is arrived to this meeting, and especially to Jacob, who is going to give the presentation. If you are unfamiliar with the Channel, then

2
00:00:20.500 --> 00:00:48.179
Gabor Szabo: we have these live presentations, meetings with live presentations, mostly about stuff related to python and rust programming, and also something about git and version control. And this area my name is Gabor. I'm the host of this. I teach python and rust at corporations. And I also help companies to get started with

3
00:00:48.960 --> 00:00:52.559
Gabor Szabo: test automation and continuous integration

4
00:00:52.630 --> 00:00:56.399
Gabor Szabo: area that that sort of area.

5
00:00:57.730 --> 00:01:04.399
Gabor Szabo: And and we have this meeting, so people can share their their knowledge with each other.

6
00:01:04.540 --> 00:01:11.199
Gabor Szabo: So thank you for arriving. And before I let Jacob start talking about

7
00:01:11.590 --> 00:01:20.060
Gabor Szabo: himself and introducing himself. Please, like the video, follow the channel. I always forget to say this. So now I remembered.

8
00:01:20.200 --> 00:01:23.540
Gabor Szabo: So the thank you, and and it's yours.

9
00:01:24.210 --> 00:01:54.160
Jacob Barhak: Okay, we're going to try to make it as a conversation as much as possible. My name is Jacob Barhack. I've been developing disease models for since 2,006. So it's almost, it's about 19 years now, a bit less than 19 years. And I have technology for disease modeling. Now, disease modeling means computational disease modeling. And I use a lot of python. This is actually, when I was introduced to Python in 2,006, and all of this project was made in python.

10
00:01:54.761 --> 00:02:10.820
Jacob Barhak: It requires a lot of computing power, and the idea is to be able to explain diseases. So I started with diabetes. I was actually hired by university to as a programmer to actually write disease modeling software.

11
00:02:11.030 --> 00:02:38.280
Jacob Barhak: I'm still using of an option offshoot of the same software like 19 years later. Now it's called missed the micro simulation tool, and it allows you to simulate many, many individuals going through a disease. And you define what the disease is. I started with diabetes. I actually got to the point that diabetes. I have one of the most sophisticated diabetes models worldwide.

12
00:02:38.280 --> 00:02:44.609
Jacob Barhak: and this is patented technology. And at the end, you will see I have a conflict of interest statement. Because

13
00:02:44.610 --> 00:03:10.790
Jacob Barhak: I believe this technology is worth a lot. So whatever I'm telling you, take it with a grain of salt. This is developed technology, everything that I promise you double check the nice thing about this technology. It does the double checking for you for some degree. We'll explain it later. It uses some AI ideas and technologies to actually implement what's happening here. But it's not the AI that you're familiar with. It's a mix.

14
00:03:11.050 --> 00:03:13.479
Jacob Barhak: And this is why it's patented. So

15
00:03:14.070 --> 00:03:24.709
Jacob Barhak: let me explain what happens. With this technology, I started with diabetes in 2,000 and 2,020

16
00:03:24.830 --> 00:03:29.980
Jacob Barhak: Covid arrived to the Us. I was in the Us. And I

17
00:03:30.140 --> 00:03:54.935
Jacob Barhak: started migrating my technology towards modeling Covid. And now I can explain Covid. But let me tell you what explain means. Oh, by the way, this presentation was given in many places you can follow up how it changed because it did change all of those things. You can download on the links at the end. You'll have a QR code. Actually, I'll show it to you now. But

18
00:03:55.550 --> 00:04:16.769
Jacob Barhak: you will have a QR code that you can download this or actually view it. You'll need a strong machine to actually view it, because it's a huge file. It's like a quarter of a gig size to actually download and view on your browser. But it has everything, including results. And it is interactive. It's an HTML file. I'm using python technology called to actually do this.

19
00:04:16.769 --> 00:04:29.960
Jacob Barhak: But it's less about all of this, more about disease models. Later on. You can ask me about everything else, so you can download and see how things changed, even in my perspective. But now I believe things have been stable for the last

20
00:04:30.390 --> 00:04:38.560
Jacob Barhak: approximately 2 years, so I'm pretty sure I can explain, at least in the Us. What happened with Covid and explain means.

21
00:04:39.030 --> 00:04:51.659
Jacob Barhak: Let's let's take it a step north before I show the model and explain it. Think about it. We might have more pandemics in the future. We probably will actually have them all the time. We have many diseases going on.

22
00:04:51.810 --> 00:05:10.500
Jacob Barhak: But can we explain really what's happening. I was amazed when I started working with the medical people that how little they know about some of the things going on, and the fact is, they are overwhelmed with data. The fact that they can remember and do something good is miraculous at this

23
00:05:10.550 --> 00:05:36.520
Jacob Barhak: speaks a lot about their profession. They are doing the best they can, but they cannot even memorize the medical papers coming out every 6 seconds, and every 6 seconds a new medical paper coming out. There's no way one doctor will remember at all. And I'm not talking about all those medical databases, huge amounts of data that are being accumulated by by bodies like the National Institutes of Health.

24
00:05:37.460 --> 00:05:59.149
Jacob Barhak: All of this means that we need now to help computers help up crunch all this and give us good results and good explanations about what's going on, because the way we are dealing with medicine now will change with the data. It's already changing. And this model and many other tools related to it will change it. So

25
00:05:59.300 --> 00:06:05.260
Jacob Barhak: now let's go back to the model and explain how I can explain things. So

26
00:06:06.270 --> 00:06:11.290
Jacob Barhak: the reference model for disease. Progression is kind of a statistical model.

27
00:06:11.690 --> 00:06:31.800
Jacob Barhak: What it does it says you. Each disease has states it's a state transition model, where you can be either no covid or can be covered, infected. You can recover or die from covid. Notice that there is no error back from recovered to infected, because I'm modeling the beginning of the disease. April 2020.

28
00:06:32.520 --> 00:06:43.590
Jacob Barhak: Because the idea is that the next disease we want to have a tool that will explain it to us in reasonable time, and I believe this is one of the tools that can help do that. So

29
00:06:43.930 --> 00:06:44.650
Jacob Barhak: oh.

30
00:06:45.080 --> 00:07:07.769
Jacob Barhak: I'm I'm trying to extract from the beginning data that people accumulated. I'm using the Covid tracking project data. They allow me to use it even for commercial purposes. And you can actually go and track and see for each State in the Us. How many people got infected, how many people died, and they kept the very pretty good record about it.

31
00:07:08.000 --> 00:07:24.509
Jacob Barhak: and later on there are other organizations that took over. But they were, I believe, the best at start. So I'm using that data. And now I'm I'm trying to get a model that explains all those numbers that they appear, that they that they report

32
00:07:25.000 --> 00:07:25.830
Jacob Barhak: so

33
00:07:26.390 --> 00:07:32.730
Jacob Barhak: to do this, I assume that there are those States, and this is the beginning of pandemic. So there is no reinfection.

34
00:07:33.160 --> 00:07:41.250
Jacob Barhak: and I'm trying to match their numbers. How do I try to match them? Each error has several words about above them. Each word.

35
00:07:41.250 --> 00:07:44.160
Gabor Szabo: Wait a second, Jacob. So- so

36
00:07:44.760 --> 00:07:54.509
Gabor Szabo: Jim is writing that screen share, not showing. If that is wanted. I I see on the screen these boxes of No. Covid.

37
00:07:54.510 --> 00:08:08.830
Jacob Barhak: No Covid Covid infected, possibly, hospitalized Jim. And look, if you have the option of actually choosing what screen you choose. But sometimes you can choose. You can see the shared screen. I can stop the share and share it again. If it's okay with you guys

38
00:08:09.000 --> 00:08:11.570
Jacob Barhak: or Jim, did you find the share.

39
00:08:11.980 --> 00:08:15.290
Jim Mccormack: I'll look, Jacob, don't let me take you out of flow. Go, please proceed. Thank you.

40
00:08:15.290 --> 00:08:22.830
Jacob Barhak: So look at. Look at the link I sent. You can actually bring up the presentation and follow up. I'm on the second tab called introduction.

41
00:08:23.460 --> 00:08:33.630
Jacob Barhak: It's it's an interactive on your machine. You should be able to download that you have good Wi-fi just download it to your machine and you can follow me there if you don't see the presentation.

42
00:08:33.730 --> 00:08:34.389
Jim Mccormack: Got it.

43
00:08:34.390 --> 00:08:35.260
Jim Mccormack: It's loading.

44
00:08:36.049 --> 00:08:38.569
Jacob Barhak: Yeah, I know it takes a minute to load.

45
00:08:39.282 --> 00:09:00.519
Jacob Barhak: It's it's huge, but it has everything encapsulated. Part of the reason is to keep it to a producible as much as possible at the end. You'll see a producibility section. I don't give away all the code, but I do give. Keep track of everything that I noted. Like. You see all those boxes here, those are all the references where you can actually extract the data.

46
00:09:00.599 --> 00:09:14.679
Jacob Barhak: And one, some of the links actually became defect. I found some other links so can show you where I got the data from, or make sure that people can actually try to reconstruct this as much as possible, because we have a reproducibility crisis in science.

47
00:09:14.909 --> 00:09:23.569
Jacob Barhak: anyway, back to the boxes. So on top of those boxes you'll see words like infectious transmission, response, recovery, and mortality.

48
00:09:24.019 --> 00:09:29.869
Jacob Barhak: Each one of those represents not one model, but many models.

49
00:09:30.449 --> 00:09:42.189
Jacob Barhak: The technology that I'm using is called an ensemble model. An ensemble is like choir in in music. Well, ensemble models are very similar. You have. Don't have one model, you have many of them.

50
00:09:42.329 --> 00:09:52.189
Jacob Barhak: so I have many model for infections, many models for transmission, many models for response, many models for recovery and mortality and hospitalization. You'll see later.

51
00:09:52.369 --> 00:10:21.229
Jacob Barhak: But on top of it. I actually have an observer looking at all of this, saying, you know your numbers are wrong. So you have to actually correct them, because your observer. Actually, you have multiple observer models, each one seeing something different, telling you something different about those numbers. Do you incorporate all of those? And now you have many, many models, and you have to run them all and takes quite a bit of computing power. Later on I'll show you I have a computer here still crunching data, because I'm still working on this and making sure that my numbers are okay.

52
00:10:21.569 --> 00:10:22.439
Jacob Barhak: So

53
00:10:24.309 --> 00:10:41.049
Jacob Barhak: all of this takes a lot of computing power, you will see later on. This computation took about 3 years of computation on a single CPU. The ones I'm working on now will take half a half a year on a big 24 core machine 32 threads. So

54
00:10:42.299 --> 00:10:54.739
Jacob Barhak: ever. And when you run it in the cloud it takes many, many, many processors, because this takes a lot of computing power just like AI because it uses AI technology, we're gonna talk about it later in a second.

55
00:10:55.605 --> 00:11:18.749
Jacob Barhak: So I take all those models. I also take information from the cover tracking project about what happened in each State like numbers of and and you see some of those numbers later. I have information from us. Census about each State States are not the same. They different sizes, different population, density, different age age

56
00:11:19.109 --> 00:11:39.639
Jacob Barhak: curves population curves in school. Also, there's information about number of interactions and even the weather. I include the weather as part of the simulations, and later we'll ask some questions. But let's say, show you what the models look like and why they are. They are the way they are. So let's

57
00:11:39.979 --> 00:11:44.819
Jacob Barhak: explain one motivation. Why, this is important. To have a model like this

58
00:11:45.769 --> 00:12:10.249
Jacob Barhak: in the Dhs is the Department of Homeland Security in the Us. During Covid. It's kept a document called the Master Question List about COVID-19, and it always very, very organized way. They say this is what we know, or we think we know. And this is what we want to know. So they had a master question list about question about Covid things they didn't know.

59
00:12:10.729 --> 00:12:24.479
Jacob Barhak: In the 26th of May 2020, in that version of that table of that paper, and which evolved throughout time. By the way, you can actually download it later in the presentation, and check it out in

60
00:12:25.089 --> 00:12:37.069
Jacob Barhak: the versions change, but it still exists somewhere. All those versions you can still find them. The Department of home security kept very, very meticulous record, which is very good. I I give them

61
00:12:37.339 --> 00:12:47.179
Jacob Barhak: a good grade, because this is one of the most important documents, so you can extract information, for from they did very good job. But

62
00:12:47.839 --> 00:12:55.989
Jacob Barhak: even with all this, in the 26th of May they were still asking that question, what is the average infections period during which individual can transmit the disease?

63
00:12:57.259 --> 00:13:07.479
Jacob Barhak: Why is it important? Think about it. You are now the government, and you have to decide. If you have a lockdown, or how much people to how much time do you keep people in curfew?

64
00:13:08.009 --> 00:13:12.569
Jacob Barhak: Or even if they're sick, how much time you keep them not roaming around.

65
00:13:14.069 --> 00:13:16.979
Jacob Barhak: They didn't know they kind of admitted.

66
00:13:18.669 --> 00:13:19.434
Jacob Barhak: So

67
00:13:21.569 --> 00:13:29.999
Jacob Barhak: Since the Department of Homeland Security didn't know those things, and they asked us. And

68
00:13:30.599 --> 00:13:33.819
Jacob Barhak: at this point I started looking for answers.

69
00:13:34.069 --> 00:13:57.659
Jacob Barhak: And actually this happened later on in the pandemic, because some of those models came in like a year later, but some of them existed even before. So you can extract some information which is semi like from this paper from Bai Lee, and let me explain what this curve means. This is the infectious curve. It's relative infection. It tells you how much virus you shed, meaning, how much virus your body

70
00:13:57.969 --> 00:14:02.709
Jacob Barhak: gives away compared to your Max, your Max is one.

71
00:14:03.449 --> 00:14:26.721
Jacob Barhak: So how much virus your body generates, and this is the day. So a day 0 almost nothing. You just got infected. You don't generate the virus, or at least not enough to actually spread around the number is so slow, low you don't see it, and then for next 2 days you don't, and then it starts growing, and then it goes away. This, actually, in this case, in this paper, actually draw, took the information from

72
00:14:27.899 --> 00:14:40.199
Jacob Barhak: I took this information and and manipulated a little bit because it was not exactly like this, but some other models. They actually says, this is how we measured it. Notice how different the models are.

73
00:14:40.199 --> 00:14:59.819
Jacob Barhak: Here's another one. Actually, in this paper. They had, like 6 of those models, but 5 or 6 I don't remember, but each one looked different. So I took 2 from that publication and think about it. Each person also must be behaves differently. When I run the simulations, I run the simulation for each individual, so each individual may be different than another.

74
00:14:59.869 --> 00:15:06.769
Jacob Barhak: but in this situation I assume that all of them have the same infections of the entire cohort, and we are looking at the average.

75
00:15:06.909 --> 00:15:11.699
Jacob Barhak: We can do the simulations not like this, but we're looking for the average curve. So

76
00:15:11.909 --> 00:15:36.589
Jacob Barhak: even if I say, Oh, this is like that, or this is like that, or this person behaves like this, or like this. Some of those papers came in later in the pandemic. But still, once you have this information, or even if you don't have this information, but you have assumptions from other diseases. Say, Oh, you know, when this disease looks like that, and maybe take the infections curve from that disease, you can plug it in.

77
00:15:37.329 --> 00:15:56.959
Jacob Barhak: And what the model does it uses? Ai techniques. Everyone probably is familiar with optimization technique called gradient descent. So using gradient descent after running all of those simulations, it will find the optimal one from all of the models that you plugged in.

78
00:15:57.279 --> 00:16:06.979
Jacob Barhak: Let me explain how it starts at the beginning. You don't know what what curve is dominant, or what is actually correct. What you do is, you assume

79
00:16:07.409 --> 00:16:23.439
Jacob Barhak: all models are the same meaning. If 5 people come to me and tell you a story. You believe them all the same way without knowing anything better. So you just average whatever they're saying. This is the average of all of the models that you saw before.

80
00:16:24.549 --> 00:16:25.659
Jacob Barhak: Now.

81
00:16:26.499 --> 00:16:47.699
Jacob Barhak: During simulation, you actually run simulations and know this is better. This is worse, and little by little, you start optimizing. And after many, many iterations, you take a lot of computing power. This is basically how AI models train using very similar technique. So I'm using the same technique over some other medium which is not a neural network. As you know it.

82
00:16:47.849 --> 00:16:58.359
Jacob Barhak: it's somewhat similar, but not exactly. It's a different state thing, state transition, and it actually runs. It runs a little bit differently. I'll I can go into details if you're interested.

83
00:16:58.589 --> 00:17:15.439
Jacob Barhak: and then you end up with something that looks like this. This is the answer for the Department of Homeland Security. Hopefully, in the future, you will see they will use technology and be able to extract an answer fairly quickly.

84
00:17:15.599 --> 00:17:29.799
Jacob Barhak: and then don't go a long time in the pandemic without knowing by the way, this may change with the numbers. But over time. And of course, there's bios variance and stuff like this. But at least the beginning, you have a basic idea of what's happening.

85
00:17:29.799 --> 00:17:49.269
Jacob Barhak: And this is what was happening according to all the numbers and all the assumptions that you will see coming in later on. Remember, a model is not true. It's an assumption, and what it does, it takes all this ensemble and kind of puts it into the places. This is the most reasonable set of assumptions that matches the best, the data best

86
00:17:50.259 --> 00:17:52.609
Jacob Barhak: anyone has any question. Or can I proceed?

87
00:17:55.109 --> 00:17:56.389
Jacob Barhak: Okay, I'll proceed.

88
00:17:56.839 --> 00:18:12.969
Jacob Barhak: Here's about transmission. Yeah, I'll make it interesting for you if I ask you if you met. It's 1 thing having, in fact, being infectious. But what if I meet April 2020? I have Covid, and let's say I meet one of you for 15 min.

89
00:18:13.269 --> 00:18:25.959
Jacob Barhak: What's the chance of you getting the Covid from me? Don't answer it. I'll tell you. I asked this question many times. Many people, many people tell me 70% or encounter for, say, 15 min.

90
00:18:26.129 --> 00:18:34.129
Jacob Barhak: And then I tell them it's slow. Then look at themselves 50%, and then tell them it's lower. Then they get to 10%. And I tell them it's still lower.

91
00:18:34.409 --> 00:18:39.339
Jacob Barhak: And then they end up amazed that it's only between one and 2%,

92
00:18:39.779 --> 00:19:00.269
Jacob Barhak: because what drives Covid crazy is not the fact that the transmission happens immediately. It's like, if if virus will be so infectious, and everyone will be infected in no time. What what drives it is the fact that we have so many interactions amongst ourselves. So a person meeting, and we have those every day with many, many people.

93
00:19:00.399 --> 00:19:03.109
Jacob Barhak: So if at some point me

94
00:19:03.429 --> 00:19:09.859
Jacob Barhak: having interaction with one person, the chance is very low. But since I meet many people for many days.

95
00:19:10.309 --> 00:19:21.119
Jacob Barhak: this is what drives it the chance for me transmitting 1% over 10 days with many people, it's much, much higher than me. With one person for 15 min.

96
00:19:21.120 --> 00:19:26.539
Gabor Szabo: Doesn't it change? Depending on the on the length of the time you spend with the person.

97
00:19:26.540 --> 00:19:42.980
Jacob Barhak: Yeah, you can argue that you can argue, think about encounter, think about like a 15 min encounter as an average. If you spend the person twice. Then basically, it's not twice the probability, but it's it's very close to twice the probability.

98
00:19:42.980 --> 00:19:50.709
Gabor Szabo: But what I'm saying is that let's say you you meet a hundred people for 1 min versus one person for a hundred minute.

99
00:19:51.370 --> 00:19:58.529
Jacob Barhak: Yeah. So all of those things scales kind of differently. It's, you know, like a Bernoulli test.

100
00:19:59.700 --> 00:20:18.979
Jacob Barhak: It looks like a Bernoulli test that you run many, many times you have a chance of like flipping a coin that is biased, and how many times each one, each period of time, let's say, 15 min. You flip one of those coins. So according to this, you can actually calculate an approximation to the function.

101
00:20:21.220 --> 00:20:28.770
Jacob Barhak: so it's simple statistics that you learned at school. But now it's actually being active, very useful in those cases.

102
00:20:28.770 --> 00:20:52.959
Jacob Barhak: Later on, you put it. We tried in the past to do it in the Marcus model. There are multiple ways to calculate it. And some people come up with different functions. It doesn't matter, really, because all of those are assumptions, all those ones are incorrect to some degree. The question is, which one is most plausible under all of the things that you know, and for this, you need a lot of assumptions, a lot of computing power. And this is what I saw.

103
00:20:53.480 --> 00:21:01.439
Jacob Barhak: So even if it's not about newly test, and someone else comes up with different infections function. I can plug it in and see what happens.

104
00:21:01.720 --> 00:21:03.770
Jacob Barhak: You you understand what I mean.

105
00:21:04.130 --> 00:21:27.249
Jacob Barhak: But in this situation I took multiple functions that took into account individual encounter the population density of the State, some random, constant, just just put plug it in just in case to make some noise. Sometimes it's helpful in some models, at least even to root out some things. And I also added something interesting temperature. Here, let me ask you

106
00:21:27.270 --> 00:21:41.540
Jacob Barhak: what happens? Colder States or warmer States, the transmission is higher. Think about it. If you're in New York or Michigan, or you've Texas or Florida, where is the chances for you to actually transmit the disease? Higher?

107
00:21:42.560 --> 00:21:54.420
Jacob Barhak: Think about it. It matters, and we'll see the answer at the end. Think about the answer to yourselves, but later on you'll you'll get the answer from from me when I show the results.

108
00:21:56.150 --> 00:22:13.710
Jacob Barhak: So I also took into account response models. Pandemics are. Also. It also matters how people behave if you are afraid of the pandemic, and you stick at home and don't go nowhere. Your chances of transmitting or getting disease are much, much lower.

109
00:22:14.640 --> 00:22:15.860
Jacob Barhak: But then.

110
00:22:16.150 --> 00:22:40.989
Jacob Barhak: if you run around and ignore the disease, like many people did, and which is model number 3 here that say, Oh, I don't care about Covid, and then eventually get Covid, and then you're at home and don't see anyone because you're at home, or even worse. If you are not at home, and you just ignore Covid and go around. It's worse. So different people behave differently, actually, different parts of society behave differently same, just like infectiousness curve.

111
00:22:41.140 --> 00:22:42.859
Jacob Barhak: Each one behaves differently.

112
00:22:42.980 --> 00:22:54.039
Jacob Barhak: So now you have different models. So I took 2 models from apple mobility, with different variations on them. Apple mobility data says, Oh, how many people looked at their phones

113
00:22:54.370 --> 00:23:03.850
Jacob Barhak: and press the map button. This indicates they want to go somewhere. It doesn't mean they went. But this kind of an an estimate of how much mobility they had.

114
00:23:03.970 --> 00:23:07.029
Jacob Barhak: So this is, I use those as a base.

115
00:23:07.618 --> 00:23:13.241
Jacob Barhak: Also, I used as a base. Later on came Eric Ferguson.

116
00:23:13.920 --> 00:23:20.750
Jacob Barhak: I I hope I didn't butcher the name. He's from Montclair University. He did a study of us States.

117
00:23:21.170 --> 00:23:28.679
Jacob Barhak: and knew whether they shut that what their shutdown orders were in the States, each State

118
00:23:29.140 --> 00:23:43.180
Jacob Barhak: decided differently. So now you incorporate all of this into the model and says and say whether, you know, non-essential shops were closed, school stay at all models, so on and so forth.

119
00:23:43.360 --> 00:24:08.491
Jacob Barhak: and at different levels of compliance. I entered it as a formula into the model it. It's a little bit more complex. I'm just giving you the idea of what's happening here. He later on published a a good version, the I used an older version that, and I state exactly what the differences are from this newest version. But

120
00:24:09.370 --> 00:24:15.069
Jacob Barhak: This is how. Now I have different models of how the States behave.

121
00:24:15.180 --> 00:24:17.640
Jacob Barhak: and each State behaves differently, of course.

122
00:24:17.970 --> 00:24:28.839
Jacob Barhak: but I have also different models of those, and all of those are part of the mix of models that are playing around. Think about it. All of those models are roaming around and doing things.

123
00:24:29.090 --> 00:24:58.840
Jacob Barhak: then came in and tell me this is fairly recent. He gave me an hospitalization model. I didn't have an hospitalization model meaning people are in hospital. The numbers that you count of people being infected is not very good estimate, because you know the tests are not that you don't test everyone, and so on, and so forth. It does errors here, but people who ended up in the hospital oh, you know they were hospitalized. So if you have a hospitalization model.

124
00:24:58.840 --> 00:25:05.610
Jacob Barhak: It kind of like helps you out. Now, interestingly enough, not all States counted hospitalizations. Well.

125
00:25:05.690 --> 00:25:15.500
Jacob Barhak: but it doesn't matter when they do. I do want better information. So authorization models is something that Kyoti gave me. And then the question is, when is the person?

126
00:25:15.720 --> 00:25:25.680
Jacob Barhak: What's frequency? The person gets hospitalized if they get the disease. So he came up with 3 models, low probability, moderate probability, and high probability, and those depend on age.

127
00:25:25.990 --> 00:25:28.579
Jacob Barhak: as you can see here, and also

128
00:25:28.770 --> 00:25:37.303
Jacob Barhak: whether a person gets hospitalized early or later, meaning how much time it takes them to get hospitalized in each age.

129
00:25:37.880 --> 00:25:38.710
Jacob Barhak: when.

130
00:25:38.870 --> 00:25:56.340
Jacob Barhak: So again, you can run the simulation and find out that the worst summary, if you take the average one, it's not the best one, actually the one with the lower probability the was not as high as we thought, at least according to data and all of the other models that we found.

131
00:25:56.970 --> 00:25:59.740
Jacob Barhak: So all of this you take into account.

132
00:26:00.830 --> 00:26:07.310
Jacob Barhak: Finally, we have mortality models. People die out of Covid, they die, they eventually everything. But then

133
00:26:07.480 --> 00:26:19.582
Jacob Barhak: what frequency? Again, what's chance of dying. And when. So, there's 1 type of modeling saying, we'll take. This is information published by the Cdc. We'll take

134
00:26:20.410 --> 00:26:31.329
Jacob Barhak: between some ever. This is more complicated. I'll just say that it's the mortality, probability and the time, and it doesn't change much

135
00:26:31.930 --> 00:26:32.720
Jacob Barhak: it

136
00:26:32.940 --> 00:26:52.660
Jacob Barhak: but Filippocilione actually did a model about how organs die out of cells dying. This is a multi-model, like a multi-scale model, because he was working in level of cells, but later on tied it all the way up up to the mortality of the person. So it's different levels of size.

137
00:26:52.860 --> 00:27:19.839
Jacob Barhak: So this is why it's called the multi-scale model. And that model, it tells me, in each day after infection. Infections. D. 0, what's the chance of a person dying? So, for example, a 20 or someone an infant dying out of day, 1917, according to his model, is less than one per 1,000 if they get infected. But if you go to a 90 year old

138
00:27:20.460 --> 00:27:30.929
Jacob Barhak: in day 20. It's 1% in day. 19, it's a little bit less. It's also 1%. But then it drops and goes high. This is according to his model.

139
00:27:31.150 --> 00:27:55.689
Jacob Barhak: So now, which one of the ones models correct, so you can mix them up and check it out. And this is what we do. But before we do this we also have to account the fact that the numbers we get are incorrect. How many people here raise of hands? How many people here were saw something about the numbers that they are showing are wrong. Someone is miscounting them. During Covid we all went through Covid.

140
00:27:55.810 --> 00:27:59.739
Jacob Barhak: Come on Upper. Did you ever.

141
00:28:00.060 --> 00:28:04.030
Jim Mccormack: I definitely did. Yeah, I can't raise my hand, but I could raise my voice.

142
00:28:04.270 --> 00:28:12.689
Jacob Barhak: Yeah. So we know that the numbers people claim they're wrong. Some people think we're overestimate some people. They're underestimated, correct.

143
00:28:12.960 --> 00:28:27.870
Jacob Barhak: Everyone had their own opinion, and we don't know what drives those opinions, but we can suspect. But it doesn't matter really. For science we have different numbers, and we don't trust them. How do we correct and say, you know what?

144
00:28:28.190 --> 00:28:31.799
Jacob Barhak: We asked the question, what if it was a different number.

145
00:28:32.250 --> 00:28:39.130
Jacob Barhak: and what different number, for example, we know almost for sure, that the number of infections that we have is

146
00:28:41.430 --> 00:28:47.100
Jacob Barhak: is miscounted. It doesn't represent the probability in the entire society

147
00:28:47.711 --> 00:28:53.980
Jacob Barhak: like probability of not probability. The the proportion of people actually infected in society, because

148
00:28:54.300 --> 00:29:10.980
Jacob Barhak: the tests are always like they have a error. It also have matters when you test the person it. It matters not only when you test the person it's like in in the accuracy of the test, but also how how you conduct the test, how you

149
00:29:11.170 --> 00:29:27.340
Jacob Barhak: like, what your sample, all of what your sample population are. All of those things matter. So we pretty much assume that the numbers are underreported, the number of infections, people that are reported because there are those who never tested. Therefore their numbers didn't appear

150
00:29:27.420 --> 00:29:42.970
Jacob Barhak: so. Now, how much we multiply them. Well, some people multiply by 5. This seems to be like a running number that everyone multiplies in epidemiology. I claimed. Okay, let's try 20. Just if there's 5, let's try 20 and and

151
00:29:43.420 --> 00:29:49.230
Jacob Barhak: Lucas, who gave me this model, actually gave you an infectious model Lucas Botcher. He

152
00:29:49.770 --> 00:30:03.270
Jacob Barhak: he actually looked at. He says that it's also about 1757, 15, you have to multiply in fraction 7, 15. And then there's another model that it's more complicated. Explain. We'll leave it for now it doesn't matter, for now

153
00:30:03.480 --> 00:30:04.600
Jacob Barhak: and then

154
00:30:06.180 --> 00:30:16.249
Jacob Barhak: the mortality is the same thing, same people who died, you know people who died out of a car crash were listed, discovered. At least this is what was reported in some newspapers.

155
00:30:17.430 --> 00:30:27.399
Jacob Barhak: and and then vice versa. Some people died of Covid, maybe were written down that they died out of something else because of complication we never know. So

156
00:30:27.770 --> 00:30:36.420
Jacob Barhak: most, you can actually do this. And this is what Lucas the watcher, did. Did it per state, and he gave me a bunch of numbers per state.

157
00:30:36.580 --> 00:30:49.569
Jacob Barhak: So now I'm running all of those models to make sure that whatever is being told is correct. So now we have the 2 numbers, the true number that the model knows of how many people are infected, and the observed numbers which

158
00:30:50.160 --> 00:30:58.770
Jacob Barhak: takes all of those, and and and adjust this to the according to the real number. So in the zoom number the it will be different.

159
00:30:59.020 --> 00:31:20.830
Jacob Barhak: So now let's look at the results. This takes a lot of computing time to actually do. It's about 3 years of computation on one CPU or on on one CPU core. I use a 24 core machine. So it takes about 6 weeks to run that simulation that, you see, I'm now running a much, much bigger simulation. I might show you the screen while it's happening later on.

160
00:31:22.470 --> 00:31:49.910
Jacob Barhak: I. Each time each state is represented by 10,000 individuals, and those 10,000 interact kind of with each other, and also with all of the equations that I showed you. And each equation comes in with a different weight. And what I do is I run all the simulations and then test whether the numbers match or don't, how well or how badly they match or don't match their reported numbers. So let's look at this.

161
00:31:50.140 --> 00:31:56.009
Jacob Barhak: It's a huge I I cannot even show you the real results. This is a cut down version.

162
00:31:56.860 --> 00:32:03.119
Jacob Barhak: because otherwise it the file sizes become enormous at some point. But let's explain what you're seeing.

163
00:32:03.240 --> 00:32:09.579
Jacob Barhak: This is the population. panel you see here for each state

164
00:32:10.720 --> 00:32:27.540
Jacob Barhak: multiple of those circles each circles will present one day in one simulation, and I will start simulations again in different times. Because, remember, like, you have the timeline running and I

165
00:32:28.190 --> 00:32:56.680
Jacob Barhak: and I start the simulations once in day, one and then once in day 5, and then check it out after whether day 10 in one, and which means day 5 in the other, are the same. I include all of those together, because I'm if I start all the simulation the same time, and some of the numbers are wrong, then I have a problem. So I have to start the simulation different times in the pandemic and in different windows. Each time I run a window of 21 days.

166
00:32:56.780 --> 00:33:00.859
Jacob Barhak: and then I check after 21 days. How good it matches the results!

167
00:33:01.300 --> 00:33:07.789
Jacob Barhak: I I turned. I tried down the I figured out that I don't. If I don't do those windows, then

168
00:33:07.930 --> 00:33:14.660
Jacob Barhak: the the results are not really good. So those windows really help stabilize the results, because all the numbers become

169
00:33:15.080 --> 00:33:23.000
Jacob Barhak: the it's much less sensitive to to wrong number. To some errors that appear so.

170
00:33:23.750 --> 00:33:37.199
Jacob Barhak: What happens here is one circle represents, for example, the electric circle. This is Kentucky code 45 means that it starts 45 days into the after April first.st

171
00:33:37.300 --> 00:34:03.680
Jacob Barhak: This is where the simulation starts, and then it runs for 21 days. So after 21 days you can look at the results here. It will give you the average age and stuff like this. But look at the numbers that says, observed, observed, infected, you will see a number before the slash, and the number after the slash. Same thing observed death before the slash and after the slash the number before is what the model tells you.

172
00:34:03.980 --> 00:34:14.260
Jacob Barhak: The number after is the actual number, as reported by Covid tracking project after, of course, being optimized after being normalized to 10,000 people per state.

173
00:34:14.650 --> 00:34:20.170
Jacob Barhak: So this is out of 10,000 people. So you see the models way off like twice here.

174
00:34:20.570 --> 00:34:24.529
Jacob Barhak: Now, the height of that circle

175
00:34:24.750 --> 00:34:47.079
Jacob Barhak: is the error. It's called the fitness score. That takes into account the differences between the infectious, the observed infection model and the Re and the observed results and the death model and the observed results and the hospitalization model observed results. They're all bundled together.

176
00:34:47.300 --> 00:34:56.389
Jacob Barhak: And then this is being optimized using gradient descend, which is an AI technique that people are familiar with. This is what the base for all our neural networks is.

177
00:34:56.739 --> 00:34:57.690
Jacob Barhak: So

178
00:34:58.200 --> 00:35:09.280
Jacob Barhak: now I'm taking all of this, and I'm starting to optimize. Notice. The height of the circle is the error, and I'm trying to drop it down ideally. I want everything to be around 0.

179
00:35:09.810 --> 00:35:18.669
Jacob Barhak: And what I'm actually optimizing. Let's explain what happens here. You see, all those 5 blue ones. Those are all infectious bottles.

180
00:35:18.890 --> 00:35:26.039
Jacob Barhak: those purple ones are transmission models. The green ones are the behavioral models.

181
00:35:26.060 --> 00:35:43.350
Jacob Barhak: those the reddish or brownish ones, and the yellow ones are the hospitalization models. You remember, we have time and probability, and those are mortality models, and finally, the purple ones are mortality observer models. All of those are being a hospital

182
00:35:43.350 --> 00:35:58.570
Jacob Barhak: optimize at the same time. So now I'm looking, I'm I'm tweaking them, and I'm running ready in the center. There are variations. And then, little by little, you said, even like after 3 iterations, see, one of the transmission models totally disappears. We'll tell you which one in a second.

183
00:36:00.610 --> 00:36:21.890
Jacob Barhak: and then it continues continues, and see some here more dominant mortality models. So some of the mortality models were not that good? And continue and continue. Now you can build those curves I showed you at the beginning, you can actually figure out what the transmission was, how people behaved. You'll see the apple mobility data disappeared completely

184
00:36:22.656 --> 00:36:29.049
Jacob Barhak: within the transmission models, the model that disappeared in this one became dominant. Those are the ones with temperature.

185
00:36:29.600 --> 00:36:35.140
Jacob Barhak: The ones with it says that colder states transmit more

186
00:36:35.590 --> 00:36:41.780
Jacob Barhak: is the one that is dominant, meaning. If you're in a hot state you'll be. You're better off than in the cold state.

187
00:36:42.110 --> 00:36:44.770
Jacob Barhak: because this almost disappeared completely.

188
00:36:46.390 --> 00:36:52.820
Jacob Barhak: here in the infectious is one. You see that some of the dominant models, the one that were longer, not the one that shorter.

189
00:36:53.680 --> 00:37:02.510
Jacob Barhak: And finally, if you look up the mortality model, the one that Felipe Castiglio gave me is the dominant one

190
00:37:02.750 --> 00:37:07.500
Jacob Barhak: meaning this is these models actually better if you look at it over time

191
00:37:08.365 --> 00:37:30.270
Jacob Barhak: and observer models tell you that some of the models don't make sense like don't multiply by 20. It's somewhere between 1 5 or 7, 5 or 7, 1, 5. Approximately, the people who said that 5 times which you multiply, the number of infections, the correct number, those who are generally correct.

192
00:37:30.440 --> 00:37:34.860
Jacob Barhak: Approximately, we can actually calculate the exact numbers. But this doesn't matter, because

193
00:37:35.070 --> 00:37:43.209
Jacob Barhak: it's it's it's enough to know that it's what's wrong and what's not. And now we can answer questions about the pandemic.

194
00:37:43.530 --> 00:37:53.749
Jacob Barhak: And I've written all those things here. But let's talk about a little bit about conclusions. I'll I'll just conclude everything in case you might have questions.

195
00:37:54.540 --> 00:37:55.809
Jacob Barhak: and I want to go

196
00:37:56.190 --> 00:38:00.710
Jacob Barhak: too much overtime. I want to keep it short. Otherwise it's me talking. I want to hear you.

197
00:38:01.224 --> 00:38:06.839
Jacob Barhak: So the idea is that this model can help the government in the next pandemic.

198
00:38:08.740 --> 00:38:09.600
Jacob Barhak: Now

199
00:38:09.710 --> 00:38:20.649
Jacob Barhak: I'm telling you this, but I am biased because I developed it. This is developing for about since 2,012, I invested my all my time and effort and resources into this

200
00:38:21.990 --> 00:38:30.209
Jacob Barhak: quite a bit. I've been doing this for many years on my own. I'm a sole proprietor now, meaning I'm a company of one person in the us.

201
00:38:31.730 --> 00:38:38.319
Jacob Barhak: It's a form of explainable artificial intelligence, because I can explain to you things as you saw.

202
00:38:38.460 --> 00:38:43.289
Jacob Barhak: So it's AI. But the explainable type. Once I'm showing you

203
00:38:43.380 --> 00:39:08.519
Jacob Barhak: it's sometime now. The question is, how how good it is. So I can tell you for sure. It is difficult to explain phenomena like COVID-19, because there are many, many parameters, and the question is, how much time you know, because the next pandemic, if someone comes to me and ask me how good this tool will be, I tell them. Well, you have to have at least 3 weeks of data after you having some sort of

204
00:39:08.560 --> 00:39:32.929
Jacob Barhak: infection going on, I started modeling April 2020. So you need at least 4 weeks of data, but not this is actually not true, because 3 weeks of data will give you initially. When I did this it will give you different results, because you don't have enough numbers. You have to forward for at least several months and then do the windows I'm talking about, and then you and then the numbers started stabilizing it.

205
00:39:33.200 --> 00:40:00.399
Jacob Barhak: I'm still running a big simulation here to make sure those numbers are correct, because I'm doing Monte Carlo simulations when I flip all those coins. And I'm making sure that I throw enough computing power there to actually make it useful, and that I didn't make any mistakes. Eventually, every once in a while I find something that it was wrong that I need to correct. This is why there are multiple versions. But in the future you'll need at least a few months of data.

206
00:40:00.940 --> 00:40:11.729
Jacob Barhak: plus you have to one of those windows, but maybe you'll get initial results after a month or 2, and and at least some sense you'll get, and then later on you'll get

207
00:40:11.860 --> 00:40:21.439
Jacob Barhak: you. You go with it, so the Government will not be completely clueless like it was in the pandemic, because now we find out how clueless they were.

208
00:40:23.490 --> 00:40:34.629
Jacob Barhak: now I can tell you that the peak average infections to about day 5 from infection. This is for covid and transmission rate is about 2% per encounter. It's a little bit less

209
00:40:34.750 --> 00:40:38.140
Jacob Barhak: warm weather seems to reduce transmission. Now.

210
00:40:38.520 --> 00:40:52.450
Jacob Barhak: this is something important. Today we published the paper lessons learned from COVID-19 for modeling COVID-19, and steps to take in the next pandemic here. I'll show you the paper it will load. It's now in the preprint.

211
00:40:53.000 --> 00:41:06.579
Jacob Barhak: We have multiple collaborators and they have actually came from different perspectives. I'm not. I did the reference model, but they did other models that figured out how to do other things better.

212
00:41:06.710 --> 00:41:24.230
Jacob Barhak: and we wrote down the paper and says, what how to do, modeling better, how to spread information better and get it correctly, how to validate the information properly, and also we have some recommendation about infrastructure and education that will help.

213
00:41:24.400 --> 00:41:33.289
Jacob Barhak: So if you're interested, please go and read the paper. It's in preprint. You can get it by following this link number 53 here.

214
00:41:34.960 --> 00:41:59.159
Jacob Barhak: All of what I showed you here cannot produce to some degree. I'm showing exactly what I what data I did. So I can trace back. If someone ever asks me about the presentation where I got the numbers from the codes that actually created the presentation. You can find it on Github. I actually release it. But not all of the data. Some things up priority. I have a conflict of interest statement here

215
00:41:59.160 --> 00:42:05.399
Jacob Barhak: because I do intend to get money out of it. I have 2 patents us patents on this technology.

216
00:42:05.871 --> 00:42:12.049
Jacob Barhak: I'm now licensing them. If someone interested know someone who's interested, please do connect us.

217
00:42:12.280 --> 00:42:32.328
Jacob Barhak: And I've many, many people to think and many organizations. Some people gave me some all sorts of all sorts of help people from all of his allowed all this the presentation technology ideas might just help me out finding some resources and connecting to some people that help.

218
00:42:32.930 --> 00:42:43.334
Jacob Barhak: people hosted my computer published the the video, you can actually see this. This is the video that's embedded. You can actually look at it later. So it was published in Siphode.

219
00:42:44.108 --> 00:42:59.230
Jacob Barhak: people who will contribute models. I'm showing some of the other work they did here. People who contributed money to actually run simulations on cloud, I actually ran several simulations in the cloud, which, instead of several weeks or months. They ran in 2 days.

220
00:42:59.850 --> 00:43:21.759
Jacob Barhak: not all the time you have money for that. So Rescale gave me money for azure, and Amazon and Midas gave me some money. I ran simulation on the Google card with them. They gave it through some grant and many, many people. I have to thank for all the way for various ideas or things. So thank you all. And I'm open for questions

221
00:43:22.170 --> 00:43:23.910
Jacob Barhak: underneath this.

222
00:43:28.300 --> 00:43:33.410
Jim Mccormack: So, Jacob, have you been able to use any of it on like bird flu, or any other pandemics that

223
00:43:34.160 --> 00:43:37.540
Jim Mccormack: that are starting or rumored to be the next pandemic.

224
00:43:37.780 --> 00:43:50.169
Jacob Barhak: Currently, I'm focusing on Covid because this is technology. Still believe it or not, it's still in development phase. Because here you show me any technology that you invested 20, many years in?

225
00:43:50.360 --> 00:43:53.360
Jacob Barhak: Is it something good enough? 20, many years?

226
00:43:53.900 --> 00:43:58.020
Jacob Barhak: This is what they? It's about 20. It's about 20 years of development.

227
00:43:59.560 --> 00:44:07.305
Jacob Barhak: You tell me so. I I'm still making sure I'm cutting all the bits and pieces.

228
00:44:07.920 --> 00:44:20.389
Jacob Barhak: so for this such technologies, you need many more resources to actually meaning I'm talking. I'm not talking about, you know, some game that blows up that people use, or something that is fairly tested.

229
00:44:20.980 --> 00:44:40.410
Jacob Barhak: Sometimes they are not really retested. They just blow up like virally. Here, you actually to be correct, that this technology works, you actually have to invest a lot of time. Now, the big problem with all of the data, which is a different project that I'm making is the fact that you cannot get medical data.

230
00:44:40.620 --> 00:44:57.669
Jacob Barhak: One of the advantages of this project is that it can actually merge data from multiple sources. This is practically not allowed in the medical world, because if you have population A and population B in the medical world. They are not allowed to merge the data between those 2.

231
00:44:58.220 --> 00:45:14.120
Jacob Barhak: No, no, because it's patient data. So the individual data is not allowed. But you're allowed to merge the models. And this is what I'm doing. This is why this technology is important, not only for the pandemics I'm doing. I'm doing it on the pandemics, because there I have good data.

232
00:45:14.220 --> 00:45:37.740
Jacob Barhak: The other model I have is the diabetes model today, as far as I know, I have the most validated diabetes model worldwide, because I tested it with more populations than anyone else. How did I do it? I connected to clinicaltrials.gov got the information from there. But the thing is even data and clinicaltrials.gov, is not that good here. I'll show you. That's another project that I'm working on.

233
00:45:38.060 --> 00:45:49.700
Jacob Barhak: Even to get the data out of those models. It's impossible. Because the units of measure are messed up, even if you do it correctly, I'm going to show you just only one thing.

234
00:45:50.650 --> 00:45:57.069
Jacob Barhak: It will take a minute to load. This is a website. It's actually active. You can check it out. But, like here, Hba, one C is a measure of diabetes.

235
00:45:57.900 --> 00:46:05.770
Jacob Barhak: So see how many ways people write. Hba, one C, the units of measure. A computer cannot understand it.

236
00:46:06.330 --> 00:46:18.110
Jacob Barhak: So you need AI to tell it how it's supposed to be. That's a different project I'm doing, which is a spin off of this project. And actually, there's some claims in the patents that relate to this project as well. So

237
00:46:18.290 --> 00:46:29.200
Jacob Barhak: eventually, being able to get the disease models correctly, you need correct data. You messing around with the data is the biggest problem.

238
00:46:29.550 --> 00:46:34.450
Jacob Barhak: So you're saying bird flu because everyone says bird flu. But you have good data about bird flu.

239
00:46:35.380 --> 00:46:39.609
Jacob Barhak: Well, once you start with Covid, you didn't have good data.

240
00:46:39.720 --> 00:46:54.809
Jacob Barhak: And this is why we had this project running. And this is where accommodations, how to get good data for the future and how to do it. So we can models can use it can actually get the results I got I got it took me about 5 years to get to the something stable that I'm showing you now.

241
00:46:55.100 --> 00:47:16.629
Jacob Barhak: and I start in the beginning of the pandemic in the next pandemic. If it'll be one year it will be better, and then it will be few 3 months, or 2 months, or 2 weeks, then it will better and better and better. But to get to that point we need an entire lubricated system that gives us all the things that we need all the correct data and all the correct models, and so on and so forth.

242
00:47:16.630 --> 00:47:25.530
Jacob Barhak: This is still a lot of work. The big systems are not yet set to it, and hopefully this paper will be helpful in this regard.

243
00:47:25.670 --> 00:47:30.479
Jacob Barhak: and think about how much money was found in Covid, and how many models are out there.

244
00:47:30.890 --> 00:47:51.490
Jacob Barhak: Think about some big machine that crunches all of those assumptions in the future that people plug in and tells them, oh, this is somebody is probably incorrect. This doesn't match this data or that data. This is what my technology does. And we do have the computing power today. But we do need the the software infrastructure, and all those many years that I only started.

245
00:47:51.660 --> 00:47:53.450
Jacob Barhak: Did did I answer your question, Jim?

246
00:47:53.710 --> 00:48:09.379
Jim Mccormack: Yeah, yeah, and very well, so it's it is. It is again, Jacob. If I restate right? So it may not be directly translatable to bird flu. But the lessons learned and the prep work right will get us to those answers faster. Using this example in this work.

247
00:48:09.530 --> 00:48:28.879
Jacob Barhak: I didn't try it on birth flu. If you give me data of birth flow, I can try it. But then I'll tell you. Oh, this is missing, and this is missing, and I need all those assumptions. And then you'll start finding all those researchers, and they won't go even finding researchers to collaborate, to give you all those models also takes time. All of this has to be centralized in a way that

248
00:48:29.370 --> 00:48:37.410
Jacob Barhak: the system was during Covid. Everything was kind of a mess. I wasn't part of that mess. I was trying to find things. I couldn't find them.

249
00:48:37.900 --> 00:48:45.199
Jacob Barhak: I I believe I was. I was stressed because I was working on this, for at that point, like 15 years, and I still was

250
00:48:45.860 --> 00:49:01.209
Jacob Barhak: feeling that I don't need. I have everything I need, like all the pieces and pieces now, and we're trying to normalize it and give more accommodations how to do it better in the future. The idea is that someone who actually is interested.

251
00:49:01.210 --> 00:49:20.360
Jacob Barhak: We'll look at it, learn from it, and then start training groups that will do those things. I have a friend who actually has some good ideas about his name is John Rice, and he actually was the instigator of this paper, saying, You know, what what did you learn from all this work that you did about Covid. So we organized it all in a way that in the next pandemic

252
00:49:20.530 --> 00:49:29.019
Jacob Barhak: there won't be such a problem. And we're now propagating this paper. If you're interested in helping take this paper, send some of your friends.

253
00:49:29.910 --> 00:49:32.570
Gabor Szabo: There's another question I see in the in the chat.

254
00:49:35.170 --> 00:49:36.230
Gabor Szabo: Can I read it out.

255
00:49:37.783 --> 00:49:38.549
Jacob Barhak: Yeah. Please.

256
00:49:38.730 --> 00:49:44.720
Gabor Szabo: For type, one diabetes modeling. Isn't that a generic disease? Autoimmune.

257
00:49:45.690 --> 00:49:46.115
Jacob Barhak: Well.

258
00:49:47.190 --> 00:49:55.940
Jacob Barhak: type diabetes is different than type 2. They have different mechanisms. I'm not a medical doctor to goes into those.

259
00:49:56.540 --> 00:50:05.610
Jacob Barhak: It was explained to me many times while I was doing diabetes type 2 diabetes. I was working with a team of experts, worldwide experts in diabetes.

260
00:50:06.670 --> 00:50:12.190
Jacob Barhak: I'm less concerned about the type of disease or what it is.

261
00:50:12.350 --> 00:50:24.139
Jacob Barhak: Diseases for me are state transition models, where you jump from one state to another, and there's a probability of moving there, and the probability depends on all sorts of parameters.

262
00:50:24.380 --> 00:50:25.230
Jacob Barhak: So

263
00:50:25.480 --> 00:50:42.630
Jacob Barhak: the source of the disease or the cures, I don't care much. I just want to be able to explain it, explain it. And how do I explain it? If I have a model that says A, and then model, says BI want to know which one of those contributes more to the numbers I see at the end.

264
00:50:42.810 --> 00:50:52.719
Jacob Barhak: The way I look at the diseases. It's all numbers and some people who understand all of the elements. They are the ones making the models.

265
00:50:53.240 --> 00:50:56.230
Jacob Barhak: So does it answer your question.

266
00:51:00.390 --> 00:51:07.479
Jacob Barhak: Okay, so this is why it is. And I'll try to send you the link for that.

267
00:51:08.800 --> 00:51:09.860
Jacob Barhak: Here we go.

268
00:51:10.650 --> 00:51:31.700
Jacob Barhak: This is the link for that paper, the lessons learned paper. So if you know people who are interested please propagate that this is important. Hopefully, some governments or some organizations will adapt. Next pandemic will have less mess than we had in this pandemic. By the way, when I started the pandemic, everyone was doing Covid

269
00:51:31.950 --> 00:51:45.610
Jacob Barhak: really. Like every every department, every institution was like financial institutions were running Covid models computation institutions were having Covid. Everyone

270
00:51:45.860 --> 00:51:53.350
Jacob Barhak: had Covid model. Now I'm i i even talking to people who model Covid is kind of hard

271
00:51:53.520 --> 00:52:16.299
Jacob Barhak: because they they all stopped doing it. It's less interesting. But for me it's interesting very much to know, because I really am dedicated to it. And this is my life's work. I've been working on this almost 20 years, and I want this to continue for and and done properly. So this is why I'm giving this talk, and Gabor. Thank you for having me.

272
00:52:17.117 --> 00:52:26.700
Gabor Szabo: Thank you for giving this talk. This presentation. And anyone any more questions before we

273
00:52:27.180 --> 00:52:29.009
Gabor Szabo: we close the video.

274
00:52:31.430 --> 00:52:40.860
Jacob Barhak: If you have python questions on how I did this with python, or how I did that, it's also I can. I'm running many, many things. Actually, maybe it's a good time to show you.

275
00:52:41.020 --> 00:52:42.370
Jacob Barhak: You see

276
00:52:43.590 --> 00:53:03.189
Jacob Barhak: this thing hopefully, I won't disconnect everything. This is a call, a screen of a computer. Behind it is a 24 core machine. Like a very good processor, it runs as fast as older supercomputers. 32, core, 32 threads. And this simulation. Now it's

277
00:53:04.120 --> 00:53:04.890
Jacob Barhak: team.

278
00:53:04.890 --> 00:53:07.520
Gabor Szabo: If you stop the screen sharing you'll see better.

279
00:53:08.430 --> 00:53:10.879
Jacob Barhak: Oh, oh, okay, I'll stop screen share.

280
00:53:11.850 --> 00:53:12.820
Jacob Barhak: Second.

281
00:53:16.910 --> 00:53:19.340
Jacob Barhak: how do I stop the screen? Share?

282
00:53:21.328 --> 00:53:25.809
Jacob Barhak: Think it shows me screen share. How do I stop it? It says, only share.

283
00:53:26.120 --> 00:53:27.730
Jacob Barhak: Did I stop the share?

284
00:53:28.380 --> 00:53:28.910
Jacob Barhak: No.

285
00:53:28.910 --> 00:53:29.850
Gabor Szabo: Oh, not yet.

286
00:53:30.770 --> 00:53:31.900
Jacob Barhak: Give me a second.

287
00:53:35.300 --> 00:53:41.260
Jacob Barhak: I'm not sure how to stop the share in this model. Oh, oh, okay, thank you.

288
00:53:41.460 --> 00:54:08.409
Jacob Barhak: You see, this. This screen is actually a computer that runs simulation, same simulation. You see. Now, it's around here. This is iteration 17. It should get to 40 to get something stable approximately, this is my currently baseline. I've seen all the simulation 40, but this one is like much, much bigger. Here. I start the simulation in each day, and I run 5 repetitions

289
00:54:08.700 --> 00:54:15.240
Jacob Barhak: for all of this. I'm I'm actually running about like 2 months of day for I have information from April to June.

290
00:54:15.260 --> 00:54:43.210
Jacob Barhak: and each time I start a different day and run for 21 days and check the numbers for 5 simulations for each State, and then I continue doing this and this state. This will take me about half a year. I started a few months ago, and I had some options, power problems. And so on. So for computer problems, I actually burned computers on this. I kid you, not. I have multiple computers dead because of running all those simulations running all throughout the world for many, many years.

291
00:54:43.340 --> 00:54:52.760
Jacob Barhak: So I started with small clusters. I created clusters. I use dusk to create clusters. To this. I still it still runs with dusk. You cannot

292
00:54:53.020 --> 00:54:54.450
Jacob Barhak: see the best. This is.

293
00:54:56.670 --> 00:54:59.559
Gabor Szabo: Yeah, I can't. We can't really see that. No? Well.

294
00:55:00.037 --> 00:55:04.800
Gabor Szabo: apologies, I cannot make it much, much closer, very bright.

295
00:55:05.370 --> 00:55:09.679
Jacob Barhak: I apologize. This is, this is the best I can do, anyway.

296
00:55:10.630 --> 00:55:16.720
Gabor Szabo: Oh, thank you very much again, and thank you everyone for for being here, and if you're watching.

297
00:55:16.830 --> 00:55:27.079
Gabor Szabo: I mean they they you share the links. So people can find you. They will be under the the video. There will be a link for all the all these things.

298
00:55:28.670 --> 00:55:30.450
Gabor Szabo: Like the video

299
00:55:30.740 --> 00:55:38.570
Gabor Szabo: share, follow the channel, share the video and talk to Jacob. If you were interested in discussing this topic.

300
00:55:38.870 --> 00:55:40.539
Jacob Barhak: Please. Thank you very much.

301
00:55:40.540 --> 00:55:41.120
Jim Mccormack: Thank you.

302
00:55:41.120 --> 00:55:41.760
Gabor Szabo: Right.

303
00:55:42.730 --> 00:55:43.610
Jacob Barhak: Bye, bye.

