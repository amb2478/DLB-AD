#required packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn import metrics
from sklearn import linear_model
from scipy.special import expit
from sklearn.metrics import classification_report, confusion_matrix

#import data
df=pd.read_csv('/Users/allisonbeers/Downloads/total.csv')
#df['scan_date'] = pd.to_datetime(df['scan_date'], format='%m/%d/%y')
#df['dod'] = pd.to_datetime(df['dod'], format='%m/%d/%y')
df.drop(['scan_date', 'dod', 'Measure.volume', 'Braak_Lewy', 'Braak_NFT', 'Braak_AB'], axis=1, inplace=True)
X_train, X_test, y_train, y_test = train_test_split(df.drop('Group', axis=1), df['Group'], test_size=0.30, random_state=101)

#logistic regression model
lr=LogisticRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
print("LR Training:", lr.score(X_train, y_train))
print("LR Test:", lr.score(X_test, y_test))
print(classification_report(y_test, y_pred))

#SVM model
svm = svm.SVC(kernel='linear')
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)
print("SVM Training:", svm.score(X_train, y_train))
print("SVM Test:", svm.score(X_test, y_test))
print(classification_report(y_test, y_pred))

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier

# Define the classifiers
classifiers = [LogisticRegression(), LinearSVC(), SVC(), KNeighborsClassifier()]

# Fit the classifiers
for c in classifiers:
    c.fit(X_train, y_train)

# Plot the classifiers
plot_4_classifiers(X_train, y_train, classifiers)
plt.show()

# #plots models
# clf=linear_model.LogisticRegression(C=1e5)
# clf.fit(X, y)
# preds = clf.predict(X_test)
# #print("LR Training:", clf.score(X_train, y_train))
# #print("LR Test:", clf.score(X_test, y_test))
# plt.clf()
# plt.scatter(X.ravel(), y, color='black', zorder=20)
# X_test = np.linspace(-5, 10, 300)

# loss = expit(X_test * clf.coef_ + clf.intercept_).ravel()
# plt.plot(X_test, loss, color='red', linewidth=3)

