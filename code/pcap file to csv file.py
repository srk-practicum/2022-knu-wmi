from CSIKit.reader import get_reader
from CSIKit.util import csitools
import pandas as pd
import numpy as np
import os
dir_pcap = os.listdir(r"D:\universe\python\GIt\knu\pcap_files")

for name in dir_pcap:
    my_reader = get_reader(fr"D:\universe\python\GIt\knu\pcap_files\{name}")
    csi_data = my_reader.read_file(fr"D:\universe\python\GIt\knu\pcap_files\{name}", scaled=True)
    csi_matrix, no_frames, no_subcarriers = csitools.get_CSI(csi_data, metric="amplitude")
    arr = csi_matrix[:, :, 0, 0]

    indx = []
    for count, i in enumerate(arr):
        if len(set(i.flat)) == 1:
            indx.append(count)
        else:
            arr[count] = np.where(i == -np.inf, np.ma.masked_invalid(i).mean(), i)
    arr = np.delete(arr, indx, axis=0)
    df = pd.DataFrame(arr)
    df.to_csv(path_or_buf=fr"D:\universe\python\GIt\knu\csv_files\{name.strip('.pcap')}.csv", index=False)