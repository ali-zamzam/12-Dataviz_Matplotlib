"""Multiple curves, line styles and legends"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
To superimpose several curves on the same graph, we can combine the plot instructions one after 
the other, like this:"""

# plt.plot(x,y)
# plt.plot(u,v)
# plt.plot(w,z)

"""or just use the following syntax:"""

# plt.plot(x,y,u,v,w,z)

"""
(a) Create a list called t composed of the sequence from 0 to 5, with a step of 0.2 , thanks to the np.arange function.
(b) In the same graph, plot the curves of the functions tt , t**2 and t**3 by delimiting the y-axis between 0 and 50."""

t = np.arange(0, 5, 0.2)

plt.plot(t, t, t, t**2, t, t**3)

plt.ylim([0, 50])

plt.show()
# ------------------------------------------------------------------------------------------------------------
"""
For each pair (x,y) of arguments, there is an optional third argument which is a character string which indicates the 
style and the color of the line of the curve. The possible curve styles are:

'-' : continuous line
'--': dashes
':' : dotted line
'-.' : dashes dots
The set of possible colors is:

'b' (blue)
'g' (green)
'r' (red)
'c' (cyan)
'm' (magenta)
'y' (yellow)
'k' (black)
'w' (white)`
For example, the default format is "b-" , which is a solid blue line."""

# ------------------------------------------------------------------------------------------------------------
"""(c) Plot the 3 curves from the previous question again, displaying them respectively: in red dotted lines, in green 
continuous lines and in blue dashes."""

t = np.arange(0, 5, 0.2)

plt.plot(t, t, ":r", t, t**2, "g-", t, t**3, "b--")

plt.ylim([0, 50])

plt.show()

# ------------------------------------------------------------------------------------------------------------
"""It is also possible to add point markers using symbols, which can be added to curve lines or used instead of lines. 
These symbols can also be concatenated with the colors shown above.
The possible symbols are:

'.' : dotmarker
',': pixel marker
'o': circle marker
'v': triangle_down marker
'^': triangle_up marker
'<': triangle_left marker
'>': triangle_right marker
'1': tri_down marker
'2': tri_up marker
'3': tri_left marker
'4': tri_right marker
's': square marker
'p': pentagon marker
'*': starmarker
'h': hexagon1 marker
'H': hexagon2 marker
'+': plus marker
'x': xmarker
'D': diamond marker
'd': thin_diamond marker
'|' : vline marker
'_': hline marker
In the style parameter, it is possible to specify all at once, in this order, and in a single character string: 
the color, the line style and the markers to be used for a curve.

For instance:

"r-*" for solid red line and star markers,
"y:d" for a yellow dotted line and diamond markers, etc.
When drawing a line, it is also possible to adjust its width using the linewidth argument of plot
Thus, the command plt.plot(x , y , "r--", linewidth=5, marker= 'o') displays a red dashed line, of thickness 5, with round markers.
"""
# ------------------------------------------------------------------------------------------------------------
"""
(d) Plot the 3 curves from the previous question again, displaying them respectively: in yellow 'hexagon1' markers, in a 
green line of linewidth 5 and in a blue line with diamond markers."""

plt.plot(t, t, "hy")
plt.plot(t, t**2, "g-", linewidth=5)
plt.plot(t, t**3, "b-d")
# or : plt.plot(t,t**3,'b', marker='D')

plt.ylim([0, 50])
plt.show()
# ------------------------------------------------------------------------------------------------------------
"""
- By attributing names to the curves in the 'label' argument, inside the plot command it is easy to add legends to the 
graphs, thanks to the legend method.

- The position of the legends can be chosen, thanks to the argument loc which can be 
'best', 'lower right', 'upper center', 'center left' etc...

- It is also possible to add a grid to the graph using the command plt.grid(True)"""
# ------------------------------------------------------------------------------------------------------------
"""In a graph provided with a grid, display the following curves:

1) The points (50.2), (100.3), (150.7), (200.10) connected by a blue line of linewidth(thickness) 0.8 
and '*' markers with the label 'Trajet 1'
2) The points (50.2), (100.7), (150.9), (200.10) connected by a green line of linewidth(thickness) 0.8 
and '+' markers with the label 'Trajet 2'

Give the abscissa and ordinate axes the labels 'Velocity' and 'Time' respectively.

Add legends to the chart."""

plt.grid(True)

plt.plot([50, 100, 150, 200], [2, 3, 7, 10], "b-*", linewidth=0.8, label="Trajet 1")
plt.plot([50, 100, 150, 200], [2, 7, 9, 10], "g-+", linewidth=0.8, label="Trajet 2")

plt.xlabel("Velocity")
plt.ylabel("Time")
plt.legend()  # plt.legend(loc = "upper left")  or plt.legend(loc = "lower right") ...
plt.show()
# ------------------------------------------------------------------------------------------------------------
"""By using the built-in methods of Pandas DataFrames you can also add style to the graph using the same parameter names. 
It is also possible to display several curves in the same graph, by inserting a list in the y parameter.
The style parameter can also receive a list, in order to associate each curve with its own style."""

# Example:
# my_df.plot(x= col1, y = [col2,col3], style = ["r--", "c-+"])

"""In a graph, display the curves relating to the 'Product1' and 'Product2' columns, according to 'Month', 
add a different style for each of the curves, as well as the title "Sales per month"."""

import pandas as pd

df = pd.read_csv("sales_data.csv")

df.plot(
    x="Month", y=["Product1", "Product2"], style=["m--", "c:."], title="Ventes par mois"
)
