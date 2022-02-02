import matplotlib.pyplot as plt
import pandas as pd
from CSIKit.reader import get_reader
from CSIKit.util import csitools
import numpy as np
import os
from collections import Counter
dir_pcap = os.listdir(r"D:\universe\samsung_practic\test_plate_standart")
dict_frames=Counter()
number_renders=0
count_marker=0
Scolor=""
marker=['s', '<', '^', 'x', '+', 'v', '^', '', '>', '', 'd']
for i in dir_pcap:
    number_renders += 1
    my_reader = get_reader(fr"D:\universe\samsung_practic\test_plate_standart\{i}")
    csi_data = my_reader.read_file(fr"D:\universe\samsung_practic\test_plate_standart\{i}")
    csi_phase, no_frames, no_subcarriers = csitools.get_CSI(csi_data, metric="phase")
    csi_amplitude, no_frames, no_subcarriers = csitools.get_CSI(csi_data, metric="amplitude")
    #print("no_frames= ", no_frames)

    if no_frames in dict_frames:
        dict_frames[no_frames] +=  1
    else:
        dict_frames[no_frames] = 1

    if number_renders==1:
        Scolor = marker[count_marker]
        plt.plot(dict_frames.keys(), dict_frames.values(), Scolor,
                 label=f"{i.strip('_1.pcap')}".format(Scolor))

    elif number_renders==15:
        number_renders=0
        count_marker+=1
        plt.plot(dict_frames.keys(), dict_frames.values(),Scolor)

    else:

        plt.plot(dict_frames.keys(), dict_frames.values(),Scolor)
    plt.legend(numpoints=1)




plt.xlabel('no frames')
plt.ylabel('count')


plt.title('Dot Plot : Red Dots')

plt.show()
