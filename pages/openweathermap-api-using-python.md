---
title: "Using the Open Weather Map API with Python"
timestamp: 2018-10-27T21:00:01
tags:
  - configparser
  - requests
published: true
author: szabgab
archive: true
---


In [Using the Open Weather Map API with curl](/openweathermap-api-using-curl) we saw how to fetch the weather using `curl`.
Now we are going to use Python as that will make it easier to use this as part of a larger application.
Before you read this article, make sure you read the one using `curl`.



## Configuration file

It is better to store all API keys and passwords in separate configuration files that are usually not stored and distributed together
with the source code. That gives a lot of flexibility.

So we create a file called <b>config.ini</b> with the following content:

```
[openweathermap]
api=wkfhshoiaslv
```

Where of course I put the API-key from [Open Weather Maps](https://home.openweathermap.org/api_keys).

In the code we have the `get_api_key` function that uses the [configparser](https://docs.python.org/3/library/configparser.html)
standard library to read the INI file.

We also use the [requests](http://docs.python-requests.org/en/master/) module to send the API request and then to convert the
resulting `JSON` into a Python dictionary.

## The code

{% include file="examples/python/get_weather.py" %}

At the end we show how to access the individual temperature data and we also print the whole data structure:
(I've changed the layout of the output to make it more readable.)

## The dumped data

```
{
   'coord': {
       'lon': 19.04,
       'lat': 47.5
   },
   'weather': [{
        'id': 701,
        'main': 'Mist',
        'description': 'mist',
        'icon': '50n'
   }],
   'base': 'stations',
   'main': {
       'temp': 3,
       'pressure': 1016,
       'humidity': 89,
       'temp_min': 3,
       'temp_max': 3
   },
   'visibility': 5000,
   'wind': {
       'speed': 2.1, 
       'deg': 350
   },
   'clouds': {
       'all': 75
   },
   'dt': 1518195600,
   'sys': {
        'type': 1,
        'id': 5724,
        'message': 0.0023,
        'country': 'HU',
        'sunrise': 1518155884,
        'sunset': 1518191922
   },
   'id': 3054643,
   'name': 'Budapest',
   'cod': 200
}
```

## Conclusion

Once we have this basic solution we can integrate this code into a larger application or change the requested URL to
match other API end-points.

