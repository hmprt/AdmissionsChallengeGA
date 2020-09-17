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
successful = []
for index, row in data.iterrows():
    time = (row["funded date"]).rstrip("-0000")
    dt = datetime.strptime(time, "%a, %d %b %Y %H:%M:%S ")
    months.append(dt.strftime("%B"))

    # Noting if projects succeeded or failed, filtering out cancellations and
    # live projects
    if (row["funded percentage"] >= 1):
        successful.append("Successful")
    else:
        successful.append("Unsucessful")


# Finally, we add a column containing months as strings. Worth noting this is all
# in O(n) - there's definitely a faster way to do this, but I'm not familair
# enough with pandas or seaborn to know what it is
data["month"] = months

# We also add our new "successful" series:
data["Project Successful?"] = successful

## Now we can use categorical to sort this data by our new Month series
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

data["month"] = pd.Categorical(data["month"], categories=months)
data.sort_values(["month"])

# Setting figure size
fig_dims = (6, 4)
fig, ax = plt.subplots(figsize=fig_dims)

sb.set_style('whitegrid')
sb.displot(data, x = "month", hue = "Project Successful?", palette=["green", "red"])
plt.xlabel("Month of funding")
plt.ylabel("Number of campaigns")
plt.title("Kickstarter campaign funding by month")

plt.show()
