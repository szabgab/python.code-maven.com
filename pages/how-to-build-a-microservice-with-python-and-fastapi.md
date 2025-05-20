---
title: How to build a microservice with Python + FastAPI to switch from RDS to DynamoDB with Nikita Baryshev
timestamp: 2025-05-20T08:30:01
author: szabgab
published: true
description:
tags:
    - FastAPI
    - RDS
    - DynamoDB
---

{% youtube id="SNJJZOKBzoc" file="2025-05-05-how-to-build-a-microservice-with-python-fastapi-to-switch-from-rds-to-dynamodb.mp4" %}

![Nikita Baryshev](images/nikita-baryshev.jpeg)

[Nikita Baryshev](https://www.linkedin.com/in/nikita-baryshev/)

Nikita writes:

The microservice processed all requests between different clients and DDB. In addition to this, during the transfer period, both RDS and DDB were supported before the full switch to DDB. I can talk about the general approaches I used to build this microservice, how I worked with the legacy code, monitoring, and what was the outcome. Also, I will give a summary of all the pros and cons I faced and things that you could do better from the beginning.

I'm a full-stack developer currently working at Check Point in Tel Aviv. My stack is Angular + Python (Flask, FastApi). I'm also interested in web accessibility.



## Transcript

1
00:00:02.040 --> 00:00:31.269
Gabor Szabo: Hello, and welcome to the Codemaven Channel and code meet and meeting meet up group. My name is Gabor Sabo. I teach Python. I'll help help companies with python and trust. And I also organize these meetings, these events online, because I think it's a very useful platform to share knowledge. And I'm really happy that Nikita agreed to give this presentation. Hello, Nikita.

2
00:00:31.270 --> 00:00:32.040
Nikita Barysheva: Hi!

3
00:00:32.250 --> 00:00:33.379
Nikita Barysheva: Nice to meet you all.

4
00:00:33.380 --> 00:00:35.440
Gabor Szabo: And sorry, and

5
00:00:36.170 --> 00:01:03.490
Gabor Szabo: Those people who are present thank you for for joining the the meeting, you can freely ask questions in the in the chat. And if you're watching the video on Youtube, then please, like the video and follow the channel and join our meet up. Meet up groups, so you will be notified when we have the new meetings new events. So with that, said Nikita, it's your turn. Please introduce yourself and give your presentation.

6
00:01:04.170 --> 00:01:13.930
Nikita Barysheva: Yeah, sure, I'll start sharing my screen, and then probably I'll start exploring one second K,

7
00:01:14.770 --> 00:01:20.399
Nikita Barysheva: Hi, everyone. Once again. My name is Nikita, and I'm a software developer checkpoint company right now.

8
00:01:20.590 --> 00:01:32.040
Nikita Barysheva: And today I want to talk about one of the things I had in my previous experience when we decided to switch from Rds to Dynamodb

9
00:01:32.160 --> 00:01:45.890
Nikita Barysheva: for our users table. And how we thought about it. What was the overall architecture, and how we build a micro services that helped us to switch to make this switch.

10
00:01:46.826 --> 00:02:05.609
Nikita Barysheva: We'll cover different topics like we will talk about general differences, about our disb. And like, I will highlight some main things that might make you think why, to switch from one database to another, or will help to understand our motivation behind it.

11
00:02:05.740 --> 00:02:17.010
Nikita Barysheva: And we will go over the architecture of the micro service that we build, and I'll give you some examples over there, and we can talk about it in more details if you want.

12
00:02:17.700 --> 00:02:23.740
Nikita Barysheva: So let's have a quick overview. I'm I don't know

13
00:02:23.990 --> 00:02:42.469
Nikita Barysheva: everyone familiar with the Dynamodb or Rds. What is the differences. But the main ones, like dynamodb, is a key value like no scale database. It's fully managed by aws, and it's very good for applications with like low latency, with like flexible data models

14
00:02:42.850 --> 00:02:48.559
Nikita Barysheva: and opposite orders, is the SQL database, and we have, like a

15
00:02:48.830 --> 00:02:59.830
Nikita Barysheva: predefined schemas, and it's also managed by aws, but the difference between diamond monds that for this you really have to invest more

16
00:03:00.110 --> 00:03:13.869
Nikita Barysheva: into like knowledge into setting setting up things over there, and that for sure, if you have like complex queries and joins and etc, this is better for your solution.

17
00:03:15.296 --> 00:03:26.219
Nikita Barysheva: When you decide on like which database to use, you will probably look at several things like scalability, performance availability.

18
00:03:26.410 --> 00:03:28.730
Nikita Barysheva: And here I present some

19
00:03:29.070 --> 00:03:36.149
Nikita Barysheva: basic stuff about differences like for each of them, and dynamic being out there but overall, saying again.

20
00:03:36.160 --> 00:04:03.969
Nikita Barysheva: the for scalability. We know that dynamodity automatically scales horizontally, and that really helps to manage like a large amount of traffics without any interventions at the same time, like our desk scales vertically, and it has to increase the instance size, and this increase. It also takes time, and there might be some gaps in performance also because of that

21
00:04:03.990 --> 00:04:05.570
Nikita Barysheva: and the

22
00:04:05.760 --> 00:04:30.199
Nikita Barysheva: for performance. It really depends on the type of instance you chose the storage. Like, as I said before, you really need to know what you are doing there, and how you're setting it up, because if you won't do it like properly, you might, you might have some slowness or database won't be available. Something will be down, and users won't be happy.

23
00:04:30.250 --> 00:04:37.455
Nikita Barysheva: And as for availability, I found out we found out basically for ourself.

24
00:04:38.560 --> 00:04:46.200
Nikita Barysheva: like, say, big difference for dynamodb. And there is a thing like you that you can activate that calls global tables

25
00:04:46.390 --> 00:04:50.660
Nikita Barysheva: like, it's like a multi-region multi master, right? Database solution

26
00:04:50.790 --> 00:05:02.400
Nikita Barysheva: for this. It supports. And let's call it multi az multi availability zones. It's replicates the data across different availability zones. But in the same region.

27
00:05:03.740 --> 00:05:09.610
Nikita Barysheva: And the another thing that you will have to consider it will be interesting for you is like

28
00:05:10.090 --> 00:05:11.680
Nikita Barysheva: cost consideration.

29
00:05:13.510 --> 00:05:28.390
Nikita Barysheva: or is, let's say, dynamic price pricing and Rds cost will increase as you scale vertical, like large instances horizontally like read replicas. Also Rds also provides like on demand.

30
00:05:28.490 --> 00:05:38.600
Nikita Barysheva: but still, if you like, chose the the instance with a special like to say storage of I don't remember exactly the batches there, but

31
00:05:38.830 --> 00:05:43.869
Nikita Barysheva: let's say, 60 gigas. You will have to pay for 60 jigas. Even you use 20 of them.

32
00:05:44.190 --> 00:06:03.179
Nikita Barysheva: So efficient hybrid handling. Dynamodb is really optimized for hybrid scenarios, and it doesn't provide different replicas. Okay, it can handle millions of requests per second with the architecture that Kws provides to us. And the

33
00:06:03.480 --> 00:06:12.200
Nikita Barysheva: Pre. We want. We all want to have, let's say, predictable cost and capacity modes, and because of that.

34
00:06:12.560 --> 00:06:18.709
Nikita Barysheva: into benefit of Dynamodb, Dynamodb offers 2 modes, provisioned capacity. When you

35
00:06:18.910 --> 00:06:24.920
Nikita Barysheva: have when you set up the database. Basically, you have to say how many read and writes like.

36
00:06:26.620 --> 00:06:34.859
Nikita Barysheva: what is the bar? Let's say for them for for your database, and or you can use on demand

37
00:06:35.010 --> 00:06:53.600
Nikita Barysheva: that will automatically scale up your traffic and ensure you pay only for the usage. We had a situation when we we worked on one online store, and we had a situation that we didn't predict, because no one is about like no one's following super bowl in United States.

38
00:06:53.800 --> 00:07:00.989
Nikita Barysheva: But we did. We just lost it. And the traffic went up

39
00:07:01.790 --> 00:07:08.899
Nikita Barysheva: and the people tried to buy beer in United States order it online, and we didn't expect that. But thanks to

40
00:07:09.060 --> 00:07:16.610
Nikita Barysheva: the dynamo debit architecture like scaled up automatically and we are, we were on the pretty good side.

41
00:07:18.662 --> 00:07:22.460
Nikita Barysheva: These are very general customer reviews. Okay.

42
00:07:22.930 --> 00:07:30.140
Nikita Barysheva: hey? I just wanted to give you some examples. Don't take it like strict that you have to calculate it like this. I just wanted to

43
00:07:30.470 --> 00:07:32.630
Nikita Barysheva: have you, Nick.

44
00:07:33.130 --> 00:07:35.150
Nikita Barysheva: Basic understanding. Okay.

45
00:07:36.065 --> 00:07:41.960
Nikita Barysheva: For this, you pay, for instance, cost and for the storage.

46
00:07:42.830 --> 00:07:50.800
Nikita Barysheva: Once again the the specification could be more complicated. But we're talking about basics.

47
00:07:50.930 --> 00:07:57.739
Nikita Barysheva: And for dynamo dB, you pay for right capacity units, read capacity units, and also for data storage.

48
00:07:58.080 --> 00:08:05.850
Nikita Barysheva: But where regarding the storage, and I wanted to give you some like more detailed calculations here.

49
00:08:07.160 --> 00:08:13.440
Nikita Barysheva: If you, for example, want to store 5 gigs, 10 gigas, 20 gigs.

50
00:08:13.610 --> 00:08:21.249
Nikita Barysheva: You will pay the same price for the storage all this time, because, as I said before, you

51
00:08:21.470 --> 00:08:24.479
Nikita Barysheva: choose the storage type, and you have to pay for it.

52
00:08:24.650 --> 00:08:28.259
Nikita Barysheva: even if you pay, even if you use less.

53
00:08:28.470 --> 00:08:36.140
Nikita Barysheva: Okay? At the same time you see that for download, my dB, this thing is dynamic.

54
00:08:37.179 --> 00:08:41.329
Nikita Barysheva: and it depends on the real real story that you use.

55
00:08:41.620 --> 00:08:48.309
Nikita Barysheva: There are more things that I mentioned here. I'm not sure if you want to be overwhelmed right now let me know. But

56
00:08:48.660 --> 00:08:56.309
Nikita Barysheva: these are the very basic things that I wanted you to consider just to understand are the dynamodity.

57
00:08:56.950 --> 00:08:57.940
Nikita Barysheva: And

58
00:08:58.050 --> 00:09:11.530
Nikita Barysheva: yeah, so we talked about different like database types like SQL, Nonsql, specifically, Rds actually mentioned didn't mention it. But it considered Postgresql.

59
00:09:11.710 --> 00:09:15.120
Nikita Barysheva: if it's important and diamond.

60
00:09:15.630 --> 00:09:22.709
Nikita Barysheva: Now, I want to talk about the the actual problem that we had and the solution

61
00:09:22.890 --> 00:09:24.870
Nikita Barysheva: that we found out for ourselves.

62
00:09:28.790 --> 00:09:33.650
Nikita Barysheva: So the overall problem was that that when the

63
00:09:34.180 --> 00:09:38.829
Nikita Barysheva: the number of users, like number of requests to the database

64
00:09:38.950 --> 00:09:42.869
Nikita Barysheva: scaled like went up, we had spikes.

65
00:09:43.020 --> 00:09:59.789
Nikita Barysheva: Our our desk like didn't work well sometimes. So we decided that we need to do something more stable. And we started to consider different databases. And because we had previous experience with dynamic or another project we had.

66
00:10:00.150 --> 00:10:09.900
Nikita Barysheva: we decided that we want to build an architecture where all our clients will go to the dynamo dB,

67
00:10:10.060 --> 00:10:15.369
Nikita Barysheva: through a user's micro service. But

68
00:10:15.520 --> 00:10:22.409
Nikita Barysheva: the problem is another problem is that today all of our users are stored in Postgrescale.

69
00:10:22.960 --> 00:10:26.039
Nikita Barysheva: So how to how to manage it.

70
00:10:26.230 --> 00:10:35.769
Nikita Barysheva: 2 different databases, and like, not just physically, database. I mean different types, databases. That's kind of challenge. Okay?

71
00:10:35.930 --> 00:10:41.610
Nikita Barysheva: So these are really again.

72
00:10:42.104 --> 00:10:49.590
Nikita Barysheva: general overview of the solution. But on the left side. You see the clients. Each of them is like A,

73
00:10:49.840 --> 00:10:51.350
Nikita Barysheva: the client that

74
00:10:51.510 --> 00:10:57.339
Nikita Barysheva: it could be a back end client that wants to get data about the special and specific user.

75
00:10:57.500 --> 00:11:01.464
Nikita Barysheva: or to get all the users by some condition and

76
00:11:02.330 --> 00:11:16.599
Nikita Barysheva: how we do it. We decided to implement several feature flags, including like that, will tell us where we should read the data from or where we want now to write the data to.

77
00:11:16.870 --> 00:11:24.160
Nikita Barysheva: And basing on this feature flex. We were doing like, get requests, or we're doing like.

78
00:11:24.690 --> 00:11:33.529
Nikita Barysheva: put post to delete. We do all the separations based on this feature flags. And this is the like

79
00:11:33.770 --> 00:11:40.780
Nikita Barysheva: Postgresql architecture, nothing like special here. And this is the user service. So we have the

80
00:11:41.200 --> 00:11:47.700
Nikita Barysheva: containers here, and we use readies for caching, for caching and Dynama dB.

81
00:11:48.030 --> 00:11:54.420
Nikita Barysheva: Without additional details here. But I mean I think it could be pretty clear what we are

82
00:11:54.760 --> 00:11:59.329
Nikita Barysheva: trying to do here. Let me know if you have any questions so far.

83
00:11:59.700 --> 00:12:06.740
Nikita Barysheva: I will. I will be happy to answer them, because this scheme, if if you have question, I will be happy to answer them just

84
00:12:06.860 --> 00:12:10.370
Nikita Barysheva: for you to be and to make it more clear later.

85
00:12:12.630 --> 00:12:13.830
Nikita Barysheva: And then.

86
00:12:15.170 --> 00:12:23.570
Nikita Barysheva: except the fact that we want to transfer to Dynamodb, we need to have this transition period. So.

87
00:12:23.800 --> 00:12:27.390
Nikita Barysheva: as you saw on the previous like scheme.

88
00:12:27.660 --> 00:12:36.229
Nikita Barysheva: we decided to plan to implement the service like Api, that will handle all crowd operations related to our dynamic.

89
00:12:36.530 --> 00:12:42.040
Nikita Barysheva: And we also need to transfer all users data from Rds to Dynamodb.

90
00:12:42.160 --> 00:12:49.420
Nikita Barysheva: This was done. We wrote different scripts. We basically can grab the data from their desk.

91
00:12:49.730 --> 00:12:58.090
Nikita Barysheva: transform the data as we want. And to basically transfer this data to Dynamodb.

92
00:12:58.640 --> 00:13:02.679
Nikita Barysheva: And we also decided, as I mentioned

93
00:13:02.860 --> 00:13:11.260
Nikita Barysheva: in a previous slide. We decided that we want to have feature flags. The feature of the 1st feature flag read user from Dynamodb.

94
00:13:11.450 --> 00:13:12.520
Nikita Barysheva: If it through.

95
00:13:12.780 --> 00:13:19.020
Nikita Barysheva: we go to Dynamodb the micro service and Dynamodb. If it's false, we go directly to the Postgrescale

96
00:13:19.160 --> 00:13:24.129
Nikita Barysheva: and read user to our Ds and write write user to our Ds and to dynamodb.

97
00:13:24.330 --> 00:13:30.630
Nikita Barysheva: these are 2 flags that basically we need to support this period when we

98
00:13:31.270 --> 00:13:37.399
Nikita Barysheva: we work with both databases. So we're trying, we try to make the spirit as short as possible.

99
00:13:37.680 --> 00:13:41.950
Nikita Barysheva: to make some like tests on the Qa. On staging and then on production.

100
00:13:42.504 --> 00:13:47.880
Nikita Barysheva: We still have to work some production. But once we saw that everything works

101
00:13:48.230 --> 00:13:51.070
Nikita Barysheva: like fine. When we don't have any

102
00:13:51.200 --> 00:14:11.700
Nikita Barysheva: request from the customers, we don't have any bugs opening. So we closed right user to our desk. So the channel, let's go back for a second if I can. Yeah, basically, this channel. This path was closed. So we just continued working directly with our user service.

103
00:14:12.150 --> 00:14:23.140
Nikita Barysheva: The read from dynamo debu was always true, and the right to dynamo debut also. True, right to our death was false. So all this scheme started

104
00:14:23.290 --> 00:14:25.420
Nikita Barysheva: working only with this part.

105
00:14:25.690 --> 00:14:27.470
Nikita Barysheva: Avoid imposed risk.

106
00:14:28.655 --> 00:14:29.020
Nikita Barysheva: Okay,

107
00:14:30.780 --> 00:14:42.270
Nikita Barysheva: I wanted to show the client side architecture. The client, as I mentioned before, like every service that wants to get information about the the user

108
00:14:42.800 --> 00:14:48.340
Nikita Barysheva: and just wanted to give some code examples and to explain what we

109
00:14:48.470 --> 00:14:50.530
Nikita Barysheva: just generally try to achieve that.

110
00:14:51.320 --> 00:15:01.800
Nikita Barysheva: We wrote like a model interface, and the purpose of such interface is to be a handle for all calls

111
00:15:01.970 --> 00:15:05.099
Nikita Barysheva: to Dynamodb through the service.

112
00:15:05.370 --> 00:15:13.029
Nikita Barysheva: Okay, handle responses from service. Manage all the Retries, manage all the caching, etcetera. So be

113
00:15:13.250 --> 00:15:19.509
Nikita Barysheva: the one that gets the data for for the client from the service.

114
00:15:20.940 --> 00:15:23.820
Nikita Barysheva: It could like look like that.

115
00:15:23.950 --> 00:15:31.610
Nikita Barysheva: And one of the functions that we could use like get user by email.

116
00:15:32.030 --> 00:15:37.850
Nikita Barysheva: we initiate the user client with some parameters over here.

117
00:15:38.050 --> 00:15:50.039
Nikita Barysheva: One of the parameters that I really like to really like to mention is a requester Id. I will explain later. I can explain actually, right now, because

118
00:15:50.260 --> 00:15:51.730
Nikita Barysheva: why we need it.

119
00:15:52.010 --> 00:16:00.319
Nikita Barysheva: basically for the login and for the tracking, something fells down. I really like that, we know which client made this request.

120
00:16:00.690 --> 00:16:16.299
Nikita Barysheva: and on the left side the function itself which uses the the feature flag. The code could be optimized. Don't look at it like as a perfect one, just wanted to make it as much clear and readable on one slide as possible.

121
00:16:16.830 --> 00:16:22.635
Nikita Barysheva: So if we want to get a user by email, we looking at this feature flag. And

122
00:16:23.180 --> 00:16:27.599
Nikita Barysheva: we basically want to get to have a request to dynamodb

123
00:16:27.790 --> 00:16:40.490
Nikita Barysheva: service. This is a client link. And we want to to make the Cpi call, else we're going as we did it before we just go into Postgresql and getting that data over there.

124
00:16:43.070 --> 00:16:48.000
Nikita Barysheva: And this is the function that user from dynamodvis

125
00:16:48.250 --> 00:16:51.309
Nikita Barysheva: made it detect more specific over here.

126
00:16:51.770 --> 00:16:54.490
Nikita Barysheva: We're setting up all the parameters that we want to get.

127
00:16:54.650 --> 00:17:08.140
Nikita Barysheva: And we're making Api call to the to the route, and we are handling the the response. You can handle it wherever you want. We at that moment in time decided that we want to return

128
00:17:08.359 --> 00:17:09.180
Nikita Barysheva: to

129
00:17:09.440 --> 00:17:25.660
Nikita Barysheva: 2 values here. The 1st one is like represents the status, if it's okay or not. And the second one is the response. So we can check if it's if the request was okay or not. And this is actually the call Api function that actually makes a request

130
00:17:26.160 --> 00:17:44.499
Nikita Barysheva: to the service it has. Like some Retries, you can set up whatever you want, and once again you can make it better. If you want. Logging. You can make your request itself, and for sure, error, error handling with logins also.

131
00:17:45.580 --> 00:17:50.759
Nikita Barysheva: And if any questions so far, let me know

132
00:17:54.020 --> 00:18:01.149
Nikita Barysheva: it's this is one of the examples how a client can make a get request

133
00:18:01.460 --> 00:18:05.160
Nikita Barysheva: to to the micro service that will then

134
00:18:05.320 --> 00:18:08.100
Nikita Barysheva: make like, get a data from the dynamo. dB,

135
00:18:08.310 --> 00:18:13.170
Nikita Barysheva: so let's have a look at one of the routes micro service itself.

136
00:18:16.340 --> 00:18:20.059
Nikita Barysheva: As we know, we decided to use Dynamodb.

137
00:18:20.620 --> 00:18:25.700
Nikita Barysheva: 1st of all, you have to create this table. I just wanted to give you some

138
00:18:25.910 --> 00:18:29.100
Nikita Barysheva: quick overview what is included like.

139
00:18:29.620 --> 00:18:36.320
Nikita Barysheva: you see here some params, including, like key schema, that defines the primary key.

140
00:18:36.680 --> 00:18:40.250
Nikita Barysheva: Primary key could be also like a composite key

141
00:18:40.490 --> 00:18:45.620
Nikita Barysheva: of 2, let's say, 2 fields, and they

142
00:18:45.940 --> 00:18:52.720
Nikita Barysheva: into. This is what actually help us to get to get the data like quicker.

143
00:18:53.170 --> 00:18:58.179
Nikita Barysheva: We have different attribute definitions that describes the primary key

144
00:18:58.901 --> 00:19:07.130
Nikita Barysheva: fields. And we can also set up different global secondary indexes. One of them for me is like email index.

145
00:19:07.260 --> 00:19:14.640
Nikita Barysheva: It can that allows us to search by email also, not only by Id, but you may have different indexes. Not only one

146
00:19:17.307 --> 00:19:19.250
Nikita Barysheva: about the routes.

147
00:19:19.872 --> 00:19:31.540
Nikita Barysheva: maybe it could be obvious for many of you. But actually, I was surprised when it wasn't for some of like other developers. When I talked to them.

148
00:19:31.670 --> 00:19:41.340
Nikita Barysheva: The basic service handles all the get put post. Delete requests easily like should should do it. Okay. But

149
00:19:41.820 --> 00:19:44.709
Nikita Barysheva: things that people are really missing like

150
00:19:45.650 --> 00:19:51.849
Nikita Barysheva: what we we want to update many users at once. What we want to create create many users at once.

151
00:19:55.600 --> 00:19:56.680
Nikita Barysheva: Someone called it.

152
00:19:57.040 --> 00:20:00.379
Nikita Barysheva: So when you talk about dynamo D,

153
00:20:01.020 --> 00:20:09.059
Nikita Barysheva: and when we talk about the cost consideration, it's much like better.

154
00:20:09.190 --> 00:20:12.480
Nikita Barysheva: Let's say you want to create 100 users.

155
00:20:12.720 --> 00:20:17.130
Nikita Barysheva: You have a reason for that. Let's say you don't go in a for loop

156
00:20:17.290 --> 00:20:20.119
Nikita Barysheva: and creating like one after another.

157
00:20:20.290 --> 00:20:35.150
Nikita Barysheva: You're sending the batch of 100 users, and they basically, this batch will be divided by 2 chunks to chunks by 25 records, and it will be like already

158
00:20:35.280 --> 00:20:41.920
Nikita Barysheva: or requests it will be done to Dynamodb, so much, much less. Okay.

159
00:20:42.170 --> 00:20:43.479
Gabor Szabo: There is a question.

160
00:20:43.770 --> 00:20:44.190
Gabor Szabo: Oh.

161
00:20:44.190 --> 00:20:44.690
Nikita Barysheva: Yep.

162
00:20:44.690 --> 00:20:49.730
Gabor Szabo: How did you convert the data model from relational to No. SQL.

163
00:20:50.550 --> 00:20:57.619
Nikita Barysheva: Yeah, okay, that's good. One 3D is actually so, since we know that SQL,

164
00:20:57.730 --> 00:21:00.940
Nikita Barysheva: he's like, Hey, we have this strong structure

165
00:21:01.050 --> 00:21:09.219
Nikita Barysheva: like a fixed structure. We now we know what to expect and basically created another dictionary.

166
00:21:09.330 --> 00:21:16.340
Nikita Barysheva: Whoever of the user and transferred it like basically renew

167
00:21:17.000 --> 00:21:21.549
Nikita Barysheva: what is the the scheme of the Postgresql.

168
00:21:21.780 --> 00:21:29.169
Nikita Barysheva: we received the the users, we transform that like basic dictionary and

169
00:21:29.620 --> 00:21:35.050
Nikita Barysheva: using the post method like with the bulk, created it in Dynamodb.

170
00:21:35.610 --> 00:21:41.820
Nikita Barysheva: And that's that's it. No, no, not really, no, no magic over there. Actually.

171
00:21:43.180 --> 00:21:49.429
Nikita Barysheva: As for the daytime object, maybe this this is what may be specifically interest interesting to you.

172
00:21:50.448 --> 00:21:56.219
Nikita Barysheva: Restored date as a string, so we can convert it.

173
00:21:56.790 --> 00:22:08.040
Nikita Barysheva: You can also store it in a milliseconds. What else we had over there. So we had booleaning like sorry Boolean Boolean fields, and

174
00:22:08.680 --> 00:22:13.980
Nikita Barysheva: nothing really special that can change you

175
00:22:14.170 --> 00:22:18.829
Nikita Barysheva: just converting an object that you're getting from a Postgresql

176
00:22:19.010 --> 00:22:25.190
Nikita Barysheva: to the object that will be suitable for dynamo. dB, yeah.

177
00:22:26.010 --> 00:22:31.520
Nikita Barysheva: and that answer your question, or it can be more specific, excellent.

178
00:22:35.980 --> 00:22:41.230
Nikita Barysheva: and just don't see if it yes or no, just sharing screen.

179
00:22:41.620 --> 00:22:43.050
Gabor Szabo: Yes, he says.

180
00:22:43.800 --> 00:22:47.959
Nikita Barysheva: Okay, yeah. I see here now.

181
00:22:50.110 --> 00:22:56.679
Nikita Barysheva: Yep. So talked about obvious, not obvious things. And

182
00:22:59.590 --> 00:23:05.980
Nikita Barysheva: this is a service set up. I also tried to put many things and

183
00:23:06.270 --> 00:23:15.079
Nikita Barysheva: one screen. Can you see it? Because when I just showed it, live, people struggle to see it. I just want to.

184
00:23:15.080 --> 00:23:20.760
Gabor Szabo: If you could enlarge a little bit the whole thing that might be nice. I don't know if it's if you can do that.

185
00:23:23.290 --> 00:23:30.279
Nikita Barysheva: One second doesn't look like it allows in in this note.

186
00:23:32.750 --> 00:23:34.000
Nikita Barysheva: This doesn't help.

187
00:23:38.820 --> 00:23:48.070
Gabor Szabo: Why did you need? There's also another question. In the meantime, why did you need readies? If dynamo dynamodb has great performance on, reads.

188
00:23:49.990 --> 00:24:00.989
Nikita Barysheva: Because it's also good for saving money actually. And the radius can be can be applied in a second.

189
00:24:01.400 --> 00:24:06.300
Nikita Barysheva: It's a good one, because let's go over here.

190
00:24:14.750 --> 00:24:15.500
Nikita Barysheva: Okay.

191
00:24:15.800 --> 00:24:21.639
Nikita Barysheva: So we now saying that we are working like this, okay.

192
00:24:21.800 --> 00:24:31.819
Nikita Barysheva: we are going from client to dynamo. dB, and I mentioned Red zone here. But also I had, I think, to mention the readies on this layer.

193
00:24:32.390 --> 00:24:40.649
Nikita Barysheva: So what's happening right now is that our client makes another Api call to another service.

194
00:24:41.000 --> 00:24:44.359
Nikita Barysheva: which, like every call, let's say, cost us something.

195
00:24:44.560 --> 00:24:46.810
Nikita Barysheva: and then we go to dynamo. dB,

196
00:24:47.776 --> 00:24:56.910
Nikita Barysheva: it's radius is not only about the speed, it's also about the the money, the costs reduction.

197
00:24:57.390 --> 00:25:02.470
Nikita Barysheva: And we, for example, here at this layer.

198
00:25:02.810 --> 00:25:07.010
Nikita Barysheva: if the if the client was created like

199
00:25:07.310 --> 00:25:13.530
Nikita Barysheva: not properly, and the many requests. You don't catch the requests. You don't catch the results.

200
00:25:13.700 --> 00:25:25.129
Nikita Barysheva: This client will make another request, another request, another request request, and it can grow up dramatically, and your and you will get like a huge cost after that. After all.

201
00:25:25.240 --> 00:25:28.289
Nikita Barysheva: so red is the solution for that. Also.

202
00:25:29.710 --> 00:25:38.919
Nikita Barysheva: Using readies for caching basically allows you, 1st of all to decrease the the load of the

203
00:25:39.190 --> 00:25:45.409
Nikita Barysheva: of the service and the as a result, to decrease the the cost.

204
00:25:45.960 --> 00:25:53.560
Nikita Barysheva: So one of the reasons which not everyone think about in the beginning is like the cost cost reductions.

205
00:25:54.890 --> 00:25:58.660
Nikita Barysheva: Yep, is that okay?

206
00:26:03.800 --> 00:26:04.800
Nikita Barysheva: Trying to

207
00:26:10.780 --> 00:26:12.339
Nikita Barysheva: that answers the question.

208
00:26:15.790 --> 00:26:23.640
Gabor Szabo: I think you can just go. So used, okay, I'm just reading out. So used redis or used aws, caching services.

209
00:26:24.360 --> 00:26:26.529
Nikita Barysheva: Redis redis. We use reddish.

210
00:26:26.530 --> 00:26:27.560
Gabor Szabo: Yeah, okay.

211
00:26:27.560 --> 00:26:34.379
Nikita Barysheva: Because we, we use it widely in all projects. And we can. Yeah, we are used to Redis.

212
00:26:41.870 --> 00:26:44.940
Gabor Szabo: I think we can. You can go back to the code example of.

213
00:26:50.400 --> 00:26:58.774
Nikita Barysheva: Okay, the basically the 1st things that you will need for for the service.

214
00:26:59.670 --> 00:27:01.669
Nikita Barysheva: It's like the the setup is.

215
00:27:01.820 --> 00:27:05.519
Nikita Barysheva: It's pretty easy. First, st where is dynamed again hydantic.

216
00:27:06.150 --> 00:27:10.750
Nikita Barysheva: even though we said that the dynamon dB. Is like a

217
00:27:11.340 --> 00:27:14.620
Nikita Barysheva: we don't have to follow this strict schema.

218
00:27:15.040 --> 00:27:17.980
Nikita Barysheva: It's a very good practice to have one, I mean

219
00:27:18.130 --> 00:27:28.449
Nikita Barysheva: in dynamic D. When you create a record with a field like none, it won't be added, so we won't find it. If you go to the Ui, you you won't have it. But when you

220
00:27:28.820 --> 00:27:33.899
Nikita Barysheva: getting the data when you return the data, it's very good to have the

221
00:27:34.400 --> 00:27:41.840
Nikita Barysheva: and the model that you can use to serialize what you receive from dynamic, from the database. This will help.

222
00:27:42.300 --> 00:27:47.980
Nikita Barysheva: like the client, to know what to expect and

223
00:27:49.110 --> 00:27:54.539
Nikita Barysheva: ex avoid some unpredictable scenarios. So

224
00:27:54.670 --> 00:27:58.719
Nikita Barysheva: the model is always good, even if you work with a

225
00:27:58.860 --> 00:28:02.199
Nikita Barysheva: dynamodity for the key value database

226
00:28:02.560 --> 00:28:08.259
Nikita Barysheva: you have, you see here, like like one of the examples of how you can model data.

227
00:28:08.590 --> 00:28:16.620
Nikita Barysheva: And if there is a function that said user cache that sets a specific key value

228
00:28:16.900 --> 00:28:21.400
Nikita Barysheva: into the into the readies with the like expiration time.

229
00:28:21.560 --> 00:28:35.010
Nikita Barysheva: And so you can find the and set exception log error, that every time that something falls down. You will see it later. We just throw a properly log. Sorry I need to move the bar.

230
00:28:36.690 --> 00:28:41.280
Nikita Barysheva: Yeah, that will give you some details.

231
00:28:42.850 --> 00:28:49.040
Nikita Barysheva: I don't know why, but I also saw a lot a lot of examples of people trying to avoid it in logs.

232
00:28:49.220 --> 00:29:04.850
Nikita Barysheva: Oh, forgetting any logs like, I think it's a must you have to to show. Like to have it written somewhere. What was the error? And what I mentioned before is like, requested Id.

233
00:29:04.950 --> 00:29:19.059
Nikita Barysheva: It's very important if you have many, many services or clients that work with the users database, and that everything goes through the service like a main point. All these cloud iterations you need to know

234
00:29:19.410 --> 00:29:28.760
Nikita Barysheva: made the request. When it's very good for analytics, you can use it for graph later on. You can use it to debug things

235
00:29:29.780 --> 00:29:34.309
Nikita Barysheva: only only positive things from the logs that I see.

236
00:29:34.890 --> 00:29:40.377
Nikita Barysheva: and also for sure it can increase the costs for some reason, for some reason. But

237
00:29:41.080 --> 00:29:43.910
Nikita Barysheva: still have to find a balance.

238
00:29:46.030 --> 00:29:48.930
Nikita Barysheva: Second, yep.

239
00:29:49.290 --> 00:30:12.569
Nikita Barysheva: this is one of the simple examples how you can get the user, and you can get it by Id, by email, you can specify which fields to project. It's like select in the postgres. Clearly, when you do select email like 1st name, last name the same, and it will return you on the the skills, the same you can do in dynamodity

240
00:30:13.270 --> 00:30:17.819
Nikita Barysheva: and basically calls projection attributes.

241
00:30:18.010 --> 00:30:26.010
Nikita Barysheva: Also, you're checking. We're checking. If there are Id, or if there is Id or email provided.

242
00:30:26.480 --> 00:30:28.410
Nikita Barysheva: because it's a very logical thing.

243
00:30:28.580 --> 00:30:34.219
Nikita Barysheva: if nothing of this is provided you don't look for for the user.

244
00:30:34.380 --> 00:30:41.199
Nikita Barysheva: Only if you don't have maybe a route that can do a conditional

245
00:30:41.747 --> 00:30:49.370
Nikita Barysheva: conditional search. But here I decided to show, like the basic one but conditional. I mean, for example.

246
00:30:49.570 --> 00:30:55.500
Nikita Barysheva: and in SQL, when you look for the user, which who's a

247
00:30:55.660 --> 00:30:59.459
Nikita Barysheva: with the name Nikita, all the users with the name Nikita.

248
00:30:59.660 --> 00:31:01.950
Nikita Barysheva: So you don't have Id or email.

249
00:31:02.150 --> 00:31:07.829
Nikita Barysheva: But anyway, you can do it. The same thing over here just didn't include it over here.

250
00:31:12.668 --> 00:31:18.590
Nikita Barysheva: This is the actual process. So before going to Dynamodb.

251
00:31:18.790 --> 00:31:20.669
Nikita Barysheva: we are checking the ready sketch.

252
00:31:20.790 --> 00:31:27.560
Nikita Barysheva: So we're checking the the cash, and if there is nothing in cash, so we proceed to actual

253
00:31:28.228 --> 00:31:30.920
Nikita Barysheva: look up at the table.

254
00:31:31.400 --> 00:31:33.129
Nikita Barysheva: So here is like

255
00:31:33.270 --> 00:31:42.380
Nikita Barysheva: users. Table is like a let's say, an agent to initiate before initiated. Before that knows the function. Get item.

256
00:31:42.770 --> 00:31:45.170
Nikita Barysheva: good item by by key.

257
00:31:45.310 --> 00:31:53.150
Nikita Barysheva: and if we provide the projection attributes, and we provide and we say that please return us some specific fields.

258
00:31:53.320 --> 00:31:59.249
Nikita Barysheva: or we search by email. Once again, you can optimize this code as you wish. But

259
00:32:00.060 --> 00:32:08.269
Nikita Barysheva: again, this is just, for example. And then in the end of the day after we found out the user. If you found out the user, we cache it

260
00:32:12.675 --> 00:32:16.210
Nikita Barysheva: in this specific example. I wanted to

261
00:32:17.120 --> 00:32:23.600
Nikita Barysheva: to mention that we we potentially may have 3 types of successful response over here.

262
00:32:25.440 --> 00:32:39.880
Nikita Barysheva: we may be in the situation. We may end up in a situation when we didn't find the any users according to condition that we were like, according to Id, that was provided or email. And we return that like empty object here.

263
00:32:40.270 --> 00:32:58.629
Nikita Barysheva: or if we provide a projection attribute, we return the data as we received it from the Dynamodb. Or if we did find the user and didn't provide any projection attributes. Here. We want to serialize it. We, as I said, we have a model.

264
00:32:58.750 --> 00:33:01.120
Nikita Barysheva: and we want to serialize the user

265
00:33:01.310 --> 00:33:11.326
Nikita Barysheva: all the day. All the fields that we have inside the user will be patched as they are like a key in its value, and those that are not will get like

266
00:33:12.490 --> 00:33:18.410
Nikita Barysheva: we'll get a default values. Normally you put them as none, because

267
00:33:18.750 --> 00:33:24.750
Nikita Barysheva: there is nothing. There is no reason to put a something not relevant

268
00:33:25.500 --> 00:33:28.119
Nikita Barysheva: depends depends on the business thing. But yeah.

269
00:33:30.190 --> 00:33:34.359
Nikita Barysheva: And another thing that might be

270
00:33:34.780 --> 00:33:38.750
Nikita Barysheva: that might be, that is also important. It's just like error handling.

271
00:33:39.500 --> 00:33:47.180
Nikita Barysheva: We have different types of error handling. Please don't forget about it, please use it, and even though it may look like overwhelmed.

272
00:33:47.320 --> 00:33:53.660
Nikita Barysheva: I find it sometimes much better to have it rather than avoiding it. And after that

273
00:33:53.850 --> 00:34:02.910
Nikita Barysheva: something is crashing, and everyone like trying to understand what was the situation. You can handle it everything, with a general exception. But it.

274
00:34:04.130 --> 00:34:09.680
Nikita Barysheva: if you are provided with the with the tools, why not use it? My idea

275
00:34:13.100 --> 00:34:18.300
Nikita Barysheva: just wanted to sum up the service it's like

276
00:34:18.480 --> 00:34:28.170
Nikita Barysheva: intended for, and there are 2 things that you see here that I didn't mention up. But they're very important for the services like that.

277
00:34:28.550 --> 00:34:40.309
Nikita Barysheva: So the service idea is like handling dynamodity requests. Like all crowd operations, it also should be able to cache things

278
00:34:40.730 --> 00:34:43.080
Nikita Barysheva: to avoid like if

279
00:34:43.239 --> 00:34:50.190
Nikita Barysheva: if the query already like, if the request already got to the service by some reason, but

280
00:34:50.460 --> 00:34:57.029
Nikita Barysheva: you have the cached values. Still, even the service got the request. There is no reason to

281
00:34:57.250 --> 00:34:59.759
Nikita Barysheva: to bother Dynamodb, because it's

282
00:34:59.940 --> 00:35:07.190
Nikita Barysheva: after all, it's another. It's another like cent. It doesn't sound like another dollar. Let's call it so.

283
00:35:07.360 --> 00:35:18.809
Nikita Barysheva: But if you think about the very big scale, like when you have millions, tens of millions of users, if something won't be covered, it could cost you a lot, so

284
00:35:19.310 --> 00:35:23.910
Nikita Barysheva: I would prefer using caching and

285
00:35:24.760 --> 00:35:27.969
Nikita Barysheva: rather than avoiding using it. And

286
00:35:28.400 --> 00:35:30.560
Nikita Barysheva: to save some money over here

287
00:35:31.805 --> 00:35:37.329
Nikita Barysheva: we need to have a proper error error handler. That's why I mentioned 4 of them.

288
00:35:37.730 --> 00:35:42.989
Nikita Barysheva: and maybe someone won't like it. But I did it, and the 2 things that I didn't mention here is like

289
00:35:43.410 --> 00:35:47.720
Nikita Barysheva: you need to have throttling mechanism and rate limiter. Actually.

290
00:35:48.970 --> 00:35:53.220
Nikita Barysheva: it depends, I mean, it could be done on the

291
00:35:53.900 --> 00:36:02.979
Nikita Barysheva: should be done also on the service side, because, like services like what? Let's say, it's standalone thing. But you also may think about like

292
00:36:03.150 --> 00:36:05.360
Nikita Barysheva: trotting on the clients. So I mean

293
00:36:06.180 --> 00:36:16.179
Nikita Barysheva: throttling for sure and rate limiter is one, since we're talking about the service already is 2 things are very important to have in your services like that.

294
00:36:16.340 --> 00:36:18.929
Nikita Barysheva: So don't forget to cover it.

295
00:36:19.090 --> 00:36:25.790
Nikita Barysheva: And then I think that's actually cute.

296
00:36:25.990 --> 00:36:26.790
Nikita Barysheva: Hey?

297
00:36:27.190 --> 00:36:29.089
Nikita Barysheva: Yeah, let's it.

298
00:36:29.270 --> 00:36:32.549
Nikita Barysheva: And I think you did it faster, you know

299
00:36:33.410 --> 00:36:39.910
Nikita Barysheva: if you have any questions, just let me know. I would be happy to answer them again, if not.

300
00:36:40.100 --> 00:36:44.509
Nikita Barysheva: thanks for listening. I hope it was interesting to you, and

301
00:36:44.830 --> 00:36:47.499
Nikita Barysheva: we'll give you some ideas, maybe, or

302
00:36:47.940 --> 00:36:50.580
Nikita Barysheva: you will decide to do something similar to this.

303
00:36:52.160 --> 00:36:53.080
Nikita Barysheva: Just let me know.

304
00:36:54.640 --> 00:36:55.580
Gabor Szabo: Well.

305
00:36:55.890 --> 00:37:05.981
Gabor Szabo: thank thank you for the presentation. Any. If anyone has any more questions. That would be a good idea to ask now. If not, then.

306
00:37:08.180 --> 00:37:16.060
Gabor Szabo: thank you very much for for giving this presentation and for being here, and for the those who were watching it live.

307
00:37:16.190 --> 00:37:23.169
Gabor Szabo: Now you have the chance. So I'm telling it also to the viewers on Youtube Channel that those people who are here

308
00:37:23.820 --> 00:37:33.870
Gabor Szabo: in the live meeting they can stay on, and after we stop the recording we can open the the mics, and then we can have a conversation

309
00:37:33.990 --> 00:37:51.040
Gabor Szabo: asking all kind of other questions that you might have not wanted to do with be on the on the video. So anyway, thank you for being here. Thank you for watching, and don't forget to like the video and follow the channel and see you next time in the next, and and

310
00:37:51.220 --> 00:37:55.589
Gabor Szabo: join the Meetup group. If if you're not there yet and thank you.

311
00:37:56.960 --> 00:37:58.029
Nikita Barysheva: Thank you. Everyone.

