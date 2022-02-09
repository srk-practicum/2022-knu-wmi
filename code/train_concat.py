import sys
import pandas
import pylab as pl
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
mypath = r"D:\universe\python\GIt\knu\csv_files"
file_names = [f.split(".")[0] for f in listdir(mypath) if isfile(join(mypath, f))]
for name in file_names:
    df = pd.read_csv(fr"D:\universe\python\GIt\knu\csv_files\{name}.csv")
    rows, _ = df.shape

    pd.concat(df[:rows],ignore_index=True)