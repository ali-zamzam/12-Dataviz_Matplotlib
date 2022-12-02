"""Scatter plots"""

"""The scatter function allows you to plot point clouds. It is used in a similar way to plot."""
plt.scatter(range(0, 7), [8, 7, 6, 5, 6, 7, 8], color="red", marker="*", s=40)

"""It is also possible to draw two scatter plots simultaneously on the same graph by using the plt.scatter command 
twice one after the other.
Parameters c (for color) and s (for size) can be:

Let be unique elements (c = 'red')
Consider lists of the same size as the number of points (c = ['red', 'green', 'blue'] if 3 points for example).
The list of colors available on Matplotlib might seem limited to some, it is possible to use HEX color codes to color 
any type of graph."""

# --------------------------------------------------------------------------------------------------------------
"""Create the lists x of abscissas from 1 to 5, then the following lists y1 and y2: [0,2, 3, 8, 15], [5, 8, 11, 16, 22].
Represent the points of coordinates x* and y1 in yellow and of increasing sizes: 30, 60, 90, 120, 150.
Represent points with coordinates x and y2, size 40 and colors: ['#d248a2', '#8b48d2', '#48a5d2', '#4dd248', '#d1d248']."""

x = [1, 2, 3, 4, 5]
y1 = [0, 2, 3, 8, 15]
y2 = [5, 8, 11, 16, 22]
plt.scatter(x, y1, c="yellow", s=[30, 60, 90, 120, 150])
plt.scatter(x, y2, c=["#d248a2", "#8b48d2", "#48a5d2", "#4dd248", "#d1d248"], s=40)

# --------------------------------------------------------------------------------------------------------------
"""When working with dataframes, the **c parameter** is used to color the points with respect to the values taken by the 
points in a column, by inserting this column as an argument to the c parameter."""

"""Display a scatter plot of abscissa df.Product1 and ordinate df.Product2, of size 30, and coloring the points 
relative to df.column3."""

import pandas as pd

df = pd.read_csv("data/sales_data.csv")
plt.scatter(df.Product1, df.Product2, c=df.Return, s=30);

# --------------------------------------------------------------------------------------------------------------
"""Here is the equivalent graph obtained directly from the plot.scatter() method of pandas dataframes."""

df.plot.scatter(x="Product1", y="Product2", c="Return", s=30, cmap="viridis");
