from CSIKit.tools.batch_graph import BatchGraph
from CSIKit.reader import get_reader
from CSIKit.util import csitools


my_reader = get_reader(r"D:\universe\samsung_practic\test_plate_standart\Falldown_1.pcap")
csi_data = my_reader.read_file(r"D:\universe\samsung_practic\test_plate_standart\Falldown_1.pcap", scaled=True)
csi_matrix, no_frames, no_subcarriers = csitools.get_CSI(csi_data)
b = BatchGraph(r"D:\universe\samsung_practic\test_plate_standart\Falldown_1.pcap")
b.heatmap()