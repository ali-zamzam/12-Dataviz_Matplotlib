"""
Matplotlib is a powerful tool for plotting graphs and visualizing data. It is intended to produce graphics of all kinds 
(see here for a gallery of images produced with Matplotlib (https://matplotlib.org/stable/gallery/index.html))

Matplotlib contains the pyplot sub-library which creates an interface close to that of the commercial software Matlab and 
which contains functions very similar to it.

To display a graph, you must first import the matplotlib.pyplot module. By convention, it is always imported under the 
shortened name of 'plt'.

Once a graph has been constructed, it is the plt.show() instruction that will allow it to be viewed.
However, on a Jupyter Notebook, adding %matplotlib inline at the beginning of the page makes it possible to automatically 
display the figures when executing a cell containing a call to a pyplot command."""
# -------------------------------------------------------------------------------------------------
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# -------------------------------------------------------------------------------------------------
"""Drawing curves"""

"""A curve drawn on a graph is a set of coordinate points (x, y) between which a line is drawn: the higher the number of points, 
the smoother the graph appears.

The plot method makes it possible to draw curves which connect points whose abscissas and ordinates are provided in lists or 
tables.
To draw a graph with the 'x' values on the abscissa and the 'y' values on the ordinate, we write:

 plt.plot(x,y)"""

# -------------------------------------------------------------------------------------------------
"""(a) Plot a curve taking the values [0,2,4,6] on the abscissa and the values [1,4,4,8] on the ordinate."""
x = [0,2,4,6]
y = [1,4,4,8]
plt.plot(x,y)

# or
# plt.plot([0,2,4,6],[1,4,4,8])

"""we can see the curves and above the graphs we can see [<matplotlib.lines.Line2D at 0x16c3ae04d00>]
so to avoids displaying text outputs above the graphs Add one( ';' )at the last line of each cell """

x = [0,2,4,6]
y = [1,4,4,8]
plt.plot(x,y);

# -------------------------------------------------------------------------------------------------
"""If we insert only one list or table in the plot command, matplotlib assumes that it is a sequence of values to be 
displayed in ordinates and generates the abscissa values automatically. The abscissa(coordinates) values will be 
the positions of the ***y**** values starting from 0.
"""

"""(b) Draw a curve from the list [1,3,2,4]."""

plt.plot([0,2,1,5,3]);

# -------------------------------------------------------------------------------------------------
"""
- To add a title to the graphs, we use the title method.
- To add labels to the axes, we use the xlabel and ylabel methods."""

"""
(c) Draw a curve through the following points: (50.1) , (140.2) , (200.4).
(d) Give the figure the title 'The title of my curve'.
(e) Give respectively to the abscissa axis and the ordinate axis the labels 'abscissa' and 'ordonnees'."""

plt.title('The title of my curve')
plt.plot([50,140,200], [1,2,4])
plt.xlabel('abscissa')
plt.ylabel('Ordonnees');

# -------------------------------------------------------------------------------------------------
"""It is possible to delimit the domains of abscissas and ordinates using the axis method.
It is used as follows: """

# axis([xmin, xmax, ymin, ymax]).

"""To fix independently the domains of abscissas or ordinates one can use respectively 

xlim(xmin, xmax) or ylim(ymin, ymax).
"""

"""Draw a curve through the following points: (50.1) , (140.2) , (200.4).
Frame the graph between the abscissas 80 and 180 and the ordinates from 1 to 5."""

plt.plot([50,140,200], [1,2,4])
plt.axis([80, 180, 1, 5]);

# or:
# plt.plot([50,140,200], [1,2,4])
# plt.xlim([80,180]); plt.ylim([1,5]);

# -------------------------------------------------------------------------------------------------
"""The plot function only connects points in the order given to it, it is possible to provide it with 
several points with the same abscissa, to draw a shape."""

x = [0, 0, 1, 1, 0, 0.5, 1]
y = [1, 0, 0, 1, 1, 2, 1]

plt.plot(x,y)
plt.axis([-1,2,-1,2]);

# -------------------------------------------------------------------------------------------------
"""
The plot function also works with Pandas Series. When working with a DataFrame, we can therefore 
easily extract the columns to create graphs. 
"""
# For example:

# plt.plot(my_df.col1, my_df.col2).

# -------------------------------------------------------------------------------------------------
"""The pandas library contains methods, using Matplotlib in the background and allowing to display, 
in a fast and optimized way, a graph from the column names of the dataframe.

They also allow you to add additional parameters directly as arguments, such as a title, a delimitation 
of the axes or legends."""

# For example: 
# df.plot(x=col1, y=col2, title = "My title", ylim = [100,700]) is enough to display a complete graph.
