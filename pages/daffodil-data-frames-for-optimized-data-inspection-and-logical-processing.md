---
title: daffodil, data frames for optimized data inspection and logical processing with Ray Lutz
timestamp: 2025-03-06T16:30:01
author: szabgab
published: true
description:
tags:
    - data
    - data frame
---

{% youtube id="L9OJtuJVOYg" file="2025-03-05-daffodil-data-frames-for-optimized-data-inspection-and-logical-processing.mp4" %}

Speaker: [Ray Lutz](https://www.linkedin.com/in/raylutz/)

![Ray Lutz](images/ray-lutz.jpeg)

[daffodil](https://github.com/raylutz/daffodil) (data frames for optimized data inspection and logical (processing)), which can create data frame instances similar to pandas, but using conventional python data types.

This means no conversion to/from the Pandas world, which I have found
from testing has a very high overhead. In fact, unless you plan to do at
least 30 repetitive column-based operations (like sums, etc) then you
should just stay in python world and avoid the conversion time, and you
win. But for many, time is not of the essence, or they stay in Pandas
world and never need any python. The syntax is easy to use and I am
extending it to use SQL database to allow for large table size and use
of the robust joins, etc. The SQL part is under work and not released yet.

## Transcript

1
00:00:02.370 --> 00:00:06.679
Gabor Szabo: Hello and welcome to the Code Maven meeting a meeting group

2
00:00:06.860 --> 00:00:12.580
Gabor Szabo: and Youtube Channel. If you are watching this on Youtube, thank you very much for everyone who joined us.

3
00:00:13.080 --> 00:00:17.649
Gabor Szabo: and especially thanks Ray, for giving this talk.

4
00:00:17.790 --> 00:00:26.829
Gabor Szabo: My name is Gabor Sabo. I usually teach python and rust and help companies introduce these languages or introduce testing in these languages.

5
00:00:27.030 --> 00:00:33.439
Gabor Szabo: And I also organize these meetings because I think it's very important to share knowledge and

6
00:00:33.640 --> 00:00:38.700
Gabor Szabo: the Zoom Meetings. And it is online. Events allow us to to

7
00:00:39.040 --> 00:00:47.660
Gabor Szabo: learn from each other, even if they are halfway around the world. And so with that, let me

8
00:00:48.120 --> 00:00:52.799
Gabor Szabo: give the word to you, Ray, and please introduce yourself and and just go ahead.

9
00:00:53.030 --> 00:01:15.399
Gabor Szabo: One thing sorry. Just one thing. Those who are here feel free to ask questions, either in the chat or in the or just speak up. Ray will tell you how it's going to work out. Just remember, if you're recording this, it's going to be in Youtube. So if you don't want to be in your in Youtube, then just write.

10
00:01:15.570 --> 00:01:17.069
Gabor Szabo: So thank you, it's yours.

11
00:01:17.660 --> 00:01:25.920
Ray Lutz: Okay, thank you so much. Gabor. Yes, my name is Ray Lutz. I'm let me go on to the let me share my screen here so we can get started.

12
00:01:27.660 --> 00:01:36.300
Ray Lutz: I am actually not that much that long term of a python user, you know only about maybe 5, 6 years.

13
00:01:36.925 --> 00:01:43.150
Ray Lutz: And then I had quite a wealth of experience before that with other languages, including.

14
00:01:43.320 --> 00:01:58.208
Ray Lutz: you know, assembly language. See? You know, Perl you know, Javascript, all these other kind of languages in one form or another, even though I do really like python. So I I did kind of settle on that

15
00:01:59.190 --> 00:02:00.310
Ray Lutz: for now.

16
00:02:00.670 --> 00:02:08.970
Ray Lutz: And so essentially, today, we're going to talk about this package called Daffodil.

17
00:02:09.110 --> 00:02:19.119
Ray Lutz: And it is data frames for optimized data inspection and logical processing. I came up with that later, you know, after we've chose the name. But

18
00:02:19.290 --> 00:02:26.149
Ray Lutz: the idea is that you see a lot. Df, if you use pandas, you're talking about data frames. Df, and

19
00:02:26.300 --> 00:02:35.600
Ray Lutz: so we wanted something kind of like that. And we use daf. So you know, throughout the code, if you see daf, you know that it's a daffodil data frame

20
00:02:35.710 --> 00:02:37.769
Ray Lutz: instead of a pandas.

21
00:02:39.390 --> 00:02:43.949
Ray Lutz: And I have a Master's degree, mostly electronics. I did do

22
00:02:44.810 --> 00:02:51.010
Ray Lutz: various medical devices and and document processing in my career.

23
00:02:52.170 --> 00:03:05.290
Ray Lutz: Most recently I'm developing audit engine, which is a ballot image auditing platform for checking elections. And underneath the citizens oversight, which is a nonprofit organization.

24
00:03:05.940 --> 00:03:11.629
Ray Lutz: Now, why, Daffodil, we already have pandas. So why would we need something new?

25
00:03:11.760 --> 00:03:20.499
Ray Lutz: Well, I needed a two-dimensional data type sort of a table structure. And so I started using pandas

26
00:03:21.433 --> 00:03:26.579
Ray Lutz: for almost everything I I use. You know, these 2 dimensional tables are really handy.

27
00:03:26.990 --> 00:03:31.890
Ray Lutz: but it turns out that pandas is mostly designed for numerics and

28
00:03:33.630 --> 00:03:35.880
Ray Lutz: it uses numpy under the hood.

29
00:03:37.400 --> 00:03:46.650
Ray Lutz: and so it's slow, really slow for row based operations, and some of them are now not even allowed. So you can't do an append

30
00:03:46.920 --> 00:03:51.099
Ray Lutz: like a Panda row. Seems like a basic thing you might want to do

31
00:03:51.290 --> 00:03:58.989
Ray Lutz: that's now not supported at all in pandas, because they know it's so desperately a disaster.

32
00:03:59.756 --> 00:04:04.090
Ray Lutz: So then you have to go over and and use something else. If you want to do that sort of thing

33
00:04:05.070 --> 00:04:06.400
Ray Lutz: and

34
00:04:07.280 --> 00:04:16.359
Ray Lutz: and also apply, they say, don't use, apply and apply is kind of a handy thing, which means you go row by row, and you apply some function to it

35
00:04:16.760 --> 00:04:18.329
Ray Lutz: at each row.

36
00:04:18.519 --> 00:04:22.530
Ray Lutz: And so you can't do that either, they said. We're deprecating all these things.

37
00:04:22.740 --> 00:04:27.689
Ray Lutz: I think you can still do apply. But they say, you know, it's really not recommended at all.

38
00:04:28.470 --> 00:04:29.809
Ray Lutz: And then

39
00:04:31.010 --> 00:04:39.919
Ray Lutz: it turns out also, when we're using files that are kind of a weird formats. Pandas assumes a lot when it reads them in.

40
00:04:40.090 --> 00:04:46.950
Ray Lutz: and you have to go jump through a lot of hoops to get it to just read it in like like something without doing anything.

41
00:04:47.090 --> 00:04:49.320
Ray Lutz: and then convert things as you go.

42
00:04:50.075 --> 00:04:53.209
Ray Lutz: It has some other problems, too, and we'll get into that.

43
00:04:53.360 --> 00:05:14.250
Ray Lutz: So this is when I started looking for another data type, and I had some various ones that I started using. And I ended up standardizing on this type of a two-dimensional data frame which is based on a list of lists. I call it a lol doesn't mean laughing out loud. It's a list of list type.

44
00:05:14.800 --> 00:05:17.030
Ray Lutz: And so it's a

45
00:05:17.430 --> 00:05:27.109
Ray Lutz: it's a python list. And in each each of these lists you have a additional list, and it's it's rectangular in form.

46
00:05:27.360 --> 00:05:33.910
Ray Lutz: So every single row is the same length, and it has a certain thing. So it's it's a rectangular

47
00:05:34.130 --> 00:05:39.620
Ray Lutz: array, but it's not the array type. It's a list of lists. So it's easy to add to.

48
00:05:39.780 --> 00:05:53.780
Ray Lutz: relatively easy to splice and insert insert rows or columns. You can do a lot of things fairly easily, mostly inserting and and rows as easy columns. Not quite so easy. But

49
00:05:55.260 --> 00:05:58.310
Ray Lutz: it's fairly malleable. And then

50
00:05:58.450 --> 00:06:07.459
Ray Lutz: also you can put anything at all in any one of these cells, and python will handle it just fine, so you could put a whole pandas array in here. If you want.

51
00:06:07.910 --> 00:06:13.879
Ray Lutz: you could put a whole numpy array of a million things in one cell if you want. Okay, so that's

52
00:06:14.000 --> 00:06:15.800
Ray Lutz: it's very versatile that way.

53
00:06:16.280 --> 00:06:27.199
Ray Lutz: So the basic thing is that you have this array, which is just numbered, and the numbers here don't stick to the columns and rows like they do in pandas?

54
00:06:28.680 --> 00:06:36.939
Ray Lutz: maybe other things. They they float like they would in a regular spreadsheet. So if you move the the rows around, the numbers of the rows

55
00:06:37.130 --> 00:06:42.429
Ray Lutz: are going to stay in the same order, even though you might have moved something up there and so forth.

56
00:06:42.870 --> 00:06:47.700
Ray Lutz: But then you can also optionally have names for each column.

57
00:06:47.940 --> 00:06:56.250
Ray Lutz: data types for the name for the columns and a separate type data types object that explains what those are.

58
00:06:56.420 --> 00:07:20.869
Ray Lutz: And then Optional row keys. Okay, these are both dictionaries. So the Header Dictionary, HD. And the Row Keys Key Dictionary are a special type of dictionary which gives you the number of the column, or the number of the row in the dictionary, so I don't know what you call this exactly, but I end up calling it a keyed list.

59
00:07:21.060 --> 00:07:27.140
Ray Lutz: In other words, this, this is this is the the the key.

60
00:07:27.430 --> 00:07:31.920
Ray Lutz: We'll go into the key list later. But but essentially this is the key.

61
00:07:32.310 --> 00:07:36.460
Ray Lutz: and this is the number that refers to an item in a list.

62
00:07:36.860 --> 00:07:37.940
Ray Lutz: And

63
00:07:39.230 --> 00:07:47.170
Ray Lutz: so your your dictionary would have a a key, and the value is always 0 1, 2, 3, 4, and so forth.

64
00:07:47.350 --> 00:08:04.169
Ray Lutz: And there isn't a standard function for this in python like there is like like you can have from keys, and you can give it a single value, and it can have nones all the way, or zeros, whatever you want all the way through. But it doesn't have it automatically. But it's easy to make.

65
00:08:04.410 --> 00:08:06.249
Ray Lutz: So this is what it looks like.

66
00:08:09.330 --> 00:08:20.650
Ray Lutz: Now, as I said, the Row keys and the Header Dictionary are dictionaries, but these are all optional. You could start with nothing, just an array of list of lists, and you still get all the functionality.

67
00:08:20.950 --> 00:08:23.839
Ray Lutz: But you would have to be using these indexes here.

68
00:08:24.280 --> 00:08:25.830
Ray Lutz: All right, let's go on to next.

69
00:08:26.100 --> 00:08:30.579
Ray Lutz: So essentially what my problem was this, if you have.

70
00:08:31.090 --> 00:08:36.630
Ray Lutz: you want to use pandas, and you import pandas here. And you say, I want to start a new data frame.

71
00:08:37.280 --> 00:08:43.970
Ray Lutz: and let's say you go through a bunch of Urls, and you harvest stuff from web pages, and you want to append to this array.

72
00:08:45.200 --> 00:08:46.570
Ray Lutz: If you say

73
00:08:46.690 --> 00:08:55.020
Ray Lutz: my data frame dot, append the web page metadata. You just take a dictionary, and you want to add it to the bottom of the pandas array.

74
00:08:55.250 --> 00:08:59.530
Ray Lutz: It's horrible! And this, in fact, this has been banned by

75
00:08:59.970 --> 00:09:02.950
Ray Lutz: the Pandas people. You can't append anymore.

76
00:09:03.190 --> 00:09:06.760
Ray Lutz: They they just said, This doesn't exist. That's how bad it is.

77
00:09:06.860 --> 00:09:09.240
Ray Lutz: Now, what were they doing? Why is it so bad.

78
00:09:09.420 --> 00:09:14.370
Ray Lutz: It's because what pandas is is, let me go back a second.

79
00:09:15.120 --> 00:09:18.980
Ray Lutz: I gotta. What is it? Shift to go back control?

80
00:09:20.630 --> 00:09:22.279
Ray Lutz: I gotta go with the keys.

81
00:09:23.050 --> 00:09:31.609
Ray Lutz: Okay, so what pandas is is essentially a numpy array vertically right here in a dictionary

82
00:09:32.010 --> 00:09:36.450
Ray Lutz: where you have the name of the dictionary, and the value

83
00:09:36.650 --> 00:09:41.830
Ray Lutz: is a numpy array vertically, and you've got to think of it that way, and they're all the same length.

84
00:09:42.370 --> 00:09:45.710
Ray Lutz: So the numpy array has data in

85
00:09:48.260 --> 00:09:57.079
Ray Lutz: numpy arrays. The data is, is, each value is like rammed up against each other. There's nothing else unlike Python, where

86
00:09:57.270 --> 00:10:06.190
Ray Lutz: even an integer, or whatever you have in here takes quite a bit of overhead. Usually it'll be like, I think, 28 Byte, just to represent an integer. There's a lot of overhead generally.

87
00:10:06.540 --> 00:10:12.820
Ray Lutz: and if you have, if you put a dictionary in each row, then you have the key for each one. That's I'll get into that in a second.

88
00:10:13.010 --> 00:10:19.259
Ray Lutz: My point, though, is that in a pandas array you have the the name, and you have a

89
00:10:20.950 --> 00:10:28.160
Ray Lutz: numpy array, and if you want to add to the bottom. You have to create all new numpy arrays, or us add to each one.

90
00:10:28.480 --> 00:10:32.420
Ray Lutz: They don't let you just add each one. They they create a whole new array every time.

91
00:10:32.770 --> 00:10:37.929
Ray Lutz: so they copy it over and add to the bottom, copy it over, add to the bottom, copy it over it. That's how they do it.

92
00:10:38.240 --> 00:10:39.739
Ray Lutz: And so it takes a long time

93
00:10:41.630 --> 00:10:51.909
Ray Lutz: if you're appending. So they they basically have disallowed this. So if you're not going to do that. Then you can do this. You can say, I want to make a list of dictionaries. I call it a lod.

94
00:10:52.460 --> 00:10:56.850
Ray Lutz: Okay? And it's a list of dictionaries with string keys and anything inside.

95
00:10:57.230 --> 00:11:05.030
Ray Lutz: And then you read the web page and you put your metadata dict and you append to the list of dictionaries. This will work fine.

96
00:11:06.100 --> 00:11:06.680
Gabor Szabo: Be fast

97
00:11:06.840 --> 00:11:15.420
Gabor Szabo: sorry. Let me just say something related to this. It's interesting, because in, in, I think in both in go and in rust

98
00:11:16.160 --> 00:11:21.789
Gabor Szabo: this you can. You can allocate more. Place space for these arrays.

99
00:11:22.090 --> 00:11:47.780
Gabor Szabo: even if you don't use them. So you can say that. Okay, I'm going to have at the end. I'm going to have a hundred or 1,000 long of these vectors or arrays right now. I have one item in there and then, whenever you so, the memory is already allocated, so you can append up till 1,000 without this overhead of recreating the whole array.

100
00:11:48.210 --> 00:11:58.869
Ray Lutz: They could have done a better job in pandas because they would not need to copy over the whole thing. I didn't even know they were doing that when I 1st started.

101
00:11:59.030 --> 00:12:07.589
Ray Lutz: And so I noticed when I got you know, when the array started to get pretty big that it just started to slow down to a snail space. And so what is this? Well.

102
00:12:07.710 --> 00:12:19.159
Ray Lutz: and then, in the documentation it says, Don't do this. What you're going to have to do is create something else, a list of dictionaries, and then at one fell swoop take your list of dictionaries and convert it into a data frame.

103
00:12:19.460 --> 00:12:21.690
Ray Lutz: and then it'll be reasonably fast.

104
00:12:22.100 --> 00:12:24.400
Ray Lutz: But this turns out, is very slow.

105
00:12:26.672 --> 00:12:33.759
Ray Lutz: But it's way faster than than the appending. Okay, so if you're going through and appending to the bottom of the array.

106
00:12:35.960 --> 00:12:42.792
Ray Lutz: this will be faster. But then this part right here is actually kind of slow. But if that's all you're gonna do. And you're just gonna write it out to a cash flow

107
00:12:43.140 --> 00:12:44.440
Ray Lutz: Csv file.

108
00:12:44.650 --> 00:12:50.110
Ray Lutz: Then then you've just wasted a lot of time because you didn't need to go through this here

109
00:12:50.700 --> 00:13:01.689
Ray Lutz: you could. You could just write it straight out. But if you did do a couple of things with it before you did that, you know you you maybe summed everything one time, and you added everything up.

110
00:13:02.681 --> 00:13:08.649
Ray Lutz: Maybe you did some other manipulation. You thought being in Panda's world was was a good idea.

111
00:13:09.272 --> 00:13:11.810
Ray Lutz: But then you had this overhead of doing this.

112
00:13:12.020 --> 00:13:16.770
Ray Lutz: So this works. But it turns out this is very slow, and when you time it.

113
00:13:17.350 --> 00:13:29.710
Ray Lutz: going from a list of dictionaries into pandas with, this is a 1 million integer table, a thousand by a thousand. Okay, that's the size table that we're using for our benchmark.

114
00:13:30.230 --> 00:13:40.079
Ray Lutz: Now, would Pandas normally have a thousand columns? No, right? Because most Panda, you know, most data tables have. Yeah, very few columns.

115
00:13:40.280 --> 00:13:43.350
Ray Lutz: Usually. Yeah, 20 to 30 columns is a big one.

116
00:13:44.218 --> 00:13:49.599
Ray Lutz: For the data tables I'm working with. They have a lot of columns. Okay, like

117
00:13:49.740 --> 00:13:57.470
Ray Lutz: something with 5,000 columns is is pretty big, but you'll see stuff under that and a lot of it. 3, 400 columns.

118
00:13:57.570 --> 00:14:00.429
Ray Lutz: So a thousand by 1,000, not unusual, that I see.

119
00:14:00.850 --> 00:14:12.250
Ray Lutz: and when you convert this in Daffodil, you take the list of dictionaries and make a list of lists with, you know, formatted for daffodil. It takes 139.

120
00:14:13.810 --> 00:14:15.009
Ray Lutz: What is it?

121
00:14:15.770 --> 00:14:22.660
Ray Lutz: Microseconds! Milliseconds, I believe Pandas takes 5,600 more than 5 seconds

122
00:14:23.640 --> 00:14:25.830
Ray Lutz: more than 5 seconds to convert

123
00:14:25.970 --> 00:14:31.070
Ray Lutz: it into pandas. So it is a ridiculous bottleneck.

124
00:14:31.830 --> 00:14:32.700
Ray Lutz: Okay.

125
00:14:33.350 --> 00:14:50.620
Ray Lutz: it takes 139 like, look at the difference here, and if you multiply this out, even though pandas is really really fast. To do certain things like summing columns is ridiculously fast compared to Daffodil. I can sum columns here at 191 ms.

126
00:14:50.720 --> 00:14:52.359
Ray Lutz: It takes only 4.

127
00:14:52.810 --> 00:14:56.289
Ray Lutz: So that's a big difference. So you do a big savings here.

128
00:14:56.430 --> 00:15:09.510
Ray Lutz: If you do a lot of these, then this might make up for this big difference here, but it takes a lot. It takes at least 30, all columns, doing all columns, all sum standard deviation. You got to do 30 of those

129
00:15:10.120 --> 00:15:12.950
Ray Lutz: before you make up for converting it into pandas.

130
00:15:14.670 --> 00:15:30.780
Ray Lutz: So for just a few things like summing columns or something, or just manipulating the data a little bit. You're just better off not getting into pandas because of this ridiculous conversion factor. Now, I tried to get around this problem here.

131
00:15:31.560 --> 00:15:34.549
Ray Lutz: and they're also another problem with pandas.

132
00:15:34.760 --> 00:15:38.289
Ray Lutz: This is integers as soon as you add a string.

133
00:15:39.620 --> 00:15:49.650
Ray Lutz: and and this is the size the size here is 38 MB. Believe it's megabytes for

134
00:15:49.750 --> 00:15:53.450
Ray Lutz: a million integers, and

135
00:15:55.600 --> 00:16:05.859
Ray Lutz: they they're only at 9.3, so it's quite a bit more compact and a pandas. Right, if you have just integers or just floats.

136
00:16:06.190 --> 00:16:12.950
Ray Lutz: but if you get a string. Then this goes up and becomes quite a bit larger by 10 times

137
00:16:13.730 --> 00:16:18.089
Ray Lutz: what, and quite a bit larger than a daffodil table, which really doesn't go up very much.

138
00:16:19.250 --> 00:16:26.170
Ray Lutz: Okay. So then, you know, numpy, we can convert things to numpy really quickly.

139
00:16:26.440 --> 00:16:33.029
Ray Lutz: 48 ms going to numpy, and from numpy doesn't take very long.

140
00:16:33.290 --> 00:16:36.139
Ray Lutz: and then you can manipulate in numpy

141
00:16:36.630 --> 00:16:47.929
Ray Lutz: one column at a time, or or add columns together, or sum the columns. Whatever you want to do. You can then do it directly in numpy and skip over pandas. Pandas is also a big beast.

142
00:16:48.170 --> 00:16:52.400
Ray Lutz: It takes a long time to load, so if you use daffodil.

143
00:16:52.890 --> 00:17:13.309
Ray Lutz: you import daffodil, and then you you create a daffodil array. You can't click on this, or it goes to the next thing. I can't highlight for that reason, but you create a daffodil. Array my daff, and then I go through the URL, and I get this stuff, and I append the dictionary to Daffodil array

144
00:17:13.369 --> 00:17:25.439
Ray Lutz: done, and then I simply write it out directly, and I skip over this thing here. Now. I was in a bad habit of using these pandas arrays for almost everything, because they're so handy.

145
00:17:25.760 --> 00:17:37.760
Ray Lutz: But little did I know that my code was getting to be really slow because of the conversion of the list of dictionaries over to Pandas was taking a long time every single time and then back.

146
00:17:40.047 --> 00:17:45.620
Ray Lutz: So this is when I came up with daffodil, and and you know what it provides is

147
00:17:46.060 --> 00:17:51.780
Ray Lutz: a way of also indexing into these. Now, if you just used a list of dictionaries.

148
00:17:52.210 --> 00:18:06.820
Ray Lutz: if you think about it? You have for every single row the keys are repeated, and then the next row. You repeat the keys, and you repeat the keys. Repeat the keys. So every single row has a lot of overhead, because the keys are being repeated.

149
00:18:09.260 --> 00:18:22.100
Ray Lutz: so when you crunch that down, you know, if we if we if we look back at the at the data, at the data type here, and you see in the row here, it's only that for each row. You just have a list of values.

150
00:18:22.260 --> 00:18:30.510
Ray Lutz: and you don't have the keys. The keys are one time, only you don't need them every single row. So you crunch all the keys up into one row.

151
00:18:31.090 --> 00:18:40.619
Ray Lutz: and then the indexing goes 2 times. So 1st you get the index of the list, and then you index into the list to get the data item. So it's 1 more step to get to it.

152
00:18:42.290 --> 00:18:48.650
Ray Lutz: But these are lists, and there's a lot of benefits to that

153
00:18:51.000 --> 00:18:59.080
Ray Lutz: 1st of all, we can use this type of indexing in python, which they provide all this as part of their infrastructure, so that you can write code

154
00:18:59.240 --> 00:19:02.600
Ray Lutz: that uses the indexing row column to.

155
00:19:03.040 --> 00:19:07.930
Ray Lutz: or you can use it for anything. But in this case the 1st index is row and then column

156
00:19:10.398 --> 00:19:16.771
Ray Lutz: so their own column can be integers, and and that can be either the array index

157
00:19:17.550 --> 00:19:18.500
Ray Lutz: or

158
00:19:20.240 --> 00:19:28.510
Ray Lutz: it can be, if you want it to be, but you have to go. If it's an integer it assumes it's going to be the array index and not a

159
00:19:28.790 --> 00:19:31.040
Ray Lutz: going through the dictionaries.

160
00:19:31.720 --> 00:19:37.109
Ray Lutz: If you want to go through the array index and you have to use a method. But

161
00:19:38.641 --> 00:19:43.559
Ray Lutz: if it's a string, then it assumes that it's a key into the dictionaries.

162
00:19:44.120 --> 00:19:57.309
Ray Lutz: and it can be a list of integers which, then, is the list of array indices that you want to choose. It can be a list of strings. It can be a list of string keys, so you can pull out individual rows, individual columns.

163
00:19:57.570 --> 00:20:03.520
Ray Lutz: Whatever you want, you can index, an individual position, and the array

164
00:20:03.790 --> 00:20:08.950
Ray Lutz: you can slice and dice it you can give it a

165
00:20:09.200 --> 00:20:14.760
Ray Lutz: a range of indexes like 5 to 10, which gives you 5, 6, 7, 8, 9,

166
00:20:15.510 --> 00:20:20.010
Ray Lutz: or you can do a range of keys in a close, closed

167
00:20:20.340 --> 00:20:28.939
Ray Lutz: kind, of which we use a tuple for that. So it's like from C to A, B, so from like column C to column A, B,

168
00:20:29.140 --> 00:20:36.129
Ray Lutz: because you don't know what's after A B, you can't say go to the next one and back up one. You have to give it a closed range.

169
00:20:36.580 --> 00:20:38.570
Ray Lutz: and so we do it like that.

170
00:20:39.070 --> 00:20:44.780
Ray Lutz: Now you can leave out the column if you want to use all columns kind of like star and sequel expression.

171
00:20:45.670 --> 00:20:49.729
Ray Lutz: But you can just leave that out and and then talk about the row.

172
00:20:50.160 --> 00:21:03.749
Ray Lutz: and you can index in. If you, if you append, the things can be in a different order, and they will always go in correctly and to the right. So here I have it screwed up where C is first, st and it ends up putting C in the right thing.

173
00:21:03.910 --> 00:21:07.139
Ray Lutz: And there's all kinds of examples here of how you would.

174
00:21:07.728 --> 00:21:28.079
Ray Lutz: Take that array that we start with here. 1, 2, 3, n045-67-8910. I don't know why I did that, but then you end up saying, I want to use rows one through 0 and one because that's a slice. You get those. You can get the columns same way. You can use the names of the columns.

175
00:21:28.200 --> 00:21:36.639
Ray Lutz: take all rows and names of columns here, and a list, so forth. We also offer

176
00:21:36.830 --> 00:21:42.830
Ray Lutz: a list of Tuples. I'm sorry a list of ranges which is kind of handy sometimes.

177
00:21:43.690 --> 00:21:45.829
Ray Lutz: and then you can

178
00:21:46.100 --> 00:21:53.070
Ray Lutz: get. You can set a value. You can say, I want to set this value to the entire array. It sets the whole thing

179
00:21:53.270 --> 00:22:02.466
Ray Lutz: you can. You can set the 1st few columns, you can slice it and do this. So this is a setting, so you can set

180
00:22:02.940 --> 00:22:11.539
Ray Lutz: and you can also pop in a list like, if you have a list, you want to put that in the column, you put that in and put a list into the row.

181
00:22:12.385 --> 00:22:17.500
Ray Lutz: You can put another daffodil array in, and it will put in this, that.

182
00:22:18.330 --> 00:22:24.870
Ray Lutz: for you know, whatever the rectangular region is, Boeing can put that in all those things work.

183
00:22:26.600 --> 00:22:33.980
Ray Lutz: Now, there's a return mode which is optional. But we're gonna end up putting this into like when you when you do this

184
00:22:35.236 --> 00:22:36.990
Ray Lutz: indexing here.

185
00:22:37.850 --> 00:22:50.590
Ray Lutz: you want to get the value out in this case, because you want to multiply 2 values together. If you set the return mode to Val, then then it'll give you the value directly. If you just did this you would get a daffodil array

186
00:22:51.560 --> 00:22:53.760
Ray Lutz: of the cell 0 1 1.

187
00:22:54.090 --> 00:23:01.039
Ray Lutz: I'm sorry one comma 0. So would be row. One is row 0 row one, and this would be 5 right.

188
00:23:01.350 --> 00:23:26.629
Ray Lutz: and you would get an array of 5. 1 thing in the middle of the ray. Well, you don't want that. You just wanted the value. So if you said, return the value, then you can just multiply it by this value over here and put that, and the one at 2 2 is 0 1 0 1, 2, 0 1, 2 is 10. Multiply those together 5 times 10, and put that in the cell. 2 comma one, and down here

189
00:23:26.890 --> 00:23:29.180
Ray Lutz: 0, 1, 2, 1 is 50.

190
00:23:29.430 --> 00:23:33.750
Ray Lutz: So we multiplied those values together and put it in here. So it's all malleable.

191
00:23:33.890 --> 00:23:38.526
Ray Lutz: You can do it like that just like a spreadsheet, and then

192
00:23:39.810 --> 00:23:43.939
Ray Lutz: we can insert columns here. So we're going to put in a first.st So the

193
00:23:44.160 --> 00:23:50.149
Ray Lutz: if you add a column like house, car and boat, and we call that category

194
00:23:52.740 --> 00:23:59.119
Ray Lutz: then we also say we want to set the key field to category. Now, what it's done is

195
00:23:59.310 --> 00:24:08.039
Ray Lutz: what it does, what it does. Is it one of the columns you can say that's going to be my key field, and then it puts it in that. That dictionary lookup!

196
00:24:08.200 --> 00:24:09.600
Ray Lutz: Called the

197
00:24:11.840 --> 00:24:20.049
Ray Lutz: Dk. Let's see, it's called HD, it's called a key key dictionary. So this is a dictionary lookup so super fast

198
00:24:20.260 --> 00:24:21.729
Ray Lutz: if you have a long one.

199
00:24:22.600 --> 00:24:30.250
Ray Lutz: but it has to be. If you do this, you can't have repeated values in here. It's gonna it's gonna hit the la, the 1st one that it sees.

200
00:24:31.774 --> 00:24:37.559
Ray Lutz: And so here, what we did was we add additional records, and it's going to add them in there

201
00:24:37.760 --> 00:24:38.690
Ray Lutz: with

202
00:24:40.260 --> 00:24:45.879
Ray Lutz: Here, you see the category is in a different order, and it still puts it in

203
00:24:46.530 --> 00:24:54.150
Ray Lutz: and if we have a double in there, it's going to modify the one that's there.

204
00:24:54.560 --> 00:24:57.849
Ray Lutz: So if you have, if you index in and you say?

205
00:24:58.403 --> 00:25:02.540
Ray Lutz: House, car, boat and house car boat, Mall Van Condo.

206
00:25:02.680 --> 00:25:04.559
Ray Lutz: I think I have it in the next one.

207
00:25:05.330 --> 00:25:15.550
Ray Lutz: where, if you say house and you give it new values. It's going to modify the one that's there. Okay, so it doesn't add another one called house.

208
00:25:16.650 --> 00:25:23.520
Ray Lutz: Then you can select by using a select where statement.

209
00:25:23.980 --> 00:25:34.650
Ray Lutz: This is where lambda statements are really useful, where you just say Lambda Row, and you say the row where the C value is greater than 20. I want to select those row those rows.

210
00:25:35.270 --> 00:25:42.259
Ray Lutz: It makes a new daffodil table, but it doesn't make new rows.

211
00:25:42.640 --> 00:25:47.410
Ray Lutz: These are actually the rows from this table just referenced over here.

212
00:25:48.110 --> 00:25:53.340
Ray Lutz: So it uses a by reference, just like Pandas Python does all the time.

213
00:25:53.460 --> 00:26:04.570
Ray Lutz: So you're not actually creating a new whole table. These are not unique values. These are actually the same list values from over here, put in over here so that you've just selected them.

214
00:26:04.770 --> 00:26:10.030
Ray Lutz: And so this daffodil table only has a list of references to the same data.

215
00:26:10.310 --> 00:26:15.149
Ray Lutz: all right, so that this way these selections are very fast because it doesn't do any copying

216
00:26:15.270 --> 00:26:17.197
Ray Lutz: unless you wanted to.

217
00:26:17.820 --> 00:26:18.740
Ray Lutz: Okay,

218
00:26:20.300 --> 00:26:30.059
Ray Lutz: you can select a record by the key. You can also just do it this way. Put the key in to the indexing, and then say, you want it to be a dictionary.

219
00:26:30.380 --> 00:26:35.700
Ray Lutz: Now, what we're going to end up doing is putting comma in here. Whoops can't click.

220
00:26:35.850 --> 00:26:44.570
Ray Lutz: You put a comma in here and put a R type return type equals Dick inside here instead of having dot 2, Dick.

221
00:26:44.730 --> 00:26:51.919
Ray Lutz: because it's handier to know, like in this mode, if you want it to be a list.

222
00:26:52.340 --> 00:26:57.040
Ray Lutz: that's what is already in the array. The list. So if you want the list out.

223
00:26:57.220 --> 00:26:59.189
Ray Lutz: You don't want to convert it to

224
00:27:00.940 --> 00:27:09.149
Ray Lutz: Say a dictionary or a whole array, because you're going to get a whole array out of this selection. One row. But it's going to be a daffodil array data type.

225
00:27:11.580 --> 00:27:21.490
Ray Lutz: so what you don't. If you want to get a list out of it. It's nice to know ahead of time. So, and we'll all show you that in a second, because there's another thing I want to show you, which is called a keyed list.

226
00:27:23.220 --> 00:27:30.630
Ray Lutz: so you can get at different types out. If you have 2 deck, 2 list, 2 value, you can just print, or there's other things to numpy

227
00:27:31.125 --> 00:27:34.909
Ray Lutz: to pandas. You know there's other things you can convert to here.

228
00:27:36.590 --> 00:27:39.989
Ray Lutz: So a common usage pattern is to process things by row.

229
00:27:40.752 --> 00:27:46.529
Ray Lutz: Where you would have somehow you're transforming the original row into a new row.

230
00:27:47.320 --> 00:27:50.870
Ray Lutz: and then you append the new row to the new daffodil table.

231
00:27:51.000 --> 00:28:09.870
Ray Lutz: Now, depending upon what the transform does, it might give you the same data again, with just something modified. It might mutate that row, and you would get it back here. When you append this, it's the same row as the original with a mutation. Guess what? That's going to modify the old row, so you don't necessarily want to do that. If you're making a mutation

232
00:28:13.400 --> 00:28:19.369
Ray Lutz: and then you would append it to the new table.

233
00:28:19.590 --> 00:28:27.799
Ray Lutz: and then you can do, you can put it out. It turns out you don't have to flatten. We've discovered later, and I want to show you that in a second it automatically flattens.

234
00:28:29.580 --> 00:28:37.630
Ray Lutz: so you can just apply. So if you have a transform row function, you just say, apply the function and it applies it, row by row

235
00:28:37.780 --> 00:28:41.289
Ray Lutz: and then gives you a new daffodil table. So you just go. You can do it this way.

236
00:28:42.380 --> 00:28:54.709
Ray Lutz: And you can also then just apply the data types at the end. If you want like, you can read it in, apply the data types, apply the transform. You don't need to flatten it anymore. Because I'll show you why most of the time.

237
00:28:54.980 --> 00:28:57.570
Ray Lutz: And then you just say to Csv and write it out.

238
00:28:57.960 --> 00:29:01.169
Ray Lutz: So here's where you write it in. You transform, row by row.

239
00:29:02.940 --> 00:29:14.319
Ray Lutz: if you're doing this, daffodil works really? Well, okay. And this same sort of transform can be applied to. I'll show you in a second, when we're expanding this to use SQL,

240
00:29:15.330 --> 00:29:16.210
Ray Lutz: backing

241
00:29:18.610 --> 00:29:24.210
Ray Lutz: so we avoid copies. This is what makes it faster way faster than pandas. Most of the time

242
00:29:24.390 --> 00:29:26.660
Ray Lutz: pandas is is fast.

243
00:29:26.990 --> 00:29:33.479
Ray Lutz: If you're doing those matrix manipulate not their array manipulations that are used in numpy.

244
00:29:33.810 --> 00:29:40.909
Ray Lutz: But if you do stupid things like like add columns and add rows and pen things and stuff. It gets really, really slow.

245
00:29:41.040 --> 00:29:48.260
Ray Lutz: And also when you're when you end up copying. So we're using references to existing data rather than recopying unless you want to

246
00:29:49.530 --> 00:29:53.550
Ray Lutz: so row selections, reuses the existing Header Dictionary

247
00:29:53.870 --> 00:30:00.470
Ray Lutz: and the selected list values from the source daffodil array, and then

248
00:30:00.730 --> 00:30:10.269
Ray Lutz: processing by columns is slower, but you can usually avoid that. What you want to do is in one fell swoop. If you want to add columns and drop them.

249
00:30:11.090 --> 00:30:12.809
Ray Lutz: You do that all at one time.

250
00:30:13.310 --> 00:30:16.820
Ray Lutz: and, in fact, if you want to do 8 that a

251
00:30:19.150 --> 00:30:20.690
Ray Lutz: if you want to flip, the

252
00:30:20.960 --> 00:30:25.246
Ray Lutz: flip, the array on a on a diagonal, which is

253
00:30:26.710 --> 00:30:29.919
Ray Lutz: Why can't I think of it? It starts with France. I can't think of a trance.

254
00:30:30.895 --> 00:30:33.259
Ray Lutz: We'll get to that in a second, but it but the

255
00:30:34.496 --> 00:30:43.109
Ray Lutz: daffodil is pretty slow with doing when you you know head to head when you're doing manipulations of

256
00:30:43.460 --> 00:30:44.700
Ray Lutz: numerics.

257
00:30:45.190 --> 00:30:51.100
Ray Lutz: But when you're doing this type of row selections, it's much faster

258
00:30:51.440 --> 00:31:03.609
Ray Lutz: and column basing. Oh, it's transposition. If you say Flip is true, and you're doing adding rows or subtracting them. You can also flip it for free, because you have to make a whole new one.

259
00:31:04.720 --> 00:31:12.470
Ray Lutz: so you can flip it for free, if you want to, when you're changing the columns, dropping them and adding them. But you want to do that all at one time.

260
00:31:13.170 --> 00:31:14.359
Ray Lutz: Add and drop.

261
00:31:14.460 --> 00:31:21.460
Ray Lutz: basically modify. The columns, end up with a new array that has the columns that you need, and then mutate it in place.

262
00:31:23.110 --> 00:31:25.880
Ray Lutz: In other words don't add columns one at a time.

263
00:31:26.470 --> 00:31:29.340
Ray Lutz: and because it's going to just be a lot of overhead.

264
00:31:31.280 --> 00:31:37.400
Ray Lutz: But if you have columns in there, then you can just don't use the ones that you don't want to use. Okay, next thing.

265
00:31:37.790 --> 00:31:44.809
Ray Lutz: So the keyed list is one of the core technologies that we developed inside this at once, we got some more experience.

266
00:31:45.500 --> 00:31:51.710
Ray Lutz: So a key keyed list is basically, if you

267
00:31:51.870 --> 00:31:58.130
Ray Lutz: take a if you do a zip of keys and values. This creates a conventional dictionary. So you have.

268
00:31:58.300 --> 00:32:04.090
Ray Lutz: if you want to. Let's say you have a list and you have keys. You want to apply to a list values.

269
00:32:04.250 --> 00:32:07.959
Ray Lutz: You have to go through this transformation, and this takes time.

270
00:32:08.570 --> 00:32:12.000
Ray Lutz: It distributes the values to each item in the dictionary.

271
00:32:12.340 --> 00:32:16.860
Ray Lutz: You create a dictionary with these keys, and then you put a value on each one.

272
00:32:17.100 --> 00:32:25.010
Ray Lutz: and it's it's in memory. Now. All of a sudden the values are distributed out in this dictionary. You don't know what order they're entering some weird order now.

273
00:32:25.760 --> 00:32:32.019
Ray Lutz: The dictionary takes care of making them in the same order, but in the actual dictionary itself. I don't know what order they're in.

274
00:32:32.610 --> 00:32:34.240
Ray Lutz: They're not a list anymore.

275
00:32:34.360 --> 00:32:35.690
Ray Lutz: Let's put it that way

276
00:32:36.480 --> 00:32:42.069
Ray Lutz: so you can get the list out by saying, Dick. Dot values. You can get the list out

277
00:32:42.560 --> 00:32:48.910
Ray Lutz: and you can get the keys out. It's it's not a list. At this point you'd have to convert it to a list. It's a keys.

278
00:32:49.290 --> 00:32:51.120
Ray Lutz: It's a keys type oops.

279
00:32:51.740 --> 00:32:56.009
Ray Lutz: So we propose this concept except of a keyed list

280
00:32:56.680 --> 00:33:01.210
Ray Lutz: which contains a header dictionary that contains indexes for each key and

281
00:33:02.950 --> 00:33:09.609
Ray Lutz: this is one way to create the header dictionary. And it's this is an easy way to understand it, but it's not the most optimal way to do it.

282
00:33:09.760 --> 00:33:11.419
Ray Lutz: So you're going to have a column

283
00:33:11.540 --> 00:33:23.539
Ray Lutz: name and the index for the index and the column for the enumeration of the keys. So this index is going to go. 0 1, 2, 3, 4, 5, and that's going to be the value. Right? You go through all the keys, and you put them up here.

284
00:33:23.640 --> 00:33:28.090
Ray Lutz: So this stays the same for every

285
00:33:28.400 --> 00:33:36.420
Ray Lutz: keyed list of the same size and with the same columns. You don't need a new header dictionary. You can use the same one for different keyed lists.

286
00:33:36.850 --> 00:33:41.490
Ray Lutz: And the key. The list is

287
00:33:41.870 --> 00:33:50.640
Ray Lutz: a list so, and like a regular dictionary that has, that distributes the values amongst all the keys in the structure.

288
00:33:50.950 --> 00:33:53.400
Ray Lutz: The list is this is still a list.

289
00:33:54.930 --> 00:34:02.499
Ray Lutz: It still looks like a dictionary. You have a key and a value, but it's structured, and you can still get the list out.

290
00:34:04.370 --> 00:34:09.670
Ray Lutz: It looks like a dictionary, but it's not designed like a dictionary.

291
00:34:10.050 --> 00:34:15.480
Ray Lutz: It has a header which has, excuse me

292
00:34:16.360 --> 00:34:19.470
Ray Lutz: like a 0 b, 1 c, 2,

293
00:34:20.190 --> 00:34:28.119
Ray Lutz: and then a list associated with that and and that this way, it's faster to to do things. So if you have a keyed list.

294
00:34:28.610 --> 00:34:32.309
Ray Lutz: and like A is 34 B, 45, and C is 56,

295
00:34:33.159 --> 00:34:36.180
Ray Lutz: and you have values here. 1, 2, 3.

296
00:34:37.460 --> 00:34:42.620
Ray Lutz: You can say, the key list. Dot values equals. This value list, assign new values.

297
00:34:43.440 --> 00:34:46.719
Ray Lutz: And now you have a new keyed list. With those values in there

298
00:34:47.530 --> 00:34:52.000
Ray Lutz: you could do the same thing with the dictionary. It would put new values into the dictionary.

299
00:34:53.510 --> 00:34:57.329
Ray Lutz: If you say, what is the value of B.

300
00:34:58.010 --> 00:35:04.480
Ray Lutz: You know you're saying, I want to assign 67 to the to the B.

301
00:35:04.930 --> 00:35:06.970
Ray Lutz: Now you have 67 here

302
00:35:07.450 --> 00:35:11.410
Ray Lutz: the values list that you originally used. Sorry I can't click

303
00:35:11.540 --> 00:35:17.100
Ray Lutz: the values list that you originally used also got changed because it's the same list.

304
00:35:17.460 --> 00:35:18.729
Ray Lutz: When you said.

305
00:35:19.160 --> 00:35:31.599
Ray Lutz: I want to use. Assign this values list to the keyed list. Dot values. It did not make a new list. It did not recopy anything. All it did is add a reference in here to this existing list.

306
00:35:33.840 --> 00:35:41.649
Ray Lutz: and then the values list is the key list. Dot values output. True.

307
00:35:41.780 --> 00:35:45.139
Ray Lutz: the is function means it is exactly the same thing.

308
00:35:45.900 --> 00:35:49.550
Ray Lutz: It's the same thing in memory. There's no new version of it.

309
00:35:50.370 --> 00:35:55.670
Ray Lutz: So a keyed list means that we can

310
00:35:57.003 --> 00:36:03.320
Ray Lutz: number one. If you have a list, and you want to put it into your daffodil array.

311
00:36:04.780 --> 00:36:11.099
Ray Lutz: Don't turn it into addiction like, if you have a list. It goes directly into that list in the array.

312
00:36:11.430 --> 00:36:15.050
Ray Lutz: Now, if you want to iterate through the daffodil array.

313
00:36:15.650 --> 00:36:20.339
Ray Lutz: it's convenient to iterate through with keyed lists, because, if you modify one.

314
00:36:20.450 --> 00:36:25.580
Ray Lutz: it actually modifies the array without having to recopy it in just the way a

315
00:36:25.730 --> 00:36:28.430
Ray Lutz: like. If you had a list of dictionaries

316
00:36:28.710 --> 00:36:35.689
Ray Lutz: and you go through the list of dictionaries, and you you have a dictionary in hand, and you change that item.

317
00:36:36.690 --> 00:36:44.360
Ray Lutz: It actually is the same dictionary as in the main ray of list of dictionaries, and it'll change it in the list of dictionaries.

318
00:36:44.560 --> 00:36:50.450
Ray Lutz: Now, if you have a daffodil array and you pull a dictionary out.

319
00:36:50.830 --> 00:36:56.150
Ray Lutz: It's not the same data as what's in the array, and if you change it, it doesn't change what's in the array.

320
00:36:56.510 --> 00:36:58.570
Ray Lutz: But if you take a keyed list out.

321
00:36:58.900 --> 00:37:07.050
Ray Lutz: and you change that item in that list. That list is the same one that's in the array, and you've changed it without having to recopy it back in. So then, it works the same way as dictionaries do.

322
00:37:07.830 --> 00:37:11.330
Ray Lutz: I don't know if I I probably can add another slide for that to explain it.

323
00:37:12.240 --> 00:37:14.490
Ray Lutz: Now we're going to go to a new topic.

324
00:37:14.940 --> 00:37:18.390
Ray Lutz: Csv, reading very, very fast. If you have

325
00:37:21.110 --> 00:37:25.429
Ray Lutz: as you stay in string type, so as long as you don't convert anything.

326
00:37:26.140 --> 00:37:30.528
Ray Lutz: the python reader is really fast

327
00:37:31.580 --> 00:37:39.080
Ray Lutz: for a million rows. According to this guy here. This reference he timed it. I'm not sure I trust this, but anyway, I used it because it was a reference.

328
00:37:39.360 --> 00:37:44.210
Ray Lutz: and if you do a Pandas read Csv. It's much more time.

329
00:37:46.960 --> 00:37:51.909
Ray Lutz: Pandas, read Csv with a chunk size is for some reason worse.

330
00:37:52.080 --> 00:37:55.340
Ray Lutz: Dask, worst data frame

331
00:37:55.630 --> 00:38:04.049
Ray Lutz: a data table, I guess, is another option. It's not as fast. This looks like absurdly

332
00:38:04.280 --> 00:38:15.620
Ray Lutz: way better than it really is, so I'll have to look into that. But it's still very, very fast, because it doesn't do any type conversion for you and pandas does this automatically try to be

333
00:38:15.780 --> 00:38:17.700
Ray Lutz: be easy to use.

334
00:38:17.830 --> 00:38:20.650
Ray Lutz: But if you don't want that, it doesn't, doesn't happen

335
00:38:21.290 --> 00:38:26.700
Ray Lutz: so later you can apply the D types and unflatten.

336
00:38:27.230 --> 00:38:36.669
Ray Lutz: unflatten them, which would would bring them up into become a data python data type, such as like, if you have a dictionary in a cell.

337
00:38:37.170 --> 00:38:42.340
Ray Lutz: and it gets turned into what either Json or what I call pyon.

338
00:38:42.490 --> 00:38:44.270
Ray Lutz: which we're going to get into in a second.

339
00:38:44.710 --> 00:38:50.050
Ray Lutz: then it will reform that into the dictionary within the cell.

340
00:38:52.220 --> 00:38:54.230
Ray Lutz: Now, Csv. Writer.

341
00:38:54.690 --> 00:39:02.520
Ray Lutz: right flattens automatically to pion. I didn't know this pion is something that I dreamed up as a name.

342
00:39:03.140 --> 00:39:07.729
Ray Lutz: It means python object notation. And it's similar to Json.

343
00:39:08.630 --> 00:39:14.329
Ray Lutz: It's actually a superset of Json Javascript. Object notation

344
00:39:14.520 --> 00:39:18.730
Ray Lutz: is Json. And this is simply python object notation.

345
00:39:18.920 --> 00:39:25.750
Ray Lutz: but it can express sets, tuples, dicks, lists, functions, etc. So we can do everything

346
00:39:26.633 --> 00:39:40.640
Ray Lutz: within python, and it already does for the most part, except for functions. It'll create sets, Tuples, diction lists automatically, and a Csv writer without any you doing anything.

347
00:39:41.710 --> 00:39:43.569
Ray Lutz: I just stumbled across this.

348
00:39:44.205 --> 00:39:50.850
Ray Lutz: Now Pyon already exists. It's already defined. It's what you get if you rep, or something.

349
00:39:53.110 --> 00:39:54.560
Ray Lutz: Generally speaking.

350
00:39:54.840 --> 00:40:02.690
Ray Lutz: not always, because sometimes the wrappers are broken in in these things, but that they should do is define this as being

351
00:40:03.190 --> 00:40:08.180
Ray Lutz: a Csv writer should use Reper, and sometimes it uses the Str function instead.

352
00:40:11.540 --> 00:40:21.019
Ray Lutz: it's better than Pickle, Json, Pickle, and other variants of Json for working with python types, in my opinion.

353
00:40:21.940 --> 00:40:25.030
Ray Lutz: So I generated this pyon pyon tools.

354
00:40:25.210 --> 00:40:30.269
Ray Lutz: python module. It isn't quite published yet, but I'm using it myself.

355
00:40:30.630 --> 00:40:37.289
Ray Lutz: and it turns out, Csv, but it's very simple, because what you're doing is you're using the wrapper method for any object.

356
00:40:37.440 --> 00:40:40.980
Ray Lutz: and it basically does it already.

357
00:40:41.090 --> 00:40:48.960
Ray Lutz: But when you're using Csv writer, you don't have to change this. So the way I stumbled across. This is, I had dictionaries

358
00:40:49.170 --> 00:40:54.449
Ray Lutz: in, and my daffodil array. I wrote it out to a file.

359
00:40:54.600 --> 00:41:01.139
Ray Lutz: and it automatically converted them and flattened them out into character strings, the normal ones that you see

360
00:41:02.866 --> 00:41:13.269
Ray Lutz: when you look at when you look at a dictionary like we just were looking at some that look just like when you look at this, this dictionary right here

361
00:41:13.420 --> 00:41:21.259
Ray Lutz: opens bracket single quote, a single quote, Colon 0, comma. All that sort of thing.

362
00:41:21.610 --> 00:41:31.939
Ray Lutz: This is the expression, a string expression that represents a dictionary. It isn't the dictionary itself. Dictionary itself is some other, you know, thing in memory, and

363
00:41:32.100 --> 00:41:42.130
Ray Lutz: of a fairly complex structure that python has suppressed. And what you understand as a dictionary, are these symbols right here?

364
00:41:42.430 --> 00:41:52.550
Ray Lutz: Those symbols are character strings that can be represented in a file. So this is what you get. If you have a dictionary, which is this header dictionary with those things in it. That's exactly what you find in the

365
00:41:52.940 --> 00:41:54.910
Ray Lutz: and the and the Csv file

366
00:41:55.290 --> 00:42:04.269
Ray Lutz: this right here. Unfortunately, he doesn't use double quotes. So it's not exactly Json. If they allowed you to say, use double quotes instead. This would be Json.

367
00:42:04.920 --> 00:42:11.979
Ray Lutz: and then you could use it with other tools, a little bit of a ripple there with what they use in python.

368
00:42:12.100 --> 00:42:14.969
Ray Lutz: and maybe we can get Csv. Writer to

369
00:42:15.140 --> 00:42:19.120
Ray Lutz: optionally. Use double quotes, so would still be valid Pyon.

370
00:42:19.750 --> 00:42:23.499
Ray Lutz: but also meets the subset of Json.

371
00:42:24.730 --> 00:42:27.319
Ray Lutz: I think the Python community should embrace

372
00:42:27.550 --> 00:42:30.940
Ray Lutz: the pyon that they've already defined, but they don't have a name for it

373
00:42:31.270 --> 00:42:38.240
Ray Lutz: and provide options for Csv. Writer to use double quotes and stuff in there, because then it would produce Json.

374
00:42:38.570 --> 00:42:43.040
Ray Lutz: But this is how we flatten things from Daffodil. We do almost do nothing.

375
00:42:43.160 --> 00:42:45.529
Ray Lutz: Python already does it for us.

376
00:42:46.340 --> 00:42:53.050
Ray Lutz: Now, when we import Csv. We do it in a very controlled, explicit manner. So it comes in as strings.

377
00:42:54.110 --> 00:43:08.590
Ray Lutz: and then we convert them. Unfortunately, pandas is optimized for tables with just numerics and simple header normal for Csv, and they don't. It's hard to work around this. You can do it, but it's just a pain in the ass to try to get it to, to do weird things.

378
00:43:10.230 --> 00:43:13.730
Ray Lutz: So what we do is it dot

379
00:43:14.000 --> 00:43:21.190
Ray Lutz: daffodil d types, which is something you can specify, and it doesn't do anything. It just gets carried around in the in the frame.

380
00:43:21.510 --> 00:43:23.669
Ray Lutz: But if you

381
00:43:23.910 --> 00:43:33.459
Ray Lutz: are importing things you can say, apply it, and then it will apply d types to the columns that you want to apply to. If the columns don't exist. It's not going to hurt it.

382
00:43:33.620 --> 00:43:35.420
Ray Lutz: You if you drop them.

383
00:43:37.130 --> 00:43:41.140
Ray Lutz: You don't want to apply d types to any columns you're not going to actually use.

384
00:43:41.410 --> 00:43:50.979
Ray Lutz: So if you bring in an array, and it's got 5,000 columns, you only need 3 of them. First, st drop everything else that you don't need, or just work on the ones that you want to work on.

385
00:43:51.120 --> 00:44:01.939
Ray Lutz: In fact, you don't need to drop them if you brought it all the way in. Just work on the columns that you want to work with, and then just ignore the rest. As soon as you start converting the thing, then you're starting to add time.

386
00:44:04.110 --> 00:44:06.869
Ray Lutz: So we have a few other features. I want to mention.

387
00:44:07.450 --> 00:44:10.200
Ray Lutz: number one. We have an indirect functionality

388
00:44:10.490 --> 00:44:15.199
Ray Lutz: where a Dick can specify the contents of specific columns. So inside of a cell

389
00:44:15.930 --> 00:44:23.250
Ray Lutz: you have a dictionary, and that dictionary actually specifies column names and values

390
00:44:23.510 --> 00:44:40.629
Ray Lutz: which are to be interpreted as part of the actual array. But it's it's got an indirection. So you 1st go into the cell, you find out what's specified there and then that's to be interpreted as the rest of the array, and this is useful for sparse arrays. As I was saying, what I was working with

391
00:44:40.760 --> 00:44:44.310
Ray Lutz: was very sparse. Away with like 5,600 columns.

392
00:44:44.740 --> 00:44:48.410
Ray Lutz: and only about 50 of them are used at any one time.

393
00:44:48.960 --> 00:44:51.849
Ray Lutz: So if you use, if you represent this as A

394
00:44:51.990 --> 00:44:55.661
Ray Lutz: as a actual Csv file or anybody like that.

395
00:44:57.050 --> 00:45:02.380
Ray Lutz: It's very, very costly, because you have all these commas right, comma comma comma comma.

396
00:45:02.530 --> 00:45:12.309
Ray Lutz: and to represent all of the 5,600 columns when you're only going to use 50, and then you have them in there, and you got to try to figure out which ones they are. It's a mess. So

397
00:45:12.850 --> 00:45:23.699
Ray Lutz: in this case, even though you want the array to be logically 5,600 columns for any one row. You don't want to have to specify more than just the 50 columns that you're working with.

398
00:45:24.380 --> 00:45:37.019
Ray Lutz: And so in that one cell, what you have is a dictionary which specifies all of the columns that you're working with, and then it is logically considered, part of the array. So if you sum the column, the rows.

399
00:45:37.340 --> 00:45:41.520
Ray Lutz: it figures out where those it takes that indirection into account.

400
00:45:41.670 --> 00:45:45.160
Ray Lutz: expands them and works with summing them that way.

401
00:45:46.600 --> 00:45:57.230
Ray Lutz: We have a from Pdf that will take a Pdf. File with a you know, header and columns and and parse it.

402
00:45:57.590 --> 00:46:06.050
Ray Lutz: usually skipping a few things. You can use a few controls there to skip things. But to just convert from basic Pdf files that you might find

403
00:46:06.692 --> 00:46:11.399
Ray Lutz: a little shortcut, you can do it yourself, but this shortcuts some work.

404
00:46:11.700 --> 00:46:19.234
Ray Lutz: It offers the adders attributes, attrs. Dictionary as part of the

405
00:46:21.550 --> 00:46:26.399
Ray Lutz: part of the class, for an instance, has this, and this is the same as in Pandas.

406
00:46:26.620 --> 00:46:35.670
Ray Lutz: You can add any day any kind of attribute you want to a data frame and

407
00:46:35.950 --> 00:46:44.030
Ray Lutz: what I find is convenient. There's is like, if I've already figured out like these are the metadata columns. They're all strings, and the rest of it is data.

408
00:46:45.090 --> 00:46:54.610
Ray Lutz: Once I parse that and I know where they are, I need to pass that along and say, these are the metadata columns. This is the number of columns that's the metadata

409
00:46:55.215 --> 00:47:00.590
Ray Lutz: and that's easy to do. You just put that into this adders, and then

410
00:47:00.810 --> 00:47:14.399
Ray Lutz: your next function says, Well, how many metadata columns are there? Oh, it's an address. I already know that now you have to know that it's in there yet, you know, but at least you don't have to pass another variable along to say here's or recalculate it even worse.

411
00:47:14.590 --> 00:47:21.159
Ray Lutz: So so that's something that turns out pandas had. And we just and using that the same way.

412
00:47:21.590 --> 00:47:27.490
Ray Lutz: And then we're now offering a join method that is efficient and mimics a join in. SQL.

413
00:47:29.430 --> 00:47:35.409
Ray Lutz: pandas doesn't have a real join, it has a merge. So when you do a merge in pandas you.

414
00:47:36.910 --> 00:47:44.299
Ray Lutz: You do this, you essentially are doing what this does here. But if when we're

415
00:47:44.440 --> 00:47:46.030
Ray Lutz: and I'll get to this in a second.

416
00:47:46.590 --> 00:47:55.179
Ray Lutz: we're extending daffodil to use SQL. In the background. And when the SQL. Machine does a join.

417
00:47:55.290 --> 00:47:59.290
Ray Lutz: it doesn't actually do anything, it actually just keeps track of the joint.

418
00:47:59.720 --> 00:48:19.770
Ray Lutz: And if you say I want to take these columns in this table, and I want to join them with these columns in this table along this key, it doesn't do anything. It just remembers that. And if you say I also want to join this table in this table, in this table and this on these keys. You could do them one at a time, and you can do up to, I think, 64 times, or maybe it's 16. But there's a certain limit.

419
00:48:19.910 --> 00:48:22.240
Ray Lutz: and then, once you have all your joints done.

420
00:48:22.720 --> 00:48:31.590
Ray Lutz: and you say I want to select these column, these rows out of my join tables. Then it does it. Then it figures it out and it pulls all the data in and does it.

421
00:48:31.980 --> 00:48:32.810
Ray Lutz: Okay.

422
00:48:32.960 --> 00:48:51.309
Ray Lutz: so it's nice that way that SQL, when it does a join, it creates a view. It doesn't actually create a it doesn't actually do anything. Now, pandas always does something. It always does a merge. It takes data from one thing, it puts it with this one and merges it together. Essentially, that's what this join does. But

423
00:48:51.470 --> 00:48:57.639
Ray Lutz: this one is, we'll be using the the SQL. Type of join when we get to that.

424
00:48:58.010 --> 00:49:00.029
Ray Lutz: So there's the plans for SQL.

425
00:49:01.270 --> 00:49:10.500
Ray Lutz: Now, right now, daffodilla rays must fit into memory at this time. So so if it doesn't fit into memory, you're going to have to chunk it

426
00:49:13.440 --> 00:49:29.729
Ray Lutz: which we do. So we have a thing where we we chunk things and there's a lot of infrastructure. I might add a daffodil that are that that chunks things. So so basically, we, we have a chunk of like a hundred things in one chunk, and we have thousands of those

427
00:49:29.980 --> 00:49:37.310
Ray Lutz: we don't actually want to combine them necessarily upfront. We combine them all at one fell swoop and then make one big file.

428
00:49:37.440 --> 00:49:39.339
Ray Lutz: or just work with the chunks.

429
00:49:40.470 --> 00:49:50.440
Ray Lutz: What we'll do here with SQL is use, and since the row-based daffodil arrays are similar to SQL. Data tables. They're also row based.

430
00:49:51.120 --> 00:49:53.339
Ray Lutz: But they have column operations. Of course.

431
00:49:53.860 --> 00:50:14.559
Ray Lutz: we'll add a quarks. We'll add additional keyword arguments in the indexing to specify whether it will be an SQL. Table or another way to say it is just you take the original daffodil.to SQL. And we'll give it a name, and then we'll get this daffodil table main underscore. SQL. Daff, we'll just call it that.

432
00:50:14.760 --> 00:50:18.009
Ray Lutz: You don't have to use this name, and that will be

433
00:50:18.800 --> 00:50:21.019
Ray Lutz: how we refer to it within python.

434
00:50:21.360 --> 00:50:25.990
Ray Lutz: And this actually will look like a daffodil table. But it's actually in SQL,

435
00:50:26.190 --> 00:50:31.890
Ray Lutz: so we don't actually have the table in daffodil. It's basically a proxy to the actual table.

436
00:50:32.610 --> 00:50:39.430
Ray Lutz: Then operations on SQL. Def. Will operate as if the table were in memory. But it actually is operating SQL. Engine.

437
00:50:39.890 --> 00:50:40.880
Ray Lutz: and

438
00:50:41.570 --> 00:50:55.309
Ray Lutz: the results is, we can allow, much larger tables while still manipulating the daffodil array paradigm with selection and indexing done in a pythonic way. So essentially, we're still going to use those square brackets, you know. The 1st one is the row.

439
00:50:55.420 --> 00:51:03.800
Ray Lutz: Well, that's like select, you know. The second one is column. So select, star. That would be kind of like the first.st The second thing, the columns that you want.

440
00:51:03.980 --> 00:51:11.139
Ray Lutz: and then you say which things you want to select in a in a SQL. Statement that would be the 1st

441
00:51:11.370 --> 00:51:15.381
Ray Lutz: parameter, and selecting it as and and the like. So

442
00:51:16.730 --> 00:51:27.859
Ray Lutz: I won't go into some of the difficulties that we found in sqlite. But sqlite does not have a row based like a vector based operation so that we can have.

443
00:51:31.860 --> 00:51:34.319
Ray Lutz: We can have python

444
00:51:34.530 --> 00:51:47.540
Ray Lutz: an apply that would take, say, a row from the table, run it through python, and return on entire row, and then add it to a new table. It doesn't provide that in SQL lite that would be an extension we'd want to see

445
00:51:47.998 --> 00:51:55.519
Ray Lutz: all they allow is Scalar returns, and then it's a lot of work to do it, so it's better to bring a chunk out of the table

446
00:51:55.850 --> 00:52:01.129
Ray Lutz: as a daffodil array. Apply it within python, and then move it back into

447
00:52:01.500 --> 00:52:05.320
Ray Lutz: the SQL. Right? That's the best way to do it right now. It's the fastest.

448
00:52:07.336 --> 00:52:10.609
Ray Lutz: So once, if you want to use

449
00:52:11.560 --> 00:52:14.560
Ray Lutz: we would also support general SQL. Queries

450
00:52:14.810 --> 00:52:20.530
Ray Lutz: and and the proxy. So if you say I want to do, I want to actually use this SQL, query.

451
00:52:21.110 --> 00:52:30.490
Ray Lutz: Then I keep doing that click can't click when I'm in this. So if you want to have an SQL. Query and apply it to this, this proxy.

452
00:52:31.860 --> 00:52:34.610
Ray Lutz: We don't know the name of the table over there, necessarily.

453
00:52:34.800 --> 00:52:38.880
Ray Lutz: And one thing about python is you.

454
00:52:39.010 --> 00:52:47.389
Ray Lutz: When you create a daffodil table. You don't know what name you're going to apply to it, because it's not the way Python works. It doesn't know what name it has. In fact, it could have many names.

455
00:52:49.910 --> 00:52:53.390
Ray Lutz: In SQL. When you have a table it has a name.

456
00:52:53.530 --> 00:52:56.559
Ray Lutz: and you have to use that name to refer to it all the time.

457
00:52:58.870 --> 00:53:05.299
Ray Lutz: so we don't. We're gonna be have to name our table with some arbitrary name, if you don't give it one.

458
00:53:05.670 --> 00:53:06.899
Ray Lutz: And then

459
00:53:07.660 --> 00:53:13.269
Ray Lutz: or we may actually always name it with arbitrary name and then map it over. But essentially.

460
00:53:14.780 --> 00:53:18.910
Ray Lutz: when you do an SQL statement.

461
00:53:19.450 --> 00:53:22.219
Ray Lutz: and you say, I want to

462
00:53:22.340 --> 00:53:25.069
Ray Lutz: like, select blah blah blah from

463
00:53:25.770 --> 00:53:27.700
Ray Lutz: you have to put in a table name.

464
00:53:27.960 --> 00:53:39.890
Ray Lutz: Okay? And you're not going to know what that name is. And so that's why we're going to have to have some substitution going on with that. And that won't be too hard for people to do if they want to use general purpose. Queries

465
00:53:42.040 --> 00:53:47.979
Ray Lutz: pretty much. Everything within pandas is repeat, is available within daffodil

466
00:53:49.160 --> 00:53:55.049
Ray Lutz: But some things that are not available in pandas are available like we can do append which has been deprecated.

467
00:53:58.270 --> 00:54:19.940
Ray Lutz: but most things run the same way. A little bit different, because pandas is normally columns of numpy arrays, and so, if you don't, and so, if you, the 1st value in the square brackets is a column by default, whereas in our mode the 1st thing by default is the row just to be aware of that

468
00:54:23.060 --> 00:54:28.340
Ray Lutz: and so pretty much they're all there. And again the timing we went over briefly at the beginning.

469
00:54:30.730 --> 00:54:38.663
Ray Lutz: Daffodil is faster for array, manipulation like appending rows. But pandas is faster. If you're going to do column based

470
00:54:39.590 --> 00:54:41.020
Ray Lutz: manipulations.

471
00:54:41.300 --> 00:54:45.950
Ray Lutz: Basically. Here was my summary about use cases, and when you want to use each one.

472
00:54:46.160 --> 00:54:50.950
Ray Lutz: if you have existing data in well-defined, column-based format, then.

473
00:54:51.820 --> 00:54:54.970
Ray Lutz: and almost all data is numeric.

474
00:54:55.760 --> 00:55:01.139
Ray Lutz: and you don't want to do appending or ponification other than maybe creating some additional columns.

475
00:55:02.210 --> 00:55:09.709
Ray Lutz: and then maybe produce plots after you analyze it, and and so forth. Then pandas might be the best choice for sure.

476
00:55:11.190 --> 00:55:13.289
Ray Lutz: as long as the data fits in memory.

477
00:55:13.980 --> 00:55:24.469
Ray Lutz: once it gets out of memory, then maybe you're going to use Daffodil, SQL. Might be a good choice. We'll have to see that hasn't really been haven't really tested that enough to know if that's going to be a better choice for you.

478
00:55:25.040 --> 00:55:30.090
Ray Lutz: If you're building data tables by analyzing converting images or other data penning to a table

479
00:55:30.250 --> 00:55:44.499
Ray Lutz: that is not going to be pandas. If you want to have small utility tables used for tracking processes or parsing data, driving state machines, all these kind of little tables you might use all the time throughout your code.

480
00:55:44.970 --> 00:55:51.520
Ray Lutz: Use daffodil tables. Don't get involved with pandas. That's for data analysis. And those specific things.

481
00:55:53.091 --> 00:55:55.550
Ray Lutz: Once you build the table.

482
00:55:55.670 --> 00:55:58.259
Ray Lutz: Then you might want to use pandas or numpy.

483
00:55:58.860 --> 00:56:07.090
Ray Lutz: We can convert individual columns, and this is pretty good way to do it. Convert it to numpy arrays so that the columns can be managed.

484
00:56:07.886 --> 00:56:13.330
Ray Lutz: There can be, you know, some, for example, like, if you sum 2 columns, you get another whole column.

485
00:56:13.760 --> 00:56:33.910
Ray Lutz: This kind of operation here will work. If it's a numpy array, or you can multiply columns, you can do all of the functions, add them together multiply by a scalar. You can all of these functions here, or say, divide one column by another one. It creates another whole column, and and that expression is very fast.

486
00:56:34.480 --> 00:56:42.450
Ray Lutz: So you can do this by just having a dictionary of numpy arrays converted on the columns that you want to use.

487
00:56:43.210 --> 00:56:55.069
Ray Lutz: If you want to do state updates like, like tracking the state of a user in a web-based application or something. Then you're going to want to use an SQL or no SQL. Or something kind of database, and not use any of these. Of course.

488
00:56:55.837 --> 00:57:03.530
Ray Lutz: Statuses that you know I've used it quite a bit myself. It hasn't really been adopted very much. That's okay. I mean, we're still

489
00:57:03.690 --> 00:57:06.800
Ray Lutz: sort of researching the best ways for this to work.

490
00:57:07.398 --> 00:57:12.489
Ray Lutz: I've used it myself. I've convert almost everything over from Pandas, and and I love it.

491
00:57:15.100 --> 00:57:22.539
Ray Lutz: and a couple of cases I still have to use. SQL. Because the tables got big. And so that's why I want to convert over to Daffodil. SQL,

492
00:57:23.301 --> 00:57:25.869
Ray Lutz: and that's pretty much what I had there.

493
00:57:26.330 --> 00:57:30.270
Ray Lutz: Okay, so I'm done. Guess

494
00:57:30.410 --> 00:57:35.550
Ray Lutz: my contact is Ray lutz@cognizys.com, or you can. That's my email.

495
00:57:37.210 --> 00:57:42.549
Ray Lutz: Any questions. I guess I I used up the whole hour a little bit more and not

496
00:57:43.430 --> 00:57:49.000
Ray Lutz: gave room for many questions. I see a chat room is okay. I'll leave.

497
00:57:49.000 --> 00:57:51.159
Gabor Szabo: I think apologies, no worries.

498
00:57:51.160 --> 00:57:51.800
Gabor Szabo: Don't do that.

499
00:57:52.590 --> 00:57:55.050
Gabor Szabo: If anyone has questions, then then please do ask.

500
00:57:55.200 --> 00:57:59.460
Gabor Szabo: I just wanted to say something. 1st of all. Thank you very much for the presentation.

501
00:57:59.750 --> 00:58:04.290
Gabor Szabo: But one thing that is sort of related.

502
00:58:04.970 --> 00:58:17.130
Gabor Szabo: that I see many people using pandas for, for I just read in Csv file and do some simple manipulation, and they always go to Pandas, because that's what they learned.

503
00:58:17.470 --> 00:58:21.289
Gabor Szabo: and they don't use the Standard Csv Library in.

504
00:58:21.805 --> 00:58:22.320
Ray Lutz: Yeah.

505
00:58:22.600 --> 00:58:33.609
Gabor Szabo: And and I had a feeling that pandas is just way too big for this. But now your your numbers show that it's way slower than than using the Standard Csv Library.

506
00:58:34.620 --> 00:58:38.569
Ray Lutz: Way slower and also just getting in and out of it.

507
00:58:39.090 --> 00:58:43.039
Ray Lutz: like, if you're if you're just staying within the Pandas world.

508
00:58:43.280 --> 00:58:46.079
Ray Lutz: and you're doing stuff that are pandas related.

509
00:58:47.080 --> 00:58:48.270
Ray Lutz: It's great.

510
00:58:48.440 --> 00:58:52.260
Ray Lutz: And and I think, though, that what we're going to find

511
00:58:52.400 --> 00:59:02.439
Ray Lutz: is that using a daffodil array and converting it to a dictionary of numpy arrays, which is kind of what's inside pandas. But pandas has grown so big

512
00:59:02.780 --> 00:59:10.259
Ray Lutz: that I've watched it load. It takes several seconds, maybe like 5, 10 seconds for it just to be imported.

513
00:59:10.600 --> 00:59:15.820
Ray Lutz: So when you're running one of these interpreters and you're using a huge library like Pandas.

514
00:59:16.550 --> 00:59:19.070
Ray Lutz: I mean the main Panda's class.

515
00:59:19.310 --> 00:59:23.379
Ray Lutz: Just one class is like 13,000 lines.

516
00:59:23.690 --> 00:59:28.290
Ray Lutz: It's a real. It's all in one file, I mean, I'm really surprised. They still write them this way.

517
00:59:28.400 --> 00:59:35.630
Ray Lutz: but it's it's a very highly functional thing. And here's the thing is that people are nowadays.

518
00:59:36.320 --> 00:59:45.059
Ray Lutz: They might be using an AI machine to assist them, and they say, You know, read this in, and and you know, do a few conversions and then put out, help me do this plot.

519
00:59:45.770 --> 00:59:52.860
Ray Lutz: The AI machines. They know perfectly well how to use pandas, and they'll do it now, for that

520
00:59:53.260 --> 00:59:59.179
Ray Lutz: efficiency is not important, really. You may wait a few extra seconds. But who cares?

521
01:00:00.353 --> 01:00:09.340
Ray Lutz: So? And Daffodil is is a little bit different animal, that actually is all python.

522
01:00:10.120 --> 01:00:15.499
Ray Lutz: and not that pandas is not, you know pandas is numpy, and

523
01:00:15.750 --> 01:00:30.809
Ray Lutz: but it's restrictive in what it can put in into its list, and it's designed around numerics. So when you start adding strings or anything else. It just freaks out. It's just like you're just going to have. Then you got to go back to a dictionary of lists, a list of dictionaries, I mean.

524
01:00:31.100 --> 01:00:36.260
Ray Lutz: and that's what I ended up doing. But then I didn't have the functionality of selecting rows and other things that you want.

525
01:00:38.170 --> 01:00:40.676
Ray Lutz: Now will this catch on? I don't know.

526
01:00:42.030 --> 01:00:46.110
Ray Lutz: I think that that it for most people

527
01:00:46.290 --> 01:00:49.019
Ray Lutz: I mean, I still like to use pandas for

528
01:00:49.170 --> 01:00:54.550
Ray Lutz: for certain things, just because I know that the AI machine knows exactly what to do with it.

529
01:00:55.293 --> 01:01:04.750
Ray Lutz: Once the AI machine understands Daffodil, it might do it, but I don't think it's really the use case. Daffodil is more for programmers than for

530
01:01:05.280 --> 01:01:07.370
Ray Lutz: people who are data analysts.

531
01:01:08.320 --> 01:01:11.200
Ray Lutz: It's more for somebody who wants to program in

532
01:01:12.350 --> 01:01:18.409
Ray Lutz: that use these, I mean, I use them all the time, because if you don't use one.

533
01:01:18.920 --> 01:01:27.129
Ray Lutz: and you're you know that it's not suitable to use pandas for this. So then you want to refer to a column of the array.

534
01:01:27.910 --> 01:01:36.059
Ray Lutz: Well, it's a list of dictionaries, so you don't have columns. You have to go through and write in a comprehension that pulls out the column. You can do that.

535
01:01:36.600 --> 01:01:41.220
Ray Lutz: but it's easier just to have something that's all well tested, and everything that pulls that column out

536
01:01:42.930 --> 01:01:47.280
Ray Lutz: makes conversions and so forth. So it's it's a handy thing to have.

537
01:01:47.590 --> 01:01:49.899
Ray Lutz: and I think it's logical to have

538
01:01:50.070 --> 01:01:52.420
Ray Lutz: a next step up. So we have

539
01:01:52.550 --> 01:01:58.670
Ray Lutz: fairly high level data structures in python, such as lists, dictionaries

540
01:01:59.010 --> 01:02:02.419
Ray Lutz: very highly functional and really nice.

541
01:02:02.920 --> 01:02:09.959
Ray Lutz: But we need to move up a level and have a two-dimensional functional data frame within the python world

542
01:02:10.220 --> 01:02:11.510
Ray Lutz: and and not

543
01:02:12.090 --> 01:02:19.120
Ray Lutz: make it numpy. Not that I'm against numpy. It's just that it's very restrictive as to what you can put into those cells.

544
01:02:20.880 --> 01:02:25.430
Ray Lutz: you can put some strings in. I think it's up to 20 characters or something. So.

545
01:02:26.550 --> 01:02:31.590
Ray Lutz: okay, all right. Well, thank you so much. I guess

546
01:02:32.030 --> 01:02:35.199
Ray Lutz: you're right. It's it's most people

547
01:02:35.570 --> 01:02:43.179
Ray Lutz: I think are going to say, well, I'm just going to continue to use python pandas, because that's what I'm used to, and

548
01:02:43.680 --> 01:02:45.039
Ray Lutz: I don't really care about

549
01:02:45.180 --> 01:02:56.389
Ray Lutz: time so much as what you're saying here, and I'm not doing appending. But if you're doing the appending, if you're building these tables up, that's when Daffodil becomes a pretty handy little tool.

550
01:02:57.490 --> 01:02:59.970
Ray Lutz: Okay, thanks a lot, Gabor. I guess that's the end.

551
01:03:00.360 --> 01:03:09.079
Gabor Szabo: Yeah. So thank you. Thank you again for for giving this presentation. Thank you. Everyone who listened to the were present and listened to the presentation.

552
01:03:09.330 --> 01:03:17.269
Gabor Szabo: If you like the video, then please like it, and follow the channel and see you next time.

553
01:03:17.810 --> 01:03:19.889
Ray Lutz: Okay, thanks. A lot. Okay. Bye.

