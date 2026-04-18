import pandas as pd

df = pd.read_excel("data/mo_financials.xlsx")
#print(df.describe())

import matplotlib.pyplot as plt

plt.plot(df["Year"], df["Budget Balance ($)"], 
         color="#6FB5CB", label="With Income Tax")   # blue

plt.plot(df["Year"], df["Adjusted Balance ($)"], 
         color="#E05A2A", label="Without Income Tax")  # orange

plt.axhline(0, color="#E8A81A")  # yellow reference line

plt.xlabel("Year")
plt.ylabel("Budget Balance ($)")
plt.title("Impact of Removing Income Tax on Missouri Budget Balance")

plt.legend()

plt.show()