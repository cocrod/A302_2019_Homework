
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact
'''Imports all necessary tools.'''


def load_and_prepare_cmd(filename):
    '''Defines the function to isolate, filter, and return desired data (2 columns g & gr).'''
    
    data = pd.read_csv('fieldA.csv')
    '''Reads in the data.'''
    
    g_minus_r = ( data['g']-data['r'] )
    data['g_minus_r'] = g_minus_r
    '''Adds a new column for g-r.'''
    
    d = data[ (data['g']>14) & (data['g']<24) & (data['g_minus_r']>-0.5) & (data['g_minus_r']<2.5) ]
    '''Creates new object with filtered data.'''
    
    return d['g'] , d['g_minus_r']

(g, gr) = load_and_prepare_cmd('fieldA.csv')
'''Uses above function to get columns g & gr.'''

def interactive_hess(g, gr):
    '''Defines a function to create a Hess Diagram.'''
    def hb(n=100):
        '''Defines a function to plot Hess Diagram for use with the interact function.'''
        plt.hexbin( g,gr , bins='log' , gridsize=n )
        plt.title("Hess Diagram")
        plt.xlabel("G-Band Magnitude")
        plt.ylabel("R-Band Magnitude")
        plt.colorbar().set_label("Stellar Density")
    
    interact( hb , n=(50,300,1) , continuous_update=False )
    '''Created interactive Hess Diagram with a modifiable gridsize.'''
