import matplotlib.pyplot as plt 

#### This is how to make custom color map 
#https://stackoverflow.com/questions/16834861/create-own-colormap-using-matplotlib-and-plot-color-scale
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)

toRGB = mcolors.ColorConverter().to_rgb
#Change the gradient of the colors 
dianasColorMap = make_colormap(
    [toRGB('purple'), toRGB('pink'), 0.33, toRGB('green'), toRGB('yellow'), 0.66, toRGB('orange')])
### END: This is how to make custom color map 

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
#RBG colors 
#https://www.december.com/html/spec/colorper.html
#ax.scatter(x_values, y_values, c=(0.36, 0.99, 0.04), s=10)
#https://matplotlib.org/stable/tutorials/colors/colormaps.html
ax.scatter(x_values, y_values, c=y_values, cmap=dianasColorMap, s=10)


#Set chart title and label axes 
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14) 

#Set the range for each axis 
ax.axis([0, 1100, 0, 1100000])

#Set size of tick labels
ax.tick_params(axis='both',which='major', labelsize=14)

plt.show()