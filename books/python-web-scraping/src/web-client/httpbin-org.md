# httpbin.org

* [httpbin.org](https://httpbin.org) a website to practice various URL requests
* [source code](https://github.com/Runscope/httpbin) of httpbin.

You can't always depend on the public service and you don't want to overwhelme it with lots of requests. Luckily the whole system is packed into a Docker image and you can run it locally:


## Run httpbin locally

Start as:

```
docker run --rm -p 80:80 --name httpbin kennethreitz/httpbin
```

Then run the code:

```
python client.py
```

To stop the Docker container open another terminal and execute

```
docker container stop -t0 httpbin
```

