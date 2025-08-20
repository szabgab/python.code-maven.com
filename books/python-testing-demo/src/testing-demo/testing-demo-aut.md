# AUT - Application Under Test

Given the following module with two functions, how can we verify that these functions work properly.

The `mymath.py` file contains the following:

{% embed include file="src/examples/testing-demo/mymath.py" %}


You probably noticed that the operators in our functions are incorrect.
The function called `add` is expected to add two numbers, but the implementation has a bug. It actually multiplies the two numbers.
The function called `multiply` on the other hand actuall adds the operands together.

I know it is a very obvious issue, but it is great as it allows us to see the mechanics of testing without getting distracted by
a complex implementation and a complex problem.

Rest assured, the mechanism of the testing would be the same even if our function was calculating the moon-landing trajectory.

Testing is not rocket science.

