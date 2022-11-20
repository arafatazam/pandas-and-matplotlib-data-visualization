#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 20:24:59 2022

@author: Muhammad Arafat Azam (id: 21087019)
"""

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Discard NaN values, take only top lavel ethnic groups
    and cast to int64
    """
    df = df.dropna()
    df = df.filter(regex='All|Total', axis="index")
    for col in df.columns:
        df[col] = df[col].str.replace(',', '')
        df[col] = pd.to_numeric(df[col])
    return df


def main():
    data = pd.read_csv('age-groups.csv', index_col=0)
    data = clean_data(data)
    print(data.iloc[1:]['All ages'].sum())


if __name__ == "__main__":
    main()
