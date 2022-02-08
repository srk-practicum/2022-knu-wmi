import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

files_csv_test = []
files_csv_train = []
for i in os.listdir('files_csv_test'):
    for j in os.listdir(f'files_csv_test/{i}'):
        df = pd.read_csv(f'files_csv_test/{i}/{j}')
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.replace(np.nan, df.mean().mean(), inplace=True)
        files_csv_test.append(df)
for i in os.listdir('files_csv_train'):
    for j in os.listdir(f'files_csv_train/{i}'):
        df = pd.read_csv(f'files_csv_train/{i}/{j}')
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.replace(np.nan, df.mean().mean(), inplace=True)
        files_csv_train.append(df)

files_csv_train_norm = []
for file in files_csv_train:
    df_norm = pd.DataFrame(StandardScaler().fit_transform(file), columns = file.columns)
    files_csv_train_norm.append(df_norm)

files_csv_train_norm_concat = pd.concat(files_csv_train_norm[65:66])
pca = PCA(0.80)
pca.fit(files_csv_train_norm_concat)

os.mkdir(f'files_csv_train_PCA/walking_prpendicular')
df_pca = pd.DataFrame(pca.transform(files_csv_train_norm[65]))
df_pca.to_csv(f'files_csv_train_PCA/walking_prpendicular/walking_prpendicular_10.csv', index=False)
print('folder with pca data is created')