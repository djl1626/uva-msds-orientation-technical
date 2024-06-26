import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel(
    "/Users/djl47/Documents/Graduate School/uva-msds-orientation-technical/Python/MSDS-Orientation-Computer-Survey.xlsx")

plt.hist(data[data['CPU Number of Cores (int)'] > 0][[
         'CPU Number of Cores (int)']], bins=10, color="pink", edgecolor="black")
plt.title("Distribution of the Number of CPU Cores")
plt.xlabel("Number of Cores")
plt.ylabel("Frequency")
plt.savefig(
    "/Users/djl47/Documents/Graduate School/uva-msds-orientation-technical/Python/presentation-fig.png")
