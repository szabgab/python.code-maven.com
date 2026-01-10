from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import HistGradientBoostingRegressor, GradientBoostingRegressor, RandomForestRegressor
import time

def train_and_check(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=432)
    # random_state fixes the randomness

    model = LinearRegression()
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    r2 = r2_score(y_test, prediction)
    print(f"r2: {r2}")

def train_and_check_with_model(model, X, y):
        start = time.time()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=432)
        model.fit(X_train, y_train)
        prediction = model.predict(X_test)
        r2 = r2_score(y_test, prediction)
        end = time.time()
        name = model.__class__.__name__
        print(f"{name:25} score: {r2} time: {end-start}")


def get_the_data_directly():
    housing = datasets.fetch_california_housing()
    #print(housing.__class__) # sklearn.utils._bunch.Bunch
    #print(housing.feature_names)
    X = housing.data
    y = housing.target

    print(X[0])
    print(y[0])

    return X, y

def get_the_data_as_a_pandas_data_frame():
    housing = datasets.fetch_california_housing(as_frame=True)
    #print(housing.__class__) # sklearn.utils._bunch.Bunch
    #print(housing.feature_names)
    df = housing.frame
    #print(df.__class__)  # pandas.core.frame.DataFrame
    #print(df.columns)

    y = df["MedHouseVal"]
    X = df.drop(columns=["MedHouseVal"])
    print(X.head(1))
    #print(X.iloc[0])
    print(y[0])

    return X, y
     
def main():
    X, y = get_the_data_directly()
    #X, y = get_the_data_as_a_pandas_data_frame()

    train_and_check(X, y)

    # Optimizations

    # poly = PolynomialFeatures()
    # print(X.shape)
    # X = poly.fit_transform(X)
    # print(X.shape)
    # train_and_check(X, y)

    # What are the extra features?
    # room size ->  (room size)^2
    # rooms * population

    # LR = LinearRegression()
    # GBR = GradientBoostingRegressor()
    # RFR = RandomForestRegressor()

    # for model in [LR, GBR, RFR]:
    #     train_and_check_with_model(model, X, y)

    # Improve and reduce time
    #HGBR = HistGradientBoostingRegressor()
    # use all the cores of the computer to reduce time
    #RFR_all = RandomForestRegressor(n_jobs=-1)

    # Hyperparameterization
    # for max_iter in [100, 150, 200, 250, 300]:
    #     model = HistGradientBoostingRegressor(
    #         max_iter=max_iter
    #     )
    #     print(f"max_iter: {max_iter}", end=" ")
    #     train_and_check_with_model(model, X, y)

    # for learning_rate in [0.2, 0.1, 0.05, 0.001]:
    #     for max_iter in [100, 150, 200, 250, 300]:
    #         model = HistGradientBoostingRegressor(
    #             max_iter=max_iter,
    #             learning_rate=learning_rate,
    #         )
    #         print(f"max_iter: {max_iter} learning_rate: {learning_rate}", end=" ")
    #         train_and_check_with_model(model, X, y)


main()
