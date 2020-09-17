import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from datetime import datetime
# Opening the CSV file with pandas, and writing to
# data structures I can work with

data = pd.read_csv("dataset.csv", engine = 'python')

## Iterating through rows
months = []
for index, row in data.iterrows():
    time = (row["funded date"]).rstrip("-0000")
    dt = datetime.strptime(time, "%a, %d %b %Y %H:%M:%S ")
    months.append(dt.strftime("%B"))
    pdb.set_trace()

# Finally, we add a column containing months as strings. Worth noting this is all
# in O(n) - there's definitely a faster way to do this, but I'm not familair
# enough with pandas or seaborn to know what it is
data["month"] = months

# Set figure size
plt.figure(figsize=(12,6))
