from CSIKit.reader import get_reader
from CSIKit.util import csitools
from CSIKit.tools.batch_graph import BatchGraph
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from os import listdir
from os.path import isfile, join
from collections import Counter


mypath = r"D:\universe\samsung_practic\test_plate_standart"

file_names = [f.split(".")[0] for f in listdir(mypath) if isfile(join(mypath, f))]
for name in file_names:
    b = BatchGraph(fr"{mypath}\{name}.pcap")
    b.heatmap()
    df = pd.read_csv(r"D:\universe\python\GIt\knu\csv_files\Falldown_1.csv")
    rows, _ = df.shape
    for i in range(rows):
        pd.DataFrame(df.iloc[i]).plot.line(ﬁgsize=[60, 10], legend=False, title=name)

plt.show()