

import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn import datasets, svm
from sklearn import tree
from sklearn.naive_bayes import CategoricalNB
from sklearn.datasets import load_digits
from sklearn.naive_bayes import GaussianNB


# Question 4.3 

digits = load_digits()
print("Digits shape: ", digits.data.shape)

# flatten the images
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Split data into 50% train and 50% test subsets
Xd_train, Xd_test, yd_train, yd_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)


# Train a GaussianNB classifier and store
# the predictions over Xd_test in yd_predict 

# YOUR CODE GOES HERE
gaus_nb = GaussianNB()

gaus_nb.fit(Xd_train, yd_train)

yd_predict = gaus_nb.predict(Xd_test)

print(
f"Classification report for classifier {gaus_nb}:\n"
f"{classification_report(yd_test, yd_predict)}\n"
)
gaussian_digits_report = classification_report(yd_test, yd_predict,output_dict=True)
# Find the gaussian_accuracy rounding to two digits 
gaussian_accuracy = np.round(gaussian_digits_report["accuracy"],2)


# Based on the classification report calculate a list of digits sorted by f1-score 
# Each item should be an integer

digits = []

# YOUR CODE GOES HERE

f1 = pd.DataFrame(gaussian_digits_report).T
print(f1["f1-score"])

f1_only = f1.drop(["accuracy"], errors="ignore")
f1_only = f1_only.drop(["macro avg"], errors="ignore")
f1_only = f1_only.drop(["weighted avg"], errors="ignore")

print(f1_only["f1-score"])

sorted_f1_only = f1_only["f1-score"].sort_values(ascending=True)
print(sorted_f1_only)

for x in sorted_f1_only.index:
    x = int(x)
    digits.append(x)

#print(digits)
sorted_digits = digits
# Repeat the process for a SVM classifier

# YOUR CODE GOES HERE

clf = svm.SVC(C=1, cache_size=10000)

clf.fit(Xd_train, yd_train)

yd_predict = clf.predict(Xd_test)

print(
f"Classification report for classifier {clf}:\n"
f"{classification_report(yd_test, yd_predict)}\n"
)
svm_digits_report = classification_report(yd_test, yd_predict,output_dict=True)
# Find the clf_accuracy rounding to two digits 
svm_accuracy = np.round(svm_digits_report["accuracy"],2)

f1 = pd.DataFrame(svm_digits_report).T
print(f1["f1-score"])

f1_only = f1.drop(["accuracy"], errors="ignore")
f1_only = f1_only.drop(["macro avg"], errors="ignore")
f1_only = f1_only.drop(["weighted avg"], errors="ignore")

print(f1_only["f1-score"])

sorted_f1_only = f1_only["f1-score"].sort_values(ascending=True)
print(sorted_f1_only)







print(sorted_digits) 
print("Digits - Gaussian Accuracy", gaussian_accuracy)
print("Digits - SVM Accuracy", svm_accuracy)

