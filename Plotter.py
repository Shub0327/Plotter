# this file contains the plotting functions

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
matplotlib.use("TkAgg")


from mpl_toolkits import mplot3d

# just styles for the output
plt.style.use(['Solarize_Light2'])
# plt.style.use(['dark_background'])


def plot2d(dataX, dataY, figure, plotcanvas, master):

    ax = figure.add_subplot(111)
    ax.clear()
    ax.grid()
    ax.set_aspect('auto', anchor='C')
    ax.set(xlabel="X-axis", ylabel="Y-axis", title="x-y plotter")
    ax.plot(dataX, dataY, '-o')
    plotcanvas.draw()
    #toolbar = NavigationToolbar2Tk(plotcanvas,master)
    # toolbar.pack(side='left')
    # this is messing with the gui


def plot3d():
    # this works for 3d plotting
    fig, ax = plt.figure(), plt.axes(projection="3d")
    ax.plot3D(X, Y, Z, 'red')
    ax.grid()
    ax.set(xlabel="X-axis", ylabel="Y-axis",
           zlabel="Z-axis", title="3D plotter")
    ax.set_aspect('auto', anchor='C')
    plt.show()