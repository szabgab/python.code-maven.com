# Docker to run the Flask app

A simple `Dockerfile` to create a Docker image. You might need a lot more complex one for your application, but the general usage will be the same.

{% embed include file="src/examples/pytest/docker/Dockerfile" %}

We also have a `.dockerignore` file to make the building of the image faster.

{% embed include file="src/examples/pytest/docker/.dockerignore" %}

We can (and probably should) build the image manually with the following command.
This will speed up the tests as the test will be able to reuse this image.
The name of the image does not really matter here.

```
$ docker build myimg -t .
```

We can run the container manually

```
docker run --rm -v$(pwd):/workdir -p5001:5000 myimg
```

Then we can access the web site from our computer using this address:

http://localhost:5001

