# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "matplotlib",
# ]
# ///

import matplotlib.pyplot as plt

x = [v / 100 for v in  range(200)]
y_linear = x
y_square = [v*v for v in x]
y_cube   = [v**3 for v in x]

#print(y_cube)


plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, y_linear, label='linear')
plt.plot(x, y_square, label='quadratic')
plt.plot(x, y_cube, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Plot numbers")
plt.legend()
plt.show()
