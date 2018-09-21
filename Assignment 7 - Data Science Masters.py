"""
Assignment 7
Data Science Masters

"""
"""
Problem Statement
Write a function to find moving average in an array over a window:
Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.

"""
import numpy as np

def moving_average(n, k) :
    ret = np.cumsum(n, dtype=float)     # calculate cummulative sum
    ret[k:] = ret[k:] - ret[:-k]        # to calculate moving sum
    return ret[k - 1:] / k              # caculate and return moving average

n = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
k = 3
moving_average(n, k)
