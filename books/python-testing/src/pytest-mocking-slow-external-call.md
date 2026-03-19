# Pytest: Mocking slow external API call

We have a module called `mymath` (again) that does some computation for us.
I think it uses the Pythagoras theorem to calculate the distance from the "origin".

{% embed include file="src/examples/pytest/external-api/mymath.py" %}

It uses an external API implemented in the `externalapi.py` file to compue the square of each number.
Unfortunatelly this external API is slow.

{% embed include file="src/examples/pytest/external-api/externalapi.py" %}

We can try to run the following code. It will take 10 seconds to compute this.
When testing the mymath library we don't want to wait 10 seconds for every test-case.

```
time python use_mymath.py
```

{% embed include file="src/examples/pytest/external-api/use_mymath.py" %}


