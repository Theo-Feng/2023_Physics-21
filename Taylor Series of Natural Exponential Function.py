#This is a program that compare your Taylor Series Prediction to the real function of the natura Exponetial FUnctionl

import numpy as np
import matplotlib.pyplot as plt

def expTaylor(x, x0, nmax): 
   
    t = 0
    for n in range(nmax + 1):
        t = t + np.exp(x0) * (x - x0)**n / np.math.factorial(n)
    return t

plt.title('The comparation of Natural Exponential Function and the prdiciton by using Taylor Series')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim([-5,50])

x_list = np.linspace(-5,5,100)
print ('The number of terms of your prediction is:')
nMax = int(input())


plt.scatter(x_list, np.exp(x_list))
plt.plot(x_list, expTaylor(x_list, 0, nMax), 'red')
