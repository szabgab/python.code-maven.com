---
title: "Send HTTP Requests in Python"
timestamp: 2017-08-25T14:30:01
tags:
  - requests
  - GET
  - header
  - status_code
  - text
published: true
books:
  - python
author: szabgab
archive: true
---


Accessing web sites from a Python program is not very difficult, but using
the [requests](http://docs.python-requests.org/) library makes it even fun.

Let's see a few examples.


We are going to use the [httpbin.org](http://httpbin.org/) site that provides an excellent set of end-point for us to experiment with. The site has both an http and an https version. (BTW It was created by the same author as the requests package.)

{% include file="examples/python/requests_get_html.py" %}

After importing the module we can call its `get` method passing a URL to it.
It will return [requests.models.Response](http://docs.python-requests.org/en/master/user/advanced/#request-and-response-objects) object.

Some of the methods it has are:

`r.status_code` is the [HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). On success it is 200.

`r.headers` is a dictionary of all the entries in the header. for example for the above request I got the following header:

```
{'content-length': '12150', 'server': 'nginx', 'connection': 'keep-alive', 'access-control-allow-credentials': 'true',
'date': 'Thu, 05 Jan 2017 09:45:02 GMT', 'access-control-allow-origin': '*', 'content-type': 'text/html; charset=utf-8'}
```

We could look at the [Content-Type](https://en.wikipedia.org/wiki/Media_type) that the server sent us using the simple dictionary access code: `r.headers['content-type']` that, in the above case, will print

```
text/html; charset=utf-8
```

`r.text` contains the full content of the page. The content that you would get if you opened the page in your browser and the clicked on "view source", or that you would get if you ran `curl` with the given URL.

You will get the exact same behavior if you change the URL to be https.

## Asking for JSON

Asking for a page that would return JSON is exactly the same as asking for an HTML page.
The difference is only in the returned values:

{% include file="examples/python/requests_get_json_ip.py" %}

The content-type is

```
application/json
```

The text is a JSON string. In the case of the 

```
{
  "origin": "31.168.125.94"
}
```

The `json` method converts the JSON string into a Python data structure.
In our case it is a dictionary holding a single key and the IP address of our computer
as the value:

```
{u'origin': u'31.168.135.94'}
```

We can access the individual values (in this case the IP address), just as
we do with any other dictionary in Python:

```
data['origin']
```

## Get the User Agent

Another URL the [httpbin.org](http://httpbin.org/) site provides return
the [user-agent](http://httpbin.org/user-agent) of our client. When
I visited that URL with my FireFox browser I got the following response:

```
{
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0"
}
```

When I visited in with Chrome, I got this:

```
{
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
}
```

When I ran the Python script: 

{% include file="examples/python/requests_get_json_ua.py" %}

I got the following:

```
{
  "user-agent": "python-requests/2.3.0 CPython/2.7.12 Darwin/16.3.0"
}
```

This means that the server can tell both the IP address I use and the browser I have when accessing the site and even the operating system on my computer.
Based on this information they can return different data to different users.

I've heard that certain sites will show you higher prices if you are using a Mac as they assume you'll be ready to pay a higher price.

Other sites will refuse to serve you unless you use a "human browser".
They would notice the "user-agent" of your Python application and return error.

## Setting the User-agent in Python requests

Luckily the requests library makes it very easy to change the User-Agent string supplied in the request and to fake any browser.

{% include file="examples/python/requests_get_json_ua_changed.py" %}

The only thing you need to do is to supply the `headers`
key with a dictionary including the User Agent:

```
    headers = {'User-agent': 'Internet Explorer/2.0'}
```

If you run this program it will send the request as if it was Internet Explorer 2.0
and let the system administrator wonder if you are really stuck with such an old browser.


## Comments

If you wanted to send a User-Agent like a name to a particular proxy, etc..... what would be the appropriate way to do that... I think I am sending it but it doesn't seem to be received. It is populated in the "header" and sent - can you suggest a better way?

---
have you tried to see what happens when you access http://httpbin.org/user-agent ? That should show you if you managed to set the User-Agent or not. The particular proxy might look for something else though. Check in the docs of that proxy.


---
Can you think of a better way to send an identifying "object" other then trying to use user-agent stuffed in the header?

---

You will need to give a bit more explanation of what do you (or the site you are connecting to) needs. Can you explain a what are you trying accomplish?

---

I am trying to pass an "id" in the header under user-agent so for example the header has an authorization code and then what was supposed to be a User-Agent: "BillyBob" so when it was passed.. the proxy would see the BillyBob and allow it to passthrough (I hope that makes sense to you)

So headers = {'user-agent': "BillyBob", 'Authorization': 'abcd-eft...'}
than
r. = requests.get("https://name.com", data=json.dumps(hec_data), headers=headers, proxies=proxies, timeout=1)


---

That does not seem right. The User-Agent is usually the name of your browser not your personal ID or username. In any case you are already talking about a solution here. My question is what server are you trying to access? What does the documentation of it say about authentication?

---

Just trying to push some captured data to Splunk that has to go through our proxy - I will have to do research as I don't have access to the proxy myself. But I agree it doesn't look right, but I am a beginning learner of Python so....

---

Have you tried using the proxies from  https://docs.python-requests.org/en/latest/user/advanced/ ?

---

Yes I have that in there as well…

<hr>

I tried - I think that it sends it - however perhaps User-Agent is not the appropriate way to do this... Being new to Python and etc... I am not really sure what is available and the best way. I will double check with the proxy team. Thank you so much for your reply :)


