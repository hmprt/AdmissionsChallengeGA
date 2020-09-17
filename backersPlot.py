import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


kickstarter_data = pd.read_csv("dataset.csv", engine = 'python')

backers = kickstarter_data["backers"]

print(backers.max())
print(len(backers))
print("Mean Backers: " + str((backers.sum()  / (len(backers)))))

test = np.logspace(np.log10(1), np.log10(10**5), 75 )


histPlot = sb.histplot(backers, bins = test, stat = "probability")
histPlot.set(xscale="log")


plt.show()
