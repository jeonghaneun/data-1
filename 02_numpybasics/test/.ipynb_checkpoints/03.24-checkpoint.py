import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.1) #x axis domain // domain = xaxis / range = y axis
x1 = 3
tangent_range = np.linspace(x1-2, x1+2,10)

def f(x):
  return x**2

def slope(x):
  return 2*x

def tangent_line(x, x1, y1):
  return slope(x1)*(x-x1) + y1

plt.figure()
plt.plot(x,f(x))
plt.scatter(x1,f(x1), color='red', s=20)
plt.plot(tangent_range, tangent_line(tangent_range, x1, f(x1)), color= 'red' , linewidth=2)
plt.savefig('image/diff_img.png')


