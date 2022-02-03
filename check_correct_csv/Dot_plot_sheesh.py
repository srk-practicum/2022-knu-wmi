import matplotlib.pyplot as plt
from CSIKit.reader import get_reader
from CSIKit.util import csitools
import os
import pandas as pd
import os
from collections import Counter

dir_csv = os.listdir(fr"D:\universe\python\GIt\knu\csv_files")
colors = ['yellow', 'blue', 'orange', 'black', 'purple', 'brown', 'green']
marker = ['s', '<', '^', 'x', '+', 'v', '^']
counter = 0
index = 0
mas_packet = Counter()
ind = 0
for i in enumerate(dir_csv):
    if counter == 15:
        counter = 0
        ind += 1
    packet = len(pd.DataFrame(pd.read_csv(fr"D:\universe\python\GIt\knu\csv_files\{i[1]}")))
    mas_packet[packet] += 1

    counter += 1
    if counter == 1:
        marker_name = i[1].strip("_1.csv")
        plt.scatter(packet, mas_packet[packet], color=colors[ind], marker=marker[ind], label=marker_name)
    else:
        plt.scatter(packet, mas_packet[packet], color=colors[ind], marker=marker[ind])

plt.grid(True)
plt.gca().set(xlim=(0, 800), ylim=(0, 20),
              xlabel='Packets', ylabel='Count')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=7)
plt.legend(numpoints=1)
plt.show()
