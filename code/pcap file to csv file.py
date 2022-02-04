from CSIKit.reader import get_reader
from CSIKit.util import csitools
import pandas as pd
import numpy as np
import os
dir_pcap = os.listdir(r"D:\universe\samsung_practic\test_plate_standart")

for i in dir_pcap:
    my_reader = get_reader(fr"D:\universe\samsung_practic\test_plate_standart\{i}")
    csi_data = my_reader.read_file(fr"D:\universe\samsung_practic\test_plate_standart\{i}", scaled=True)
    #csi_phase, no_frames, no_subcarriers = csitools.get_CSI(csi_data, metric="phase")
    csi_amplitude, no_frames, no_subcarriers = csitools.get_CSI(csi_data, metric="amplitude")
    arr = csi_amplitude[:, :, 0, 0]
    for count, name in enumerate(arr):
        arr[count] = np.where(name == -np.inf, np.ma.masked_invalid(name).mean(), name)

    # df = pd.DataFrame(csi_amplitude.reshape(187, 256))
    df = pd.DataFrame(csi_amplitude.reshape(no_frames, no_subcarriers))
    new_filename = i.split('.')[0] + ".csv"
    df.to_csv(path_or_buf=fr"D:\universe\python\GIt\knu\csv_files\{new_filename}", header=False, index=False)
