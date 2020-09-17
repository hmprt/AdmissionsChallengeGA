import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

kickstarter_data = pd.read_csv("dataset.csv", engine = 'python')

duration = kickstarter_data["duration"]

print(duration.max())
print(len(duration))
print("Mean Duration: " + str((duration.sum()  / (len(duration)))))

plt.title("Distribution of Kickstarter Fundraising Durations")
plt.xlabel("Fundraiser duration in days")
plt.ylabel("Proportion of dataset")

histplot = sb.histplot(duration, bins = 30, stat = "probability")

plt.savefig('output/durationPlot.png')
print("Saving to file...")
plt.show()

plt.show()
