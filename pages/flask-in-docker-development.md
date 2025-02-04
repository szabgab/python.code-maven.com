---
title: "Flask in Docker - development"
timestamp: 2019-04-19T07:30:01
tags:
  - Dockerfile
  - flask
published: true
books:
  - docker
author: szabgab
archive: true
---


In this example we'll see how to use Docker for development and for a simple way of distibution.



## Directory layout

```
.
├── Dockerfile
├── README
├── Release
└── web
    ├── app.py
    └── templates
        └── main.html
```

## Code and templates of the application

{% include file="examples/docker-flask/web/app.py" %}

{% include file="examples/docker-flask/web/templates/main.html" %}

If you install Python and the requirements directly on your computer and cd to the root of this project
then you can start the development server with the following command:

```
FLASK_APP=web.app FLASK_DEBUG=1 flask run --host 0.0.0.0 --port 5000
```

You can then access the web application via http://localhost:5000/ .


## Docker image for development

We have cerated a Dockerfile with everything needed to develop and run this application:

{% include file="examples/docker-flask/Dockerfile" %}

To create a Docker image for development based on the Dockerfile run

```
docker build -t mydocker .
```

This will create an image called "mydocker".

To run this as a Docker container execute the following:

```
docker run -v $(pwd):/opt -p 5001:5000 --rm mydocker  flask run --host 0.0.0.0 --port 5000
```

This will launch a Docker container based on the "mydocker" image.
The `-v $(pwd):/opt` will map the current working
directory on your computer to the /opt directory inside the Docker image. (The Dockerfile set /opt
as the working directory of Docker so when it starts to run /opt will be the current working directory
inside Docker that will allow flask to find the right module.

The `-p 5001:500a` will map port 5000 of the Docker container to port 5001 of the host computer.
(The could be the same number, I just wanted to make it easier to see which port is which.)

`--rm` tells docker to remove the container once it finished running.

`mydocker` is the name of the image we created earlier.

Then on the command line we pass the command to launch flask: `flask run --host 0.0.0.0 --port 5000`


You can access the site via http://localhost:5001/

Now, as in the Dockerless mode, if you change one of the files of the application on the disk,
the server will restart and the application will be reloaded. You will also get helpful error messages
on the web page.

All thanks to the `ENV FLASK_DEBUG=1` line in the Dockerfile telling Flask it is in development mode.

If you need to access the command line of the docker container you can launch it in interactive mode without
running flask.

```
docker run -it --rm mydocker
```

## Release (Distribution / Deployment)

Once you are done with development you will probably want to create a Docker image that is self-contained.
That in addition to all the dependencies also contains your application.

For this we have a second Dockerfile called Release that layers on top of the docker image we used for development.
It clears the environment setting development mode, copies the whole "web" directory to the Docker image
and tells docker what to run when it is launched.

{% include file="examples/docker-flask/Release" %}


We can create the new docker image with the following command:

```
docker build -t myrelease . --file Release
```

Then we can launch the Docker container from anywhere on our filesystem with the following command:

```
docker run  -p 5002:5000 --rm myrelease
```


You can access the site via http://localhost:5002/

If you encounter an error now (e.g. visit a not-existing page) you will get a plain error page
without any details of the application. Just as you would expect from a public application.


This Docker image could be now distributed to whoever needs to run this code or could be deployed on
a server, but only for demo purposes as we have used the built-in server of flask which was designed
for development, but not suitable for production.



