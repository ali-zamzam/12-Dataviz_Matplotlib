"""Bar Graphics (Bar plots)"""

"""
The plt.bar function allows you to draw vertical bar charts with a single or multiple series of values. 
To display a bar plot, simply enter into the function as the first argument the positions of the abscissa axis on
which the bars will be centered, and as the second argument the heights of the bars.
The most important additional parameters are: the color of the inside of the bars (color) and the relative width of 
each bar (default width 0.8, ie 20% empty space between each bar).
"""

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# range() --> the positions of the abscissa axis , range(3) for a list with 3 values
# the list is the highest of the bar
plt.bar(range(3), [2, 3, 5] , color = 'green', width = 0.6);

plt.bar(range(4), [2, 3, 4, 5] , color = 'white', width = 0.6, edgecolor = "red");

"""Like all pyplot functions there are many other parameters like:

edgecolor: the color of the borders.
linewidth: the thickness of the lines.
yerr: the values of the error bars.
ecolor: the color of error bars.
align: the abscissa axis corresponds to the center of the bar, or the left edge.
orientation: 'horizontal' to display a horizontal bar plot.
hatch = '/': the hatches. Possible values: '/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'."""

# --------------------------------------------------------------------------------------------------------------------------------
"""Display the column of dataframe  in the form of a bar plot."""

import pandas as pd

df = pd.read_csv("data/sales_data.csv")

plt.bar(range(len(df)), df.Product1);

# --------------------------------------------------------------------------------------------------------------------------------
"""It is possible to display several diagrams on the same graph, by calling as many plt.bar commands one after the other.

As for the plot method, it is possible to give a label to a bar plot by specifying it as an argument, to display the 
legends."""

"""Create a graph displaying two bar plots, one blue and one green, labeled "Example 1" and "Examples 2" with the 
respective lists [1,3,5,7,9],[5,2,7,8 ,2] and [2,4,6,8,10],[8,6,2,5,6] as arguments.
Give the abscissa axis the label 'Number', and the ordinate axis the label 'Height'.
Show legends and give the chart the title 'My bar chart'."""

plt.bar([1,3,5,7,9],[5,2,7,8 ,2], color = "g" ,label= "example 1")
plt.bar([2,4,6,8,10],[8,6,2,5,6], color = "b", label= "example 2")

plt.xlabel("Number")
plt.ylabel("Height")
plt.legend(loc="upper right")
plt.title("My bar chart");

# --------------------------------------------------------------------------------------------------------------------------------
"""It is also possible to create a bar plot from 2 series of values, superimposed on each other, by adding the bottom 
parameter to the second plt.bar() call."""

# Example:

# plt.bar(x, y1); plt.bar(x, y2, bottom = y1)
# superimposes the series y2 on y1.

"""Display one above the other, two columns of dataframe (the bottom is column 1).
Add legend."""

plt.bar(range(len(df)), df.Product1, label = "col1")
plt.bar(range(len(df)), df.Product2, label = "col2", bottom = df.Product1)
plt.legend();

# or on the same line we put (;) to seperate the two plt.bar functions
# plt.bar(range(len(df)), df.column1, label = "col1") ; plt.bar(range(len(df)), df.column2, label = "col2", bottom = df.column1)
# plt.legend();
# --------------------------------------------------------------------------------------------------------------------------------
"""If you prefer to obtain a graph with bars side by side and not stacked, you just have to play with the abscissas of 
the bars and their thickness.

It is also possible, with any graph, to modify the graduations of the axes thanks to the xticks and yticks methods."""

# Example :
# The command

# plt.xticks([1,2,3], ['one', 'two', 'three'])
# replaces the x-axis tick marks with the three tick marks 'one', 'two', 'three'.

"""Create a variable called barWidth which is 0.4
Create a x1 sequence of numbers from 0 to 11
Create a list x2 whose elements are the elements of x1 plus barWidth
Create in the same figure, 2 bar plots, with respective abscissa x1 and x2 and thickness barWidth , and 
displaying the number of type 1 and 2 products sold over the first 12 months.
Display on the abscissa axis only the following months: 'January', 'March', 'May', 'July', 'September', 'December'."""

barWidth = 0.4

x1 = range(5)
x2 = [r + barWidth for r in x1 ]


df5 = df.head(5)

plt.bar(x1, df5.Product1, width = barWidth, label = "Produit1")
plt.bar(x2, df5.Product2, width = barWidth, label = "Produit2")
plt.xticks([0,2,4,6,8,11], ['Janvier', 'Mars', 'Mai', 'Juillet', 'Septembre', 'Decembre'])
plt.legend();

# --------------------------------------------------------------------------------------------------------------------------------
"""To directly display a bar plot from a Pandas Data Frame, you can use the **plot.bar()** method which will automatically
display a bar chart from the columns indicated in the y parameter.
By default, the bars are displayed side by side, but it is possible to use the **argument stacked = True**, to stack them. 
It should be noted that this method, although very effective, allows less customization in the details and the choice 
of parameters, so it is recommended for the production of fast and simple graphics."""

# Here is an example of its use:

df.head(6).plot.bar(x = 'Month', y=['Product1', 'Product2', 'Return'], stacked=True,
                     rot=0)
plt.xticks(range(6), ["January","February","March","April","May","June"])
plt. legend();
