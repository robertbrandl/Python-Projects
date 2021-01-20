#Robert Brandl
#Goal: develop machine learning skills (mean, median, etc.) using numpy, scipy
import numpy
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pandas 
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

#using mean, median, and mode
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)
x = numpy.median(speed)
print(x)
x = stats.mode(speed)
print(x)

#standard deviation and variance (stand. dev. squared)
speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)
speed = [32,111,138,28,59,77,97]
x = numpy.var(speed)
print(x)

#percentile  - how many at or below
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75) #find the value representing the percentile
print(x)
x = numpy.percentile(ages, 90)
print(x)

#generating data sets, histograms, and data distribution
x = numpy.random.uniform(0.0, 5.0, 250) #low, high, quantity of data
print(x)
plt.hist(x, 5) #data, number of bars for a histogram
plt.show()
x = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()

#normal data distribution
x = numpy.random.normal(5.0, 1.0, 100000) #average or mean, standard deviation, number of values
plt.hist(x, 100)
plt.show()

#scatter plots
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x, y) #x and y points
plt.show()

x = numpy.random.normal(5.0, 1.0, 1000) #using random data to generate scatterplot
y = numpy.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)
plt.show()

#linear regression
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
print(r)#r is relationship between x and y or coefficient of correlation between -1 to 1
speed = myfunc(10)#predict future values or not given values
print(speed)

#polynomial regression
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
myline = numpy.linspace(1, 22, 100)#start position, end position
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
print(r2_score(y, mymodel(x)))#r^2 value indicates relationship
speed = mymodel(17)#predict future values
print(speed)

#multiple regression: more than one independent variable, predicting value based on 2 or more variables
df = pandas.read_csv("cars.csv")
X = df[['Weight', 'Volume']]
y = df['CO2']
regr = linear_model.LinearRegression()
regr.fit(X, y)
#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)
print(regr.coef_)#coefficient matching how one of the x will affect the y (weight coefficient, volume coefficient)

#scaling using sklearn
scale = StandardScaler()
scaledX = scale.fit_transform(X)
regr = linear_model.LinearRegression()
regr.fit(scaledX, y)
scaled = scale.transform([[2300, 1.3]])
predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)

#train/test - 80% training and 20% testing
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
plt.scatter(x, y)
plt.show()

train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
plt.scatter(train_x, train_y)
plt.show()

plt.scatter(test_x, test_y)
plt.show()

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))#using points, determine polynomial is best fit
myline = numpy.linspace(0, 6, 100)
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

r2 = r2_score(train_y, mymodel(train_x))#get relationship from r2 value of training data
print(r2)
r2 = r2_score(test_y, mymodel(test_x))#gets relationship from r2 value of testing data
print(r2)
#if values match, then model is acceptable
print(mymodel(5))#after that, you can start making predictions
