"""Subplots and Nested Plots"""


"""On the same Matplotlib figure, it is possible to display several grid graphs thanks to the subplot function which 
creates a figure automatically and divides it as much as desired.
The subplot function takes as arguments: the number of rows in the figure (numrows), the number of columns (numcols) 
and the number of the graph on which we want to position ourselves (between 1 and numrows x numcols).

Commas are optional if numrowsxnumcols<10numrowsxnumcols<10 . So subplot(211) is identical to subplot(2, 1, 1).

Example: Writing plt.subplot(4,3,2) at the beginning of a cell creates and splits a figure into 4 x 3 plot locations 
(4 rows and 3 columns) and selects the 2nd location for subsequent plot instructions.
To display a graph on the next box, just write plt.subplot(4,3,3) followed by the plt functions you want.

 Graph numbers are counted per line. The graph located on the second line and the third column, for example, will 
 therefore be graph n°6.
 When using a pyplot function, a figure is created automatically, in the standard format by default.
It is possible to create a figure with dimensions (h,l) thanks to the command plt.figure( figsize= (h, l) )."""
# ------------------------------------------------------------------------------------------------
"""Read the 'sales_data.csv' file.
Display on the same figure, of size (10,10) the following four graphs:
A barplot of the number of sales of Product 1.
A scatterplot of the number of sales of product 2 versus the number of sales of product 1.
A curve representing the number of item returns.
A histogram representing the monthly turnover."""

%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/sales_data.csv')

fig = plt.figure(figsize=(10,10))

plt.subplot(221)
plt.bar(range(len(df)), df.Product1, label = 'Product1')
plt.legend()

plt.subplot(222)
plt.scatter(df.Product1, df.Product2, c = 'm', label = "Product2")
plt.legend()

plt.subplot(223)
plt.plot(df.Return,'r-*', label = "Returns")
plt.legend()

plt.subplot(224)
plt.hist(df.Turnover, color='green', rwidth = 0.8, label = "Turnover")
plt.legend();

# --------------------------------------------------------------------------------------------------------------------
"""The graphic methods of Data Frames Pandas do not allow to directly display several different graphics within the same 
figure.
However, it may be useful to note that some methods like plot contain the subplots parameter which, if it is True, 
divides the figure into as many graphs as there are variables present. The layout parameter is used to choose the 
layout of the cells that are created."""

df.plot(y = ['Product1', 'Product2', 'Return', 'Turnover'], subplots=True, layout= (2,2),
        style = ['b--', 'm:p', 'g-.', 'c-d'], figsize=(7,7));

# --------------------------------------------------------------------------------------------------------------------
"""insert a graph inside another"""

"""On matplotlib, it is also possible to insert a graph inside another, thanks to the axes function.
Just give it as argument a list containing the x and y positions of the point at the bottom left of the 
graph to be inserted, (values between 0 and 1, independently of the axes chosen), as well as the dimensions
 of the latter (width and height , between 0 and 1).
For more visibility, it is recommended to give this axis a different color background, thanks to the 
addition of the facecolor argument. For example, plt.axes([.5, 0.6, .2, .2], facecolor='grey') creates a 
graph with a gray background whose lower left point is located on the abscissa in the middle of the 
current graph, in ordered at 60% height, and whose width and height are 20% of those of the current chart.

 For the sake of aesthetics, it is preferable to remove the tick marks from the axes of the graphs 
 inserted into others. The plt.xticks([ ]) and plt.yticks([ ]) commands are sufficient to remove the x 
 and y axes respectively."""
# --------------------------------------------------------------------------------------------------------------
"""Create a figure of size (7.7), containing the boxplot associated with the monthly turnover ('Turnover')

We are now looking to insert a second graph within this first one:

Create a second graph at position (0.65, 0.65) and size (0.2, 0.15) with a background color code #ffe5c1.

Inside, plot the histogram of the same #FFC575 color code variable.
Delete the axes and give the abscissa the label: 'Distribution'."""

plt.figure(figsize=(7,7))
plt.boxplot(df.Turnover)
plt.title("boxplot")

plt.axes([0.65, 0.65 , 0.2, 0.15], facecolor= "#ffe5c1")
plt.hist(df.Turnover, color="#FFC575")
plt.xlabel("Distribution")
plt.xticks([])
plt.yticks([]);
