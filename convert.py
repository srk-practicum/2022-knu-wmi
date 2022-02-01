import pandas
import os
from CSIKit.reader import get_reader
from CSIKit.util import csitools

path = r'C:\Users\nelly\PycharmProjects\pythonProject4\data'

for root, dirs, files in os.walk(path):
    for _file in files:
        my_reader = get_reader(_file)
        csi_data = my_reader.read_file(_file)
        csi_amplitude, no_frames, no_subcarriers = csitools.get_CSI(csi_data, metric="amplitude")
        df = pandas.DataFrame(csi_amplitude.reshape(no_frames, no_subcarriers))
        a = _file.split(".")
        df.to_csv(a[0]+".csv")
