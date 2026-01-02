# Split data set to evaluate the model


* How can we really evaluate the model?
* We can check if using the model on the input data we trained it on will get predictions similar to what the real results were. If the error is too big then we know the model is not that good. If the predictions are very close to the real values then we might be happy. It is like testing students with the very same problems we have solved in the class-room. It gives you some level of confidence in the student, but how do you know if they can use that knowledge to solve other problems. How can you evaluate if they learned the material or only learned the answers to the specific questions you had in the class?

What we really would like to see is how the students (or our model) will fare with similar but not exactly same situation.

* We need a new set of input data with the corresponding results.
* Then using the model we can make predictions and we can compare the predictions to the actual data.

* Instead of trying to get more data, what we usually do is take the original data-set and split it into two parts.
* One part we'll use to train the model and the other part we'll use to test the model.


* In supervised learning you receive a dataset of N elements (N rows) in each row you have X features (column) + 1 or more results y (also column)
* You can divide the rows into two parts: training and testing.
* You use the training part to train your model and you use the testing part to check how good your model can predict other values.
* `train_test_split()` of `scikit-learn` can do this.

* **examples/ml/basic_linear_regression_more_data.ipynb**

* fix the seed by setting `random_state` to any fixed non-negative integer
* `stratify` splitting for classification of inbalanced datasets


---

* train_test_split
