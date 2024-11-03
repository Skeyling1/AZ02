import pandas as pd
import matplotlib.pyplot as plt

dates = { 'data' : [12, 14, 45, 23, 35, 5, 45, 67, 76, 67, 788, 34, 34, 687, 23, 565, 67, 87, 4, 3]}

df = pd.DataFrame(dates)

df.boxplot(column='data')
plt.show()

