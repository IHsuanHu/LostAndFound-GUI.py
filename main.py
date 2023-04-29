# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 14:53:27 2022

@author: user
"""

import pandas as pd

#read the excel if it is present
try:
    path = 'Lost_and_Found.xlsx'
    with open(path, 'rb') as f:
        df = pd.read_excel(f, 0)
        
    
#create a excel file
except:    
    df = pd.DataFrame(columns= 
                      ['Item', 'Date', 'Color', 'Location', 'Note', 'Check'])
    df.to_excel('Lost_and_Found.xlsx', index= False)
    

