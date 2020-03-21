# Thiago Lima
# This program  plots a chart on screen based on these 3 formulas: f(x)=x, g(x)=x2 and h(x)=x3

"""
Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

"""

import numpy as np # this is needed because we are going to do maths formula with array values
import matplotlib.pyplot as plt # matplotlib is what is going to build the plot

x = np.linspace(1.0, 4.0, 100) # defines which values will be used on X axis

y1 = x # X axis values themselves (f(x)=x))
y2 = x ** 2 # X axis values power to 2 (g(x)=x2)
y3 = x ** 3 # X axis values power to 3 (h(x)=x3)

plt.title("Functions",fontsize = '20') # Defines a title for our plot
plt.xlabel("X",fontsize = 20) # Defines a name for the X axis
plt.ylabel("Y",fontsize = 20) # Defines a name for the Y axis


plt.plot(x,y1, 'g.', label = "f(x) = x" ) # Ploting f(x)=x 
plt.plot(x,y2, 'y.', label = "g(x) = x²") # Ploting g(x)=x²
plt.plot(x,y3, 'b.', label = "h(x) = x³") # Ploting h(x)=x³
plt.legend(loc = 'upper left',fontsize = '14') # Ploting a legend
plt.grid() # Drawing a grig on the plot - source from https://stackoverflow.com/questions/7125009/how-to-change-legend-size-with-matplotlib-pyplot
plt.show() # Display our plot on screen



"""
 ATTENTION:
 numpy and matplotlib might need to be installed in order to python be able to plot. 
 You will see the error below if numpy and matplotlib are not present:

 ModuleNotFoundError: No module named 'numpy'
 ModuleNotFoundError: No module named 'matplotlib'

 To install numpy from console you can simply use:

 pip install numpy
 Or for python3, use
 pip3 install numpy
 source: https://stackoverflow.com/questions/7818811/import-error-no-module-named-numpy
 """