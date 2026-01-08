# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "matplotlib",
#     "numpy",
#     "pandas",
#     "scikit-learn",
#     "seaborn",
# ]
# ///

# Titanic dataset by Brenda N https://www.kaggle.com/datasets/brendan45774/test-file
# Based on this vide: https://www.youtube.com/watch?v=SW0YGA9d8y8

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns

# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
def data_cleaning(df):
    df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"], inplace=True)
    #df["Embarked"].fillna("S", inplace=True)
    #df.drop(columns=["Embarked"], inplace=True)

    df["Fare"] = df.apply(lambda row: 0 if pd.isnull(row["Fare"]) else row["Fare"], axis=1)


    # Fill missing ages
    ## take the median in the given passenger class
    age_fill_map = {}
    for pclass in df["Pclass"].unique():
        if pclass not in age_fill_map:
            age_fill_map[pclass] = df[df["Pclass"] == pclass]["Age"].median()

    df["Age"] = df.apply(lambda row: age_fill_map[row["Pclass"]] if pd.isnull(row["Age"]) else row["Age"], axis=1)

    # Convert gender
    df["Sex"] = df["Sex"].map({'male': 1, 'female': 0})

    # Feature Engineering
    df["FamilySize"] = df["SibSp"]  + df["Parch"]
    df["IsAlone"] = np.where(df["FamilySize"] == 0, 1 , 0)
    df["FareBin"] = pd.qcut(df["Fare"], 4, labels=False)
    df["AgeBin"] = pd.cut(df["Age"], bins=[0,12,20,40,60, np.inf], labels=False)

    df.drop(columns=["Embarked"], inplace=True)


# For KNN k Nearest neigbor
def hypermarameter_tuning(X_train, y_train):
    param_grid = {
        "n_neighbors":range(1, 21),
        "metric": ["euclidean", "manhattan", "minkowski"],
        "weights": ["uniform", "distance"],
    }

    model = KNeighborsClassifier()
    grid_search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1)
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_


def ml_preprocessing(X_train, X_test):
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test

def evaluate(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    matrix = confusion_matrix(y_test, predictions)
    return accuracy, matrix

def plot_model(matrix):
    plt.figure(figsize=(10, 7))
    sns.heatmap(matrix, annot=True, fmt="d", xticklabels=["Survived", "Not Survived"], yticklabels=["Not Survived", "Survived"])
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted Value")
    plt.ylabel("True Value")
    plt.show()

def main():
    filename = "titanic.csv"
    df = pd.read_csv(filename)
    df.info()
    print(df.isnull().sum())
    data_cleaning(df)
    print(df.isnull().sum())

    X = df.drop(columns=["Survived"])
    y = df["Survived"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    X_train, X_test = ml_preprocessing(X_train, X_test)
    model = hypermarameter_tuning(X_train, y_train)
    accuracy, matrix = evaluate(model, X_test, y_test)
    print(f"Accuracy: {accuracy*100:.2f}")
    print(f"Confusing matrix {matrix}")

    plot_model(matrix)

if __name__ == "__main__":
    main()
