# Testing Flask in Docker

We create a small Flask-based web application.

1. First we test it internally using the `test_client` feature flask provied.
1. Then we start the web application and test it with external tools.

We could start the web application natively on our operating system, but for more complex applications
it will be probably a good idea to use a container to make it repeatable.

So we create a Docker image and run the application in a Docker container.

Actually we let the test build both the image and run the container.
