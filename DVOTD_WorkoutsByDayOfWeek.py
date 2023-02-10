# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 09:19:36 2023

@author: HuntS2
"""

import pandas as pd
import plotly_express as px
import plotly.io as pio
pio.renderers.default = "browser"

df = pd.read_csv(r"C:\Users\Hunts2\OneDrive - AECOM\Documents\Data Science Projects\Other Projects\2023-02-10\2023 Workouts - January.csv")


fig = px.bar(df,
             x = "Day Of Week",
             color = "Workout",
             title = "January 2023 Workouts by Day of Week",
             labels = {"count" : "Count"})
fig.show()