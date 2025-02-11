import pandas as pd

data = pd.read_csv("diabetes.csv")

data.head()

# print total null values
print("Null values are :")
for col in data.columns:
  print("{} : {}".format(col, sum(data[col].isnull())))

# summarize data
data.hist(figsize = (30, 30))

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 5)


gnb = GaussianNB()
y_pred = gnb.fit(x_train, y_train).predict(x_test)

print("Number of mislabeled points out of total %d points : %d"
      % (x_test.shape[0], (y_test != y_pred).sum()))
print("Accuracy : %.3f" % ((y_test == y_pred).sum() / x_test.shape[0] * 100))
