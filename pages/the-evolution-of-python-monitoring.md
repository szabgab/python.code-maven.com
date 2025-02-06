---
title: The Evolution of Python Monitoring with May Walter
timestamp: 2025-02-06T08:30:01
author: szabgab
published: true
description:
---

In this lecture, we will explore the evolution of Python monitoring over the years, covering tools and techniques from sys.monitoring to import hooks, highlighting advancements and best practices in keeping your Python code in check.

Join us and time-travel across the evolution of Python monitoring mechanisms. We'll delve into history from dedicated tools like sys.monitoring to more advanced techniques such as ceval and import hooks. This session will provide a comprehensive overview of how monitoring practices have developed over the years, offering insights into the best practices for maintaining and debugging your Python code and the pros and cons of each approach. Whether you're a seasoned developer or new to Python, you'll gain valuable knowledge on how to keep your code running smoothly and efficiently without hurting performance or your dev velocity with tedious maintenance.

![May Walter](images/may-walter.jpeg)

{% youtube id="XIqoYYWaWFI" file="2025-02-05-the-evolution-of-python-monitoring.mp4" %}


## Transcript

1
00:00:00.720 --> 00:00:02.690
Haki Benita: This meeting is being recorded.

2
00:00:03.400 --> 00:00:04.320
Gabor Szabo: Okay.

3
00:00:05.800 --> 00:00:12.250
Gabor Szabo: yeah. So Hi, and welcome to the python Maven, let's call it Python Maven. This is the code Maven

4
00:00:12.500 --> 00:00:41.910
Gabor Szabo: Youtube channel. And we are organizing these meetings in the Codebay Events group, but sort of it has 3 separate sessions, and this is going to be the the Python specific one. My name is Gabor Sabo. I usually teach python and rust and help companies introduce testing, and I also like to organize these events and allow people to share their knowledge with with each other.

5
00:00:42.270 --> 00:00:46.010
Gabor Szabo: You're welcome. I'm really happy that you're here

6
00:00:46.140 --> 00:01:04.909
Gabor Szabo: in this session, listening, as I mentioned earlier, you're welcome to to comment or use the chat and ask questions. And if you're just watching the video recorded on Youtube, then please remember to like the video and follow the channel.

7
00:01:05.080 --> 00:01:11.990
Gabor Szabo: and let's welcome hockey now, and let him introduce you. Introduce yourself and and

8
00:01:12.700 --> 00:01:17.579
Gabor Szabo: and give the presentation. So thank you for accepting the invitation.

9
00:01:18.970 --> 00:01:31.149
Haki Benita: Thank you. Thank you, Gabo. 1st of all, I like the fact that we have this intimate group that we can freely talk. I actually encourage you to consider opening the mics.

10
00:01:31.210 --> 00:02:01.090
Haki Benita: Because I think we can actually have a conversation throughout the presentation. I like to give interactive presentation. Your call. You're the boss, and just a quick introduction about the subject and about myself. So we are going to talk about how to make your back end war. And I want to start by apologizing for the tacky headline. But unfortunately, these types of tacky headlines do work. Believe it or not.

11
00:02:01.610 --> 00:02:09.010
Haki Benita: So. My name is Jake Benita. I'm a software developer and a technical lead. I'm currently leading a team

12
00:02:09.289 --> 00:02:18.949
Haki Benita: of developers working on a very large ticketing platform and Israel serving about one and a half unique

13
00:02:19.580 --> 00:02:32.470
Haki Benita: 1.5 million unique paying users every month. And I also like to write and talk about python performance and databases. And you can find my stuff on my website.

14
00:02:33.110 --> 00:02:47.839
Haki Benita: So today, we are going to talk about some lesser known features of indexes. And we're going to try and understand how they work and when we can and should use them

15
00:02:47.850 --> 00:03:14.629
Haki Benita: to do that, we are going to build a URL shortener together, and we're going to do it in Django. I would say that since this is a talk about python, I'm going to use Django and the Django Orm. But the concepts that I'm going to describe are not specific to Django, and they're not specific to Postgres. Heck. They're not even specific to python. But this is a good environment to explain the concepts with.

16
00:03:15.390 --> 00:03:19.889
Haki Benita: So what is a URL shortener? You probably know about

17
00:03:19.900 --> 00:03:39.330
Haki Benita: other types of URL shorteners? You have bitly. You have the late googl buffer, Li, and so on. Basically, URL shortener is a system that provides a short URL that redirects to a longer URL. Now, why would you want to do that

18
00:03:39.330 --> 00:04:02.240
Haki Benita: first.st If you are operating in text constrained environments like SMS messages or Tweets, you might want to share a very large link. So you want to make it shorter, so it consumes less space. This is where short Urls can be handy. Another nice feature of URL shortening that whenever someone clicks the short URL,

19
00:04:02.240 --> 00:04:16.500
Haki Benita: the URL shorten and redirects to the long URL, and keeps a track of how many people click that link. So if you have something like a campaign that you want to launch, and you want to keep track of how many people clicked your link.

20
00:04:16.820 --> 00:04:20.149
Haki Benita: This is what you would use a URL shortener for

21
00:04:20.310 --> 00:04:48.240
Haki Benita: so to build our URL shortener in Django, we're going to start with this very, very simple model. We are calling the model short URL, we have an Id column which is the primary key. It's just an auto incrementing integer field. We have the key. That's a unique short piece of text that uniquely identifies our short URL. This is the short key at the end of the short URL.

22
00:04:48.500 --> 00:05:07.030
Haki Benita: We then have the URL, which is the long URL, we want to redirect to. We also want to keep track of when the URL was created. We do that using the created at column. And finally, we want to keep track of how many users click the link, and we do that with the hits column

23
00:05:07.180 --> 00:05:08.110
Haki Benita: at the bottom.

24
00:05:08.960 --> 00:05:19.650
Haki Benita: So for our demonstration. So we actually have something to work with. I loaded 1 million short Urls into the table. Okay, now, this is not a lot. But we are going to see, some

25
00:05:20.700 --> 00:05:25.929
Haki Benita: performance gains with just 1 million rows. Okay.

26
00:05:26.810 --> 00:05:33.380
Haki Benita: so this talk is about python. But it's essentially about SQL, so

27
00:05:33.510 --> 00:05:54.859
Haki Benita: in Django, if you want to get the SQL. Generated by Django for a given query set. You can do that by accessing the query, set dot query and print it. In this case I'm doing short URL filter on a specific key dot query. And I can actually get Django to print

28
00:05:55.190 --> 00:05:59.549
Haki Benita: the SQL. That it generated for this query set right.

29
00:06:00.040 --> 00:06:26.740
Haki Benita: So, after viewing the query set, it's also very interesting to see how the database is planning to execute my query. Right? So I can do that by executing the function. Explain. This, translates into an explain query, command in SQL. And what I get in return is not the results of the query, but the execution plan, which is how the database is planning

30
00:06:26.930 --> 00:06:30.979
Haki Benita: to execute my query. Now, when we just use, explain

31
00:06:31.200 --> 00:06:36.260
Haki Benita: the database doesn't actually execute the query. It just produces a plan

32
00:06:36.370 --> 00:06:53.839
Haki Benita: sometimes, especially when we're benchmarking and we're trying to improve performance. It can be useful to produce the execution plan, but also have the database, execute this query and return some useful execution data. For that we can use a slightly different variation of the explain command.

33
00:06:53.970 --> 00:07:13.319
Haki Benita: which is, explain, analyze in Django. You can do that by using. Explain, analyze. True in SQL. Postgres. Specifically, you can do explain, analyze on timing on in parenthesis, following by the query, and then you get some additional information about the execution plan.

34
00:07:13.350 --> 00:07:27.339
Haki Benita: first, st because the database actually executed the query. You can see at the bottom that we get how long it took the database to produce an execution plan in this case that would be 0 point 1 4 0 ms.

35
00:07:27.710 --> 00:07:38.510
Haki Benita: and I also get how long. It took the database to execute the query from start to end. In this case that would be 0 point 0 4 6. Okay.

36
00:07:39.430 --> 00:07:47.120
Haki Benita: Now, in addition to the timing. I'm also getting a very, very interesting piece of information inside the execution plan.

37
00:07:47.260 --> 00:07:53.699
Haki Benita: Okay, what I get is the estimated cost and the actual cost

38
00:07:53.820 --> 00:07:58.059
Haki Benita: that the database encountered while executing the query. So

39
00:07:59.010 --> 00:08:15.400
Haki Benita: discussing the cost-based optimizer is slightly outside the scope of this talk, I would just say that, comparing the expected cost to the actual cost is a very useful measure to try and identify bad execution plans.

40
00:08:16.100 --> 00:08:17.350
Haki Benita: Finally.

41
00:08:17.990 --> 00:08:28.419
Haki Benita: another way of viewing queries is to turn on the logger for the database backend in Django. This way, whenever the database, whenever Django executes a query.

42
00:08:29.040 --> 00:08:32.620
Haki Benita: it logs the SQL. That was produced by the aura.

43
00:08:33.510 --> 00:08:34.475
Haki Benita: So

44
00:08:35.700 --> 00:09:05.329
Haki Benita: to actually start discussing some indexing techniques, we need to start implementing some. You know, business processes. So let's start with the most basic thing that URL shortener actually does. And that's look up the URL to redirect to by a key. So a user uses one of our short Urls, we get the unique key. And we need to find the long URL to redirect to. Okay, this is like the bread and butter of this system.

45
00:09:05.440 --> 00:09:27.109
Haki Benita: So if we want to implement this very, very simple function. We can do something like that. Def resolve. Okay, that's the name of the function. We want to resolve a key to a URL. We accept a key, and then we execute this simple query to just get a show, URL for this key. If we don't find anything we return none. Otherwise we return the URL to redirect to

46
00:09:27.110 --> 00:09:37.730
Haki Benita: okay. Now we want to look at the SQL. That Django generated for this function. Right? So we execute this function on some random key

47
00:09:37.950 --> 00:09:57.950
Haki Benita: with SQL. Logging turned on, and we can see the query right here. Now, if you look at this query, it looks like Django, basically fetch everything from the short URL table for the key that we asked for right select star from short URL, where Key equals something.

48
00:09:58.270 --> 00:10:05.050
Haki Benita: If we want to look at how postgres is actually executing this query.

49
00:10:05.210 --> 00:10:12.719
Haki Benita: we can use the explain command. And what we get is that Postgres is planning to use an index scan

50
00:10:13.535 --> 00:10:20.159
Haki Benita: on the index we have on the key column. Okay, now.

51
00:10:21.180 --> 00:10:28.839
Haki Benita: to understand what exactly it means in index scan. Let's take a second to talk about btree index.

52
00:10:29.040 --> 00:10:42.120
Haki Benita: So Btree index is like the king of all indexes. This is the default index in most database engines. If you're not sure what type of index you're using. You're probably using a btree index. Okay?

53
00:10:42.560 --> 00:11:11.160
Haki Benita: So to understand how A B tree index works. Let's start by building one. So imagine you have these values, one through 9, and you want to create a B tree index on them. You start by sorting the values and storing them in leaf blocks. You can see the leaf blocks at the bottom. They are sorted from left to right. We have 1, 2, 3, all the way through 9. Now every entry in the leaf blocks contains a list of tids. These are pointers to rows in the table.

54
00:11:11.400 --> 00:11:15.460
Haki Benita: That store rows with these values. Okay.

55
00:11:16.290 --> 00:11:28.179
Haki Benita: now, above the leaves, we have branches and root block that acts as a directory to these leaf blocks. So let's see how this works. Let's imagine that we want to look.

56
00:11:28.180 --> 00:11:38.290
Gabor Szabo: Sorry. Just someone says says that it doesn't see this the slides. So I just wanted to. And I'm unsure if the other people do see the light slide. So if

57
00:11:38.670 --> 00:11:53.529
Gabor Szabo: I asked it in the chat, but no one answered. So I hope that people other people okay. So some other people see it so my recommendation is to Eduard Eduardo to turn, maybe on and off the I mean, maybe exit zoom and enter zoom again. Sorry for the.

58
00:11:53.530 --> 00:11:54.940
Haki Benita: Okay, no problem.

59
00:11:55.120 --> 00:11:56.160
Haki Benita: Yeah.

60
00:11:56.400 --> 00:11:59.700
Haki Benita: Okay, okay, so let's

61
00:12:01.690 --> 00:12:31.100
Haki Benita: okay. So let's try to search for the value 5 in the V 3 index that we just built. So we start with the root block and we start scanning from left to right. So 5 is larger than 3. So we skip the 1st entry 3 is between 3 and 7, 5 is between 3 and 7, so we follow this pointer to the middle leaf block. We then start scanning the leaf block from left to right. The 1st value is 4. It's not a match.

62
00:12:31.100 --> 00:12:36.150
Haki Benita: The next value is 5. That's a match, and now we can

63
00:12:36.150 --> 00:12:47.970
Haki Benita: scan. We can follow the pointers from this leaf block to the rows in the table. We can read the rows and do whatever we need to do with these rows. Okay, now.

64
00:12:48.310 --> 00:13:15.100
Haki Benita: let's go back to our query. Okay, one second, yeah. Let's go back to our query. Remember that we said that Django generated this query and this query is fetching everything right, basically select star from short URL. But, in fact, if you think about it, we don't actually care about all these fields right? We only care about the URL. I mean, we're not looking to resolve

65
00:13:16.290 --> 00:13:27.129
Haki Benita: a key to a URL for the purpose of redirecting. I don't care when it was created. I don't care about the Id. I already have the key right, and I don't care about the head counter at this point

66
00:13:27.610 --> 00:13:30.209
Haki Benita: right? So I don't care about all these fields. So

67
00:13:30.770 --> 00:13:55.089
Haki Benita: one thing that we can do is instead of fetching all of these fields, how about if we just fetch what we actually need. Right? So in Django, we can do that by adding values list. URL. Now the function is slightly different. But if we look at the SQL. Generated by this function, we can see that now, instead of fetching all the columns in the row, we just fetch the URL. So this is exactly what we need.

68
00:13:55.200 --> 00:14:10.249
Haki Benita: If we look at this execution plan once again for this query, we can see that again. Django is using postgres is using an index scan on the unique index that we have on the key. Right? So now.

69
00:14:10.920 --> 00:14:30.719
Haki Benita: once we found a matching row, we can follow the pointer to the table. We can get the URL from the table. So if you imagine the amount of disk reads, I need to do to satisfy this query. I'm starting by reading their root block. Right? So that's 1 read. Then I need to follow the branch all the way to the leaf. Let's say that we have just.

70
00:14:30.730 --> 00:14:41.789
Haki Benita: you know, root block, and then directly to the leaf. So reading the leaf is another read, and then we need to follow the link from the leaf block to read the row from the table. So this is a unique

71
00:14:41.970 --> 00:14:52.020
Haki Benita: column. So we have at most one row. So that's another read. So basically, we did 3 random reads to satisfy this query right now.

72
00:14:53.290 --> 00:15:03.019
Haki Benita: this query is executed a lot. This is basically what our system is doing right. It's getting keys and resolving them to Urls to redirect right

73
00:15:03.360 --> 00:15:17.979
Haki Benita: now. We already established that all we care about in this specific scenario is just the URL. I don't care about anything else. I care just about the URL. So what if? And stay with me? This is mind blowing.

74
00:15:17.980 --> 00:15:34.249
Haki Benita: What if, instead of going to the table to get the URL. What if I could include the URL in the leaf block in the index this way? When I found a matching entry in the leaf block, I would have the URL just sitting there.

75
00:15:34.310 --> 00:15:52.420
Haki Benita: Right? So this mind-blowing idea is called inclusive index. Okay, in other databases it's called covering index or inclusive indexes, and what it allows us to do, it allows us to store additional information in the leaf block.

76
00:15:52.500 --> 00:16:14.569
Haki Benita: So if we want to use an inclusive index in Django, we can add the include argument to the unique constraint. Now look, the key is indexed. The URL is not indexed. It's just included in the leaf block. Okay. Now, if we generate a migration, we apply it and we try the query again.

77
00:16:15.500 --> 00:16:21.569
Haki Benita: You can see that once again, Postgres is using our index, our unique index on the key. But there is

78
00:16:21.900 --> 00:16:33.889
Haki Benita: very, very subtle difference here. If you notice. Previously we had an index scan using our unique index. This time we have an index only scan.

79
00:16:34.020 --> 00:17:03.620
Haki Benita: This means that Postgres was able to satisfy the query without accessing the table. All the data that it needs was already in the leaf block. So if we once again imagine how many reads we need to do to satisfy this query, using the inclusive index, we read the root block. We follow the pointer all the way down to the leaf block, and now, instead of going to the table to read the URL. We have the URL right there in the leaf block. So we only need to read

80
00:17:03.670 --> 00:17:05.849
Haki Benita: 2 blocks from disk.

81
00:17:06.150 --> 00:17:17.110
Haki Benita: Okay, the way to identify. This is by the operator on the index only scan right? So we have an index scan, and we have an index. Only scan.

82
00:17:18.170 --> 00:17:39.170
Haki Benita: So quick recap about inclusive indexes, as I mentioned in other databases. They are sometimes called covering indexes, and they allow us to fulfill queries without accessing the table. However, you should use them with caution. Because if you think about it, we're basically duplicating data from the table to the index. Okay?

83
00:17:39.170 --> 00:17:49.959
Haki Benita: So if you have a very big big piece of like information like URL can be very, very big. So basically, I'm now storing the URL

84
00:17:50.140 --> 00:18:09.440
Haki Benita: twice. So the index could get very, very big. I'm actually not a big fan of inclusive indexes. But I can think of 2 scenarios where it might be a good idea. First, st if you have very wide tables. Imagine, like data, warehouse type of tables, denormalized tables.

85
00:18:09.600 --> 00:18:11.520
Haki Benita: and you have a very

86
00:18:12.250 --> 00:18:22.290
Haki Benita: predefined set of queries that are executed very, very often on a very, very small subset of columns, you can consider doing using

87
00:18:23.440 --> 00:18:50.249
Haki Benita: an inclusive index. And also, I personally found that non unique composite indexes can be good candidates for inclusive indexes that is, indexes on multiple columns that are not used to enforce a unique constraint. Sometimes they can benefit from switching to just a composite index to an inclusive index. Okay, questions so far before we move on to the next use case.

88
00:18:55.710 --> 00:19:02.210
Haki Benita: Okay, if you have any questions, feel free, let's move on to the next to the next use case.

89
00:19:02.800 --> 00:19:04.080
Haki Benita: So now

90
00:19:04.230 --> 00:19:16.229
Haki Benita: we want to find unused keys right? We have this business question. We want to know how many show through ours. We have with no hits at all. Okay, we have 0 hits.

91
00:19:17.070 --> 00:19:23.050
Haki Benita: So we start by implementing this very, very simple function. We call it, find unusedindexes.

92
00:19:23.350 --> 00:19:26.190
Haki Benita: and it returns a query set where

93
00:19:26.790 --> 00:19:43.480
Haki Benita: with short Urls, where hits equals 0. Once again, if we want to see what the query looks like we can print the result of query. We can see that it returns like star from short URL, where hits equals 0.

94
00:19:44.560 --> 00:19:58.929
Haki Benita: Once again, through the process, we produce an execution plan. This time. We can see that Postgres is doing a sequential scan on short URL. A sequential scan is basically a full table. Scan postgres is just

95
00:19:59.010 --> 00:20:18.369
Haki Benita: reading the table row by row, looking for rows where hits equals 0. We can see that the execution time at the bottom is 116 ms. Let's say, for the sake of discussion, that this is very, very slow, and we want to try and improve that.

96
00:20:18.450 --> 00:20:48.250
Haki Benita: So if you go to like 99% of developers at Dba, they will tell you what's the problem and just slap a B tree on it. Right. So we add a B tree index on the hits column. We do that in Django using dB index equals. True, we generate a migration. We apply the migration. We once again produce the execution plan with, analyze, and lo and behold.

97
00:20:48.310 --> 00:20:56.180
Haki Benita: Postgres is using our index short. URL hits Ix. And, as you can see the execution. Time

98
00:20:56.810 --> 00:21:02.370
Haki Benita: is very, very fast compared to before, so we're done right.

99
00:21:03.230 --> 00:21:06.060
Haki Benita: We can call it the day we can go for lunch.

100
00:21:06.330 --> 00:21:08.609
Haki Benita: We're happy. It's fast. Now

101
00:21:09.310 --> 00:21:20.299
Haki Benita: stop, let's take a second to talk about performance and what it actually means. Okay? Because intuitively, when we talk about performance, we talk about

102
00:21:20.380 --> 00:21:37.639
Haki Benita: speed right? We want things to be very, very quick. But I think, or the way I view performance is that we need to balance different types of resources. And I want to illustrate this with an example. Okay, let's say that you have this batch processing job running at night.

103
00:21:37.640 --> 00:21:53.420
Haki Benita: Now, this batch processing job runs at the middle of the night, where you have very, very little users, and it runs very, very fast. It takes like this batch processing job like 10 seconds to complete. You're so happy, so fast. However.

104
00:21:53.720 --> 00:22:05.569
Haki Benita: however, this job consumes huge amounts of memory, huge amounts of CPU and huge amounts of disk space right. What if I told you that

105
00:22:06.440 --> 00:22:12.950
Haki Benita: if we are willing to compromise, and instead of completing in 10 seconds, it takes a minute

106
00:22:13.410 --> 00:22:38.970
Haki Benita: right? It consumes very little memory disk space and CPU, right? I'm guessing that if you pay a lot of money for memory, you are willing to make this compromise. Okay, I'll give you another example. Let's say that you have this background job running in the middle of the day. Right now, this background job consumes a lot of CPU so much CPU, in fact, that it starts to interfere with user traffic in the system.

107
00:22:39.030 --> 00:23:07.120
Haki Benita: In this case, instead of optimizing for time, you might be optimizing for CPU, right? You're willing to compromise a few seconds. But you don't want the background job to consume a lot of CPU. So when we talk about performance. We talk about more than just speed. We're talking about how we can balance different resources in the system, usually depending on some type of context time of day the type of resource that we have available at this time. Right?

108
00:23:07.670 --> 00:23:23.450
Haki Benita: So remember that we slapped A B tree on it right? And it was very, very fast, but I'm not sure that was like the most optimal thing that we could done. We could have done. So. Let's go to the database and see

109
00:23:23.580 --> 00:23:33.769
Haki Benita: and check the size of the index we created to solve this teeny, tiny problem. Okay, so this index.

110
00:23:34.570 --> 00:23:41.979
Haki Benita: right is 7 MB. Okay, so that's pretty big for for this type of index.

111
00:23:42.120 --> 00:23:47.420
Haki Benita: So our 7 MB index includes

112
00:23:47.630 --> 00:23:57.789
Haki Benita: all the rows in the table. Right? We just add a dB index through create a B tree index on the column. So it contains all the 1 million rows in the table. But

113
00:23:58.570 --> 00:24:05.790
Haki Benita: we actually don't care about all the rows in the table. Right? Nobody asked us how many

114
00:24:06.150 --> 00:24:25.690
Haki Benita: short Urls you have with less than 5 hits, or more than 266 hits, or exactly 1,000 hits. Nobody cares about that. We had a very specific question that we wanted to answer in regards to the hits. We wanted to find how many short Urls we have with exactly 0 hits.

115
00:24:26.100 --> 00:24:37.350
Haki Benita: So what if, instead of indexing the all the rows in the table, we could index just a portion of the rows, the part of the table that we actually care about.

116
00:24:37.810 --> 00:24:51.950
Haki Benita: Right? So this is a once again mind-blowing idea, and this is made possible with something called partial indexes. Partial indexes, allows us to index just a part of the table that we actually care about.

117
00:24:52.810 --> 00:25:08.019
Haki Benita: So going back to our Django model right. 1st we start by removing the dB index from the column definition, you should never use dB index. Regardless of this, and then, instead of adding this default index. On the column.

118
00:25:08.020 --> 00:25:28.989
Haki Benita: we add a proper index. Right? But we add a condition. Okay, so what this does, it creates an index on the Id column with a condition where hits equals 0. This would cause postgres to create an index just on the rows that satisfy this query. Just on rows

119
00:25:29.200 --> 00:25:54.569
Haki Benita: where hits equal 0. Right? So we generate the migration. We apply the migration, and we try the query again. We produce an execution plan, and we can see that Postgres is using our index. Right? We see an index scan using short URL unused part Ix. This is the index we just created. Okay, so Postgres is able to use the index we just created the partial index

120
00:25:55.000 --> 00:26:04.670
Haki Benita: to satisfy this very specific query. We can also see that the query is very, very fast, even compared to the full index. Right?

121
00:26:05.090 --> 00:26:13.180
Haki Benita: But that wasn't the motivation here, right? This is not what we look to optimize. If we go back

122
00:26:13.320 --> 00:26:28.990
Haki Benita: to the database, and we look at the size of this index. Look at that. The partial index is just 88 kB in size. Okay? Previously the full index was 7 MB. The partial index is 88 kB.

123
00:26:28.990 --> 00:26:48.659
Haki Benita: So I did the math seriously. I opened excel. I did the math. That's 99% smaller. Okay, so that's a lot of space. Now, at this point you're probably saying, Come on, man, it's just 7 MB. Who cares? But if you go back to your system, and you have huge tables with hundreds and billions of rows. Right?

124
00:26:48.840 --> 00:27:06.290
Haki Benita: Check the size of your B 3 indexes. They can become huge. I've seen situations where the B 3 index was larger than the table. Okay, and if you have a lot of indexes it can grow out of control very, very quickly.

125
00:27:07.020 --> 00:27:21.090
Haki Benita: So, as you may guess, I'm a very, very big fan of partial indexes. They produce smaller indexes, and I highly encourage you to use them whenever possible. One limitation of partial indexes is that

126
00:27:22.030 --> 00:27:26.349
Haki Benita: the database can only use partial indexes when

127
00:27:26.500 --> 00:27:52.249
Haki Benita: the query uses the exact same condition as the predicate in the index. Right? The database is not even smart enough to do something like like, where hits equal one minus one. Okay to this level. Okay, so it's limited to queries that use the exact same condition. Usually it's fine, because you know, why would you do hits equal one minus one.

128
00:27:52.380 --> 00:27:53.080
Haki Benita: I don't know.

129
00:27:53.520 --> 00:27:58.490
Haki Benita: I personally found that noble columns are great candidates

130
00:27:58.780 --> 00:28:09.290
Haki Benita: for partial indexes, because in postgres, for example, null values are indexed, and usually you don't want to use an index for is null queries. So I found that

131
00:28:09.480 --> 00:28:34.749
Haki Benita: whenever I have a noble column with an index on it, I can benefit from making it a partial indexes. In fact, I wrote an entire article on how we save 20 GB of unused disk space simply by identifying noble columns with indexes and switching them to use partial index. Okay, so questions about partial indexes before we move on to the next use case.

132
00:28:36.780 --> 00:28:38.540
Haki Benita: Gabor, you have a question.

133
00:28:42.160 --> 00:28:42.730
Haki Benita: No.

134
00:28:42.730 --> 00:28:45.249
Gabor Szabo: Sorry there is this sorry? Actually, there is this question.

135
00:28:46.340 --> 00:29:04.110
Haki Benita: Oh, is it a good idea to recalculate the hits and partial indexes? How frequently! Well, the nice thing about indexes and btrees in general that they are always in sync with the data in the table, it's actually part of the transaction. So when you, for example, increment.

136
00:29:05.180 --> 00:29:07.990
Haki Benita: when you increment the counter for the 1st time

137
00:29:08.290 --> 00:29:11.070
Haki Benita: the row would just disappear from the index.

138
00:29:11.250 --> 00:29:26.029
Haki Benita: Right? So I'm guessing that you're asking, because you have some experience with like materialized views and stuff like that. So you don't actually have to maintain it actively. It's just maintained by the database.

139
00:29:26.460 --> 00:29:32.839
Haki Benita: It's truly an amazing feature. You should definitely use that any more questions before we move on to

140
00:29:33.140 --> 00:29:36.009
Haki Benita: a very exotic type of index in postgres.

141
00:29:36.750 --> 00:29:38.110
Haki Benita: Ow.

142
00:29:41.210 --> 00:29:46.360
Haki Benita: okay, great. So let's talk about another type. Another use case.

143
00:29:47.270 --> 00:30:00.790
Haki Benita: So first, st in the 1st use case, we wanted to resolve the key to a URL right? This is the redirect action. This time we want to do a reverse. Look up. We want to ask

144
00:30:01.000 --> 00:30:09.090
Haki Benita: how many keys we have pointing to this specific URL. So we wanna search for keys by the URL.

145
00:30:09.530 --> 00:30:20.539
Haki Benita: So we implement this very simple function called reverse lookup. It accepts a URL and returns query, set of short Urls. Okay?

146
00:30:21.210 --> 00:30:49.150
Haki Benita: So if we want to see what the query looks like. We use dot query. And we can see select star from short URL where URL equals something. Okay, if we produce an execution plan. We can see that the database is doing a sequential scan on the short URL table that is, scanning the entire table, sifting row by row, finding matches for our query.

147
00:30:49.430 --> 00:30:50.800
Haki Benita: Whoa!

148
00:30:51.590 --> 00:30:55.929
Haki Benita: And we can see that it's relatively

149
00:30:56.140 --> 00:31:00.379
Haki Benita: slow, right? It's like 105

150
00:31:00.500 --> 00:31:03.990
Haki Benita: milliseconds so compared to the index

151
00:31:04.320 --> 00:31:08.840
Haki Benita: queries that we saw before. That's that's pretty slow. Right?

152
00:31:09.220 --> 00:31:23.659
Haki Benita: So you know, once again, 99% of the people would just say, Come on, man, I'm hungry. Let's order some food. Just slop a B tree on it. So this is what we do right? We start by adding A B tree on the URL

153
00:31:23.860 --> 00:31:37.679
Haki Benita: right? We generate and apply the migration. Now we execute the exact same query again, and we can see that now Postgres is using the index that we just created. We can see an index scan using

154
00:31:38.030 --> 00:31:57.059
Haki Benita: the index on the URL column, and also it's very fast. Previously it was like a 100 ms. Now it's 0 point 1 ms. So that's a very, very big and significant improvement. We can all seek to launch and be very, very happy and satisfied with ourselves. But

155
00:31:57.770 --> 00:32:09.459
Haki Benita: are we done? Do you think that we are done? Is there anything that we can optimize? Now, if you are paying attention throughout this presentation. You know that we can definitely do better than that.

156
00:32:09.830 --> 00:32:16.550
Haki Benita: Let's go to the database and check the size of the index. Okay? So the size of the index.

157
00:32:16.740 --> 00:32:22.669
Haki Benita: Okay, stay with me. 47 MB. If you remember the previous

158
00:32:23.050 --> 00:32:28.779
Haki Benita: use case, we had an index on all the heads. It was 7 MB. I told you it was large.

159
00:32:28.950 --> 00:32:44.159
Haki Benita: This index on the same amount of rows is 47 MB. That's very, very big, and the reason that it's very, very big is that the URL is very, very big, right? The beach index

160
00:32:44.390 --> 00:32:49.879
Haki Benita: holds the actual values in the leaf block. So if we are indexing.

161
00:32:50.020 --> 00:32:58.219
Haki Benita: A column with very large values like Urls, can be very, very big. So if we are indexing

162
00:32:58.430 --> 00:33:03.490
Haki Benita: a column with very, very big values, these values are also present in the index.

163
00:33:04.000 --> 00:33:14.130
Haki Benita: and the index can get very, very big. So previously, when we were indexing integers, it was 7 MB. Now we're indexing large pieces of text Urls.

164
00:33:14.410 --> 00:33:18.940
Haki Benita: and that's 47 MB. Okay, so

165
00:33:19.430 --> 00:33:28.389
Haki Benita: let's pause for a second. Okay, I know that btree is like the magic for 90% of the use cases. But there are other types of indexes that we can use.

166
00:33:28.955 --> 00:33:32.949
Haki Benita: So let's pause for a second and ask ourselves, what do we know about.

167
00:33:33.210 --> 00:33:48.990
Haki Benita: what do we know about the URL? Okay? So 1st of all, we know that URL is not unique. Right? We can have multiple keys pointing to the same URL. We can have, for example, different campaigns with different short Urls

168
00:33:49.100 --> 00:33:55.800
Haki Benita: pointing to the same URL. There's no restriction in the system. You can have many keys pointing to the same URL. So it's not unique.

169
00:33:55.930 --> 00:33:57.940
Haki Benita: However, however.

170
00:33:59.780 --> 00:34:06.770
Haki Benita: if we actually look at the data, we see that we don't have a lot of duplicate long Urls right

171
00:34:06.970 --> 00:34:07.889
Haki Benita: like.

172
00:34:09.444 --> 00:34:18.389
Haki Benita: It's not likely that people will use the same show to a lot to point to the same URL like at the at the very least.

173
00:34:18.650 --> 00:34:22.639
Haki Benita: they would have different utm parameters for the same. URL.

174
00:34:22.780 --> 00:34:33.040
Haki Benita: So while it's it's, it's not a restriction. You can have many keys, pointing to the same URL. It's not likely, so we don't have a lot of duplicate values.

175
00:34:34.199 --> 00:34:36.219
Haki Benita: So now I want to introduce you

176
00:34:36.710 --> 00:35:00.369
Haki Benita: to what I call the Ugly Duckling of index types in postgres, the Hash Index. Okay? And to understand how a hash index works and why it's different from B 3 index. Let's start by actually building a hash index ourselves. So imagine we have these values, A, BC and D, and we want to index them using a hash index.

177
00:35:00.730 --> 00:35:20.800
Haki Benita: So we start by applying a hash function on each value. So postgres in our example, it has different hash functions for different types. So you can see that we have hash for text char arrays, even Json types, Timestamps, and so on.

178
00:35:20.930 --> 00:35:34.680
Haki Benita: In our case we have just one character. So it uses hashchar. If we actually apply this function on the values we get the hash values. The next step is we want to divide these

179
00:35:34.870 --> 00:35:36.829
Haki Benita: values into buckets.

180
00:35:37.030 --> 00:35:43.100
Haki Benita: So we start by dividing them into 2 buckets. Basically, we apply modular 2 on

181
00:35:44.050 --> 00:36:04.600
Haki Benita: on the hash value, and then we assign each value to a bucket. So we can see that A goes to bucket one and BC and D goes to bucket 0. So this is our hash index. Okay, so we have 3 hash values in bucket 0, each hash value points to

182
00:36:04.860 --> 00:36:10.809
Haki Benita: somewhere in the table. Okay, just like we had the Tids in the B tree. We have

183
00:36:10.980 --> 00:36:32.230
Haki Benita: the tids right here in the hash index. Now, if we want to use this hash index to find some value, we do the exact same thing, but the opposite, but the other way around, right? So if you want to search for the value B, for example, we apply a hash function on it. We get the hash value. We apply modulus number of buckets to get the

184
00:36:32.360 --> 00:36:54.430
Haki Benita: bucket. In this case 0, and then we go to bucket 0 and we start scanning the pointers to find matching hash. Once we found a matching hash, we can take this 2, which is a pointer to a place in the table, and we can go scan this row and look for matching rows. Okay, so this is how a hash index works in postgres.

185
00:36:55.190 --> 00:37:14.639
Haki Benita: Now, if we want to create a hash index in Django. We need to use the special hash index from postgres contrip. Okay? The reason for that is that hash index is not the default index type in postgres. So we need to explicitly say, we want a hash index. Okay.

186
00:37:15.260 --> 00:37:19.239
Haki Benita: so in this case we are creating a hash index on the URL field.

187
00:37:19.770 --> 00:37:46.360
Haki Benita: and the name of this index is going to be short. URL Hix. I like to use a suffix that indicates the type of the index. So when you know, when I look at execution planes, I can quickly identify the type of the index. So I usually use Ix for B. 3 indexes, and then I use part Ix. For partial hix for hash indexes, and so on. You can come up with whatever convention you want.

188
00:37:47.920 --> 00:37:48.900
Haki Benita: So

189
00:37:49.530 --> 00:38:00.809
Haki Benita: we generate the migration, we apply the migration and produce an execution plan. And we can see that Postgres is using our hash index. Okay? Now.

190
00:38:00.940 --> 00:38:01.990
Haki Benita: okay.

191
00:38:02.180 --> 00:38:18.460
Haki Benita: 1st observation. This is very, very fast. Okay, so you can see that 0 point 0 7 ms. That's very, very fast. But that's not all. If we look at the size of our hash index. Compared

192
00:38:18.730 --> 00:38:34.859
Haki Benita: to the Beecher index, we can see that the hash index is 30% smaller. Okay, trust me, I took a calculator, an old casio. And I calculated the difference. It's 30% smaller. Okay, that's very, very significant. Okay.

193
00:38:35.340 --> 00:38:37.929
Haki Benita: if we put all the data in a table.

194
00:38:38.180 --> 00:38:46.570
Haki Benita: You can see that the hash index in this case, with both faster and smaller.

195
00:38:46.860 --> 00:38:47.990
Haki Benita: So that's

196
00:38:48.170 --> 00:39:06.030
Haki Benita: a win-win all around. Okay, faster and smaller than the default. B, 3. Index. Now, I did a little experiment. Okay. So what I did was, I created a hash index and a btree index on the key and on the URL. Okay, you can see the the chart right here.

197
00:39:06.490 --> 00:39:35.660
Haki Benita: I have a hash index on the key. I have a hash index on the URL, I have a B tree on the key, and I have a B tree on the URL. And what I did is I started adding rows to the table. Okay, you can see at the bottom the bottom axis. That's the number of rows. So I started adding rows into the table until I get to a million rows. Now, every time I added rows to the table I took a snapshot of the sizes of the hash index of all the indexes, and then I put this

198
00:39:35.740 --> 00:39:39.649
Haki Benita: all the data in this chart, and we can see some

199
00:39:39.740 --> 00:39:43.597
Haki Benita: interesting things. Okay. 1st of all.

200
00:39:44.510 --> 00:39:46.580
Haki Benita: 1st of all, if you look at the.

201
00:39:47.000 --> 00:39:49.219
Haki Benita: If you look at the red line.

202
00:39:49.470 --> 00:39:52.999
Haki Benita: which is the B tree on the URL big piece of text.

203
00:39:53.690 --> 00:40:18.479
Haki Benita: and the green line which is the B tree on the key the short piece of text. 1st of all, you can see that both of them grow basically linearly as I add more rows to the table, right? So we can see like this linear line increasing right? As I add, more rows, the size of the index increases. We can also see that the red line, the B tree on the URL is always larger.

204
00:40:18.850 --> 00:40:21.239
Haki Benita: the the B tree on the key right?

205
00:40:21.780 --> 00:40:30.559
Haki Benita: So the reason for that is that the URL is a big piece of text, and the key is a short piece of text. This tells us

206
00:40:30.890 --> 00:40:33.730
Haki Benita: that the size of the bee tree is

207
00:40:33.840 --> 00:40:36.900
Haki Benita: very much affected by the size

208
00:40:37.250 --> 00:40:40.240
Haki Benita: of the column that it indexes.

209
00:40:40.380 --> 00:40:49.959
Haki Benita: So A B tree on URL will be bigger than A B tree on key for the same amount of rows, because a URL is bigger than a key.

210
00:40:50.270 --> 00:40:56.780
Haki Benita: So that's about the B 2 indexes. However, if we look at the hash indexes. That's the blue.

211
00:40:57.900 --> 00:40:59.700
Haki Benita: the yellow lines.

212
00:41:00.190 --> 00:41:02.260
Haki Benita: 1st of all, we can see that

213
00:41:03.480 --> 00:41:10.410
Haki Benita: the size of the hash index, if I add more rows is not affected by the size of the value.

214
00:41:10.540 --> 00:41:18.259
Haki Benita: because URL is big key small. But as I add more rows to the table. The size of the hash index is the same. Okay.

215
00:41:18.400 --> 00:41:27.409
Haki Benita: The second thing that I can see is that in this specific case the hash index was consistently lower, smaller.

216
00:41:27.690 --> 00:41:35.050
Haki Benita: Then the same index, the same B, 3 index on the same column. Okay. So in this case the hash index was always smaller.

217
00:41:35.520 --> 00:41:40.680
Haki Benita: Another thing that we can see in this chart that, unlike the B 3 index that grows linearly.

218
00:41:41.050 --> 00:41:48.299
Haki Benita: the hash index grows in like steps. Right? You can see the step, and then it's flat. Step flat.

219
00:41:48.700 --> 00:42:09.099
Haki Benita: So what's happening in a hash index is once we have, we start adding rows to the hash index, and then we have some bucket, and this bucket starts to fill up. Now, when a bucket fills up, postgres, needs to split this bucket. Now, when the bucket is split, postgres, pre allocates

220
00:42:09.580 --> 00:42:12.570
Haki Benita: storage disk space for this bucket.

221
00:42:12.700 --> 00:42:16.419
Haki Benita: So the steps that you see is the bucket splits

222
00:42:16.540 --> 00:42:21.430
Haki Benita: where postgres allocates additional storage to split the bucket.

223
00:42:21.770 --> 00:42:22.630
Haki Benita: Right?

224
00:42:22.970 --> 00:42:25.229
Haki Benita: So this is why hash index

225
00:42:25.420 --> 00:42:28.239
Haki Benita: grows in in, in, in steps.

226
00:42:29.060 --> 00:42:35.259
Haki Benita: So hash index is ideal. When we have very few duplicates

227
00:42:35.470 --> 00:42:59.300
Haki Benita: in the rows that we want to index, and the reason for that is, if we have lots of duplicates, the values would map to the same bucket, and we won't get the benefit of a hash index. The reason that a hash index made sense in our case is that URL is mostly unique. It's almost unique. Okay, it's not unique by definition. But there's not a lot of duplicates.

228
00:42:59.680 --> 00:43:18.200
Haki Benita: We also saw that, unlike a B tree index, hash index is not affected by the size of the values that it indexes, and the reason for that is that the hash index doesn't actually include the values. It includes hash values. Okay, this is why I can index very, very big values, big strings

229
00:43:18.540 --> 00:43:40.110
Haki Benita: with a relatively small index. Okay, as we saw hash index under some circumstances, can be both smaller and faster than A. B 3 index, and the reason that a lot of people are unfamiliar with a hash index is that prior to Postgres 10, which is already pretty old because we're now at Postgres 17.

230
00:43:40.580 --> 00:44:04.829
Haki Benita: If you went to the documentation for Hash Index, there would be like this huge warning, saying, Beware, do not use hash indexes. They are not production ready. So a lot of developers became used to not using hash indexes, but starting in postgres 10, you can definitely use hash indexes in production. They are production ready, and as we saw, they can be very, very good under some circumstances.

231
00:44:06.160 --> 00:44:12.890
Haki Benita: We're talking about hash indexes. It is very important to also know the restrictions of hash indexes. 1st of all, hash index

232
00:44:14.290 --> 00:44:32.920
Haki Benita: cannot be used to create. You can create a unique hash index, and the reason that you can is that a hash index does not contain the actual values, just hash values. And technically, you can have multiple different values producing the exact same hash value.

233
00:44:33.090 --> 00:44:43.399
Haki Benita: So it can. You can create a unique hash index. However, okay, and that's the comment at the bottom, we can talk about it later. If you want. You can enforce unique

234
00:44:43.680 --> 00:44:47.209
Haki Benita: with the hash index using an exclusion constraint.

235
00:44:47.440 --> 00:44:56.589
Haki Benita: Okay, next, we can't have a composite hash index. We can't have a hash index on multiple columns. Okay?

236
00:44:57.410 --> 00:45:02.989
Haki Benita: And we can use hash index for sorting and range searches, because once again.

237
00:45:03.280 --> 00:45:10.940
Haki Benita: hash index does not contain the actual values. Just the hash values right? So I can't use a hash index for things like.

238
00:45:11.390 --> 00:45:17.379
Haki Benita: you know, between greater than less than and so on. Just equality.

239
00:45:18.540 --> 00:45:24.421
Haki Benita: So quick. Recap just 4 more slides. I promise. Okay,

240
00:45:26.090 --> 00:45:34.610
Haki Benita: when to use indexes. So remember, indexes can make queries faster. We saw that in all of our examples.

241
00:45:34.650 --> 00:45:56.340
Haki Benita: using an index, made the query faster. However, the not free, they come at a cost. You need to maintain this index, and this index maintenance happens when you insert when you update and when you delete. So the more indexes you create, the faster your queries are. But the slower every other operation is

242
00:45:56.500 --> 00:46:18.380
Haki Benita: okay. Another thing to consider, and this is often overlooked. Indexes can be very, very big. They consume a lot of disk space when you go back to your databases. After this talk, please go do slash di plus, and look at the sizes of your index. I think that if you never looked at the size of your indexes.

243
00:46:18.620 --> 00:46:23.349
Haki Benita: You're going to be very much surprised at what you're going to find.

244
00:46:24.180 --> 00:46:41.909
Haki Benita: and finally using an index is not always best. If you have a query that needs to access a large portion of the table. Sometimes it doesn't make sense to use an index for that. Okay, there's no magic number, but, you know.

245
00:46:42.190 --> 00:46:43.480
Haki Benita: keep that in mind.

246
00:46:44.710 --> 00:46:55.220
Haki Benita: So we talked about index types and features. We talked about partial indexes, inclusive between indexes, and we talked about hash index.

247
00:46:55.420 --> 00:47:07.439
Haki Benita: We talked a little bit about how to evaluate performance. I don't know if you noticed, but throughout throughout this presentation we went through the same process over and over again. We start by

248
00:47:07.600 --> 00:47:25.639
Haki Benita: executing some query with, explain, analyze, to get the timing with no indexes. This is basically establishing a baseline right? And then we start by experimenting with different types of indexes. So usually, we start with a B tree. We take a measure of the time using, explain, analyze.

249
00:47:25.640 --> 00:47:40.620
Haki Benita: and then we take the size of the index. We put it all in a nice table. We start experimenting. And once you have all the data organized like that. It's a lot easier to reach a decision on what is the best indexing approach

250
00:47:40.630 --> 00:47:42.499
Haki Benita: for your specific use case.

251
00:47:42.560 --> 00:47:53.119
Haki Benita: And also and hopefully, you remember that indexes performance is not just about speed. As we saw, we can get significant

252
00:47:53.660 --> 00:47:57.540
Haki Benita: disk space reductions with a very, very.

253
00:47:57.600 --> 00:48:09.329
Haki Benita: with a very small price of speed sometimes makes sense to make this compromise. We also, throughout this talk, saw how to use, explain

254
00:48:09.360 --> 00:48:31.259
Haki Benita: how to use, explain, analyze how to debug SQL in Django, and we also saw a lot of execution plans. I don't know if you noticed, but if you've never seen execution plans before, hopefully, when you go back to your system. You start doing, explain, analyze some of the queries you run a lot. You get to actually understand what the database is doing. Now

255
00:48:31.560 --> 00:48:45.659
Haki Benita: in this talk I talked only about inclusive indexes, partial indexes, and hash index, but, in fact, there are many, many different other types of indexes that are exotic and very, very cool. We have

256
00:48:46.330 --> 00:48:56.900
Haki Benita: Brent indexes. We have function based indexes, and we have a lot of different flavors of things that we can do. And you can check out this

257
00:48:57.300 --> 00:49:04.960
Haki Benita: class 3 h packed with astral magic for your benefit and

258
00:49:05.810 --> 00:49:13.720
Haki Benita: finally check me out in all of these places, and I'm happy to take questions or discuss whatever you want.

259
00:49:19.490 --> 00:49:22.113
Gabor Szabo: Whoa, thank you.

260
00:49:23.750 --> 00:49:26.585
Gabor Szabo: Because, yeah.

261
00:49:27.400 --> 00:49:28.630
Haki Benita: Hectic.

262
00:49:30.335 --> 00:49:35.410
Gabor Szabo: Yeah, this is not a question, Hank. His article on Hash Indexes is truly excellent.

263
00:49:35.520 --> 00:49:42.589
Gabor Szabo: I believe it remains one of the top search results for anyone looking for resources on hash indexes.

264
00:49:42.760 --> 00:49:47.639
Haki Benita: It's true, it's true. This is one of the top searches for hash index in postgres.

265
00:49:47.910 --> 00:49:48.340
Gabor Szabo: Yeah.

266
00:49:48.340 --> 00:49:53.060
Haki Benita: Yeah, I managed to catch this trend very, very early on.

267
00:49:54.515 --> 00:49:55.540
Gabor Szabo: Okay.

268
00:49:55.790 --> 00:49:56.270
Haki Benita: Mom.

269
00:49:56.270 --> 00:50:01.189
Gabor Szabo: Comments, questions before we. We close this session.

270
00:50:02.340 --> 00:50:05.000
Gabor Szabo: We know where where to find you.

271
00:50:05.160 --> 00:50:07.829
Gabor Szabo: We have the. We'll have the link.

272
00:50:08.320 --> 00:50:16.320
Gabor Szabo: You can add the links to the post of the of the of the video as well, so people can find find it easily, easily.

273
00:50:17.100 --> 00:50:19.660
Gabor Szabo: and any comments.

274
00:50:19.660 --> 00:50:20.020
Haki Benita: Okay.

275
00:50:20.020 --> 00:50:21.859
Gabor Szabo: Questions, apparently not.

276
00:50:21.860 --> 00:50:24.780
Haki Benita: Yeah, I want to thank you, Gabra, for hosting this meeting.

277
00:50:24.780 --> 00:50:25.650
Gabor Szabo: It was excellent.

278
00:50:26.146 --> 00:50:27.139
Haki Benita: Meet up!

279
00:50:27.140 --> 00:50:32.660
Gabor Szabo: Yeah. Well, yeah. So thank you very much for this presentation.

280
00:50:32.770 --> 00:50:41.470
Gabor Szabo: If anyone has questions, then we'll see how to find the hockey later on in this on this slide, and then we'll put it in under the video.

281
00:50:42.020 --> 00:50:52.750
Gabor Szabo: Thank you for for supporting us. Thank you for being here. Thank you very much to you to giving the presentation, please, like the video and follow the channel. Yeah.

282
00:50:53.020 --> 00:51:10.139
Gabor Szabo: And if you would like to give any presentation, you're welcome to contact me as well, and we'll see how we can schedule a presentation at what time, and and so on. So thank you very much, and

283
00:51:10.430 --> 00:51:15.029
Gabor Szabo: see you at the next meeting next video, whatever.

284
00:51:15.400 --> 00:51:16.869
Gabor Szabo: Thank you. Bye, bye.

285
00:51:16.870 --> 00:51:18.830
Haki Benita: Thank you very much. Everyone. Good night.

