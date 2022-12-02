"""Histogrammes"""

"""((((A histogram is a graph showing frequency distributions.
It is a graph showing the number of observations within each given interval.))))"""

# example:

# plt.hist([0, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5], range=(0, 6), bins=3);

# -------------------------------------------------------------------------------------------------------------
"""The plt.hist function displays histograms. It mainly takes as arguments:

- a series of (x) values,
the limits of the values to use (range: by default (min(x), max(x)) )
the number of intervals (bins) or the explicit limits of the intervals.
In the case where the number of intervals is the only element filled in, these will be of equal size, but intervals 
of different sizes are possible when they are filled in explicitly.
By default, intervals are open on the right, and closed on the left.
"""

# Examples:
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data/sales_data.csv")

plt.hist([0,8,10,13,15,16,16,18,32,36,39,40,43,45,48,49], bins = [0,10,20,40,50])
# ------------------------------------------------------------------------------------------------------------------
"""For more readable histograms, the rwidth parameter reduces the width of the bars with a space between them 
(percentage between 0 and 1).
"""
"""Create a histogram from 40 randomly chosen numbers between 0 and 10, thanks to the np.random.choice function, 
composed of 7 intervals, of thickness 0.8, and of orange color."""
# random.choice(arr, size=)
x = np.random.choice(11, 40)
plt.hist(x, bins = 7, rwidth = 0.8 , color = "orange");

# ------------------------------------------------------------------------------------------------------------------
"""It is possible to display the probabilistic frequencies rather than the numbers in ordinate by adding the 
argument ***density = True.***
Adding ***orientation = 'horizontal'*** plots a horizontal histogram."""


"""Display a horizontal histogram from the series of values x: [1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5], with the numbers 
between 1 and 5, 5 intervals, bars reduced by 0.6, colored pink (code '#EE3459') and replacing the numbers of 
occurrences by the corresponding probabilistic frequencies.
Give the abscissa axis the label 'Probability', the ordinate axis the label 'Values', and the graph the 
title 'Horizontal histogram'."""

x = [1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5]
plt.hist(x, range=(1,6), bins = 5,color = ['#EE3459'],rwidth=0.6, orientation = 'horizontal', density = True);

plt.xlabel('Probability')
plt.ylabel('Values')
plt.title('Horizontal histogram');
# ---------------------------------------------------------------------------------------------------------------
"""As for the bar plots, it is possible to display several histograms on the same graph, side by side or superimposed, 
by passing as argument a list of the series of values. For a histogram with the series of superimposed values, simply 
add the parameter ***histtype = 'barstacked'.****"""

"""Read the 'sales_data.csv' file.
Create a histogram from df.Product1 and df.Product2, containing 6 intervals, and whose bars are colored 
'#f27750' and '#f7bf59'.
Add the corresponding labels to each series. Give the chart the title 'Histogram 2 series', the x-axis the label 
'Sales' and the y-axis the label 'Workforce'.
Show legends on the chart."""

df = pd.read_csv('data/sales_data.csv')

plt.hist([df.Product1, df.Product2], bins = 6, color = ['#f27750', '#f7bf59'],
         label = ['Product1', 'Product2'])
plt.xlabel('Sales')
plt.ylabel('Workforce')
plt.title('Histogrammme 2 series')
plt.legend();


"""Create a histogram of the series of values df.Product1, df.Product2 superimposed, whose bars are colored 
'#0086ad', '#97ebdb', with the corresponding labels, and separated by rwidth = 0.8. The intervals used 
will be [100,200,280,325,450,600,800].
Give the graph the title '2 superimposed series', the x-axis the label 'Sales' and the y-axis the label 'Workforce'.
Show legends on the chart.
"""

plt.hist([df.Product1, df.Product2], bins = [100,200,280,325,450,600,800], color = ['#0086ad', '#97ebdb'],
         label = ['Product1', 'Product2'],  histtype = 'barstacked', rwidth = 0.8 )
plt.xlabel('sales')
plt.ylabel('Workforce')
plt.title('2 superimposed series')
plt.legend();

# ------------------------------------------------------------------------------------------------------------------
"""Pandas' plot.hist() method allows you to display a histogram directly from a DataFrame. When more than two series of 
values are present in the DataFrame, or specified in arguments, the histograms are displayed together within the same 
graph.

To separate them, just add the argument subplots=True, and set the layout of the cells with the layout parameter.

A second method, hist() also allows to display histograms, but automatically creates one histogram per column, and 
does not allow for example different colors per histogram.
"""

df.plot.hist(y=['Product1', 'Product2'], bins = 7, rwidth = 0.8 , color= ['#0c4c83', '#830c4c'], alpha=0.5);
df.plot.hist(y=['Product1', 'Product2'], bins = 7, subplots=True, rwidth = 0.8 , color= ['#0c4c83', '#830c4c'], alpha=0.5);

df.hist(column=['Product1', 'Product2'], bins = 7, rwidth = 0.8 , color= ['#0c4c83']);
