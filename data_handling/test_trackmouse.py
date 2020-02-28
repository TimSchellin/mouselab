# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 10:25:20 2020

@author: Tim-Laptop
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

from trackmouse import *

def test_record():
    record()
    
def time_this(x):
    l = []
    for i in range(x):
        start = time.time()
        ### THIS IS THE CODE TO TIME
        
        win32api.Sleep(POLLING_RATE_MS)
        
        # --- END TIMED CODE
        end = time.time()
        print(((end - start) - POLLING_RATE_S) * 1000)
        l.append(((end - start) - POLLING_RATE_S) * 1000)
        # --- CUSTOM TIME OPTIONS

        # print(print(.1 - (end-start)))
        
        ###
    print("max: {}".format(max(l)))


def test_logic():
    loop_num = 0
    while True:
        while not mouse_click():
            print(loop_num)
            time.sleep(0.05)
            if mouse_click():
                loop_num += 1
   
             
def analyze_recording():
    delta_times = []
    log = record()
    for i in range(1, len(log)):
        delta_times.append((log[i][3] - log[i-1][3]) // 1000)

    data = np.asarray([x for x in delta_times if x < POLLING_RATE_MS * 5])
    fig, ax = plt.subplots()
    counts, bins, patches = ax.hist(data, facecolor='red', edgecolor='gray')
    
    # Set the ticks to be at the edges of the bins.
    ax.set_xticks(bins)
    # Set the xaxis's tick labels to be formatted with 1 decimal place...
    ax.xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
    
    # Label the raw counts and the percentages below the x-axis...
    bin_centers = 0.5 * np.diff(bins) + bins[:-1]
    for count, x in zip(counts, bin_centers):
        # Label the raw counts
        x = int(x)
        ax.annotate(str(count), xy=(x, 0), xycoords=('data', 'axes fraction'),
                    xytext=(0, -18), textcoords='offset points', va='top',
                    ha='center')
    
        # Label the percentages
        percent = '%0.0f%%' % (100 * float(count) / counts.sum())
        ax.annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),
                    xytext=(0, -32), textcoords='offset points', va='top',
                    ha='center')
    
    # Give ourselves some more room at the bottom of the plot
    plt.subplots_adjust(bottom=0.15)
    plt.show()
    
    '''
    N_points = 100000
    n_bins = 20
    
    # Generate a normal distribution, center at x=0 and y=5
    x = np.random.randn(N_points)
    y = .4 * x + np.random.randn(100000) + 5
    
    fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
    
    # We can set the number of bins with the `bins` kwarg
    axs[0].hist(x, bins=n_bins)
    axs[1].hist(y, bins=n_bins)
    
    '''
    
def main():
     ''' choose which test functions to execute '''
     
     analyze_recording()
     #test_logic()
     #test_record()
     #time_this()
     
if __name__ == "__main__":
    main()

