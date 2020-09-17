import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
# Opening the CSV file with pandas, and writing to
# data structures I can work with

kickstarter_data = pd.read_csv("dataset.csv", engine = 'python')

## Q1: getting the mean pledge
pledged = kickstarter_data['pledged']
indivPledges = pledged.shape
sumPledges = pledged.sum()

meanPledge = sumPledges / indivPledges

# Q2: Generating histogram of average total pledges

test = np.logspace(np.log10(1), np.log10(10**7), 25)
histPlot = sb.histplot(pledged, bins = test, stat='probability')


#Setting x axis to a log scale
histPlot.set(xscale="log")
# plt.ylim(0, 150000)
plt.title("Distribution of Kickstarter Pledges")
plt.xlabel("Total amount pledged in USD")
plt.ylabel("Proportion of dataset")

plt.savefig('output/pledgePlot.png')
print("Saving to file...")
plt.show()
