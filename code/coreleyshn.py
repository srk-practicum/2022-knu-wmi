import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"D:\universe\python\GIt\knu\csv_files\Falldown_10.csv")
sns.heatmap(df.corr(), xticklabels=False, yticklabels=False)
plt.show()
