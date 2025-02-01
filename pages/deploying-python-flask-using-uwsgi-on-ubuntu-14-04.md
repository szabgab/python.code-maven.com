---
title: "Deploying Python Flask using uWSGI and Nginx on Ubuntu 14.04"
timestamp: 2016-03-25T12:30:01
tags:
  - Python
  - uWSGI
  - Nginx
  - Ubuntu
  - Flask
books:
  - flask
published: true
author: szabgab
---


The following is a tutorial on how to set up uWSGI with an Nginx front end to serve a [Flask](/flask) based
application.

In this tutorial we will only use the packages that are supplied by Ubuntu and we will deal with a very simple
[Hello World](/hello-world-with-flask-and-python) application.


It was tested on an Ubuntu 14.04 x64 droplet of [Digital Ocean](/digitalocean) though a very
similar process was used earlier on Ubuntu 13.10 [for plain Python web application](https://perlmaven.com/deploying-pyton-with-uwsgi-on-ubuntu-13-10).

After you create a droplet with Ubuntu 14.04 x64 you'll get an e-mail with your IP address
and the password of root. In this example I'll use 1.2.3.4 as the IP address. You'll have to replace
the commands with the IP address of your server.

First just ssh to the server. On Linux/Unix/OSX you would type this:

```
$ ssh root@1.2.3.4
```

On Windows you'd probably install [putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) and use that.

You don't have to, but I recommend, the first thing you do after logging in to the server is to update the packages to the latest by typing the following:

```
# aptitude update
# aptitude -y safe-upgrade
```

Then reboot:

```
# reboot
```

This will disconnect you from the server. After a few seconds you can continue and connect again using `ssh`

Personally I have a public key on file at [Digital Ocean](/digitalocean) that they install on the server
when it is created so I did not have to do the following, but if you don't yet have a public key with them,
I'd recommend copying your public ssh key to let you ssh without password:

```bash
$ scp ~/.ssh/id_rsa.pub root@1.2.3.4:.ssh/authorized_keys
$ ssh root@1.2.3.4
```

If the first command worked well, then the second won't ask for a password.

## Hello World using Pyton Flask

Before the deployment options, let's write and try our
[Hello World using Flask](/hello-world-with-flask-and-python).

Check the version of Python. I got the following:

```bash
# python --version
Python 2.7.6
```

Then create a user called <b>dev</b> so we won't do everything as root.

```
# adduser --gecos '' --disabled-password  dev
```

Switch to the new user and create a directory for the project.

```bash
# su - dev
$ mkdir project
$ cd project/
```

In the project/ directory create a file called app.py with the following content:


```pyhton
from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def main():
   return "Hello World at " + time.time().__str__() + "\n";

if __name__ == "__main__":
    app.run(debug=False)
```

This is slightly more complex than the Hello World in our stand-alone, as it also includes the timestamp
to make it easy to observe that the code runs again on every reload of the browser.

Please also note, our `app.run()` call is protected by `if __name__ == "__main__":`
so the code will only run immediately when this file is executed as a script and not when it
is loaded as a module.

Let's run our application:

```bash
$ python app.py
Traceback (most recent call last):
  File "app.py", line 1, in <module>
    from flask import Flask
ImportError: No module named flask
```

## ImportError: No module named flask

Well, we can't use Flask without installing it, can we?

In order to make life a bit easier down the road I've opened a second terminal window and ssh-ed to the server in that window as well.
Now I have one window where I am used "dev" and another window where I am user "root".

I've installed Flask provided and pre-packaged by Ubuntu. In the window where I am "root":

```bash
# aptitude -y install python-flask
```

Then I could switch back to my "dev" window and run the application again:

```bash
$ python app.py 
 * Running on http://127.0.0.1:5000/
```

in order to try it, I've switched to the "root" window and used `curl` to fetch the page:

```bash
curl http://127.0.0.1:5000/
Hello World at 1458888407.29
```

At this point I could ran the `curl` command a few more times to see how time is passing....


Anyway, I switched back to the "dev" console where I saw a new line on the screen:

```
127.0.0.1 - - [25/Mar/2016 04:47:43] "GET / HTTP/1.1" 200 -
```

This is just the server telling me about the request I generated using `curl` and that it served it well.

At this point I've also tried to access the server using my regular browser typing in 
`http://1.2.3.4:5000/` but I have not received any response. Apparently the default server of Flask only listens
on localhost (127.0.0.1).

I pressed `Ctrl-C` to stop the web server.

## Install and setting up uWSGI

Now that we know our "application" works we can make the next step and serve it using uWSGI which is a much more robust
server than the one used for our development.

First thing was to switch to the "root" window and install uWSGI and the Python Plugin for it:

```
# aptitude -y install uwsgi  uwsgi-plugin-python
```

Then, just for good measures, I've checked the version number:

```bash
# uwsgi --version
1.9.17.1-debian
```

Once I had uWSGI installed I've tried to launch it with the "Hello World application" on port 9090:

I've got a lot of output

```bash
$ uwsgi --http-socket :9090 --plugin python --wsgi-file app.py 

*** Starting uWSGI 1.9.17.1-debian (64bit) on [Fri Mar 25 02:56:14 2016] ***
compiled with version: 4.8.2 on 23 March 2014 17:15:32
os: Linux-3.13.0-79-generic #123-Ubuntu SMP Fri Feb 19 14:27:58 UTC 2016
nodename: flask
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 1
current working directory: /home/dev/project
detected binary path: /usr/bin/uwsgi-core
*** WARNING: you are running uWSGI without its master process manager ***
your processes number limit is 3750
your memory page size is 4096 bytes
detected max file descriptor number: 1024
lock engine: pthread robust mutexes
thunder lock: disabled (you can enable it with --thunder-lock)
uwsgi socket 0 bound to TCP address :9090 fd 3
Python version: 2.7.6 (default, Jun 22 2015, 18:01:27)  [GCC 4.8.2]
*** Python threads support is disabled. You can enable it with --enable-threads ***
Python main interpreter initialized at 0x1723c80
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 72792 bytes (71 KB) for 1 cores
*** Operational MODE: single process ***
unable to find "application" callable in file app.py
unable to load app 0 (mountpoint='') (callable not found or import error)
*** no app loaded. going in full dynamic mode ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI worker 1 (and the only) (pid: 2128, cores: 1)
```

It seemed to be working sow I switched to the "root" window and using `curl` on port 9090
I've tried my luck:

```bash
root@flask:~# curl http://127.0.0.1:9090/
Internal Server Error
```

That does not look good.

In the meantime, in the "dev" window where I launched the server I've got some additional output:


```bash
--- no python application found, check your startup logs for errors ---
[pid: 4384|app: -1|req: -1/1] 127.0.0.1 () {24 vars in 247 bytes}
     [Fri Mar 25 04:59:12 2016] GET / => generated 21 bytes in 0 msecs (HTTP/1.1 500) 1 headers in 57 bytes (0 switches on core 0)
```

Stopped the server using Ctrl-C.

## uWSGI needs an "application"

The key word both in this error message and in the initial output was <b>application</b>.
Apparently uWSGI is looking for an object called "application" in our web, well, application.

There are a number of ways to solve this:

1) We can replace the word `app` by `application` in our code.

2) We can keep using @app, but also create a copy of "app" called "application" like this:

```pyhton
application = app  # make uwsgi happy
```

3) We can tell uWSGI that our "application" is called "app" by adding
`--callable app` to our command line:

Using the new command line I've launched the server again:

```
$ uwsgi --http-socket :9090 --plugin python --wsgi-file app.py --callable app
```

This time, after switching to the "root" window, I got the expected response to the
`curl http://127.0.0.1:9090` command.

Now you can already visit the we site by following th URL:
http://1.2.3.4:9090 (remember to replace the IP with the one you have).


Further uWSGI configuration (3 processes handle the requests) can be provided
on the command line:

```
$ uwsgi --http-socket :9090 --plugin python --wsgi-file app.py --callable app --process 3
```

But, instead of  the command line, it is probably better to create a configuration
file called `/home/dev/project/my-uwsgi.ini` with the following content:

```
[uwsgi]
http-socket    = :9090
plugin    = python
wsgi-file = /home/dev/project/app.py
process   = 3
callable = app
```

Now we can launch the server using the following command:

```
uwsgi --ini project-uwsgi.ini
```

We can try it from the other window or from our own browser.

We can shut it down by pressing Ctrl-C.

We can then, using the "root" window, create a symbolic link so uWSGI will start our server automatically
when the server boots up:

```
# ln -s /home/dev/project/my-uwsgi.ini /etc/uwsgi/apps-enabled/
```

and launch the service as root with the following command:

```
# service uwsgi start
```

At this time it might be worth to reload the page in our browser again, to make sure every thing still works.


## Add Nginx to the mix

Install Nginx and remove the default configuration file:

```
# aptitude install nginx
# service nginx start
# rm /etc/nginx/sites-enabled/default
```

Instead of that create a new configuration file in
`/home/dev/project/my-nginx.conf`
with the following content:

```
server {
  location / {
    include uwsgi_params;
    uwsgi_pass 127.0.0.1:9090;
  }
}
```


Create a symbolic link in the directory of Nginx so when Nginx starts this configuration
file is taken in account.

```
# ln -s /home/dev/project/my-nginx.conf /etc/nginx/sites-enabled/
# service nginx restart
```

Now you can visit http://1.2.3.4/ and see <b>502 Bad Gateway</b>.
What a bummer.

## 502 Bad Gateway

Looking at the error log of Nginx in `/var/log/nginx/error.log` I see the following:

```
upstream prematurely closed connection while reading response header from upstream, client: 192.117.127.193, server: ,
request: "GET / HTTP/1.1", upstream: "uwsgi://127.0.0.1:9090", host: "159.203.101.19"
```

Apparently what was missing was that I had to replace <b>http-socket</b> by <b>socket</b> in my-uwsgi.ini file.
I did that and restarted uWSGI using

```
# service uwsgi restart
```

The application started to work!

## The correct uwsgi config file

This time with socket and not http-socket!

```
[uwsgi]
socket    = :9090
plugin    = python
wsgi-file = /home/dev/project/app.py
process   = 3
callable = app
```


## Troubleshooting

There are two places to look for error messages: `/var/log/nginx/error.log` is the error log of Nginx
and `/var/log/uwsgi/app/my-uwsgi.log` where the log of uWSGI can be found. Assuming you called the config file
my-uswgi.ini.

For other options you might want to check out the [Deploying Flask on uWSGI](http://flask.pocoo.org/docs/0.10/deploying/uwsgi/) in the documentation.

## Comments

Got my app up and running, thank you, command "uwsgi --http-socket :9090 --plugin python --wsgi-file app.py --callabe app" worked. But there is still a typo - callale

---
fixed. thanks

