import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
# Opening the CSV file with pandas, and writing to
# data structures I can work with

data = pd.read_csv("dataset.csv", engine = 'python')

# Sorting our dataframe let's remove all cases where people didn't raise their goal money
# or the goal money was less than 10 dollars
data = data[data["funded percentage"] >= 1]
data = data[data["goal"] >= 10]


# Let's use a logarithmic scale on the x-axis
test = np.logspace(np.log10(10), np.log10(10**6), 25)

# Now let's plot our goals
histplot = sb.histplot(data["goal"], bins = test, stat = "count")
histplot.set(xscale = "log")

# Labelling this graph
plt.xlabel("Campaign goal in USD")
plt.ylabel("Number of campaigns")
plt.title("Distribution of campaign fiscal goals for all funded campaigns")

# Save our image to use in our slide deck
plt.savefig("output/bestGoal.png")
print("Saved image!")

plt.show()
