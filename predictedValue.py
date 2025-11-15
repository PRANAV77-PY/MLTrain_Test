import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3,1,100)
y = numpy.random.normal(150,40,100)/x

x_train = x[:80]
y_train = y[:80]

x_test = x[80:]
y_test = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(x_train,y_train,4))

print(mymodel(5))