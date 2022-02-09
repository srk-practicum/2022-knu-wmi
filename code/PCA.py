import pandas as pd
from os import listdir
from os.path import isfile, join
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
def norm_data_frame(path, filenames):
    df = pd.DataFrame()  # empty dataframe

    for name in filenames:
        file = pd.read_csv(path + name + ".csv")
        file = pd.DataFrame(StandardScaler().fit_transform(file))
        df = pd.concat([df, file], axis=0)


    return df
def main():

    mypath = r"D:\universe\python\GIt\knu\train"
    filenames = [f.split(".")[0] for f in listdir(mypath) if isfile(join(mypath, f))]
    test_files = filenames[:len(filenames) // 4]
    #Amplitude
    amplitudes = norm_data_frame(r"D:\universe\python\GIt\knu\csv_files\\",test_files)
    #print(amplitudes)
    pca_amplitude = PCA(0.6)

    training_amplitudes = amplitudes[:600]
    pca_amplitude.fit(training_amplitudes.values)

    print(pca_amplitude.explained_variance_ratio_)

    for name in test_files:
        df = pd.read_csv(fr"D:\universe\python\GIt\knu\csv_files\{name}.csv")
        df = pd.DataFrame(StandardScaler().fit_transform(df))
        df = pd.DataFrame(pca_amplitude.transform(df.values))

        df.to_csv(path_or_buf=fr"D:\universe\python\GIt\knu\train\{name}.csv", index=False)

    for name in filenames:
        df = pd.read_csv(fr'D:\universe\python\GIt\knu\csv_files\{name}.csv')
        df = pd.DataFrame(StandardScaler().fit_transform(df))

        df.to_csv(path_or_buf=fr"D:\universe\python\GIt\knu\test\{name}.csv", index=False)
    for i, name in enumerate(test_files[:10]):
        df = pd.read_csv(fr"D:\universe\python\GIt\knu\csv_files\{name}.csv")
        df[f'{i}'].plot.line(figsize=(12, 6), subplots=True, legend=False)
        plt.show()
    for i, name in enumerate(test_files[:10]):
        df = pd.read_csv(fr"D:\universe\python\GIt\knu\csv_files\{name}.csv")
        sns.heatmap(df, xticklabels=False, yticklabels=False)
        plt.show()
    df = pd.read_csv(fr"D:\universe\python\GIt\knu\csv_files\Nothing_1.csv")
    sns.heatmap(df, xticklabels=False, yticklabels=False)
    plt.show()
main()
