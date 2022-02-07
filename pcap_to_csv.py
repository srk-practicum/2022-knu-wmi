from CSIKit.reader import get_reader
from CSIKit.util import csitools
import os
import pandas
import csv

dir_pcap = os.listdir("files_pcap")
for i in dir_pcap:
    files_list = os.listdir(f"files_pcap/{i}")
    os.mkdir(f"files_csv/{i}")
    for j in files_list:
        my_reader = get_reader(f"files_pcap/{i}/{j}")
        csi_data = my_reader.read_file(f"files_pcap/{i}/{j}")
        csi_amplitude, no_frames, no_subcarriers = csitools.get_CSI(csi_data, metric="amplitude")
        df = pandas.DataFrame(csi_amplitude.reshape(no_frames, no_subcarriers))
        a = j.split('.')
        new_name = a[0] + ".csv"
        df.to_csv(f"files_csv/{i}/{new_name}")
        file_csv = f"files_csv/{i}/{new_name}"
        data = pandas.read_csv(file_csv, index_col=(0, 1))
        lines = list(data.values)
        writer = csv.writer(open(file_csv, 'w'))
        writer.writerows(lines)