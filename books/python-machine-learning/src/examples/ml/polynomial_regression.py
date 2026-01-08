#get_ipython().system('pip install numpy pandas scikit-learn matplotlib joblib')

import sys
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
from joblib import dump
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


def generate_data_with_noise(size, noise_level):
    x = np.arange(size)
    noise = noise_level * (np.random.rand(size)-0.5)
    y = x*x + noise
    df = pd.DataFrame(data=[x, y]).T
    df = pd.DataFrame({"x":x, "y":y})
    return df

def main():
    if len(sys.argv) != 4:
        exit(f"Usage: {sys.argv[0]} SIZE NOISE MODE")
    size, noise, mode = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]

    np.random.seed(42)
    df = generate_data_with_noise(size, noise)
    #df.plot()
    #df.plot.scatter(x='x', y='y', c='Blue');
    X = df[["x"]]
    #print(X)
    y = df["y"]
    print(y.head(3))

    x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=4)
    print(len(y_train), len(y_test))

    if mode == "P":
        model = Pipeline([
            ('poly_features', PolynomialFeatures(degree=3)),
            ('linear_regression', LinearRegression())
        ])
    elif mode == "L":
        model = LinearRegression()
    else:
        exit(f"Invalid mode {mode}")


    model.fit(x_train, y_train)
    #print(f"intercept: {model.intercept_}  coef: {model.coef_}")
    print('train coefficient of determination:', model.score(x_train, y_train))
    print('test coefficient of determination:', model.score(x_test, y_test))
    print('coefficient of determination:', model.score(X, y))

    #x1, x2 = min(df["x"]), max(df["x"]) # 0, size-1
    #y1, y2 = model.predict(pd.DataFrame({'x': [x1, x2]}))
    #plt.plot([x1, x2], [y1, y2], color="red");
    #plt.scatter(df["x"], df["y"]);
    #plt.show()
    #dump(model, 'linear.joblib')



main()
