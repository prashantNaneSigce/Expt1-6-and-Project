#Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

#Importing the dataset
dataset = pd.read_csv("D:\\Sem 7\\ML\\EXPTS\\1\\Salary_Data.csv")
X = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values

z = X*y #for sum(xy)
X2 = X* X #for sum(x 2)

a = ((len(X)*sum(z))-(sum(X)*sum(y)))/((len(X)*sum(X2))-(sum(X)*sum(X)))
b = (sum(y) - (a * sum(X)))/(len(X))

x_test = [1.7,2.3,3.9,4.5,5.4]
y_pred = []
for i in range(len(x_test)):
    y_pred.append((a * x_test[i]) + b)

#Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X.reshape(-1,1),y)

#Visualising the Test set results
plt.plot(X.reshape(-1,1), regressor.predict(X.reshape(-1,1)), color = "blue", label= "Best fit line")
plt.scatter(X, y, color = 'green', label = 'Actual points')
plt.scatter(x_test, y_pred, color= 'red', label = "Predicted points")
plt.title( "Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend(loc='upper left')
plt.show()