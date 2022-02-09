import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pywt import cwt , scale2frequency
from os import listdir
from os.path import isfile, join
import seaborn as sns
import matplotlib.pyplot as plt
import pywt
import pywt.data

mypath = r"D:\universe\python\GIt\knu\train"
filenames = [f.split(".")[0] for f in listdir(mypath) if isfile(join(mypath, f))]



N = 10
L = 30
frequencies = [2 ** (n + (l / L)) for n in range(N) for l in range(L)]
df = pd.read_csv(mypath + "\Falldown_2.csv")
coef,freqs = cwt(df['1'],frequencies,wavelet='morl')
sns.heatmap(coef,xticklabels=False, yticklabels=False,cmap="viridis")
plt.show()
coef,freqs = cwt(df['2'],frequencies,wavelet='morl')
sns.heatmap(coef,xticklabels=False, yticklabels=False,cmap="viridis")
plt.show()