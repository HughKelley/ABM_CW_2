# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:12:36 2019

@author: Hugh
"""

# Script for analyzing netlogo output 

# too big for excel and even libre calc?

>>> my_cols = ["A", "B", "C", "D", "E"]
>>> pd.read_csv("ragged.csv", names=my_cols, engine='python')


import csv
import pandas as pd
import os as os

data = pd.read_csv('spreadsheet.csv')


cwd = os.getcwd()

lengths = []

with open("Trail_2/spreadsheet.csv", "r") as data:
    reader = csv.reader(data, delimiter = ',')
    for i, line in enumerate(reader):    
        lengths.append(len(line))
        print(len(line))
    
    
    
    
    
    
    
    
    
#    for i, line in enumerate(f):
#        print 





#with "Output\Trial_2\Sugarscape 1 Immediate Growback CW2-spreadsheet.csv" as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    line_count = 0
#    for row in csv_reader:
#        if line_count == 0:
#            print(f'column names are)





