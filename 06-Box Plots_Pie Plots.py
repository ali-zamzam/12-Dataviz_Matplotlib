"""Box Plots(Boîtes à Moustaches) and Pie Plots(Camemberts)"""


"""Box plots are much appreciated and used graphs, especially during descriptive analyzes of continuous data.
The plt.boxplot function displays box plots on a graph.
It takes as argument one or more sequences of values joined together in another sequence.
The main box gives the first and last quartile boundaries, the middle red bar shows the median.
The whiskers go to the most extreme value in the limit of 1.5 times the height of the box. The points beyond the 
whiskers are represented by +, they are outliers."""

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example :
plt.boxplot([[1, 2, 3, 4, 5], [7, 5, 8, 4, 9, 5, 7]])

# -----------------------------------------------------------------------------------------------------------------
"""Display the box plots created from the series representing the number of sales of Product 1 and Product 2.
Give a title to the graph."""

df = pd.read_csv('data/sales_data.csv')

plt.boxplot([df.Product1, df.Product2])

plt.title("sales_boxplot");

# -----------------------------------------------------------------------------------------------------------------
"""In descriptive statistics, it is often necessary to create more elaborate boxplots, depending for example on a 
qualitative variable."""

"""Create a new variable 'Month', which keeps only the month of the 'Month' column. It will therefore be necessary
 to extract for each element of 'Month', from the 4th to the last character of the string.

Create a blank list l.

Thanks to a loop over all the months of the year, successively add to l the Series containing the turnover ('Turnover') extracted for each of the 12 months.

Display the boxplot of the series contained in l.

Add the months in graduation of the abscissa axis."""

df['Mois']= df.Month.apply(lambda x : x[3:])

l=list()
for i in df.Mois.unique():
    l.append(df[df['Mois'] == i]['Turnover'])
plt.boxplot(l)
plt.xticks(range(7),df.Mois.unique())

plt.show()
# -----------------------------------------------------------------------------------------------------------------
"""The boxplot() method of Pandas DataFrames, allows to display box plots for each column indicated in the column 
parameter, for all the columns otherwise. The by parameter is the most interesting, it displays a boxplot for 
each category of a qualitative variable.
"""
"""Good to know: The figsize parameter is used to modify the dimensions of the figure containing the graph."""

"""Using the boxplot() method, easily recreate the previous plot in a figure of size (7.7)."""

df.boxplot(column= 'Turnover', by='Mois', figsize= (7,7));

# -----------------------------------------------------------------------------------------------------------------
"""Pie Charts"""

"""Pie charts are circular diagrams divided by sectors (wedges). This is an efficient way to represent information 
when one is primarily interested in comparing one slice with the whole pie rather than between two slices.

The pie function allows you to draw circular diagrams from a sequence X.
Each element xixi of X is represented by a share proportional to xixi /sum(X). If the sum of the elements 
of X is less than 1, the pie chart is represented using the values of X directly, no normalization is 
performed, leaving an empty space.

 Pie charts display best if the figure is enlarged and square.
When using a pyplot function, a figure is created automatically, in the standard format by default.
The figure can be created with dimensions (h,w) thanks to the command plt.figure( figsize= (h, w) ).
 Adding to plt.pie the argument labels allows to give names to the different parts of the pie chart."""
# -----------------------------------------------------------------------------------------------------------------
"""Create a figure with dimensions (6, 6).
Create a list x including the numbers [1, 2, 3, 4, 10].
Display a pie chart from x, and label it ['A', 'B', 'C', 'D', 'E'].
Show legends on the chart."""

plt.figure(figsize=(6,6))

x = [1, 2, 3, 4, 10]
plt.pie(x, labels= ['A', 'B', 'C', 'D', 'E'] )
plt.legend();

# -----------------------------------------------------------------------------------------------------------------
"""Many parameters allow you to customize your pie chart.

explode: list of the same size as the data sequence, allows one or more parts to be moved away from the center 
by indicating by which fraction of the radius each part must be moved away (0 by default).
colors: sequence of colors to use for the parts.
labeldistance: the distance of the labels from the center (> 1 to be outside the circle).
autopct: a function (lambda) that takes the calculated percentage for a share and returns what should be 
displayed for that percentage.
pctdistance: the distance from the center at which the previous percentage should be displayed 
(1 = on the circle).
shadow = True: indicates to display a shadow."""

# -----------------------------------------------------------------------------------------------------------------
"""Create a figure of size (7, 7).
Display a pie chart from the turnover of the first 6 months of the period, with the labels from 
'Jan' to 'June' and the colors: red, orange, yellow, green, blue, purple.
Move the fourth part away from the center by 0.2.
Display the percentage of each share, rounded to 2 decimal places, followed by the '%' sign.
Display these percentages at a distance of 0.7 from the center, and the labels at a distance of 1.2.
Add shadows to the camembert.
Show legends on the chart."""


plt.figure(figsize = (7, 7))

plt.pie(x = df.head(6).Turnover, labels = ['Janv', 'Fev', 'Mars', 'Avril', 'Mai', 'Juin'],
           colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple'],
           explode = [0, 0, 0, 0.2, 0, 0],
           autopct = lambda x: str(round(x, 2)) + '%',
           pctdistance = 0.7, labeldistance = 1.2,
           shadow = True)
plt.legend();
