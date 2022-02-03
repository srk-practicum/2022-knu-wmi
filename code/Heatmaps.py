from CSIKit.tools.batch_graph import BatchGraph

import pandas as pd

import matplotlib.pyplot as plt

from os import listdir
from os.path import isfile, join



mypath = r"D:\universe\samsung_practic\test_plate_standart"

file_names = [f.split(".")[0] for f in listdir(mypath) if isfile(join(mypath, f))]
for name in file_names:
    b = BatchGraph(fr"{mypath}\{name}.pcap")
    b.heatmap()
