from CSIKit.tools.batch_graph import BatchGraph
from os import listdir
from os.path import isfile, join



mypath = r"D:\universe\samsung_practic\taste_plate_new"

file_names = [f.split(".")[0] for f in listdir(mypath) if isfile(join(mypath, f))]
for name in file_names:
    b = BatchGraph(fr"{mypath}\{name}.pcap")
    b.heatmap()
