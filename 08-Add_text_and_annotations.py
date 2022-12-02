"""Add text and annotations"""

"""It is possible to add text to graphics by indicating the coordinates where you want to display the beginning 
of it, using the plt.text command.
"""
# Example: Using the plt.text Command
# plt.text(3, 5,'myText') displays 'myText' horizontally from point (3,5) on the graph.


%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

"""Display the curve of the function f(x)=cos(2πx)f(x)=cos(2πx) over the interval [0,2].
Clip the y-axis to [-2, 2].
Add the text 'local maximum', at point (0.8,1.1)."""
t = np.arange(0.0, 2.0, 0.01)
# We create the sequence of points between 0 and 2, with a step of 0.01

plt.plot(t, np.cos(2*np.pi*t))
# We draw the curve of the function f(t)cos(2*pi*t)
plt.ylim(-2,2)
# We delimit the ordinate axis between -2 and 2.

plt.text(0.8, 1.1, 'maximum local');
# We display the text 'local maximum', at the point (1.5, 1.1) of the graph.
# -------------------------------------------------------------------------------------------------------------------
"""To add an annotation with a descriptive arrow pointing to a specific point on the graph, we use plt.annotate.
This method takes the following arguments:

the text you want to display.
xy, which indicates the coordinates where the point to annotate is located.
xytext, which indicates the coordinates of the point where the text starts.
arrowprops, which are the properties of the annotation arrow between { }: colors, arrow size, arrow style, etc..."""

# Example: Using the plt.annotate Command
# plt.annotate('Limit', xy=(1, 2), xytext=(1, 2.5), arrowprops={'facecolor':'blue'} )
# displays a blue arrow pointing to the coordinate point (1, 2) and displays the text 'Limit' at the point (1, 2.5).

"""In a grid graph, display the curve of the function f(x)=sin(2πx)xexp(-x)f(x)=sin(2πx)xexp(-x) over the interval 
[0 , 5] .
Display the curves of the functions exp(-x)exp(-x) and -exp(-x)-exp(-x) on the same interval.
Add an annotation arrow, green, at point (1.5, 0.25), with the text 'Asymptote: exp(-x)' starting at point (2, 0.5).
Add an annotation arrow, colored red, at point (1.5, -0.25), with the text 'Asymptote: - exp(-x)' starting at point 
(2, -0.5)."""


plt.grid(True)

x = np.arange(0., 5., .01)

y = np.sin(2*np.pi*x) * np.exp(-x)
plt.plot(x, y)
plt.plot(x, np.exp(-x))
plt.plot(x, -np.exp(-x))

plt.annotate('Asymptote: exp(-x)', xy=(1.5, 0.25), xytext=(2, 0.5), 
            arrowprops={'facecolor':'green'} )
# On crée une flèche orientée vers le point (1.5, 0.25), avec l'annotation 'Assymptote: exp(-x)'
# qui débute au point(2, 0.5). Puis on lui donne la couleur verte.

plt.annotate('Assymptote: - exp(-x)', xy=(1.5, -0.25), xytext=(2, -0.5), 
            arrowprops={'facecolor':'red' } );
# -------------------------------------------------------------------------------------------------------------------
x = np.linspace(-6, 2, 40)
# We create a sequence of 40 points in the interval [-6, 2]

plt.grid(True, linestyle = '--')
# We add a grid to the graph

plt. plot(x, x**2, 'b', label='$x^2$')
# Draw the curve x^2 and give it the corresponding label for the legend.

plt.plot(x,np.exp(-x), 'g--', label='$exp(-x)$')
# We draw the curve exp(-x) in dotted lines and we give it the corresponding label for the legend.

plt.axis([-5,2,0,25])
# We modify the amplitude of the axes

plt.plot([-3, -2, -2, -3, -3],[5, 5, 10, 10, 5],'r', alpha = 0.6)
# We create the square that surrounds the part of the graph that we are going to reproduce
# The 'alpha' argument gives the opacity percentage of the plot (1 opaque, 0 transparent invisible)

plt. annotate('Zoom', xy=(-1.8, 7.5), xytext=(-0.5, 7.5),
            arrowprops={'facecolor':'red'} )
# We create the red arrow, with the text 'Zoom' pointing to the point (-1.8, 7.5).

plt.title('My balance sheet graph')
#We give a title to the graph

plt.legend()
# We display the captions

plt.axes([.55, 0.4, .2, .2])
# We create a new graph inside the previous one,
# whose lower left corner starts at point (0.55, 0.4) in relative distance,
# where 0 represents the origin, and 1 the end of the axis.
# This graphic will have a width and a height representing 20% ​​of the width
# and the height of the original graphic.

#From then on, the 'pyplot' commands will only apply to this new plot.

plt.plot(x,x**2, 'b')
plt.plot(x,np.exp(-x), 'g--')
# We draw the same curves as before.

plt.axis([-3,-2,5,10])
# But we limit the axes to the coordinates of the square we drew.

plt.xticks([])
plt.yticks([]);
# We remove the tick marks on the new graph.
