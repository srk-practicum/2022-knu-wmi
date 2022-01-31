from CSIKit.reader import get_reader

my_reader = get_reader("D:/universe/samsung_practic/test_plate_standart/Falldown_1.pcap")
csi_data = my_reader.read_file("D:/universe/samsung_practic/test_plate_standart/Falldown_1.pcap")

from CSIKit.reader import IWLBeamformReader

my_reader = IWLBeamformReader()
csi_data = my_reader.read_file("path/to/log.all_csi.6.7.6.dat")