# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:32:07 2019

@author: Hugh
"""

import pandas as pd

data = pd.read_csv('clean_table.csv')

list(data.columns.values)

data = data.drop(columns = 'visualization')

list(data.columns.values)

data['key'] = str(data['[run number]'] + str(data['[step]']))
