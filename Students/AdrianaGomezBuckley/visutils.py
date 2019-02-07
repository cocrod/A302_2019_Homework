import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, fixed

def load_and_prepare_cmd(filename):
    array = np.genfromtxt(filename, dtype=float, delimiter=",", names=True)
    g = array['g']
    r = array['r']
    g_mask = (g>14) & (g<24)
    g = g[g_mask]
    r = r[g_mask]
    gr = g-r
    g_r_mask = (gr>(-0.5)) & (gr<2.5)
    g = g[g_r_mask]
    gr = gr[g_r_mask]
    return g, gr

def interactive_hess(g, gr):
    def hess_plot(g, gr, grid):
        plt.hexbin(gr, g, gridsize=grid, bins='log')
        plt.show()
    interact(hess_plot, g=fixed(g), gr=fixed(gr), grid=(50,300,1))