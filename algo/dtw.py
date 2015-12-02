import math
import csv
import numpy as np
from math import factorial
import sys
import collections



# class DynamicTimeWarping(object):
    
#     def __init__(self,max_window=10000):
#         self.max_window = max_window
       
   

#     def distance(self, series1, series2, dist = lambda x,y: abs(x-y)):
   
#         series1 = np.array(series1)    
#         series2 = np.array(series2)
#         M = len(series1)
#         N = len(series2)
     
#         cost = sys.maxint * np.ones((M, N))

#         # Initialize the first row and column
#         cost[0, 0] = dist(series1[0], series2[0])
#         for i in xrange(1, M):
#             cost[i, 0] = cost[i-1, 0] + dist(series1[i], series2[0])

#         for j in xrange(1, N):
#             cost[0, j] = cost[0, j-1] + dist(series1[0], series2[j])

#         # Populate rest of cost matrix within window
#         for i in xrange(1, M):
#             for j in xrange(max(1, i - self.max_window),
#                             min(N, i + self.max_window)):
#                 choices = cost[i - 1, j - 1], cost[i, j-1], cost[i-1, j]
#                 cost[i, j] = min(choices) + dist(series1[i], series2[j])

#         # Return DTW distance given window 
#         return cost[-1, -1]

class Dtw(object):

    
    def __init__(self, n_neighbors=3, max_warping_window=10000, subsample_step=1):
        self.n_neighbors = n_neighbors
        self.max_warping_window = max_warping_window
        self.subsample_step = subsample_step
    
    def fit(self, x, l):
        self.x = x
        self.l = l
        
    def _dtw_distance(self, ts_a, ts_b, d = lambda x,y: abs(x-y)):
          # Create cost matrix via broadcasting with large int
        ts_a, ts_b = np.array(ts_a), np.array(ts_b)
        M, N = len(ts_a), len(ts_b)
        cost = sys.maxint * np.ones((M, N))

        # Initialize the first row and column
        cost[0, 0] = d(ts_a[0], ts_b[0])
        for i in xrange(1, M):
            cost[i, 0] = cost[i-1, 0] + d(ts_a[i], ts_b[0])

        for j in xrange(1, N):
            cost[0, j] = cost[0, j-1] + d(ts_a[0], ts_b[j])

        # Populate rest of cost matrix within window
        for i in xrange(1, M):
            for j in xrange(max(1, i - self.max_warping_window),
                            min(N, i + self.max_warping_window)):
                choices = cost[i - 1, j - 1], cost[i, j-1], cost[i-1, j]
                cost[i, j] = min(choices) + d(ts_a[i], ts_b[j])

        # Return DTW distance given window 
        return cost[-1, -1]

        

