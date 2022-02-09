import pandas as pd
from os import listdir
from os.path import isfile, join
from sklearn import preprocessing
# from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# from sklearn.preprocessing import LabelEncoder
#
#
# # action = {
# #     'Nothing': 0,
# #     'Falldown': 1,
# #     'Hand_circle': 2,
# #     'Hand_move_up': 3,
# #     'Smoking': 4,
# #     'Walking_along': 5,
# #     'Walking_Perpendicular': 6,
# # }
massiv = []
mypath = r"D:\universe\python\GIt\knu\csv_files"
file_names = [f.split(".")[0] for f in listdir(mypath) if isfile(join(mypath, f))]
for name in file_names:
    df = pd.read_csv(fr"D:\universe\python\GIt\knu\csv_files\{name}.csv")
    name = name.strip("_1234567890")
    massiv.append(name)
labelencoder = preprocessing.LabelEncoder()

labelencoder.fit(massiv)
print(list(labelencoder.transform(massiv)))
print(labelencoder.classes_)

