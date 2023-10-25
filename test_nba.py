#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 20:18:05 2023

@author: vedagrawal
test
"""

# cell 1
import pandas as pd

df = pd.read_csv("NBAAverages2022-2023.csv")

df

# cell 2
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
sns.set()

# plots relationship between points and mpg
px.scatter(df, x='PTS', y='MP', hover_data = ['Player'], title = 'PTS vs MPG')

