---
title: "CLI phone book in Python using SurrealDB as a database"
timestamp: 2024-02-24T21:30:01
tags:
  - SurrealDB
description: "Show how to INSERT new data, remove data, update date in a persistent SurrealDB database."
published: true
books:
  - python
  - surrealdb
author: szabgab
archive: true
show_related: true
---


In this small example we are going to create a simple command line phone-book in Python using [SurrealDB](/surrealdb) running in a Docker container as the database.


## Install and run SurrealDB in Docker

I find it easier to manage the various technologies I use if I can run them in Docker containers. So while you could certainly run SurrealDB "natively" on your computer
I prefer to run it in a Docker container.

Based on the instruction on [Docker Hub](https://hub.docker.com/r/surrealdb/surrealdb) I ran the following command:

```
docker run --rm --pull always --name surrealdb -p 8000:8000 --user root \
   -v$(pwd)/db:/database surrealdb/surrealdb:latest \
   start --log trace --user root --pass root file://database
```

This will start a Docker container and map the database to be stored in the "db" folder of the current directory on my host computer.
This part <b>$(pwd)/db</b> defines the folder on my host computer.

I ran this on Ubuntu 23.10.

On MS Windows you'd probably need to provide the full path to the folder where you'd want to store the database.


## Python environment and requirements

We are using <b>virtualenv</b> to separate the installed Python packages from other projects and we have a small requirements.txt file:

{% include file="examples/python/surrealdb-cli-phonebook/requirements.txt" %}

I used the following commands to create the virtual environment and to install the Python library connecting to SurrealDB.

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to use this example

```
$ python phonebook.py
Usage: phonebook.py
               add NAME PHONE
               show NAME
               update NAME PHONE
               delete NAME
               list
```

```
$ python phonebook.py add foo  123
[{'id': 'people:srpx839gh1rni0vft74q', 'name': 'foo', 'phone': '123'}]


$ python phonebook.py add bar 456
[{'id': 'people:yl8p0wqpyjv8bdl9xqq8', 'name': 'bar', 'phone': '456'}]

$ python phonebook.py list
bar   456
foo   123


$ python phonebook.py update foo 789
[{'result': [{'id': 'people:srpx839gh1rni0vft74q', 'name': 'foo', 'phone': '789'}], 'status': 'OK', 'time': '186.852µs'}]


$ python phonebook.py list
bar   456
foo   789


$ python phonebook.py add foo 123456789
Exception: There was a problem with the database: Database index `people_name` already contains 'foo', with record `people:srpx839gh1rni0vft74q`


$ python phonebook.py delete foo
[{'result': [], 'status': 'OK', 'time': '158.489µs'}]

$ python phonebook.py list
bar   456

$ python phonebook.py delete bar
[{'result': [], 'status': 'OK', 'time': '191.41µs'}]
```


OK, so I could have printed out nicer responses as well, but actually these might help us understand better what's going on.




## Let's walk thought the code

At the bottom of this page you'll find the whole code together, here we'll go thought it line-by-line.


Import the necessary modules and create a an async function:


```python
from surrealdb import Surreal
import asyncio
import sys

async def main():
```

At the end of the file we have a function defined to print the usage hint we saw when we ran the program without any parameters
and we also have the invocation of the async loop.

```python
def usage():
    exit(f"""Usage: {sys.argv[0]}
               add NAME PHONE
               show NAME
               update NAME PHONE
               delete NAME
               list
""")

asyncio.run(main())
```


Connect to the database we that we are running on our own computer (in a Docker container) that listens on port 8000.

```python
    async with Surreal("ws://localhost:8000/rpc") as db:
```


Authenticate with the server. We set up this user and password in the <b>docker run</b> command.

```python
        await db.signin({"user": "root", "pass": "root"})
```


Connected to the "code-maven" namespace and in that namespace to the "phonebook" database.

There is no need to defined them. The namespace might map to a department in your company and the database to a project
or you might have some other 2-level hierarchy above the actual data.

```python
        await db.use("code-maven", "phonebook")
```

Even without defining tables and the schema of the tables we can crate indices. This one will be attached to the "name" column of the "people"
table. It is useful especially as we marked it <b>UNIQUE</b>. This will make sure the names in the phonebook are unique.

```python
        await db.query("DEFINE INDEX people_name ON TABLE people COLUMNS name UNIQUE")
```


If the user did not provide parameters, print the usage-info and exit.

If there was at least one parameter, put it in the "action" variable.

```python
        if len(sys.argv) == 1:
            usage()
        action = sys.argv[1]
```

We use the <b>query</b> method and include a query in SurrealQl (Surreal Query Language) which is quite similar to regular SQL.o
It returns a list of one element that includes the "result" which itself is a list of all the records we have in the database.

```python
        if action == "list":
            res = await db.query("SELECT * FROM people ORDER BY name")
            # print(res)
            for entry in res[0]['result']:
                # print(entry)
                print(f"{entry['name']}   {entry['phone']}")
            return
```


Add a new person-phone pair. Here we don't need to use SQL as the Python library has a convenience method called <b>create</b>.
The first parameter is the name of the table, then the following dictionary is the data.

This call will raise an exception of we try to add the same name twice. Unfortunately as of this writing the exception
is of type <b>surrealdb.ws.SurrealPermissionException</b> and does not indicate the real problem.
Luckily the text reveals it: "There was a problem with the database: Database index `people_name` already contains 'foo', with record".

```python
        if action == "add":
            if len(sys.argv) != 4:
                usage()
            (name, phone) = sys.argv[2:4]
            try:
                res = await db.create("people", {
                    'name': name,
                    'phone': phone,
                })
                print(res)
            except Exception as err:
                print(f"Exception: {err}")
            return
```


In order to fetch a specific document we use the <b>query</b> method again, but this time we have a <b>WHERE</b> clause.
We use the <b>$name</b> placeholder that will be filled by the value passed in the dictionary that follows the query.

It is important to use placeholder and not to embed the value using Python string formatting to avoid [SQL injection attacks](https://bobby-tables.com/)

```python
        if action == "show":
            if len(sys.argv) != 3:
                usage()
            name = sys.argv[2]

            res = await db.query("SELECT * FROM people WHERE name=$name", {
                'name': name,
            })
            if len(res[0]["result"]) == 0:
                print(f"Could not find '{name}'");
            if len(res[0]["result"]) > 1:
                print("More than 1 found")
            for entry in res[0]['result']:
                print(f"{entry['name']}   {entry['phone']}")
            return
```

We can use the <b>DELETE</b> statement, again with a <b>WHERE</b> clause to delete selected record(s).

```python
        if action == "delete":
            if len(sys.argv) != 3:
                usage()
            name = sys.argv[2]
            res = await db.query("DELETE FROM people WHERE name=$name", {
                'name': name,
            })
            print(res)
            return
```


Finally in order to update a field in a record we use the <b>UPDATE</b> statement.

```python
        if action == "update":
            if len(sys.argv) != 4:
                usage()
            (name, phone) = sys.argv[2:4]
            res = await db.query("UPDATE people SET phone=$phone WHERE name=$name", {
                'name': name,
                'phone': phone,
            })
            if len(res[0]["result"]) == 0:
                print(f"Could not find '{name}'");
            else:
                print(res)
            return
```


## The full example

{% include file="examples/python/surrealdb-cli-phonebook/phonebook.py" %}



