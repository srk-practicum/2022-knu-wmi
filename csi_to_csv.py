import os

import pandas
from CSIKit.reader import get_reader
from CSIKit.util import csitools
dir_pcap = os.listdir("pcap_files")
for i in range( len(dir_pcap)):
    files_list = os.listdir(f"pcap_files/{dir_pcap[i]}")
    os.mkdir(f"csv_files/{dir_pcap[i]}")
    for j in files_list :
        my_reader = get_reader(f"pcap_files/{dir_pcap[i]}/{j}")
        csi_data = my_reader.read_file(f"pcap_files/{dir_pcap[i]}/{j}")
        csi_amplitude, no_frames, no_subcarriers = csitools.get_CSI(csi_data, metric="amplitude")
        df = pandas.DataFrame(csi_amplitude.reshape(no_frames, no_subcarriers))
        new_filename = j.split('.')[0]+".csv"
        df.to_csv(f"csv_files/{dir_pcap[i]}/{new_filename}.csv")



# print(df)
