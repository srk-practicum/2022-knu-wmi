import os
import pandas
from CSIKit.reader import get_reader
from CSIKit.util import csitools

# getting all dirs with pcap files
dir_pcap = os.listdir("pcap_files_one_move")
# simple iteration of all dirs
for i in dir_pcap:
    # getting all files in every dir
    files_list = os.listdir(f"pcap_files_one_move/{i}")
    # making new dir with same name in dir "csv_files"
    os.mkdir(f"csv_files/{i}")
    # simple iteration of all files in this dir
    for j in files_list:
        # reading our file
        my_reader = get_reader(f"pcap_files_one_move/{i}/{j}")
        csi_data = my_reader.read_file(f"pcap_files_one_move/{i}/{j}")
        # getting amplitude, no_frames and no_subcarriers
        csi_amplitude, no_frames, no_subcarriers = csitools.get_CSI(csi_data, metric="amplitude")
        # making DataFrame
        df = pandas.DataFrame(csi_amplitude.reshape(no_frames, no_subcarriers))
        # making the same filename but with another file extension like "blabla.csv"
        new_filename = j.split('.')[0] + ".csv"
        # making new file in changed directory
        df.to_csv(f"csv_files/{i}/{new_filename}")

# print(df)
