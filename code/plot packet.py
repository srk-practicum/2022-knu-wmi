import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

mypath = r"D:\universe\python\GIt\knu\csv_files"
file_names = [f.split(".")[0] for f in listdir(mypath) if isfile(join(mypath, f))]
for name in file_names:
    df = pd.read_csv(fr"D:\universe\python\GIt\knu\csv_files\{name}.csv")
    rows, _ = df.shape
    for i in range(rows):
        pd.DataFrame(df.iloc[i]).plot.line(ﬁgsize=[60, 10], legend=False, title=name)
        plt.show()
