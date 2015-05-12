# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:54:03 2015

@author: ramku
"""

import requests
import json
import pandas
import scipy.stats

def myScipy(filename):
    
    base_ball_data = pandas.read_csv(filename)
        
    base_ball_data_left = base_ball_data[base_ball_data['handedness'] == 'L'];
    
    base_ball_data_right = base_ball_data[base_ball_data['handedness'] == 'R'];
    
    
    result = scipy.stats.ttest_ind(base_ball_data_left['avg'], base_ball_data_right['avg'], equal_var=False);
    # result is p value
    
    if result[1] <= 0.05:
        print ("hello scipy");
    else:
        print("hello scipy stats");


def compare_averages(filename):
    """
    Performs a t-test on two sets of baseball data (left-handed and right-handed hitters).

    You will be given a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg'). You can look at the csv
    file via the following link:
    https://www.dropbox.com/s/xcn0u2uxm8c4n6l/baseball_data.csv
    
    Write a function that will read that the csv file into a pandas data frame,
    and run Welch's t-test on the two cohorts defined by handedness.
    
    One cohort should be a data frame of right-handed batters. And the other
    cohort should be a data frame of left-handed batters.
    
    We have included the scipy.stats library to help you write
    or implement Welch's t-test:
    http://docs.scipy.org/doc/scipy/reference/stats.html
    
    With a significance level of 95%, if there is no difference
    between the two cohorts, return a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.  
    
    If there is a difference, return a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.
    
    For example, the tuple that you return may look like:
    (True, (9.93570222, 0.000023))
    """
    base_ball_data = pandas.read_csv(filename)

    base_ball_data_left = base_ball_data[base_ball_data['handedness'] == 'L'];
    
    base_ball_data_right = base_ball_data[base_ball_data['handedness'] == 'R'];
    
    
    result = scipy.stats.ttest_ind(base_ball_data_left['avg'], base_ball_data_right['avg'], equal_var=False);
    # result is p value
    
    if result[1] <= 0.05:
        print ("hello scipy");
    else:
        print("hello scipy stats");


compare_averages("/Users/ramku/Downloads/intro_to_ds_programming_files/lesson_3/t-test/baseball_data.csv")