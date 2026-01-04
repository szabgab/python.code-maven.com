
# !pip install numpy scikit-learn matplotlib joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt



# Generate the input data uisng random numbers
def generate_data(size):
    x = np.random.randint(1, 100, size=size)
    error = np.random.rand(size)
    y = x * x + error
    print(error)
    #print(x)
    #print(y)

    X = x.reshape((-1, 1))
    #print(X)
    return X, y


#transformer = PolynomialFeatures(degree=2, include_bias=False)
#transformer.fit(X)
#X = transformer.transform(X)
## X = PolynomialFeatures(degree=2, include_bias=False).fit_transform(X)
##print(X)
#
#
#model = LinearRegression().fit(X, y)
#r_sq = model.score(X, y)
#print('coefficient of determination:', r_sq)
#print('intercept:', model.intercept_)
#print('coefficients:', model.coef_)

def main():
    size = 300
    X, y = generate_data(size)
    print(len(y))

main()
