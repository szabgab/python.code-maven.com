
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











