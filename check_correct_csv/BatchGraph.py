from CSIKit.tools.batch_graph import BatchGraph
from CSIKit.reader import get_reader
from CSIKit.util import csitools

my_reader = get_reader(r"D:\universe\samsung_practic\test_plate_standart\Falldown_1.pcap")
csi_data = my_reader.read_file(r"D:\universe\samsung_practic\test_plate_standart\Falldown_1.pcap", scaled=True)
csi_matrix, no_frames, no_subcarriers = csitools.get_CSI(csi_data)
b = BatchGraph(r"D:\universe\samsung_practic\test_plate_standart\Falldown_1.pcap")
b.heatmap()
for name in onlyfiles:
    my_reader = get_reader(fr"test_plate_standart/{name}.pcap")
    csi_data = my_reader.read_file(fr"test_plate_standart/{name}.pcap", scaled=True)
    csi_matrix, no_frames, no_subcarriers = csitools.get_CSI(csi_data)
    arr = csi_matrix.reshape(no_frames, no_subcarriers)

    for count,i in enumerate(arr):
        arr[count] = np.where(i == -np.inf, np.ma.masked_invalid(i).mean(),i)

    df.to_csv(path_or_buf = fr"C:\Users\Saber\OneDrive\Practise\csv\{name}.csv",index = False,header = False)