
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

def load_and_prepare_cmd(filename):
    """Reads in a csv file using pandas, calculated g minus r values, and filters entries to be within range."""
    file = pd.read_csv('fieldA.csv', header = 0)
    file['gr'] = file.g - file.r
    fltrd = file[(-.5 < file.gr) & (file.gr < 2.5) & (14 < file.g) & (file.g < 24)]
    global g
    global gr
    g = fltrd.g
    gr = fltrd.gr
    return g, gr

def plot_hess(bins):
    """Takes in g-r and g data to construct Hess diagram with variable bin number."""
    plt.hexbin(gr, g, bins = 'log', gridsize = bins)
    plt.gca().invert_yaxis()
    
def interactive_hess(g,gr):
    """Calls the plot_hess function and makes bin size interactive."""
    interact(plot_hess, bins = (50, 300, 5), continuous_update=False)