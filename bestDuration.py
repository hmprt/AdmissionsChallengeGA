import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
# Opening the CSV file with pandas, and writing to
# data structures I can work with

data = pd.read_csv("dataset.csv", engine = 'python')

# Sorting our dataframe - we want to reorganise around descending funding percentage...
data = data.sort_values(["funded percentage"], ascending = False)

# And then grab the top 1000 values
data = data.head(1000)

# Changing x ticks for readability
xticks = np.arange(0, 120, 10)
plt.xticks(xticks)

# Making our plot
sb.set_style('whitegrid')
sb.histplot(data["duration"], bins = 30, stat = "count" )

# Setting descriptive labe;s
plt.xlabel("Duration of campaign in days")
plt.ylabel("Number of projects")
plt.title("Duration of top 1000 Kickstarter campaigns by funded percentage")

# Save our image to use in our slide deck
plt.savefig("output/bestDuration.png")
print("Saved image!")

plt.show()





# plt.ylim(-50, 50)
# plt.show()
