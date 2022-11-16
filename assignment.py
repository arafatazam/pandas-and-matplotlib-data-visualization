#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 20:24:59 2022

@author: Muhammad Arafat Azam (id: 21087019)
"""

import pandas as pd

def clean_data(df:pd.DataFrame):
    pass
    

def main():
    data = pd.read_csv('age-groups.csv', index_col=0)
    print(data.head())
    
if __name__=="__main__":
    main()