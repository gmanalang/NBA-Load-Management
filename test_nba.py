#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 20:18:05 2023

@author: vedagrawal
test
"""

# cell 1
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/NBAAverages2022-2023.csv")

df

# cell 2
sns.set()

# plots relationship between points and mpg
px.scatter(df, x='PTS', y='MP', hover_data=['Player'], title='PTS vs MPG')
