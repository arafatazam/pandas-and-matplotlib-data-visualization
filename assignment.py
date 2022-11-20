#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 20:24:59 2022

@author: Muhammad Arafat Azam (id: 21087019)
"""

import pandas as pd
import matplotlib.pyplot as plt


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Discard NaN values, take only top lavel ethnic groups
    and cast to int64, rename the indexes & columns and
    merging some ranges for uniformity
    """
    df = df.dropna()
    df = df.filter(regex='All|Total', axis="index")
    for col in df.columns:
        df[col] = df[col].str.replace(',', '')
        df[col] = pd.to_numeric(df[col])
    df = df.rename({
        'All Ethnic groups': 'All',
        'White: Total': 'White',
        'Mixed/multiple ethnic group: Total': 'Mixed',
        'Asian/Asian British: Total': 'Asian',
        'Black/African/Caribbean/Black British: Total': 'Black',
        'Other ethnic group: Total': 'Other'
    })
    df = df.rename({
        'All ages': 'All',
        'Age 0 to 4': '0-4',
        'Age 5 to 7': '5-9',
        'Age 8 to 9': '8-9',
        'Age 10 to 14': '10-14',
        'Age 15': '15-19',
        'Age 16 to 17': '16-17',
        'Age 18 to 19': '18-19',
        'Age 20 to 24': '20-24',
        'Age 25 to 29': '25-29',
        'Age 30 to 34': '30-34',
        'Age 35 to 39': '35-39',
        'Age 40 to 44': '40-44',
        'Age 45 to 49': '45-49',
        'Age 50 to 54': '50-54',
        'Age 55 to 59': '55-59',
        'Age 60 to 64': '60-64',
        'Age 65 to 69': '65-69',
        'Age 70 to 74': '70-74',
        'Age 75 to 79': '75-79',
        'Age 80 to 84': '80-85',
        'Age 85 and over': '85-'
    }, axis='columns')
    df['5-9'] = df['5-9']+df['8-9']
    df['15-19'] = df['15-19']+df['16-17']+df['18-19']
    df = df.drop(columns=['8-9', '16-17', '18-19'])
    return df


def plot_percentage_by_age_group(df: pd.DataFrame):
    """
    Plotting percentage of poeple in each age group for
    different ethnicity
    """
    data = df.iloc[:, :].div(df['All'], axis=0).mul(100)
    plt.figure()
    line_style = 'solid'
    for i in range(len(data.index)):
        plt.plot(data.iloc[i, 1:], label=data.index[i], linestyle=line_style)
        line_style = 'dashed'
    plt.xticks(rotation=45)
    plt.legend()
    plt.ylabel('Percentage of the ethnic population')
    plt.title('Percentage of people in age groups for each enthnic group')
    plt.show()


def piechart_of_nonwhite_ethnicities(df: pd.DataFrame):
    """
    Pie chart to show the non-white population's ethnicity shares
    by major ethnic groups
    """
    data = df.iloc[2:, 0]
    plt.figure()
    plt.pie(data, labels=data.index, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.show()


def main():
    data = pd.read_csv('age-groups.csv', index_col=0)
    data = clean_data(data)
    plot_percentage_by_age_group(data)
    piechart_of_nonwhite_ethnicities(data)


if __name__ == "__main__":
    main()
