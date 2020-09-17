import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
# Opening the CSV file with pandas, and writing to
# data structures I can work with

data = pd.read_csv("dataset.csv", engine = 'python')

# Sorting our dataframe. Let's remove all unsucessful projects
data = data[data["funded percentage"] >= 1]

# And we'll grab the top 1000 projects again
data = data.head(1000)
