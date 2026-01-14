
* Spam detection: given an email decide if it is a SPAM or not. Or give it a weight of how much it looks like spam.

How to Evaluate a model?

## Classification in case of 2 classes

* Accuracy (simple, only one number, maybe a bit too simple)

number of correctly classified instances / total number of instances

(TP + TN) / (TP + TN + FP + FN)

* Precision.

TP / (TP + FP)

* Recall

TP / (TP + FN)



## Classification in case of more classes

Accuracy (T1 + ... + Tn)  / (T1 + .. + Tn + F1 + ... + Fn)

Take the metrics of each class and calculate the average of that
Maybe use a weighted average if your problem is better served by it. (e.g. the cost of getting something wrong is very high)


## F1 score

A combination of Precision and Recall and it gives you only one number so it is easier to compare.

2 / (1/Precision) + (1/Recall)

Usually best used together with some other metrics. (e.g. PR curve, or ROC curve)


PR Curve (Precision Recall curve)

ROC Curve

True positive rate (TPR), also known as sensitivity or recall  `TP/(TP+FN)`

False positive rate (FPR) `FP/(FP+TN)`


AUC (Area Under the Curve) an expression people use. (for both of the above curves you want AUC to be as high as possible.

## Crossentropy

Distance between two probabilities (??)


## Regersssion metrics

## MAE - Mean Absolute Error

sum(abs(Yactual - Yexpected)) / n

## MSE - Mean Squared Error

sum((Yactual - Yexpected)^2) / n


## RMSE - Root Mean Squared Error

The square root of MSE

## R^2 - Coefficient of Determination

* 1 is perfect match
* 0 is no match at all

## Cosine similarity

How similar two vectors are to each other.



# Machine learning models

[scikit-learn algorithm cheat sheet](https://duckduckgo.com/?t=ffab&q=scikit-learn+algorithm+cheat+sheet&ia=images&iax=images)



* Logistic regression is just a variant of lienar regression

Instead of a liean function we try to fit a sigmoid function on the curve. It is still `y = f(x)` S-curve.
It will tell us the probability of being in one of two classes.


* K nearest neighbors algorithm (KNN)
    It can be used for both regression and classification (it is a non-parametric algorithm)
    for any new data point we'll predict the target to be the average of the k nearest neighbors.
    Choosing the right K is an art. Too small a K will result in overfitting, too high a K will result in underfitting.
    Methods of finding the right K including cross validation


* Support Vector Machine (SVM)
    Primarily for classification, but it can also be used for regression
    Drawing a decision boundary between data-points.
    e.g. classifying cats vs elephants based on their weight and nose length will result in a straight line.
    It is also very powerful in multi-dimensional cases where the boundaries are hyperplanes.

* Kernel functions
    * Highly complex non-linear decision boundaries.
    * Turn original features into new, better features
    * BMI
    * Implicit Feature engineering


* Naive Bayes classifier

* Decision tree classifiers

* Single Decision tree
* Gradient boosted trees
* Random forest

* Ensamble algorithm.
    * Bagging: create multiple models on different subsets of the data-set and then combining the results.
    * Boosting: training each model in sequence. Each model focuses on fixing the errors made by the previous models. (several week models one after the other can become a strong model)
        * Adaboost
        * Gradient boosting
        * xgboost

## Neural networks and Deep learning

Deep neural network


## Clustering

* K-mean clustering
    k is a hyper parameter and tells us how many clusters we are looking for.
    Finding the right k is an art and require trial and error and domain knowladge.

* Hiearchical clustering
* DBSCAN


## Dimensinality reduction
Reduce the features (or dimensions) of the data-set keeping as much information as possible.
Remove some redundant data.

e.g. do you need to have two values: the color of the left eye and the color of the right eye or is one of them enough?

e.g. Do you need a big, high-quality picture or can you use a lower resolution or a smaller picture with a lot less pixels in them?

Principal component analysis (PCA)




# Unsupervised Learning

* Clustering (Divide by similarity) eg. targetted marketing
* Association (Identify sequences) eg. customer recommendations
* Dimensionality reduction (wider dependencies) eg. big data visualization



----

conda create -n env python=3.12
conda activate env
pip install scikit-learn jupyter
jupyter lab





# Tutorials: https://numiqo.com/tutorial/roc-curve

The titanic.py is based on this video: https://www.youtube.com/watch?v=SW0YGA9d8y8

