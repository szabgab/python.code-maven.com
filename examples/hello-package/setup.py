from setuptools import setup

setup(
    name="hello",
    version="0.1.0",
    packages=["hello"],
    entry_points={
        "console_scripts": [
            "hello=hello.app:say_it",
         ]
    }
)

