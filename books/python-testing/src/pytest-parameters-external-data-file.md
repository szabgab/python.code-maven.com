# Pytest parameters external data file

We can move the data of the test-cases into external CSV or Excel file.
Let someone els update  and maintain the cases.

{% embed include file="src/examples/pytest/parametrize/cases.csv" %}

Our code then reads the data from the data-file and uses that to fill the parameters.

{% embed include file="src/examples/pytest/parametrize/test_mymath_parameters_from_csv.py" %}
