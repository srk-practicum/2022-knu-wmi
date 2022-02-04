import matplotlib.pyplot as plt
from CSIKit.reader import get_reader
from CSIKit.util import csitools
import os
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler

dir_csv = os.listdir(fr"D:\universe\python\GIt\knu\csv_files")

ind = 0
for i in enumerate(dir_csv):
    packet = pd.DataFrame(pd.read_csv(fr"D:\universe\python\GIt\knu\csv_files\{i[1]}"))

    StandardScaler().fit_transform(packet.)