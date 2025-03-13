---
title: Using Streamlit to create interactive web apps and deploy machine learning models with Leah Levy
timestamp: 2025-03-13T07:30:01
author: szabgab
published: true
description:
---


{% youtube id="cnaNvhuolBs" file="2025-03-11-using-streamlit-to-create-interactive-web-apps-and-deploy-ml-models.mp4" %}


Discover how to quickly turn your Python scripts into interactive web apps using [Streamlit](https://streamlit.io/). This session will cover key features like visualisations, widgets, and deployment, empowering you to create user-friendly interfaces with minimal effort.

* [Leah Levy on LinkedIn](https://www.linkedin.com/in/llevy1/)
* [Leah Levy on GitHub](https://github.com/LLevy1/)

![Leah Levy](images/leah-levy.jpeg)


## Transcript

1
00:00:02.390 --> 00:00:05.820
Gabor Szabo: So hello and welcome to the Code Maven Channel.

2
00:00:05.960 --> 00:00:14.180
Gabor Szabo: My name is Gabor. I organize these events because I think it's very important for people to be able to share their knowledge.

3
00:00:14.410 --> 00:00:38.479
Gabor Szabo: and it's very useful for everyone else to learn from other people all around the world. I myself usually teach python and rust and help companies introduce testing in these 2 languages or introduce these languages. And that's it. Basically, this channel is mostly with. Now these videos from these meetings.

4
00:00:38.860 --> 00:01:07.330
Gabor Szabo: and I am really happy that you agreed to give this presentation in our meeting, and thank you everyone for joining us here. If you are in the Zoom Meeting. Then feel free to ask questions. Just remember that it's going to be in Youtube. If you're watching it in Youtube, then. And if you enjoy this video, then please, like the video and follow the channel, and later on we'll have below the the video links

5
00:01:07.380 --> 00:01:14.970
Gabor Szabo: and where you can contact layer as well if you are interested later on. So now it's your turn. Go ahead.

6
00:01:15.950 --> 00:01:16.850
Gabor Szabo: Welcome now.

7
00:01:21.690 --> 00:01:30.810
Leah Levy: so hopefully, you can see my screen. So my name is Leah. I'm currently living in the Uk, I'm a data scientist in the Uk.

8
00:01:30.810 --> 00:01:41.190
Gabor Szabo: Maybe I it's only just me, but I can see all the list of the people who are joined. Is it on your screen, or it's just mine. No, it's it's I think you're sharing that one.

9
00:01:43.930 --> 00:01:44.700
Leah Levy: Yeah.

10
00:01:49.860 --> 00:01:53.950
Gabor Szabo: Wait a second. Maybe it's my, it's mine. No view.

11
00:01:54.720 --> 00:01:56.819
Gabor Szabo: Yeah, no, it was mine. Sorry.

12
00:01:58.430 --> 00:02:00.800
Gabor Szabo: Sorry, confusing you. Okay.

13
00:02:02.020 --> 00:02:02.550
Leah Levy: It's okay.

14
00:02:02.550 --> 00:02:06.490
Gabor Szabo: Go ahead. No, no, it's okay. It was on my screen in the.

15
00:02:11.030 --> 00:02:22.899
Leah Levy: yeah. So I'm a data scientist in the for the Uk government. I'm currently get living in in England. I'm hoping to move to Israel soon. So be nice to meet everybody.

16
00:02:23.611 --> 00:02:42.418
Leah Levy: I'm gonna talk today about streamlit, which is a python library and how I use it to like deploy machine learning models and just build web apps. I'll put my contact details in the chat. If you wanna connect with me on Linkedin or follow me on Github.

17
00:02:43.200 --> 00:02:45.630
Leah Levy: be great to be great, to connect

18
00:02:46.694 --> 00:02:55.610
Leah Levy: and please feel free to ask questions as we go along. I've I can see the chat. So if you want to put messages in the chat or come off mute, whatever you prefer.

19
00:02:56.760 --> 00:03:02.790
Leah Levy: So streamlet is a python library. It's open source.

20
00:03:02.790 --> 00:03:10.029
Gabor Szabo: Sorry. Sorry. Just one note, I mean, right now we can see both you and and this and the slides.

21
00:03:10.300 --> 00:03:11.630
Gabor Szabo: and.

22
00:03:11.900 --> 00:03:12.880
Leah Levy: Oh, okay.

23
00:03:12.880 --> 00:03:22.350
Gabor Szabo: So maybe you want to turn off your your camera, or or just show the slides, because in the recording you you will be seen, anyway, probably at the top right corner

24
00:03:23.000 --> 00:03:25.769
Gabor Szabo: that now you can. I can see myself.

25
00:03:26.950 --> 00:03:28.720
Leah Levy: I'll share again. Hold on.

26
00:03:29.060 --> 00:03:29.850
Gabor Szabo: Okay.

27
00:03:36.170 --> 00:03:40.759
Leah Levy: Oh, yeah, it was on a strange I think I was messing around with the settings before.

28
00:03:40.960 --> 00:03:41.710
Leah Levy: Okay.

29
00:03:46.550 --> 00:03:47.979
Gabor Szabo: Oh, now it's good!

30
00:03:48.590 --> 00:03:49.296
Leah Levy: Yeah, okay.

31
00:03:50.100 --> 00:03:50.510
Gabor Szabo: Okay.

32
00:03:51.450 --> 00:03:56.100
Leah Levy: Thanks for letting me know. So you can see just like there's the slideshow.

33
00:03:57.130 --> 00:03:57.710
Gabor Szabo: Yeah.

34
00:03:58.130 --> 00:03:58.790
Leah Levy: Yeah,

35
00:04:02.210 --> 00:04:22.959
Leah Levy: so how many of you ever perhaps worked on a data science project? You've built a machine learning model. And you've wished you could deploy it quickly for others to use. Or perhaps you've built a web application. But front end development isn't really your expertise. It's too complicated. So this is where stream it really comes into its own.

36
00:04:23.270 --> 00:04:41.560
Leah Levy: It makes it easy for python developers to and data scientists to create beautiful interactive web apps without needing any front end development expertise. So it's lightweight. It's really easy to use doesn't require, you know, hundreds of lines of code.

37
00:04:41.620 --> 00:04:56.920
Leah Levy: And there's a really strong community online. So there's people building like add ons constantly. And there's also a strong community of people happy to answer questions and help if you have any issues.

38
00:05:01.950 --> 00:05:10.450
Leah Levy: So Streamline allows you to turn your python scripts into interactive web applications and just a few lines of code. So you don't need to be. Know any like

39
00:05:10.620 --> 00:05:19.650
Leah Levy: break traditional web frameworks like Flask or Django. You don't need any HTML Css. Or javascript. It's all python.

40
00:05:20.640 --> 00:05:32.522
Leah Levy: You can easily customize your web application using like sliders, buttons, check boxes making it interactive. And you're able to capture user, input too.

41
00:05:34.180 --> 00:05:53.920
Leah Levy: The app automatically updates when you're coding in in whatever id prefer, like visual studio code, as soon as you update the code and save it then updates in the in the actual application. I'll show I'll do a demo of it a bit later, so you could see exactly what I mean.

42
00:05:55.020 --> 00:06:00.160
Leah Levy: And but that just like makes development much faster. So you can see your changes as you go along.

43
00:06:00.400 --> 00:06:05.189
Leah Levy: And it works really well with other python libraries, popular ones like

44
00:06:05.370 --> 00:06:11.689
Leah Levy: numpy pandas plotly, even data science ones like tensorflow and scikit-learn.

45
00:06:11.900 --> 00:06:18.939
Leah Levy: So it enables you to visualize data. You can build dashboards, graphs, charts and also

46
00:06:19.470 --> 00:06:23.439
Leah Levy: integrate machine learning models directly into your application.

47
00:06:26.840 --> 00:06:51.719
Leah Levy: So a bit about deploying machine learning models so often. In data science, you go. You put a lot of work into creating it in a model. You've got your data, you've cleaned it. You've built a model. You've tested it, optimized it. You've evaluated the performance. But the real key is to kind of surface that to your end users or your clients

48
00:06:52.170 --> 00:07:01.079
Leah Levy: and using stream that makes it easy. It's quite user friendly interface. And it can handle resource, intensive tasks.

49
00:07:01.690 --> 00:07:03.910
Leah Levy: And it's easy to deploy as well.

50
00:07:04.050 --> 00:07:14.830
Leah Levy: You a basic workflow could be something like loading a pre-trained model from pickle file or on something from hugging face or tensorflow.

51
00:07:16.480 --> 00:07:32.710
Leah Levy: collect input from users. So as soon as they could enter some text. If it's like a chat bot, they could use some sliders and then it uses the machine learning model to make predictions and display the results to users.

52
00:07:33.150 --> 00:07:39.510
Leah Levy: So I've created a couple of examples of

53
00:07:39.610 --> 00:07:46.359
Leah Levy: what it can do. Just like kind of basic one's a dashboard and one's uses a pre-trained machine learning model.

54
00:07:50.010 --> 00:07:59.530
Leah Levy: I'm gonna I've taken some screenshots, but I think it'd be better to just show it live. So I'm just gonna have a go showing like, can you see this.

55
00:08:00.660 --> 00:08:01.400
Gabor Szabo: Then like.

56
00:08:03.980 --> 00:08:06.170
Leah Levy: Because, yeah, the code.

57
00:08:06.620 --> 00:08:07.280
Gabor Szabo: Yes.

58
00:08:09.100 --> 00:08:14.939
Leah Levy: So I've just pre pre-built like this very basic dashboard.

59
00:08:15.070 --> 00:08:17.750
Leah Levy: What it does is

60
00:08:18.230 --> 00:08:24.410
Leah Levy: I've got some dummy data about British culture. I thought I'd make it relative to me.

61
00:08:25.030 --> 00:08:27.209
Leah Levy: and I've just put it into a.

62
00:08:27.210 --> 00:08:29.650
Gabor Szabo: Saying, maybe you can enlarge the fonts a little bit.

63
00:08:32.220 --> 00:08:32.970
Leah Levy: Yeah, let me.

64
00:08:33.276 --> 00:08:33.889
Gabor Szabo: Yeah. Thanks.

65
00:08:35.520 --> 00:08:36.020
Gabor Szabo: Think so.

66
00:08:38.250 --> 00:08:38.909
Gabor Szabo: Noon.

67
00:08:42.010 --> 00:08:43.020
Gabor Szabo: Okay, well.

68
00:08:43.020 --> 00:08:43.420
Leah Levy: Oh, 2.

69
00:08:43.429 --> 00:08:47.150
Gabor Szabo: Yeah, yeah, no, it's good. I see.

70
00:08:48.430 --> 00:08:49.330
Leah Levy: Pardon.

71
00:08:50.920 --> 00:08:51.859
Gabor Szabo: I think it's fine now.

72
00:08:52.500 --> 00:08:53.440
Leah Levy: Okay?

73
00:08:54.357 --> 00:09:02.049
Leah Levy: So in the terminal I just use the command stream. Let run. So I do. Stream lit.

74
00:09:02.210 --> 00:09:06.640
Leah Levy: run, and then the name of your file.

75
00:09:06.830 --> 00:09:13.420
Leah Levy: In this case it's in the app folder, and it's called English chat, Hi.

76
00:09:16.530 --> 00:09:21.744
Leah Levy: and it takes a couple of seconds and it should pop up in like your browser.

77
00:09:23.780 --> 00:09:28.030
Leah Levy: so here you can have you stream it up in your browser. It's popped up here.

78
00:09:29.430 --> 00:09:37.429
Leah Levy: and here's the very basic app that I built in the top right hand corner. You see it running

79
00:09:38.360 --> 00:09:42.490
Leah Levy: and then there's a option here to deploy. If you want. If you're ready to deploy it.

80
00:09:43.405 --> 00:09:45.339
Leah Levy: Oh, what's this?

81
00:09:48.310 --> 00:09:49.360
Leah Levy: Okay?

82
00:09:56.720 --> 00:10:03.289
Leah Levy: If this doesn't work, I will just show you the screenshot instead.

83
00:10:03.890 --> 00:10:05.980
Leah Levy: Okay, so I've saved it here.

84
00:10:06.750 --> 00:10:10.696
Leah Levy: And you'll see an example now, actually, of

85
00:10:12.450 --> 00:10:23.590
Leah Levy: of how it updates in real time. So I've updated the file, the source file. And you see in the top right hand corner. Now there's an option I'll just zoom in and make it a bit bigger.

86
00:10:25.070 --> 00:10:28.779
Leah Levy: but it says source file change, and it gives you the option. Rerun

87
00:10:29.161 --> 00:10:33.799
Leah Levy: and they can click, always rerun. So I don't have to click that every time. So if I try that.

88
00:10:34.150 --> 00:10:38.630
Leah Levy: and it's work now. So this is just like a

89
00:10:39.100 --> 00:10:46.520
Leah Levy: basic application. There's a dropdown menu here, so you can select the category if I wanted to. Just see landmarks. See that

90
00:10:46.830 --> 00:10:50.740
Leah Levy: some reason it's giving me error sports

91
00:10:54.010 --> 00:11:03.280
Leah Levy: and the size of each bubble is the size of visitors per year, and you can hover over, and it gives you a little bit more information. And then if

92
00:11:04.900 --> 00:11:12.589
Leah Levy: yeah, I think I think the map plot little bit is broken on bottom. So that's 1 example. The next

93
00:11:13.270 --> 00:11:22.030
Leah Levy: application. Let me just cancel this. I'll just do control. C, let's run another

94
00:11:23.102 --> 00:11:30.350
Leah Levy: another. This is more of like a machine learning one. So I just run, stream, let run and

95
00:11:31.820 --> 00:11:32.980
Leah Levy: spell check.

96
00:11:50.550 --> 00:11:54.489
Leah Levy: Oh, I know why it's giving me an error because I haven't installed the packages.

97
00:12:09.660 --> 00:12:13.009
Leah Levy: I'm actually just using poetry library, which

98
00:12:13.200 --> 00:12:34.820
Leah Levy: it's it's not sure how common, how widely it's used. But it's a 3rd party. It's like A, it's not an inbuilt typically, you might manage your libraries, use your dependencies using like requirements, dot text file and then have a virtual create a virtual environment. But I'm just.

99
00:12:35.420 --> 00:12:45.569
Leah Levy: I've got used to using poetry, which is another like dependency package. So and that's just

100
00:12:46.130 --> 00:12:48.370
Leah Levy: just to clarify exactly what it is.

101
00:12:51.940 --> 00:12:58.580
Leah Levy: Yeah, that's not working. So let me just show you on the on the slide show.

102
00:12:59.580 --> 00:13:00.750
Leah Levy: Sorry?

103
00:13:09.314 --> 00:13:18.655
Leah Levy: What this is. Is. It imports text blog, which is a light, very lightweight kind of natural language processing library

104
00:13:20.020 --> 00:13:26.119
Leah Levy: and what happens is you put in your spelling. So you put in some text. In this case

105
00:13:26.530 --> 00:13:35.059
Leah Levy: I'm so bad at spelling spell really wrong, and then it returns the correct spelling and then in the top right. You can see it's very kind of

106
00:13:35.320 --> 00:13:47.810
Leah Levy: simply. There's only like 16 lines of code. It's quite lightweight. And I've put a link here to more community projects. You can see on on the stream website.

107
00:13:48.440 --> 00:13:50.030
Leah Levy: they've actually got

108
00:13:51.100 --> 00:13:59.750
Leah Levy: community projects. You can kind of get an idea of flavor, of exactly what's possible. So this one's quite cool. This is like a map.

109
00:14:00.445 --> 00:14:06.500
Leah Levy: Application that somebody's built that's called pretty map, where you kind of visualize

110
00:14:07.361 --> 00:14:11.959
Leah Levy: maps in like different, cool, different, cool ways.

111
00:14:13.051 --> 00:14:22.290
Leah Levy: But just so you can get kind of get an idea of like, it's quite personalizable. It doesn't have to look like they did. All the applications don't necessarily have to look the same.

112
00:14:38.920 --> 00:14:40.470
Leah Levy: Sorry gone too far.

113
00:14:45.890 --> 00:14:53.241
Leah Levy: Okay. So I wanted to talk about deployment. So I mentioned. It's there's different options to deploy.

114
00:14:54.210 --> 00:14:59.230
Leah Levy: Just gonna wait for the slides to kind of sync.

115
00:15:07.560 --> 00:15:08.619
Leah Levy: Not sure.

116
00:15:09.560 --> 00:15:10.799
Leah Levy: Okay, there we go.

117
00:15:13.880 --> 00:15:27.930
Leah Levy: There's a there's a couple of different options you could deploy locally, which is kind of what we've done. Just before we do the stream that run. But in most cases you want to deploy it to a cloud or servers.

118
00:15:28.370 --> 00:15:31.159
Leah Levy: So there's stream that has its own kind of

119
00:15:31.370 --> 00:15:39.799
Leah Levy: built like customized deployment option called the stream community cloud where you can deploy from, get straight from Github.

120
00:15:40.551 --> 00:15:46.568
Leah Levy: But that also supports other deployment options like Docker, Aws

121
00:15:48.475 --> 00:15:53.880
Leah Levy: and all these other options. The another benefit of the community cloud is.

122
00:15:54.720 --> 00:16:12.700
Leah Levy: you can it provides you with analytics data. So how many people have clicked on on your onto your dashboard. Total viewers, most recent viewers, timestamps of people's last visit. So you can kind of get an idea of when people have have used your application.

123
00:16:14.520 --> 00:16:18.800
Leah Levy: So I want to talk about the testing framework in the app.

124
00:16:18.910 --> 00:16:21.500
Leah Levy: This is something.

125
00:16:22.090 --> 00:16:35.319
Leah Levy: Last time I gave this talk at Pi Web in Tel Aviv. Someone asked me about testing. And I thought, Oh, yeah, that's I've not really used the testing framework. So I thought, I put a section in here to to show you kind of how I've done it.

126
00:16:36.415 --> 00:16:58.584
Leah Levy: So stream that has its own. You can use pi test, and and those usual kind of testing frameworks and stream. It has its own framework, which enables developers to build and run headless tests, which I executes the app code directly. So it simulates that user input and inspects the output for correctness.

127
00:16:59.090 --> 00:17:07.560
Leah Levy: for those who don't know headless tests is like a way to run automated browser tests without having, like the user interface.

128
00:17:08.027 --> 00:17:13.299
Leah Levy: So it's a more efficient way of testing the application because it doesn't need to like render the HTML.

129
00:17:13.569 --> 00:17:27.959
Leah Levy: It just sends requests to the server the same way like you would do in a browser, and it's much faster because you don't need to wait for a page to load, and it integrates well into your like any crcd pipelines you might have as well.

130
00:17:29.670 --> 00:17:47.450
Leah Levy: So an example of testing. So on the left hand side. I've written what might be a more traditional way to write a test. So you would import streamlet and also import textblob, which is the library I mentioned before that we used for the spell checker.

131
00:17:47.660 --> 00:17:49.590
Leah Levy: You kind of set up a

132
00:17:50.100 --> 00:17:57.630
Leah Levy: set up the app just as it appears in that, just as what you've to kind of mirror what you've written

133
00:17:58.258 --> 00:18:07.070
Leah Levy: and have some simulated user input and then load the text blob and then run the

134
00:18:07.520 --> 00:18:15.440
Leah Levy: run. The text Blob Library to generate the correct spelling, and then have an assert to correct, to ensure that

135
00:18:15.740 --> 00:18:23.610
Leah Levy: that is, what the output is is what you've expected is that should be the corrected spelling of what you've inputted.

136
00:18:24.489 --> 00:18:32.130
Leah Levy: But on the right, all you need to do is run install the streamer testing framework

137
00:18:32.250 --> 00:18:45.980
Leah Levy: with app test. App test is is what simulates the running of the app, and it provides different methods to set up, manipulate and inspect the app via the Api instead of doing it in the browser

138
00:18:49.370 --> 00:18:57.074
Leah Levy: And then I've just written a function to test the spelling. So you you've got app test, which runs the

139
00:18:57.710 --> 00:19:03.239
Leah Levy: which runs the application as if I was running it in the terminal.

140
00:19:03.950 --> 00:19:09.750
Leah Levy: I is simulate an input of the incorrect spelling and run that.

141
00:19:10.520 --> 00:19:16.360
Leah Levy: and then the assert that the corrected text equals the correct spelling.

142
00:19:17.358 --> 00:19:25.871
Leah Levy: And then I've just written some a couple of other tests this next function just asserts that the

143
00:19:27.180 --> 00:19:33.809
Leah Levy: the application is running and not producing any exception errors. And then this one tests that the title is

144
00:19:33.990 --> 00:19:36.970
Leah Levy: displaying the correct title as we've expected.

145
00:19:39.550 --> 00:19:48.459
Leah Levy: so you'll see it's much quicker. It's fewer lines of code. And you could just run it using like in the terminal using. I test

146
00:19:48.680 --> 00:19:51.339
Leah Levy: as you would like any other testing.

147
00:19:54.660 --> 00:20:03.330
Leah Levy: you can add multiple pages to an app. So you kind of create a new pages folder in the same folder where your application is running

148
00:20:03.934 --> 00:20:15.910
Leah Levy: and then you can give it. You can, whatever you name the whatever you name. The file is what kind of appears on the sidebar and you can amend the

149
00:20:17.040 --> 00:20:23.254
Leah Levy: you can amend the content as you would like any other application. I've put a link in here.

150
00:20:24.030 --> 00:20:25.680
Leah Levy: just so you can kind of

151
00:20:27.610 --> 00:20:30.949
Leah Levy: I was gonna show how to

152
00:20:32.609 --> 00:20:36.229
Leah Levy: it. It gives a good example rather than me, like giving

153
00:20:36.680 --> 00:20:41.279
Leah Levy: setting up lots of different ones. But you can kind of see the from the. It's got a good

154
00:20:41.750 --> 00:20:44.358
Leah Levy: kind of demo page.

155
00:20:49.446 --> 00:20:53.703
Leah Levy: hey? It's got a hello page. It's got a plotting demo.

156
00:20:54.980 --> 00:20:58.089
Leah Levy: yeah, you can have a look in your own time if you like.

157
00:21:24.610 --> 00:21:27.299
Leah Levy: Sorry. My computer's running super slow.

158
00:21:30.410 --> 00:21:32.449
Gabor Szabo: So I just I was just saying.

159
00:21:33.350 --> 00:21:38.320
Leah Levy: It's also supports chat inputs. So oops.

160
00:21:38.920 --> 00:21:47.796
Leah Levy: So if you if you everybody wants to build their own chat bots nowadays, and it provides support for that

161
00:21:48.380 --> 00:21:55.700
Leah Levy: where it kind of mimics a user. And it's got like an assistant with these like different emojis

162
00:21:56.242 --> 00:22:02.159
Leah Levy: so as if you were speaking to a person. Similar to kind of.

163
00:22:02.720 --> 00:22:07.300
Leah Levy: you know, like chat. Gpt's got an assistant kind of answer.

164
00:22:07.560 --> 00:22:30.921
Leah Levy: You can also like stream, the reply, you know how chat gpt kind of streams it, or writes it word by word, instead of just giving you an answer right away. As if somebody just to like make it look like somebody's typing. You can add a delay as well of like a couple of seconds to make it seem like it's thinking about a reply.

165
00:22:32.280 --> 00:22:52.160
Leah Levy: And different things like that. So this is just a an echo bot which just echoes, echoes whatever you type into it. Obviously not using any large language models. But you can use kind of any large language models that you want, and kind of just plug it in to a streaming dashboard.

166
00:23:01.040 --> 00:23:04.700
Leah Levy: So finally, just some additional features

167
00:23:05.710 --> 00:23:16.739
Leah Levy: which I've oops added kind of some links to. So, as I mentioned before, it's got like a whole wide range of different input widgets. And

168
00:23:17.180 --> 00:23:32.760
Leah Levy: I didn't kind of include them all on the dashboard, because I think that this page actually does it in a nicer way. You can see it's got different buttons, check boxes, feedback options, radio buttons.

169
00:23:33.550 --> 00:23:35.240
Leah Levy: sliders.

170
00:23:35.966 --> 00:23:39.269
Leah Levy: Numeric inputs. Yeah, I could just go on, but

171
00:23:40.150 --> 00:23:49.400
Leah Levy: pretty much you know anything you would need to build a nice looking app. It's got another

172
00:23:49.840 --> 00:23:56.568
Leah Levy: another thing is status elements of like progress bars loading

173
00:23:58.890 --> 00:24:03.326
Leah Levy: call out messages, but error boxes I've used before.

174
00:24:04.080 --> 00:24:08.824
Leah Levy: I can't say I've used the balloon ones, but that looks fun

175
00:24:12.470 --> 00:24:20.803
Leah Levy: And it also has integration for like interactive maps, as we saw before, like that, the map application that I

176
00:24:21.340 --> 00:24:27.209
Leah Levy: And it's also you can build interactive charts with like plotly and other similar libraries.

177
00:24:27.640 --> 00:24:36.139
Leah Levy: You can cache large data sets. So particularly when you're working with machine learning models. You're often dealing with

178
00:24:36.250 --> 00:24:48.150
Leah Levy: lot really, really, large data sets which you can cache into memory. So rather than reloading the reloading like a data set each time it can just store it in memory.

179
00:24:50.161 --> 00:25:12.448
Leah Levy: From a safety point of view. I've just looked at the privacy policy and took this this 4th bullet point straight from the privacy policy which is stream that cannot see and does not store any information contained inside stream. The apps like text shots and images, but as general advice, I would say, not to expose sensitive data.

180
00:25:13.020 --> 00:25:17.580
Leah Levy: unless you yeah.

181
00:25:18.310 --> 00:25:40.254
Leah Levy: you can expect, unless you're kind of like it's locked down. It's in a safe, secure environment. And you've got like full access controls and ensure your app is also protected from malicious input, like sequel injections, because, you know any. Any application is susceptible to to being hacked. So I guess just

182
00:25:41.480 --> 00:25:48.060
Leah Levy: be wary of this is probably no different either to to malicious input like that.

183
00:25:52.590 --> 00:25:53.465
Leah Levy: But

184
00:25:54.630 --> 00:26:01.731
Leah Levy: yeah, that's all I prepared for now, but happy to answer questions and go into into more detail on different bits.

185
00:26:03.040 --> 00:26:07.319
Leah Levy: but thank you for your time, and happy to answer any questions.

186
00:26:12.910 --> 00:26:15.524
Gabor Szabo: So thank you for the presentation.

187
00:26:17.190 --> 00:26:25.759
Gabor Szabo: I heard it the second time. I really like the testing part. I always think about testing when I, whatever I try to show.

188
00:26:25.890 --> 00:26:26.970
Gabor Szabo: And

189
00:26:27.810 --> 00:26:38.989
Gabor Szabo: if anyone has questions, then please ask. Now we can also, after the recording, after we stop the recording, we can stay around and have a conversation without the recording.

190
00:26:39.240 --> 00:26:45.520
Gabor Szabo: But anyway, it seems that there are no questions now.

191
00:26:46.440 --> 00:26:50.600
Gabor Szabo: So, Leah, thank you very much for for this presentation.

192
00:26:50.780 --> 00:26:56.499
Gabor Szabo: If we'd like to add anything more, I mean, I'll I'll have the links below also the the video.

193
00:26:59.180 --> 00:27:05.545
Gabor Szabo: So thank you for for giving this presentation. And thank you. Thank you. Thanks. Everyone who was attending. And

194
00:27:06.420 --> 00:27:11.800
Gabor Szabo: and everyone who was watching. So please remember to like the video and follow the Channel and see you

195
00:27:11.980 --> 00:27:15.530
Gabor Szabo: at one of our next one of our upcoming events.

196
00:27:15.960 --> 00:27:16.850
Gabor Szabo: Bye, bye.

197
00:27:18.140 --> 00:27:19.260
Leah Levy: Thanks, bye.

