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
# N.B: Not using the successul tag as it doesn't include live projects which may
# have already met their funding goal - for the purposes of this assignment,
# I'm considering them as successful too

data = data[data["funded percentage"] >= 1]

print(len(data))

plt.figure(figsize=(12,6))

sb.countplot(x = "category", data = data)
sb.set(rc={'figure.figsize':(100,8.27)})

plt.xlabel("Project category")
plt.ylabel("Number of projects")
plt.title("Succesful campaigns by category")

plt.savefig("output/bestCategories.png")
print("Saved image!")


plt.show()
