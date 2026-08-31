---
title: How Python and FFmpeg Let Us Handle Conference Video Post-Production at Zero Cost
timestamp: 2026-08-31T19:30:01
author:
published: true
description:
tags:
---

## Description:

In this session, we'll go through the different stages of conference video production.

We'll gradually move toward the challenges one may face during post-production.

We'll look at how repetitive and redundant editing steps can be identified and generalized.

We'll explore how Python and FFmpeg can be used to automate these steps.

We'll introduce another level of abstraction over the underlying video-editing operations.

The session will include a live demo of the resulting script and pipeline.

We'll also review how the pipeline works and discuss how it can be adapted to similar post-production workflows.

## Bio:

[Suren Poghosyan](https://www.linkedin.com/in/surenpoghosyan/) is a Computer Science student at the American University of Armenia and an open-source community organizer. He co-organizes PyData & PyCon Yerevan, PyData Yerevan, QGIS Armenia, and Julia Yerevan, and is interested in core concepts of software engineering, enthusiastic about data science, scientific computing, GIS, and open-source software.

He is driven by a growth mindset and maintains consistent curiosity for employing software for solving existing operational problems that will free up human power and time for focusing on problems of greater matters.

{% youtube id="kjinQxOGH90" file="2026-08-30-python-and-ffmpeg-to-handle-conference-video-post-production-at-zero-cost-with-suren-poghosyan.mp4" %}


## Transcript

1
00:00:01.850 --> 00:00:19.389
Gabor Szabo: So, hello and welcome to the Code Maven YouTube channel, if you are watching the video, and welcome everyone to the Python Maven session that you just joined. My name is Gabor Szabo, I organize these events, and I invite interesting people to give interesting presentations.

2
00:00:19.430 --> 00:00:22.640
Gabor Szabo: And, hello, Suren. Welcome to this,

3
00:00:22.970 --> 00:00:32.610
Gabor Szabo: session. I hope you'll introduce yourself in a… after I, I give you the floor. If you are,

4
00:00:32.770 --> 00:00:47.870
Gabor Szabo: here in the session, remember that you can ask questions via the chat. You can't speak, but you can… I mean, you can speak, we just won't hear you. You can ask questions in the chat, and I will ask those questions on your behalf.

5
00:00:47.960 --> 00:00:57.860
Gabor Szabo: And we are recording this, and it will be on YouTube. And also, after we stop the video, after we finish the presentation and all the questions.

6
00:00:57.860 --> 00:01:14.050
Gabor Szabo: that are really, really relevant to this. We can stop… we stop the recording, and then you have the chance to have a further session, a further free conversation among ourselves, with our guests, or about basically anything. So that's the…

7
00:01:14.200 --> 00:01:32.549
Gabor Szabo: privilege of being here. Below the video, on YouTube, you'll find a link to some more details about this session, and a link to the further events if you are interested in registering. With that said, Suren, thank you, really, for coming on and agreeing to give this presentation.

8
00:01:32.650 --> 00:01:34.870
Gabor Szabo: The floor is yours.

9
00:01:35.830 --> 00:01:52.630
Suren Poghosyan: Hi everyone, hi people. Thank you, Gabor for introducing me and inviting me to this event. I am Suren, a student at the American University of Armenia, and our today's topic is video production, and…

10
00:01:52.860 --> 00:02:03.140
Suren Poghosyan: video post-production automation. A short story, how I ended up at this point. At the beginning of the year, or even

11
00:02:03.610 --> 00:02:06.700
Suren Poghosyan: Two years before I started helping.

12
00:02:06.850 --> 00:02:15.349
Suren Poghosyan: to organize events for the local PyData community, which is called Pi Data Yerevan, and I start contributing through

13
00:02:17.060 --> 00:02:26.970
Suren Poghosyan: helping with video equipment, picking equipment, and recording the sessions, and editing those. When you have a single meeting.

14
00:02:27.180 --> 00:02:35.779
Suren Poghosyan: single meetup. You have a single recording, and it's pretty easy to handle, and…

15
00:02:35.950 --> 00:02:53.699
Suren Poghosyan: within your routine, and it's not noticeable. But when you're organizing a conference, and you have 35 sessions, and usually you spend from 1 to 2 hours on video editing, and now you have to spend 35 to 70 hours

16
00:02:53.810 --> 00:03:12.019
Suren Poghosyan: On video editing, it doesn't sound well. Especially when these are not some unique steps, but 35 repetitive group of steps that you have to apply to each video, which feels annoying, tiring, and…

17
00:03:12.910 --> 00:03:16.849
Suren Poghosyan: At some point, you will want to give up.

18
00:03:17.050 --> 00:03:28.139
Suren Poghosyan: just not to do all these repetitive tasks. So what it led me to is creating some predefined workflow.

19
00:03:28.220 --> 00:03:37.510
Suren Poghosyan: that captures the steps that I was doing during the meetups, during the video editing of the meetups.

20
00:03:37.720 --> 00:03:41.720
Suren Poghosyan: And capture that in a FFmpeg workflow.

21
00:03:42.340 --> 00:03:49.720
Suren Poghosyan: So, what you see here is part of that workflow, but… before,

22
00:03:50.920 --> 00:03:58.750
Suren Poghosyan: Before explaining how the code works, what methods I used, why I used that, I would like to explain you the

23
00:03:58.910 --> 00:04:02.950
Suren Poghosyan: Scale and the steps, done during the conference.

24
00:04:04.640 --> 00:04:13.829
Suren Poghosyan: Which affect your further decisions and, your further, Steps during the post-production.

25
00:04:14.040 --> 00:04:18.979
Gabor Szabo: Sure, could you please… there's a request, could you please enlarge the phones a little bit?

26
00:04:19.649 --> 00:04:22.479
Suren Poghosyan: enlarge the fonts, I mean, the screen.

27
00:04:22.850 --> 00:04:24.179
Gabor Szabo: On the screen, yeah.

28
00:04:24.390 --> 00:04:24.939
Suren Poghosyan: Of course.

29
00:04:24.940 --> 00:04:27.710
Gabor Szabo: Oh, thank you. Oh, but yeah, I think it's way better, thank you.

30
00:04:27.710 --> 00:04:28.960
Suren Poghosyan: Is this better?

31
00:04:28.960 --> 00:04:30.030
Gabor Szabo: Yeah, yeah, huh?

32
00:04:31.210 --> 00:04:35.310
Gabor Szabo: a response from the audience, but yeah, I think it's one better.

33
00:04:36.790 --> 00:04:51.020
Suren Poghosyan: So, the steps are these. You have, parallel tracks, say 3 to 4 tracks, during the conference. Each of the track has its, video camera, a PC, which records the screen, and

34
00:04:51.250 --> 00:04:54.700
Suren Poghosyan: some… Equipment for audio?

35
00:04:55.150 --> 00:05:09.369
Suren Poghosyan: Some of the equipment is directly connected to the camera and records the audio to the main video, which can't be later separated or processed because it's getting embedded into the video.

36
00:05:09.860 --> 00:05:23.459
Suren Poghosyan: And, some audio recordings are taken from the system audio of the room, say we have a big room, and we have an audio infrastructure there, and…

37
00:05:23.460 --> 00:05:35.919
Suren Poghosyan: We just connect to that line of audio and record that line. And also, besides that, there's the third audio recording method that, I…

38
00:05:36.030 --> 00:05:40.160
Suren Poghosyan: Applied in my design, it was the backup audio for the keynote speeches.

39
00:05:40.350 --> 00:05:46.750
Suren Poghosyan: well, this was in case if the… May recording was.

40
00:05:48.380 --> 00:05:58.459
Suren Poghosyan: bad, or that the camera recording had some issues. It was for the case that the keynote speeches have audio, at least.

41
00:05:59.260 --> 00:06:06.559
Suren Poghosyan: And, that describes what kind of files you will have at the end to work with.

42
00:06:06.560 --> 00:06:30.479
Suren Poghosyan: You have a video recording that has the audio coming from the microphone attached to the speaker. There is a video recording coming from the system, which is not synced with the video, which is just a file, and there is the third audio recording which you have, which is also not synced with the main video file. It's just a recording, independent of

43
00:06:30.970 --> 00:06:32.730
Suren Poghosyan: All of the other stuff.

44
00:06:33.640 --> 00:06:34.990
Suren Poghosyan: So,

45
00:06:36.790 --> 00:06:44.239
Suren Poghosyan: Actually, recording the audio on the video is the best. You don't have to deal with synchronization of the video and audio.

46
00:06:45.820 --> 00:06:52.779
Suren Poghosyan: But having these other files is just a measure of safety in order to later be able to do that manually.

47
00:06:53.130 --> 00:06:55.210
Suren Poghosyan: And not lose any data.

48
00:06:55.460 --> 00:06:58.780
Suren Poghosyan: Regarding the screen recording, you…

49
00:06:59.030 --> 00:07:04.430
Suren Poghosyan: I decided to record the audio on the screen recording as well, in order

50
00:07:04.640 --> 00:07:16.869
Suren Poghosyan: for me later to be able to apply some synchronization techniques on the speaker video and screen recording, because when you start the screen recording and then

51
00:07:16.870 --> 00:07:26.540
Suren Poghosyan: run to start the video recording, there's a gap between, there's an offset of seconds that you have to cut in the post-production, and

52
00:07:27.120 --> 00:07:29.390
Suren Poghosyan: In order to,

53
00:07:30.120 --> 00:07:45.700
Suren Poghosyan: avoid that, or prevent having that manually without a software solution, you have to be really fast to click on the recording button and run and start the screen recording button. So, in this case, recording the

54
00:07:45.760 --> 00:07:52.989
Suren Poghosyan: Audio on the screen recording as well, helps you to synchronize the speaker,

55
00:07:54.590 --> 00:08:07.899
Suren Poghosyan: To synchronize this through what speaker says, because there are, like, amplification of the audio that can be later, like, shifted and synced together and trimmed on the start and on the end.

56
00:08:08.200 --> 00:08:10.069
Suren Poghosyan: So, speaking about that.

57
00:08:10.310 --> 00:08:25.899
Suren Poghosyan: We can already start exploring our code, and a small detail before looking into the code is the banners. Videos are usually look like this. You have a banner for the first few seconds.

58
00:08:25.900 --> 00:08:43.180
Suren Poghosyan: Which, say, introduces the sponsors, organizers, the speaker, their name, and their position, and then the main video starts with the layout, where there is the screen recording, there's the speaker, and the, say, your chapter name, Python Maven, or…

59
00:08:43.179 --> 00:08:48.120
Suren Poghosyan: the conference name, PyData, PyCon, Yerevan 2026 that we had.

60
00:08:49.120 --> 00:08:51.810
Suren Poghosyan: And that's it. That's the whole thing that you…

61
00:08:51.810 --> 00:08:58.110
Gabor Szabo: You also… you also probably have, intro music, right, during this first slide.

62
00:08:58.840 --> 00:09:06.150
Suren Poghosyan: Sometimes, it's kind of a template that you define in your workflow. We had, say, an intro video.

63
00:09:06.300 --> 00:09:22.339
Suren Poghosyan: for, say, Acheon College, but for the regular meetups, but in this case, we don't have that. So, in order to have that, you have to modify the pipeline. That's what makes it more complicated in this case.

64
00:09:22.860 --> 00:09:35.540
Suren Poghosyan: that could be easily done with, say, Adobe or any similar tools which provide you layering, and you can drag and drop stuff there. But it's easy for a single clip, not…

65
00:09:35.700 --> 00:09:53.880
Suren Poghosyan: for applying many, many… too many, many clips. Well, I had some ideas on how to apply that using Adobe. I will talk about that and drawbacks of that as well a bit later. So, let's start from, say, the banner pipeline.

66
00:09:54.270 --> 00:10:02.080
Suren Poghosyan: So there is this package called ImageMagic, which is similar to FFmpeg, but is, for,

67
00:10:02.900 --> 00:10:11.630
Suren Poghosyan: editing images, it's like a foundational library for that. If I'm not mistaken, it is also written in C, so it's pretty foundational.

68
00:10:11.730 --> 00:10:19.149
Suren Poghosyan: Here, we have, modifications regarding the, pads, like, you…

69
00:10:19.430 --> 00:10:34.450
Suren Poghosyan: You have some predefined assets, such as a template that does not change through banners, say, the sponsors, the conference name, and the organizer label.

70
00:10:34.860 --> 00:10:41.579
Suren Poghosyan: But there are stuff that change. For example, speaker pictures, and title, and description.

71
00:10:41.960 --> 00:10:52.189
Suren Poghosyan: So, what you want to automate is not just assembling the whole template for all the banners, but just creating

72
00:10:52.300 --> 00:11:03.329
Suren Poghosyan: One for where other stuff, such as the conference name and else, are fixed, and only apply the things that are changing.

73
00:11:03.690 --> 00:11:13.829
Suren Poghosyan: So, here we firstly define the layout. Say we want the avatar to have this much size, 275 pixels.

74
00:11:15.620 --> 00:11:25.159
Suren Poghosyan: I think it applies to both, dimensions. It is… it becomes a square picture, and the coordinates are,

75
00:11:25.750 --> 00:11:29.339
Suren Poghosyan: Calculate it from the top left corner.

76
00:11:30.750 --> 00:11:46.869
Suren Poghosyan: And this means I want the speaker picture to be 110 points or pixels to the right from the top left corner, and down by 412 points or pixels from the top.

77
00:11:46.920 --> 00:12:01.609
Suren Poghosyan: And the same applies to the text, but here you also specify some kind of font. I mean, you can choose better readable fonts in order to use in your banners, but in this case, I used this one.

78
00:12:01.670 --> 00:12:07.099
Suren Poghosyan: To comply with the licensing and distribution, and not have further problems.

79
00:12:07.420 --> 00:12:10.400
Suren Poghosyan: And distributing the open source tool.

80
00:12:10.830 --> 00:12:26.109
Suren Poghosyan: And the same for the title of the person, which is, like, at the same time, the description. Say, student at some university, or senior engineer at some company.

81
00:12:26.760 --> 00:12:29.010
Suren Poghosyan: Here we have an array of…

82
00:12:29.580 --> 00:12:36.340
Suren Poghosyan: objects, say, which represent each speaker, and their picture

83
00:12:36.470 --> 00:12:44.830
Suren Poghosyan: unique background that you can use. Maybe you want to use… you have multiple templates, sometimes

84
00:12:45.390 --> 00:12:58.989
Suren Poghosyan: You have to put two speakers on the same banner, but this case doesn't cover that. But just for an example, you can modify these and get different outcomes.

85
00:12:59.310 --> 00:13:07.010
Suren Poghosyan: And the speaker photo, name, and title as well, as we defined previously in this, configuration.

86
00:13:09.040 --> 00:13:19.439
Suren Poghosyan: In order to connect to that command line tools, we use subprocess, which is a default package coming with Python.

87
00:13:20.280 --> 00:13:21.919
Suren Poghosyan: And,

88
00:13:22.540 --> 00:13:34.029
Suren Poghosyan: Initially, you have to define your canvas size, which are defined as variables in the beginning. This is the Full HD 1609 resolution.

89
00:13:34.200 --> 00:13:38.340
Suren Poghosyan: Same, no… as known as, if…

90
00:13:39.580 --> 00:13:51.440
Suren Poghosyan: it's called landscape, right? There's the portrait one, which is vertical, and landscaped, which is horizontal. So we do all the stuff horizontally, because we make regular videos.

91
00:13:52.190 --> 00:14:03.429
Suren Poghosyan: After defining the canvas sizes, we… I mean, this provides the commands that later will be utilized for defining the canvas size.

92
00:14:03.660 --> 00:14:06.959
Suren Poghosyan: And we have, another command for…

93
00:14:07.920 --> 00:14:11.169
Suren Poghosyan: Creating the banner itself, the intro banner.

94
00:14:11.200 --> 00:14:27.529
Suren Poghosyan: So, note, the intro banner is not currently used in this workflow, because in our videos, we decided to have a single banner, which includes the speaker and all the other information, to have that for 5 seconds, instead of, like, having the

95
00:14:27.530 --> 00:14:43.360
Suren Poghosyan: sponsors and organizers banner at first, for the first 5 seconds, and later have the speaker banner, which will extend that intro to, 10 seconds, split it into two parts, which may,

96
00:14:43.420 --> 00:14:46.350
Suren Poghosyan: I don't know… field.

97
00:14:46.950 --> 00:14:54.649
Suren Poghosyan: too long for the viewer, because when they click on the video, they expect to watch the video right away, and you are… and if you are showing them

98
00:14:55.720 --> 00:15:00.699
Suren Poghosyan: a series of introductions, they may get tired and just close the video, or…

99
00:15:00.810 --> 00:15:02.900
Suren Poghosyan: I'll skip to the center of the video.

100
00:15:03.710 --> 00:15:10.340
Suren Poghosyan: So here we have the, the actual banner creation workflow.

101
00:15:10.860 --> 00:15:24.819
Suren Poghosyan: We have the avatar configurations, name, and title, and the sizes, coming from the very first configuration web that we defined, and we run it through this

102
00:15:24.820 --> 00:15:31.559
Suren Poghosyan: ImageMagic workflow, and… also, this is a function.

103
00:15:31.730 --> 00:15:37.089
Suren Poghosyan: Defined per each banner, which later we iterate through

104
00:15:38.120 --> 00:15:45.580
Suren Poghosyan: Which later we use for iterating through the array of sessions and applying it to each banner.

105
00:15:45.720 --> 00:15:47.550
Suren Poghosyan: So let's run this,

106
00:15:47.830 --> 00:15:58.119
Suren Poghosyan: workflow, and I want to show you… oh, I can't show you, actually, but… because I shared only my Chrome screen, but,

107
00:15:59.120 --> 00:16:06.389
Suren Poghosyan: Yes. Let me, let's just run this, and later we will go to another tab, another…

108
00:16:06.800 --> 00:16:10.730
Suren Poghosyan: window, and I will show you how it looks like there.

109
00:16:11.110 --> 00:16:18.639
Suren Poghosyan: running… it takes a few seconds for ImageMagic to run, because it's a single frame, and I'm running it on my

110
00:16:18.890 --> 00:16:21.849
Suren Poghosyan: MacBook Pro M1 Pro chip.

111
00:16:22.280 --> 00:16:34.109
Suren Poghosyan: So it's pretty fast. And I also will talk about my plans that I had for running all this workflow on an independent machine, say a Raspberry or a Jetson.

112
00:16:36.450 --> 00:16:38.730
Suren Poghosyan: why I am not doing that.

113
00:16:39.810 --> 00:16:47.709
Suren Poghosyan: So, this workflow gives us the banner located in, in this path…

114
00:16:48.830 --> 00:16:54.059
Suren Poghosyan: in the banner output, and it uses the layout that I told you about.

115
00:16:54.680 --> 00:17:05.790
Suren Poghosyan: And so on. After creating the banner, you want to synchronize your videos, your speaker video and your,

116
00:17:05.980 --> 00:17:17.509
Suren Poghosyan: screen recording, because these are definitely not synchronized because of the same issue that I described to you regarding that you have to be the flash in order to

117
00:17:17.690 --> 00:17:21.980
Suren Poghosyan: We are quick enough to start both videos at the same time.

118
00:17:22.630 --> 00:17:35.829
Suren Poghosyan: So here, we as well define the paths that our videos are located and that our project folder is located. In our case, it is located in the

119
00:17:36.500 --> 00:17:42.229
Suren Poghosyan: where the SymPy is. SymPy is the tool

120
00:17:42.650 --> 00:17:44.669
Suren Poghosyan: That you are going through.

121
00:17:45.520 --> 00:17:49.169
Suren Poghosyan: That's why we don't specify any base path for that.

122
00:17:49.620 --> 00:17:52.829
Suren Poghosyan: We have the base part here, but we use for…

123
00:17:55.370 --> 00:18:00.689
Suren Poghosyan: specifying the full path in the FFmpeg commands, because FFmpeg

124
00:18:00.940 --> 00:18:17.910
Suren Poghosyan: doesn't care if you are in a certain folder, it is located on a system level. So when you're calling it, it sees its initial pad, and it doesn't see that you are, say, in the SynPy folder. That's why you have to specify the absolute pad.

125
00:18:18.090 --> 00:18:31.930
Suren Poghosyan: So here we use FFmpeg to extract the MPET3, the audio track from both videos, which later we'll use to understand the overlap of Ts.

126
00:18:32.210 --> 00:18:35.649
Suren Poghosyan: We also use a package called Librosa.

127
00:18:35.820 --> 00:18:39.800
Suren Poghosyan: In order, to,

128
00:18:40.150 --> 00:18:44.319
Suren Poghosyan: Convert these files into, readable arrays.

129
00:18:44.770 --> 00:18:54.739
Suren Poghosyan: and later compare these arrays. Proceeding to that part, This is the part wherein… We actually compare this

130
00:18:54.850 --> 00:19:05.420
Suren Poghosyan: two audio files, and we want to understand their similarity. In order to understand their similarity, we create these two arrays of

131
00:19:05.560 --> 00:19:16.269
Suren Poghosyan: Say, information, data, that… Tells you about the loudness at each variable point of time.

132
00:19:16.980 --> 00:19:25.500
Suren Poghosyan: So, when we use… we also apply NumPy at this stage in order to understand that correlation. When we use NumPyCorrelate.

133
00:19:25.640 --> 00:19:42.320
Suren Poghosyan: It actually… imagine taking these two arrays and shifting this point by… item by item over each other, and taking the dot product of the items that are below and above each other.

134
00:19:43.980 --> 00:19:50.770
Suren Poghosyan: I mean, taking the dot product of these two vectors. And later, you…

135
00:19:51.060 --> 00:20:05.050
Suren Poghosyan: do that shift with all the items. So, the way that the beginning of this vector is at the ending of the other vector, and that way you will have all the variations of dot products, and…

136
00:20:05.050 --> 00:20:13.260
Suren Poghosyan: Later, you find the dot product which has the highest value, which means, at that point, this,

137
00:20:14.010 --> 00:20:19.210
Suren Poghosyan: Two, vectors were able to produce to you the highest

138
00:20:19.500 --> 00:20:27.639
Suren Poghosyan: volume means they coincided, or they were similar at that point the most.

139
00:20:28.650 --> 00:20:34.959
Suren Poghosyan: Later, you use some calculations to understand the offset.

140
00:20:37.180 --> 00:20:47.050
Suren Poghosyan: between the, first… between the two videos. Say, they are… one starts 20 seconds earlier, and the other starts…

141
00:20:47.380 --> 00:20:58.129
Suren Poghosyan: 20 seconds later, you want to understand that offset in order to later trim your video and consider them synchronized by the beginning of the videos.

142
00:20:59.050 --> 00:21:14.159
Suren Poghosyan: So, speaking about that, you proceed… you get a final variable, which is called offsetSeconds, which can be positive or negative, and based on that, if these are positive and negative, or negative.

143
00:21:14.400 --> 00:21:21.030
Suren Poghosyan: You decide if you want to trim the speaker video, or you want to trim the screen recording.

144
00:21:21.470 --> 00:21:24.490
Suren Poghosyan: And in this case, you could

145
00:21:24.790 --> 00:21:36.869
Suren Poghosyan: For the trimmable video, you create a new sequence, because you need to delete the first part of the video. For the video that you don't trim, that was, say.

146
00:21:37.120 --> 00:21:39.900
Suren Poghosyan: That,

147
00:21:40.130 --> 00:21:59.450
Suren Poghosyan: doesn't have the information that the first video had, and you want to remove the information from the first video in order to have them aligned, you don't do anything to that. Here, I create a new video to free encoding that into a new file with FFmpeg, but I…

148
00:21:59.450 --> 00:22:05.450
Suren Poghosyan: Renamed the other video, which wasn't necessary to re-encode.

149
00:22:05.540 --> 00:22:08.199
Suren Poghosyan: Into, say, Video 1 Synced.

150
00:22:08.650 --> 00:22:16.580
Suren Poghosyan: In this case, it means your video 1 is your speaker video, and video 2 is your screen recording video.

151
00:22:17.280 --> 00:22:25.119
Suren Poghosyan: So in this case, we learned that our screen recording started a bit earlier, and we need to

152
00:22:25.400 --> 00:22:28.069
Suren Poghosyan: Trim it at the beginning.

153
00:22:28.960 --> 00:22:35.750
Suren Poghosyan: And, just to rename the second, video for, using that in the,

154
00:22:36.000 --> 00:22:40.369
Suren Poghosyan: main workflow. Actually, I agree, this might be,

155
00:22:40.930 --> 00:22:55.150
Suren Poghosyan: Problematic, because you are working on the original sequence of the videos, you're renaming the original sequence, and it would be great, before doing that, to programmatically, copy your videos into,

156
00:22:55.640 --> 00:23:08.630
Suren Poghosyan: a new folder, or copy this in a new folder and work on that, so you have your original source of truth preserved. But, in my case, as I was trying to cut down the time that I was

157
00:23:09.070 --> 00:23:15.589
Suren Poghosyan: Spending on the video production, this didn't matter, that much, so…

158
00:23:15.790 --> 00:23:20.570
Suren Poghosyan: This can be done in the further iterations when it is being prepared to

159
00:23:21.230 --> 00:23:28.540
Suren Poghosyan: More wider use, say, for people that are not, able to…

160
00:23:29.400 --> 00:23:33.019
Suren Poghosyan: Work on the developer environments, and that they need just to

161
00:23:34.410 --> 00:23:36.660
Suren Poghosyan: have a UI and apply that.

162
00:23:37.260 --> 00:23:41.029
Suren Poghosyan: Through some… Buttons and inputs.

163
00:23:41.160 --> 00:23:43.760
Suren Poghosyan: That… something that is easier to use.

164
00:23:44.670 --> 00:23:53.550
Suren Poghosyan: So… Actually, we… I think we can resolve the issue regarding the,

165
00:23:54.370 --> 00:24:01.650
Suren Poghosyan: the screen sharing through this way. If I tried to do it less, yes, it's wonderful, it works this way.

166
00:24:01.910 --> 00:24:08.369
Suren Poghosyan: And I think at the end of the script, I will add, some code that…

167
00:24:09.610 --> 00:24:13.019
Suren Poghosyan: We'll show which files we had, and…

168
00:24:13.390 --> 00:24:20.010
Suren Poghosyan: later which files appeared there. So I'll try to do a CD into Clark's session.

169
00:24:22.180 --> 00:24:29.079
Suren Poghosyan: parks… Clark is our imaginary character, which had a…

170
00:24:29.700 --> 00:24:38.489
Suren Poghosyan: session, in order not to use some names and titles and videos, which may be,

171
00:24:38.760 --> 00:24:45.689
Suren Poghosyan: Protected with copyright, or maybe some people won't want to have their information shared here.

172
00:24:46.770 --> 00:24:55.799
Suren Poghosyan: So we are in the Clark Session folder, then we apply LS. Alright, that doesn't change the stuff. I guess we will have to just…

173
00:24:55.910 --> 00:24:59.180
Suren Poghosyan: I'll show you that in the folder itself.

174
00:25:01.730 --> 00:25:12.810
Suren Poghosyan: Alright, we'll do that a bit later after applying all the steps. So, we assume that we have only input 1 and input 2. These are the.

175
00:25:12.810 --> 00:25:32.270
Gabor Szabo: Sorry, sorry to interrupt you. Is there some error handling here? I mean, each stage uses… the question here, I'll read it out, that's the easiest. Each stage here assumes the FFmpeg OS commands succeed. Is there a way to check for that and add some error handling?

176
00:25:33.600 --> 00:25:48.650
Suren Poghosyan: Well, actually, here, when you're executing the subprocess command, it just trims the output, and I'm not aware if it's possible to receive feedback from the subprocess command.

177
00:25:48.880 --> 00:25:58.249
Suren Poghosyan: Back to your, notebook, but that's a good matter to think about, and,

178
00:25:59.270 --> 00:26:19.460
Suren Poghosyan: I think it's a problem in the scopes of Jupyter, or even if you are not in the scopes of Jupyter, that will be a problem as well. If you are a package and calling to FFmpeg, you will need some feedback. In this case, I just take care of that by monitoring it visually. I mean, if I see that,

179
00:26:19.460 --> 00:26:24.570
Suren Poghosyan: There was an error in the output, say it says no such file or directory.

180
00:26:24.570 --> 00:26:28.900
Suren Poghosyan: then it had some problems. But programmatically, I'm not doing that.

181
00:26:29.670 --> 00:26:35.770
Suren Poghosyan: I'm not aware if it's possible to do with the subprocess. I will,

182
00:26:36.510 --> 00:26:43.179
Suren Poghosyan: address that matter, after our presentation, and I think I will prepare a document with the answers.

183
00:26:43.460 --> 00:26:45.040
Suren Poghosyan: And I will provide you that.

184
00:26:46.060 --> 00:26:47.700
Suren Poghosyan: Thanks for the question.

185
00:26:48.530 --> 00:26:53.870
Suren Poghosyan: so at this point, let's, assume that we have…

186
00:26:53.870 --> 00:27:08.129
Gabor Szabo: Sorry, sorry, wait a second. I just looked at the documentation of the subprocess.run, and it says, as I understand, that it raises an exception if the process is failing.

187
00:27:08.570 --> 00:27:11.619
Suren Poghosyan: Does it give you a code or a reason with the.

188
00:27:11.620 --> 00:27:15.940
Gabor Szabo: I thought that… I thought that it will return the exit code, but

189
00:27:16.080 --> 00:27:35.230
Gabor Szabo: the 3 seconds that I spent on reading the documentation, I think it says it raises an exception. But it should, or some… I know that some version of the subprocess package returns, or allows you to access the exit code from the external program that it runs.

190
00:27:40.050 --> 00:27:42.289
Suren Poghosyan: Yeah, it will be logical, I guess.

191
00:27:42.940 --> 00:27:46.770
Suren Poghosyan: From the point of the creators of sub-processing maintainers.

192
00:27:46.770 --> 00:27:52.579
Gabor Szabo: Oh, there's a parameter called check in order to make it an exception or not, I think.

193
00:27:53.360 --> 00:27:54.460
Suren Poghosyan: Understood.

194
00:27:55.510 --> 00:28:00.810
Suren Poghosyan: I mean, if it throws an exception, then you are in a good position and you can handle that.

195
00:28:00.950 --> 00:28:03.870
Suren Poghosyan: At least understand that it wasn't successful.

196
00:28:03.870 --> 00:28:14.800
Gabor Szabo: Yeah, there should be… so there is, in some places, there is something called return code. That's how it's called, what, what, in Linux,

197
00:28:14.800 --> 00:28:21.330
Suren Poghosyan: I mean, we can even try that, you know? We can write a try-catch block here.

198
00:28:22.530 --> 00:28:25.670
Suren Poghosyan: try… Yeah, exception.

199
00:28:31.990 --> 00:28:34.219
Suren Poghosyan: Yes, we can do that.

200
00:28:34.220 --> 00:28:40.479
Gabor Szabo: to run LS on a non-existing folder, and that would…

201
00:28:41.060 --> 00:28:42.970
Suren Poghosyan: That's what I want to do.

202
00:28:43.850 --> 00:28:51.230
Suren Poghosyan: So we'll run this without running the first one, then we must have some, problems regarding that.

203
00:28:51.510 --> 00:28:56.140
Suren Poghosyan: Except… Perfect.

204
00:28:57.110 --> 00:28:58.070
Suren Poghosyan: Print.

205
00:28:59.510 --> 00:29:00.330
Suren Poghosyan: Oops.

206
00:29:05.480 --> 00:29:10.899
Suren Poghosyan: M… What does it say?

207
00:29:12.250 --> 00:29:14.320
Suren Poghosyan: And do we have an input?

208
00:29:16.550 --> 00:29:18.430
Suren Poghosyan: We have an output.

209
00:29:19.300 --> 00:29:25.249
Suren Poghosyan: Hmm… Maybe, yeah, there are variables.

210
00:29:25.460 --> 00:29:32.760
Suren Poghosyan: But I have to… exist then there. Let's do it this way. Let's say we have input 11.

211
00:29:33.470 --> 00:29:42.210
Suren Poghosyan: And in this case, yeah, it says no such file or directory, but it doesn't throw anything. See, it's just an output without…

212
00:29:42.470 --> 00:29:48.299
Suren Poghosyan: the, without this print, so we don't have… oops.

213
00:29:48.790 --> 00:29:52.539
Suren Poghosyan: Which means it doesn't throw any exceptions.

214
00:29:52.540 --> 00:29:56.419
Gabor Szabo: Set the… set the parameter called CHECK into true.

215
00:29:58.500 --> 00:30:02.160
Gabor Szabo: For the stop process run, another parameter called check.

216
00:30:02.850 --> 00:30:04.810
Gabor Szabo: And set it to true.

217
00:30:05.760 --> 00:30:08.150
Suren Poghosyan: Alright, as a variable…

218
00:30:08.770 --> 00:30:13.020
Gabor Szabo: That's a parameter, yeah. It's just… So it's just Czech.

219
00:30:13.630 --> 00:30:15.549
Gabor Szabo: Without the cud.

220
00:30:16.610 --> 00:30:17.440
Gabor Szabo: Yeah.

221
00:30:17.870 --> 00:30:20.680
Suren Poghosyan: Oh yeah, you have the oops, then the output.

222
00:30:21.020 --> 00:30:22.700
Suren Poghosyan: Of the error.

223
00:30:23.780 --> 00:30:32.280
Suren Poghosyan: Then, yes, there's a method for addressing the, errors coming from the commands.

224
00:30:33.950 --> 00:30:40.390
Suren Poghosyan: Well, let's proceed to executing the rest of the… Commands…

225
00:30:43.070 --> 00:30:47.870
Suren Poghosyan: And proceeding to the main script, where we have all the interesting stuff.

226
00:30:48.200 --> 00:30:58.319
Suren Poghosyan: I mean, honestly, this was the, the coolest part that I wanted to take… I wanted to take over, the synchronization part.

227
00:30:58.700 --> 00:31:03.069
Suren Poghosyan: And there's some linear algebra applied, which I'm happy about.

228
00:31:04.610 --> 00:31:05.420
Suren Poghosyan: Yeah.

229
00:31:05.890 --> 00:31:12.380
Suren Poghosyan: And then let's… Execute that… oh, we have an issue, I didn't fix this.

230
00:31:15.000 --> 00:31:18.709
Suren Poghosyan: Yes, so now we have the, both

231
00:31:18.910 --> 00:31:29.700
Suren Poghosyan: audios extracted from the videos, and then we convert them to, WAF format in order to, avoid,

232
00:31:31.410 --> 00:31:34.340
Suren Poghosyan: this being converted with Liprosa.

233
00:31:34.510 --> 00:31:40.829
Suren Poghosyan: Because we don't know how it works under the hood, and we don't want to face the issues.

234
00:31:41.140 --> 00:31:44.189
Suren Poghosyan: that come from the Librosa itself.

235
00:31:44.650 --> 00:31:46.509
Suren Poghosyan: That's why we do it beforehand.

236
00:31:47.620 --> 00:32:00.619
Suren Poghosyan: And we immediately see that there's a 5-second difference between these, videos. And in this case, if it's negative, we have to trim the…

237
00:32:01.210 --> 00:32:04.970
Suren Poghosyan: The second video, which is the presentation.

238
00:32:05.850 --> 00:32:13.409
Suren Poghosyan: We trim that, then we get two videos called. One is called Video 1 Synced, and the other Video 2 Synced.

239
00:32:13.610 --> 00:32:19.120
Suren Poghosyan: Video 1 is the speaker video, video 2 is the, screen recording.

240
00:32:19.730 --> 00:32:28.060
Suren Poghosyan: And… As we already have these videos, we can proceed to assembling them into one video.

241
00:32:28.870 --> 00:32:35.390
Suren Poghosyan: In the main script, well, first we have to run the dependencies. Here we have

242
00:32:35.490 --> 00:32:50.949
Suren Poghosyan: a faster whisper for transcribing your audios into text, and later that… feeding that into Gemini API and deciding where the video starts. I mean, sometimes there's an introduction where

243
00:32:51.250 --> 00:32:54.519
Suren Poghosyan: Some administrative information is being,

244
00:32:55.730 --> 00:33:02.459
Suren Poghosyan: Told to the audience, and you don't want it to be in the video. And that layer makes the decision.

245
00:33:02.620 --> 00:33:10.799
Suren Poghosyan: And… We have some basic packages for the environment, and… Working with the audio.

246
00:33:11.500 --> 00:33:19.130
Suren Poghosyan: Yes, hopefully all these requirements are already satisfied, and I have prepared some kind of,

247
00:33:19.560 --> 00:33:30.130
Suren Poghosyan: slides in my Jupyter notebook in order to have the stuff summarized. For that, I use Pillow, and I use… and I load some images.

248
00:33:30.330 --> 00:33:41.329
Suren Poghosyan: So here is the tool, that we were talking about. It is called ScenePie, and these are all the videos that were already edited. We did, more than 35.

249
00:33:41.440 --> 00:33:47.329
Suren Poghosyan: Videos, including the opening, closing, and other stuff, published.

250
00:33:47.760 --> 00:33:49.379
Suren Poghosyan: After the conference.

251
00:33:50.400 --> 00:33:57.890
Suren Poghosyan: And this helps you to, not use the, Adobe layers or any other layers.

252
00:33:58.040 --> 00:34:16.000
Suren Poghosyan: that we are used to in the video production, because when you create a layer, you want it to be a template, you want to apply it to the other videos as well, but there's problem with that in the Adobe or other software, because

253
00:34:16.360 --> 00:34:20.070
Suren Poghosyan: When you apply template.

254
00:34:20.280 --> 00:34:26.950
Suren Poghosyan: Or when you adjusted it to a specific video, say you synced a video and a screen recording.

255
00:34:27.050 --> 00:34:37.589
Suren Poghosyan: And these are in that template, and you, need… and you do the second session, you get different videos with different offsets.

256
00:34:37.850 --> 00:34:41.000
Suren Poghosyan: And you want to apply it to the same template.

257
00:34:41.179 --> 00:34:52.960
Suren Poghosyan: You can't do that because you have to reapply the synchronization effects to that video. That means you have to go to your editor, apply manually that effects again.

258
00:34:53.730 --> 00:35:01.700
Suren Poghosyan: And… like, adjust the timeline to your new videos. That doesn't work, and…

259
00:35:02.040 --> 00:35:03.970
Suren Poghosyan: You don't want to do it.

260
00:35:05.160 --> 00:35:07.689
Suren Poghosyan: Actually, I had an idea,

261
00:35:07.880 --> 00:35:24.609
Suren Poghosyan: as you already know, there is this Adobe project file, which includes… it looks like a lot to XML format. If you open it with a text editor, it shows how it is structured, there are paths, there are layer names.

262
00:35:24.930 --> 00:35:35.749
Suren Poghosyan: And, some of that part you could automate. I mean, if you replace the path name to your new video, then you will have it applied to your

263
00:35:35.940 --> 00:35:54.449
Suren Poghosyan: to your template, and you can do that programmatically, I mean, create 35 different project files, and just go and export these files. But again, you don't have the sequence of actions applied to your videos in that template, it just

264
00:35:54.660 --> 00:36:01.769
Suren Poghosyan: It's just the dump structure of, of your, timeline. I mean, we're,

265
00:36:02.060 --> 00:36:11.419
Suren Poghosyan: the location of videos, the location of text, logos, and so on. It's for the layout, not for the pipeline, not for the actions.

266
00:36:12.200 --> 00:36:29.939
Suren Poghosyan: Moving forward, there's some, environment configurations. You don't want your keys directly used in the notebook, just for security reasons, and just to have this, and just to be able to, safely push that to GitHub.

267
00:36:30.430 --> 00:36:36.380
Suren Poghosyan: And here are the steps of the, of the main pipeline.

268
00:36:36.510 --> 00:36:42.589
Suren Poghosyan: Again, you are extracting the audio from already synced videos, because you assume that

269
00:36:42.730 --> 00:36:49.399
Suren Poghosyan: You want to have your speaker in a video always. I mean, if you have,

270
00:36:49.560 --> 00:37:13.370
Suren Poghosyan: more longer presentation than the speaker video. You don't have just presentation running without the speaker in the corner. So you extract that audio from the speaker video. And later, you do the transcription, you feed that into the model, you get the seconds where your video starts, you trim that video.

271
00:37:13.620 --> 00:37:18.699
Suren Poghosyan: And you proceed to… The final rendering.

272
00:37:19.730 --> 00:37:27.589
Suren Poghosyan: Below, you can see these configurations, which, are for handling…

273
00:37:28.390 --> 00:37:48.220
Suren Poghosyan: your workflow in an easier way. I mean, this lets you to pull some levers and change the modifications. These are the steps that I described previously. There are steps, for example, if you set the do transcript to false.

274
00:37:48.250 --> 00:37:49.260
Suren Poghosyan: Then…

275
00:37:49.560 --> 00:38:01.700
Suren Poghosyan: you may want to load the file which had the transcript in it, which you saved in here, and you need that in order to feed that to the LLM.

276
00:38:01.950 --> 00:38:04.679
Suren Poghosyan: If you don't want to do that, you just…

277
00:38:04.800 --> 00:38:13.110
Suren Poghosyan: set everything to false, and you skip the transcriptions and the AI part.

278
00:38:13.360 --> 00:38:20.930
Suren Poghosyan: Which can, which may take you a lot of time. I mean, this is an automation, but…

279
00:38:21.030 --> 00:38:25.170
Suren Poghosyan: this itself Can take you…

280
00:38:25.360 --> 00:38:37.509
Suren Poghosyan: more time than just looking at the video and fixing the seconds that the video starts at and ends at. It's much easier to do yourself than to do that,

281
00:38:39.430 --> 00:38:46.280
Suren Poghosyan: this automation. It's just for switching off your brain, running the script, and having the video at the end.

282
00:38:46.700 --> 00:39:05.439
Suren Poghosyan: Here you can specify the model. Sometimes, Gemini 3.57 Flash has, downtime. I mean, there are a lot of requests to it, and API says, oops, we can't provide you some computation power, because we are having troubles serving all these requests, and you are

283
00:39:05.910 --> 00:39:07.479
Suren Poghosyan: Yeah, at the end of the lease.

284
00:39:07.980 --> 00:39:27.100
Suren Poghosyan: And there are a few different steps. The trimming that you cut the beginning and the end of the video, the preview of the frame, this is needed to understand if your layout looks fine or not. If your layout is not fine, and you exported a 50-minute video, you just lost your time.

285
00:39:27.390 --> 00:39:34.140
Suren Poghosyan: And if you see that the frame preview is fine, you want to understand if the

286
00:39:34.640 --> 00:39:45.250
Suren Poghosyan: the sec… the video settings were fine as well. Say, the audio frequency, the audio in general, if there's an audio or not, or there's a problem with that.

287
00:39:45.250 --> 00:39:55.309
Suren Poghosyan: You do a short export of, like, 30 seconds, or as long as you want it to be, and only then you proceed to,

288
00:39:55.400 --> 00:40:04.679
Suren Poghosyan: building your layout. It's the layout without the intro. It's, it's, it's the main body.

289
00:40:04.970 --> 00:40:18.090
Suren Poghosyan: where everything is being explained is the part of the session. And then, when your do export is, enabled, all this stuff is being concatenated, and…

290
00:40:18.990 --> 00:40:21.190
Suren Poghosyan: Provided as final output.

291
00:40:22.160 --> 00:40:24.049
Suren Poghosyan: So here again,

292
00:40:24.290 --> 00:40:38.480
Suren Poghosyan: we define some paths which can be modified and adjusted to your folder, wherever it is located. It can be located on an external volume, like I did for our production. It was on an external SSD.

293
00:40:39.050 --> 00:40:43.230
Suren Poghosyan: And let's run these steps. So actually, we…

294
00:40:43.460 --> 00:40:48.420
Suren Poghosyan: Don't want to do transcript, because it takes long, we don't want to…

295
00:40:48.750 --> 00:40:55.789
Suren Poghosyan: Or, I mean, let's do that, because we have a short video, and it's fine to do that. If we had a 15-minute video, it won't…

296
00:40:55.920 --> 00:41:02.160
Suren Poghosyan: Be the wisest decision to, run through all these steps.

297
00:41:03.140 --> 00:41:10.060
Suren Poghosyan: Actually, it looks fine for me, we have all the inference steps, and we move forward, defining the,

298
00:41:10.570 --> 00:41:16.159
Suren Poghosyan: pads… Actually, this can be replaced here, because it's redundant to call

299
00:41:16.890 --> 00:41:21.579
Suren Poghosyan: this command twice, we can't… we have already… We have this already.

300
00:41:21.930 --> 00:41:23.879
Suren Poghosyan: And we can execute that.

301
00:41:24.560 --> 00:41:39.250
Suren Poghosyan: And there's the step when we extract the audio, only the audio itself without the video, and there are the descriptions of its speed rate, of its…

302
00:41:39.630 --> 00:41:43.230
Suren Poghosyan: Format and the method of extracting the audio.

303
00:41:44.350 --> 00:41:59.789
Suren Poghosyan: And we do that in order to later feed that audio file into OpenAI's Fast Whisper model, which transcribes our video, and which later will pass to the API.

304
00:42:00.560 --> 00:42:05.860
Suren Poghosyan: So, this is a pretty quick step compared to video encoding.

305
00:42:06.210 --> 00:42:11.830
Suren Poghosyan: And, there's the description of the, how the,

306
00:42:13.210 --> 00:42:21.380
Suren Poghosyan: transcription works. Actually, if you want to understand where the video starts and where it ends, you don't need to,

307
00:42:22.370 --> 00:42:26.770
Suren Poghosyan: Get the transcription of the… of all the audio.

308
00:42:26.890 --> 00:42:34.479
Suren Poghosyan: You just need to get the first and last few minutes. In this case, we have a 2-minute video, but there…

309
00:42:34.870 --> 00:42:36.980
Suren Poghosyan: This method, is…

310
00:42:37.130 --> 00:42:47.600
Suren Poghosyan: Will be problematic on this sequence of the video, because it looks for the first and last 10 minutes, and if your video is short, they overlap.

311
00:42:48.050 --> 00:42:53.499
Suren Poghosyan: It just feeds that only sequence into the, into this.

312
00:42:54.020 --> 00:42:54.970
Suren Poghosyan: method.

313
00:42:56.440 --> 00:43:15.440
Suren Poghosyan: In this step, we will wait for a few moments until the model is… the small English-only model, transcribes the audio using only INT8MAT, because it's easier to handle rather than

314
00:43:15.500 --> 00:43:20.559
Suren Poghosyan: Float 16 or float 32, which is the full quality.

315
00:43:21.330 --> 00:43:26.249
Suren Poghosyan: Which may take a lot of resources to do on our machine.

316
00:43:26.810 --> 00:43:30.940
Suren Poghosyan: In our case, as I mentioned, we have the,

317
00:43:31.690 --> 00:43:39.040
Suren Poghosyan: Max Silicon M1 Pro, which is fast enough, compared to, say.

318
00:43:40.270 --> 00:43:49.930
Suren Poghosyan: the same Raspberry or other small devices, which take forever to do this encoding and transcribe… transcription and so on.

319
00:43:50.640 --> 00:43:58.870
Suren Poghosyan: Actually, this video is one of the most popular videos on the PyData YouTube channel, which is very old.

320
00:43:59.350 --> 00:44:09.540
Suren Poghosyan: and still popular enough, it is Wes McKinney's, introduction to Pandas in 10 minutes, and this is some part of it.

321
00:44:10.260 --> 00:44:19.979
Suren Poghosyan: This video, this audio sequence, we assume is the speaker audio, which has a good quality, which comes from the microphone.

322
00:44:20.200 --> 00:44:33.909
Suren Poghosyan: If you record the audio from the screen recording, and if you take the audio of the screen recording, you are… you're standing far from the computer, and your audio is far… has…

323
00:44:34.040 --> 00:44:47.820
Suren Poghosyan: lower volume, and may have far worse quality. But these are synchronizable and usable later. So we use the speaker video in order to have a good quality for the transcription.

324
00:44:48.290 --> 00:44:57.610
Suren Poghosyan: And we have, say, the start of this sentence and the end of this sentence, which sometimes may cause you problems because

325
00:44:59.860 --> 00:45:11.500
Suren Poghosyan: It might not be the exact beginning, and your words might be cut. Instead of going, it may say the last part of the word, and you might need to adjust it, but

326
00:45:11.960 --> 00:45:14.549
Suren Poghosyan: Most of the time, it works fine.

327
00:45:15.510 --> 00:45:17.280
Suren Poghosyan: If one could

328
00:45:17.470 --> 00:45:27.639
Suren Poghosyan: find a method that described the exact timeline of each word said in this transcription, it would provide a far better,

329
00:45:30.020 --> 00:45:31.999
Suren Poghosyan: Far better trimming.

330
00:45:32.180 --> 00:45:34.939
Suren Poghosyan: Of the video from the beginning.

331
00:45:36.360 --> 00:45:50.619
Suren Poghosyan: So, now we have the transcription. These are the other options of the models that you could use for the transcription. As you may see, we used the small English one, which performed well.

332
00:45:50.760 --> 00:46:08.589
Suren Poghosyan: executed in a fair amount of time, based on the experiments that I made. The small ones were making a lot of mistakes. I mean, some invalid translations, or if you take non-English specified one, it may

333
00:46:09.760 --> 00:46:14.720
Suren Poghosyan: assume that the speaker is talking in Chinese, which is not the case.

334
00:46:14.830 --> 00:46:22.090
Suren Poghosyan: So we just use the English specified, knowing that our speaker exactly speaks, in English.

335
00:46:23.110 --> 00:46:31.530
Suren Poghosyan: And there are the computation types. If you want a better quality, you may use the float 32, And…

336
00:46:32.180 --> 00:46:38.540
Suren Poghosyan: spend more time, but get a better quality of transcription, I assume.

337
00:46:39.530 --> 00:46:46.519
Suren Poghosyan: Later, we save that transcription to a file in order to have this information preserved.

338
00:46:46.700 --> 00:46:57.089
Suren Poghosyan: And not repeat the transcription, in case if you change the configurations on the very top of the, pipeline.

339
00:46:57.360 --> 00:46:58.689
Suren Poghosyan: I mean…

340
00:47:00.040 --> 00:47:09.470
Suren Poghosyan: these configurations. You may need to change this, you may need to re-export, change the layout, and you don't want to do this,

341
00:47:09.830 --> 00:47:12.600
Suren Poghosyan: Power-consuming steps in between.

342
00:47:13.060 --> 00:47:22.800
Suren Poghosyan: And later, when we are, trying to fit this into Gemini API, there are a lot of instructions to the model to.

343
00:47:23.310 --> 00:47:30.540
Suren Poghosyan: Pay attention, where the video starts, where, let's say this,

344
00:47:31.020 --> 00:47:39.580
Suren Poghosyan: Keywords are said that, they… it has to ignore, and it has to detect the,

345
00:47:39.770 --> 00:47:48.169
Suren Poghosyan: The part where the speaker starts, their presentation, and find the, it's find deep.

346
00:47:49.490 --> 00:47:52.809
Suren Poghosyan: Timeline, and fix that as the beginning of the video.

347
00:47:54.250 --> 00:48:04.929
Suren Poghosyan: And also, there are some, confidence intervals, which indicate how confident the model was,

348
00:48:05.210 --> 00:48:16.420
Suren Poghosyan: That it is the exact beginning, and if it's not confident enough and can't, detect where the speech starts, there are some default cases that,

349
00:48:16.720 --> 00:48:19.129
Suren Poghosyan: Are programmed in order to

350
00:48:19.980 --> 00:48:23.599
Suren Poghosyan: In order to have the video exported anyway.

351
00:48:24.890 --> 00:48:29.459
Suren Poghosyan: So, we proceed and make a call to Gemini API, I hope.

352
00:48:29.770 --> 00:48:38.469
Suren Poghosyan: The 3.1 flashlight is fine, and yes, we receive a JSON according to our requirements.

353
00:48:38.700 --> 00:48:41.330
Suren Poghosyan: That were in this part.

354
00:48:42.350 --> 00:48:47.009
Suren Poghosyan: So, it… it describes the reason why it chose

355
00:48:47.320 --> 00:49:05.010
Suren Poghosyan: this start cut, and the end cut, and what the speaker is talking about, which helps for the internal reasoning. So, as we can see, our video is a 2-minute video, and it was cut out from the middle of the actual video.

356
00:49:05.010 --> 00:49:12.569
Suren Poghosyan: So there's no, defined beginning, and there's no defined ending, so it decided to just

357
00:49:13.240 --> 00:49:21.089
Suren Poghosyan: cut to just include the whole video itself. And if you can't see in the transcription, it says.

358
00:49:21.210 --> 00:49:38.219
Suren Poghosyan: The transcript begins in the middle of the sentence, of a sentence, but the content is clearly part of the technical lecture. There is no host introduction or preceding noise, the speaker is already delivering content, so there is no

359
00:49:38.590 --> 00:49:44.440
Suren Poghosyan: Point for trimming that content further, into its roots.

360
00:49:44.750 --> 00:49:48.240
Suren Poghosyan: It is already… it is already missing the introduction.

361
00:49:49.160 --> 00:49:53.940
Suren Poghosyan: And, there are the packages used in the… in there.

362
00:49:54.450 --> 00:49:59.269
Suren Poghosyan: Here's the coal that is being made,

363
00:49:59.270 --> 00:50:15.129
Suren Poghosyan: to the API, and this is not a predefined JSON. This is… this was generated right away through an API call. After that, we also saved that output, because, again, we may need to rerun our script.

364
00:50:15.220 --> 00:50:18.060
Suren Poghosyan: In order to apply different settings.

365
00:50:19.040 --> 00:50:25.319
Suren Poghosyan: And, below, we are going to define the layout of the, of our video.

366
00:50:25.880 --> 00:50:27.639
Suren Poghosyan: We want to have the…

367
00:50:28.830 --> 00:50:41.359
Suren Poghosyan: presentation as a bigger part of the video, speaker video as a smaller part, and the logo below. Well, you actually may want to put your sponsors in the bottom, but…

368
00:50:41.560 --> 00:50:47.790
Suren Poghosyan: I mean, it's a question of… Preference.

369
00:50:48.880 --> 00:50:50.620
Suren Poghosyan: A situation that you are in.

370
00:50:51.160 --> 00:51:00.120
Suren Poghosyan: Again, there's this coordinate system that is being used. Again, we are defining the size of the canvas. It's full HD.

371
00:51:00.460 --> 00:51:08.139
Suren Poghosyan: 16 over 9, 1920, or… or 1080.

372
00:51:09.630 --> 00:51:16.380
Suren Poghosyan: And here are the, coordinates of the… here are the sizes of the, presentation.

373
00:51:17.050 --> 00:51:30.869
Suren Poghosyan: Because you have to define the size of the box, and also its positions. Again, it is being counted from the top left corner, and it goes down, and it goes to the right, according to your variables.

374
00:51:31.080 --> 00:51:37.090
Suren Poghosyan: Same for the camera, and same for the logo, and there's some centering logic.

375
00:51:38.690 --> 00:51:41.299
Suren Poghosyan: That we're trying to understand the…

376
00:51:41.990 --> 00:51:48.889
Suren Poghosyan: The remaining distance, if we compare the logo and video widths.

377
00:51:49.030 --> 00:51:53.860
Suren Poghosyan: In order to have the logo under the video, but centered.

378
00:51:54.280 --> 00:52:08.010
Suren Poghosyan: So, this centers the logo, and this adds some offset from the left. Maybe you want it to be a bit right, because visually it is not centered, but practically the file is centered.

379
00:52:08.620 --> 00:52:12.440
Suren Poghosyan: These are some… Things to take care of.

380
00:52:12.700 --> 00:52:22.629
Suren Poghosyan: And here's the example that I was talking about. As you can see, there's… there relatively can be 19 pixels from the lid, and 109

381
00:52:22.930 --> 00:52:27.159
Suren Poghosyan: 109 from the top, and this is the presentation.

382
00:52:27.530 --> 00:52:30.410
Suren Poghosyan: And this is the speaker video,

383
00:52:30.870 --> 00:52:43.870
Suren Poghosyan: And the chapter logo, and it actually is centered with the speaker video, and there's 10 pixels added from the left, because it seems to me it is not aligned enough.

384
00:52:44.630 --> 00:52:49.330
Suren Poghosyan: Maybe I'm just going crazy about that, but… That's how it felt.

385
00:52:50.560 --> 00:53:02.460
Suren Poghosyan: So, we process… we proceed to, the step where we try to understand the,

386
00:53:03.450 --> 00:53:05.449
Suren Poghosyan: the trimming configurations.

387
00:53:06.410 --> 00:53:11.449
Suren Poghosyan: We take the, confidence intervals, we understand the…

388
00:53:11.580 --> 00:53:26.549
Suren Poghosyan: if we need to trim or not, based on the LLM output, it is this whole part that is dedicated to that. That whole workflow was to, have these two variables, trim start and trimEnd.

389
00:53:27.030 --> 00:53:44.960
Suren Poghosyan: And if you don't want to spend time on this LLM execution and transcription, you just comment out this part, you look out in the video, you see that the video starts at the third second, you say, oh, alright, it is the third second, and your video was

390
00:53:45.440 --> 00:53:58.500
Suren Poghosyan: say, almost 10 minutes long, and you write 600, and that is the end of the video. So you want your video to be cut from the third second to the

391
00:53:59.300 --> 00:54:02.639
Suren Poghosyan: Up… all the way to the end of the video.

392
00:54:03.470 --> 00:54:08.779
Suren Poghosyan: And you just specify these two variables. If you don't want that, you uncomment this and…

393
00:54:09.340 --> 00:54:12.469
Suren Poghosyan: You go with the confidence intervals and so on.

394
00:54:12.730 --> 00:54:20.479
Suren Poghosyan: If you don't want to trim at all, you just use this package in order to detect the length of your audio clip.

395
00:54:20.670 --> 00:54:24.899
Suren Poghosyan: Take the zero as the stock, and then

396
00:54:26.920 --> 00:54:41.410
Suren Poghosyan: detect the length of the audio, and as it is in milliseconds, you multiply it with 1000 in order to get seconds. And you determine the trim duration in order to feed that into the FFmpeg command.

397
00:54:42.400 --> 00:54:44.030
Suren Poghosyan: In order to understand.

398
00:54:44.690 --> 00:54:47.959
Suren Poghosyan: The final length of the final sequence.

399
00:54:48.910 --> 00:54:56.700
Suren Poghosyan: So that's it, we have… we indeed have the trim configurations, it will go into the… into this part, and…

400
00:54:56.860 --> 00:55:06.589
Suren Poghosyan: print out. I would like to also, print out this stream start and… Treatment for you to see.

401
00:55:06.800 --> 00:55:10.630
Suren Poghosyan: That it is from 0 to 124th seconds.

402
00:55:11.010 --> 00:55:16.429
Suren Poghosyan: And, as you can see, yes, it says 0 and 124, it is…

403
00:55:16.720 --> 00:55:18.969
Suren Poghosyan: Up to the end of the video.

404
00:55:19.470 --> 00:55:24.279
Suren Poghosyan: And it just prints out the reasons given from the API.

405
00:55:24.610 --> 00:55:25.580
Suren Poghosyan: output.

406
00:55:26.510 --> 00:55:33.020
Suren Poghosyan: At this point, everything begins, the hell begins, the encoding, and…

407
00:55:33.240 --> 00:55:37.780
Suren Poghosyan: All the stuff, and where your device is going to suffer, and…

408
00:55:37.910 --> 00:55:45.750
Suren Poghosyan: raise the temperatures up to, like, 100 degrees of Celsius, and you… Fans will be revving.

409
00:55:46.720 --> 00:55:51.540
Suren Poghosyan: At this point, we… Are going to define

410
00:55:53.300 --> 00:55:58.560
Suren Poghosyan: the… a few things. First of all, we want to define

411
00:55:59.430 --> 00:56:13.250
Suren Poghosyan: we want to convert those images into video sequences, because if you put an image in the Adobe, it detects that it's an image, and under the hood, it converts to a video. Say, by default.

412
00:56:13.250 --> 00:56:20.139
Suren Poghosyan: it converts into a 5-second video. But in this case, you have to, loop it

413
00:56:21.040 --> 00:56:25.840
Suren Poghosyan: Like, with the duration you want, say it's 5 seconds.

414
00:56:26.270 --> 00:56:35.299
Suren Poghosyan: And you want it to be a 5-second video with no audio. So, here where you… here is where you loop your video.

415
00:56:36.370 --> 00:56:45.610
Suren Poghosyan: at this point, this is… you're looping the logo. You're creating the, 5-second, sequence…

416
00:56:47.950 --> 00:56:56.690
Suren Poghosyan: Through flopping the logo, and again, there are some input as well, this might be the…

417
00:56:57.060 --> 00:57:00.989
Suren Poghosyan: the one that is already exporting the video. So…

418
00:57:01.520 --> 00:57:10.579
Suren Poghosyan: Above that, you gain… is… you're defining the layout by specifying the width and height, and…

419
00:57:11.370 --> 00:57:20.820
Suren Poghosyan: All the stuff that you have, and yes, there's a duration, which is… if you set it to a second, if you set it to 1,

420
00:57:21.320 --> 00:57:39.679
Suren Poghosyan: It will export a single frame, if you will set it to a different sequence, it will export the test layout of the video that you want to see, if the introduction is fine, if the video is fine, and if the layout is fine.

421
00:57:40.650 --> 00:57:44.759
Suren Poghosyan: and, proceed to the full export.

422
00:57:45.510 --> 00:57:59.549
Suren Poghosyan: Let's execute these commands in order to have them defined. These are the preview steps, and you can specify a timestamp at which point you want your preview to be exported from.

423
00:58:00.680 --> 00:58:05.159
Suren Poghosyan: In here we have 1.5 seconds in.

424
00:58:05.580 --> 00:58:14.259
Suren Poghosyan: In order to see, say, The layout, or the intro of the composite.

425
00:58:16.100 --> 00:58:18.909
Suren Poghosyan: We are executing that,

426
00:58:20.540 --> 00:58:27.169
Suren Poghosyan: further, there's a meme that I may show you at the end.

427
00:58:27.540 --> 00:58:34.010
Suren Poghosyan: It's quite a feeling about some configurations that you have to specify in order to

428
00:58:34.330 --> 00:58:39.319
Suren Poghosyan: have it running on Mac, and with all the encodings that

429
00:58:39.730 --> 00:58:44.809
Suren Poghosyan: that may work or may not work with QuickTime. The…

430
00:58:46.010 --> 00:58:50.059
Suren Poghosyan: built-in player for the videos on the Mac.

431
00:58:52.930 --> 00:58:56.330
Suren Poghosyan: Yes, we have the test output.

432
00:58:56.820 --> 00:59:01.900
Suren Poghosyan: At this point, as you… Let me see…

433
00:59:02.270 --> 00:59:07.120
Suren Poghosyan: We have build layout test, and here we are executing it.

434
00:59:07.310 --> 00:59:09.169
Suren Poghosyan: And it exports.

435
00:59:09.320 --> 00:59:17.469
Suren Poghosyan: by the default duration of 10 seconds. If you want a different duration, you… or different configurations.

436
00:59:17.660 --> 00:59:29.069
Suren Poghosyan: Regarding if you want it to be… to be done quickly, you may specify these two arguments for the method, for the function, and…

437
00:59:30.340 --> 00:59:32.050
Suren Poghosyan: have it differently.

438
00:59:32.460 --> 00:59:41.300
Suren Poghosyan: Currently, we have 10 seconds of that. Here, we define the final outputs of the videos, and the duration of the banners.

439
00:59:41.480 --> 00:59:47.270
Suren Poghosyan: Where… well, there is a duration for the intro banner, but we are not using it, so we can ignore that.

440
00:59:47.480 --> 00:59:50.779
Suren Poghosyan: What matters is this… just this banner duration.

441
00:59:52.040 --> 00:59:59.529
Suren Poghosyan: We have already executed that, and at this point, we are defining the frame rate, which is very important.

442
01:00:00.330 --> 01:00:11.440
Suren Poghosyan: and also the audio frequency. Frame rate and audio frequency are important, because if These are not orchestrated.

443
01:00:12.060 --> 01:00:14.729
Suren Poghosyan: You may have problems with the synchronization.

444
01:00:14.890 --> 01:00:21.069
Suren Poghosyan: If originally these were, say, 25 frames per second, say your,

445
01:00:21.410 --> 01:00:27.020
Suren Poghosyan: Intro is 25 frames per second, and your video is 30 frames per second.

446
01:00:27.310 --> 01:00:32.019
Suren Poghosyan: And you normalize their audio, for,

447
01:00:32.300 --> 01:00:45.890
Suren Poghosyan: you normalize the audio for all the sequences to the same number, you may have mismatch for the video and audio. For example, I had 44,000

448
01:00:46.060 --> 01:00:47.530
Suren Poghosyan: Hertz.

449
01:00:48.420 --> 01:00:53.030
Suren Poghosyan: For, one sequence, and 48 for another.

450
01:00:53.160 --> 01:00:59.290
Suren Poghosyan: And it felt like… And one of these sounded like a slow-mo.

451
01:00:59.850 --> 01:01:02.680
Suren Poghosyan: Because we had… we… we had…

452
01:01:02.940 --> 01:01:17.580
Suren Poghosyan: more frames per second than we had more audio information per second. So, that's why it was an issue, and that's why you have to define this for all the stuff, and normalize that, and make sure that…

453
01:01:17.970 --> 01:01:19.809
Suren Poghosyan: these are matching.

454
01:01:19.980 --> 01:01:27.540
Suren Poghosyan: Because the initial synchronization We'll go down the drain, if not done appropriately.

455
01:01:28.600 --> 01:01:36.060
Suren Poghosyan: And, this is the final step for exporting your final video. You may see the time.

456
01:01:36.860 --> 01:01:40.380
Suren Poghosyan: So, since it's running, you may see the…

457
01:01:41.100 --> 01:01:50.629
Suren Poghosyan: relative speed, say, if, you're… you have a 100 second, 120 second video, it will be,

458
01:01:51.350 --> 01:02:00.689
Suren Poghosyan: exported in 12 seconds, because you have a speed of 10x, it is 243 frames per second.

459
01:02:01.500 --> 01:02:05.370
Suren Poghosyan: And later, there is a drawback.

460
01:02:05.690 --> 01:02:09.180
Suren Poghosyan: When you are creating the composite,

461
01:02:10.140 --> 01:02:14.240
Suren Poghosyan: Actually, you are encoding the… your sequence

462
01:02:14.450 --> 01:02:20.929
Suren Poghosyan: First time, and when you're concatenating everything together, you're re-encoding everything.

463
01:02:21.000 --> 01:02:38.649
Suren Poghosyan: from scratch. It's like you are doing the work twice. If you are just wanting to concatenate the videos, which is done pretty quickly, you're starting to have the issues that I highlighted, the same…

464
01:02:38.650 --> 01:02:43.930
Suren Poghosyan: Slow-mo sounding-like audios, which… I,

465
01:02:45.320 --> 01:02:51.730
Suren Poghosyan: I was convinced that it is because that frequency

466
01:02:51.960 --> 01:02:55.120
Suren Poghosyan: That was different for different sequences.

467
01:02:55.830 --> 01:03:04.109
Suren Poghosyan: And so, at this point, you have your stuff already exported in your folder, and you can go and check this.

468
01:03:04.890 --> 01:03:13.490
Suren Poghosyan: Gabor, how… if I stop the screen sharing, the recording won't stop, right?

469
01:03:15.100 --> 01:03:18.589
Gabor Szabo: No, it won't. No, no. But we'll see whatever you… okay.

470
01:03:19.130 --> 01:03:30.909
Suren Poghosyan: Yeah, so I want to reshare my… instead of the Chrome tab, the audio window. Yeah, I may show you the example, in the YouTube channel that I opened.

471
01:03:31.070 --> 01:03:33.640
Suren Poghosyan: So, here is where your

472
01:03:34.090 --> 01:03:49.779
Suren Poghosyan: speaker picture is being located, from the top and from the left, and the name and the position. You have the organizers, the sponsors and stuff, and later you proceed to your main layout. And there's the logo, there's…

473
01:03:49.910 --> 01:03:54.560
Suren Poghosyan: The speaker, and… There's the… the presentation.

474
01:03:55.950 --> 01:04:03.110
Suren Poghosyan: And, let me stop the record… stop the sharing, and, reshare it.

475
01:04:03.300 --> 01:04:04.420
Suren Poghosyan: In a moment.

476
01:04:07.450 --> 01:04:12.029
Suren Poghosyan: Mmm… Yes, I want to share my desktop.

477
01:04:12.700 --> 01:04:19.710
Suren Poghosyan: Yeah, I see, it's fine, yeah. It's the university, the campus part on my screen.

478
01:04:20.160 --> 01:04:34.459
Suren Poghosyan: And here is the folder. As you can see, let's actually quickly run through all the steps, because it takes a short amount of time to do so. We have the twin manifest,

479
01:04:35.770 --> 01:04:43.989
Suren Poghosyan: we have the… these are already the exported stuff, say, the preview, the LLM output.

480
01:04:44.200 --> 01:04:49.230
Suren Poghosyan: with the decisions, the transcription, and so on. Let's remove all of this.

481
01:04:50.210 --> 01:04:54.390
Suren Poghosyan: Do that once again in order to show you how that works.

482
01:04:55.140 --> 01:05:00.960
Suren Poghosyan: We also have the banner output, we removed this in order to export the banner as well.

483
01:05:01.300 --> 01:05:03.519
Suren Poghosyan: And yes, we are good to go.

484
01:05:03.840 --> 01:05:09.730
Suren Poghosyan: We go and run the pipeline for the banners, as we did already.

485
01:05:09.870 --> 01:05:15.460
Suren Poghosyan: We go back, we… See, our…

486
01:05:15.800 --> 01:05:25.889
Suren Poghosyan: layout. This is the empty layout without the speaker and the title and so on. And this is the instruction, what has to be in here.

487
01:05:26.420 --> 01:05:31.000
Suren Poghosyan: If we go to the banner output folder.

488
01:05:31.470 --> 01:05:35.720
Suren Poghosyan: We already see that Mr. Clark is here with

489
01:05:35.870 --> 01:05:40.099
Suren Poghosyan: Their position, and with the template itself in here.

490
01:05:40.300 --> 01:05:44.239
Suren Poghosyan: Next, we go to this main folder.

491
01:05:45.200 --> 01:05:51.289
Suren Poghosyan: we need to firstly, sync these videos. I don't know, Ken, let me open the video.

492
01:05:52.290 --> 01:05:54.660
Suren Poghosyan: Tell me if you hear the…

493
01:05:54.660 --> 01:05:55.710
Gabor Szabo: Copyrighted.

494
01:05:55.990 --> 01:05:57.179
Gabor Szabo: That's the overview?

495
01:05:57.340 --> 01:06:03.040
Suren Poghosyan: I'm afraid it might be, so let's not do that, yeah.

496
01:06:03.040 --> 01:06:04.779
Gabor Szabo: Then we kind of have to cut it out.

497
01:06:05.020 --> 01:06:05.660
Suren Poghosyan: Yeah.

498
01:06:05.760 --> 01:06:07.590
Suren Poghosyan: So…

499
01:06:07.890 --> 01:06:16.870
Suren Poghosyan: Theoretically, in this video, there is a good quality of audio which starts a bit earlier, and in this video, we have an audio which starts a bit later.

500
01:06:18.380 --> 01:06:22.429
Suren Poghosyan: And, here, we run the pipeline.

501
01:06:23.070 --> 01:06:30.390
Suren Poghosyan: That takes this input 1 and input 2 as an input, and gives us the video 1 synced and video 2 synced.

502
01:06:31.030 --> 01:06:33.230
Suren Poghosyan: And here they are. Let me…

503
01:06:33.470 --> 01:06:36.390
Suren Poghosyan: Yeah, so these are the synced videos.

504
01:06:36.720 --> 01:06:42.050
Suren Poghosyan: Which are trimmed. Actually, you can, clone the repo and do… try it yourself.

505
01:06:42.240 --> 01:06:43.800
Suren Poghosyan: On your own machine?

506
01:06:44.730 --> 01:06:48.450
Suren Poghosyan: And you may have all these assets in there as well.

507
01:06:49.010 --> 01:06:54.860
Suren Poghosyan: Next, we proceed to the main, main script, and…

508
01:06:54.860 --> 01:07:05.409
Gabor Szabo: Wait a second, there's a question, sorry. Can we use it also to create flyers, posters, JPEG, PDF, to promote speakers and their talks?

509
01:07:07.130 --> 01:07:24.360
Suren Poghosyan: Actually, you can create flyers, let's say, you can do that with ImageMagic, because what you do is you take your assets, you put on the canvas, and you export it. It's… if you add some,

510
01:07:25.120 --> 01:07:29.469
Suren Poghosyan: Some bank of assets that you have, so your brand assets.

511
01:07:29.590 --> 01:07:35.350
Suren Poghosyan: And you add some description of this, and you invite another layer of

512
01:07:35.550 --> 01:07:40.540
Suren Poghosyan: Decision-making from the side of the, AI API?

513
01:07:40.940 --> 01:07:48.019
Suren Poghosyan: and define some structure, you can have that automated as well. That can be done, but this is more for,

514
01:07:48.960 --> 01:07:50.930
Suren Poghosyan: Handling repetitive stuff.

515
01:07:51.270 --> 01:08:04.739
Suren Poghosyan: Because when you have the main template and you see that only the speaker image and only their title is changing, it is pretty overwhelming to manually

516
01:08:04.740 --> 01:08:14.200
Suren Poghosyan: open that template, manually switch the pictures, the title, and so on, and do that yourself. But in this case, if you are a fan of coding.

517
01:08:14.240 --> 01:08:19.799
Suren Poghosyan: you can definitely do that through, using ImageMagic.

518
01:08:20.090 --> 01:08:21.209
Suren Poghosyan: Yeah, who can?

519
01:08:22.399 --> 01:08:26.520
Suren Poghosyan: I guess there's another question as well. I see the comment count increased.

520
01:08:26.930 --> 01:08:29.809
Suren Poghosyan: But in that time, let's just run the script.

521
01:08:29.819 --> 01:08:33.559
Gabor Szabo: Oh, it was just a comment that thanks, yes, for 10 plus speakers.

522
01:08:34.300 --> 01:08:35.600
Suren Poghosyan: Oh, oh.

523
01:08:36.090 --> 01:08:40.559
Suren Poghosyan: Alright, thanks for, great questions.

524
01:08:40.890 --> 01:08:44.590
Suren Poghosyan: So we are, we, we're running the,

525
01:08:45.740 --> 01:08:48.279
Suren Poghosyan: The pipeline, the main pipeline already.

526
01:08:48.850 --> 01:08:55.380
Suren Poghosyan: And we see that this step's being executed. It is now being transcribed.

527
01:08:56.090 --> 01:09:15.919
Suren Poghosyan: Yeah, it is done again. We see the description zone, the decision layer, then we define the canvas sizes. This is where you can experiment. Sometimes speaker on the… standing on… if the speaker video is on the right, and your speaker is,

528
01:09:16.130 --> 01:09:20.600
Suren Poghosyan: In the speaker video, speaker shows to the right, and in the presentation.

529
01:09:21.430 --> 01:09:27.370
Suren Poghosyan: And the presentation is physically on the right, but on the left side of the screen.

530
01:09:27.390 --> 01:09:42.159
Suren Poghosyan: feels not right, and you may want to swap the speaker video and presentation by their places, then you have to play around with these coordinates. So that's what I plan to do so, because

531
01:09:42.160 --> 01:09:50.299
Suren Poghosyan: I did a mistake in our conference videos, and it is exactly that way, and I would love to have them swept.

532
01:09:50.790 --> 01:09:54.019
Suren Poghosyan: From right to left.

533
01:09:54.380 --> 01:10:03.470
Suren Poghosyan: And we go, again, Elmo, again, the fire starts, and at this point, you want to slap some…

534
01:10:04.070 --> 01:10:14.170
Suren Poghosyan: FFmpeg, decision makers through the internet, but that's a joke. Don't take it serious, it's for just… Making…

535
01:10:14.490 --> 01:10:26.010
Suren Poghosyan: things more funnier, and at the end, you get the videos that we got through this almost 70 minutes already. Oh, I'm sorry for taking this long, but…

536
01:10:26.360 --> 01:10:32.640
Suren Poghosyan: It was… I wanted to explain you all this stuff, and again, there are a lot of stuff that could be…

537
01:10:32.810 --> 01:10:40.130
Suren Poghosyan: talked about, but we don't have to go into much details. If you have questions later, you can text me.

538
01:10:40.590 --> 01:10:43.540
Suren Poghosyan: email me… And we can discuss that.

539
01:10:43.720 --> 01:10:49.069
Suren Poghosyan: But again, here we can come and see that we have the final output already.

540
01:10:49.450 --> 01:10:54.850
Suren Poghosyan: Which is the, 5-second, video… 5-second…

541
01:10:55.350 --> 01:11:03.120
Suren Poghosyan: of banner, and then as long as your… as your speech was. Sometimes, again, your,

542
01:11:03.700 --> 01:11:13.670
Suren Poghosyan: screen recording video might be much longer than your speaker video, or no, the opposite. Speaker video might be longer than the screen recording, and it will be a blank.

543
01:11:13.770 --> 01:11:16.239
Suren Poghosyan: A black square of Malevich.

544
01:11:16.800 --> 01:11:22.900
Suren Poghosyan: On the screen, and you might want to replace it with another…

545
01:11:23.260 --> 01:11:28.169
Suren Poghosyan: asset, say, a thank you banner or something else, which is not…

546
01:11:28.330 --> 01:11:30.770
Suren Poghosyan: Taken care of right now, and…

547
01:11:31.020 --> 01:11:38.589
Suren Poghosyan: You might feel free to, take over the code and fork the repo, Do that yourself.

548
01:11:38.750 --> 01:11:43.370
Suren Poghosyan: And also, there are some configurations that I would love to make.

549
01:11:44.020 --> 01:11:46.209
Suren Poghosyan: Let me show you the,

550
01:11:46.870 --> 01:11:53.990
Suren Poghosyan: the GitHub repo. It is called SamePie, that I uploaded recently, almost 2 weeks ago.

551
01:11:54.200 --> 01:12:08.060
Suren Poghosyan: And it has some human-made instructions, which are a bit faulty, and that I have to update to include more steps that may help you, and talk about more issues that may happen.

552
01:12:08.590 --> 01:12:11.559
Suren Poghosyan: And there are… I've created some issues.

553
01:12:11.630 --> 01:12:30.770
Suren Poghosyan: that I would like to approach, the same containerizing all the stuff, so you don't have to install FFmpeg on your own system, because, say, on Windows, it may have different problems, on Mac, it has its own problems, and on Linux its own.

554
01:12:30.770 --> 01:12:36.039
Suren Poghosyan: And you won't have to deal with encoding mismatch

555
01:12:36.640 --> 01:12:46.820
Suren Poghosyan: if you are doing Truth Docker, because you may just create the Linux image, and do everything in that Linux environment, and…

556
01:12:47.910 --> 01:12:50.609
Suren Poghosyan: Utilize these encodings.

557
01:12:50.800 --> 01:12:57.229
Suren Poghosyan: Maybe with the… you may have some problems with the exported videos playing on…

558
01:12:58.630 --> 01:13:01.699
Suren Poghosyan: on your Mac or on your Windows machine, but…

559
01:13:02.010 --> 01:13:05.319
Suren Poghosyan: I guess you can upload that to,

560
01:13:06.430 --> 01:13:22.570
Suren Poghosyan: to, like, YouTube or somewhere else, and this will work pretty well, because YouTube handles that, very well. Or, if you have some experience with it, or if you are enthusiastic, you can take over and handle the,

561
01:13:23.630 --> 01:13:29.759
Suren Poghosyan: the code for other platforms as well. Modularize it, add some configurations on the top, such as

562
01:13:29.910 --> 01:13:33.829
Suren Poghosyan: String configurations, or enums.

563
01:13:36.960 --> 01:13:39.900
Suren Poghosyan: And just… so people can handle that.

564
01:13:40.310 --> 01:13:47.180
Suren Poghosyan: And also, there are some, other issues regarding having that… having all of this in… Notebooks.

565
01:13:47.870 --> 01:13:58.449
Suren Poghosyan: an alternative to Docker, but I don't know how FFmpeg will behave, say, in Google Colab, or will it be able to install it

566
01:13:59.140 --> 01:14:01.859
Suren Poghosyan: at all into Google Colab, so…

567
01:14:02.170 --> 01:14:08.440
Suren Poghosyan: We have to experiment, we have to, play around with it.

568
01:14:09.310 --> 01:14:17.739
Suren Poghosyan: So, pretty much, this was everything that I had to talk about, or also there's this environment stuff.

569
01:14:17.870 --> 01:14:22.789
Suren Poghosyan: Where you have to put your Gemini API key, or any other API key.

570
01:14:23.430 --> 01:14:26.010
Suren Poghosyan: That you may use, and…

571
01:14:26.170 --> 01:14:29.989
Suren Poghosyan: The very last thing is the license.

572
01:14:30.270 --> 01:14:35.160
Suren Poghosyan: It is,

573
01:14:36.020 --> 01:14:50.990
Suren Poghosyan: AGPL 3.0 license with some extensions that you can't use this for commercial… for having a profit in commercial, world, and you…

574
01:14:52.960 --> 01:14:56.180
Suren Poghosyan: These have to stay open source, and if you are

575
01:14:57.410 --> 01:15:02.020
Suren Poghosyan: Using just for your own cause, and not for selling it.

576
01:15:02.410 --> 01:15:06.760
Suren Poghosyan: Feel free to do so, as long as you're sharing the updates with the community, and…

577
01:15:07.190 --> 01:15:20.220
Suren Poghosyan: That's it. I wanted this truly to be a community project, because a lot of communities use the same layout, the presentation, speaker, video, logo, and that's it. And, yeah.

578
01:15:20.620 --> 01:15:23.649
Suren Poghosyan: Thank you for listening me this long.

579
01:15:24.030 --> 01:15:25.270
Suren Poghosyan: And being there.

580
01:15:25.810 --> 01:15:42.180
Gabor Szabo: Well, thank you very much for your presentation. If there are any more last-minute questions which you still want to ask in the video, then, I mean, the audience, I'm telling, then do it now, and if not, then we are going to

581
01:15:42.680 --> 01:15:49.330
Gabor Szabo: stop the video, so people who are watching the video, then now please like it. I should have stopped it in the beginning, but…

582
01:15:49.410 --> 01:16:03.390
Gabor Szabo: Better at the end than ever. And follow the channel, and then below the video, you will find the links to various things related to this presentation and to future presentations.

583
01:16:03.460 --> 01:16:11.280
Gabor Szabo: So again, thank you very much, Sister Anne, for this presentation, and for all the people in the audience for the questions, and for just listening.

584
01:16:11.610 --> 01:16:14.329
Gabor Szabo: See you next time. Bye-bye.

