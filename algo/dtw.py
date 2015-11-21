import math
import csv
import matplotlib.pyplot as plt
import numpy as np
from math import factorial
import sys
import collections



class DynamicTimeWarping(object):
    
    def __init__(self,max_window=10000):
        self.max_window = max__window
       
   

    def distance(self, series1, series2, dist = lambda x,y: abs(x-y)):
   
        series1 = np.array(series1)    
        series2 = np.array(series2)
        M = len(series1)
        N = len(series2)
     
        cost = sys.maxint * np.ones((M, N))

        # Initialize the first row and column
        cost[0, 0] = dist(series1[0], series2[0])
        for i in xrange(1, M):
            cost[i, 0] = cost[i-1, 0] + dist(series1[i], series2[0])

        for j in xrange(1, N):
            cost[0, j] = cost[0, j-1] + dist(series1[0], series2[j])

        # Populate rest of cost matrix within window
        for i in xrange(1, M):
            for j in xrange(max(1, i - self.max_window),
                            min(N, i + self.max_window)):
                choices = cost[i - 1, j - 1], cost[i, j-1], cost[i-1, j]
                cost[i, j] = min(choices) + dist(series1[i], series2[j])

        # Return DTW distance given window 
        return cost[-1, -1]

