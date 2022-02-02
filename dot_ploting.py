import os
import pandas
import matplotlib.pyplot as plt

dir_csv = os.listdir("csv_files")
colors = ['yellow', 'blue', 'orange', 'black', 'purple', 'brown', 'green']
for ind, i in enumerate(dir_csv):
    files_list = os.listdir(f"csv_files/{i}")
    counter = 1
    for j in files_list:
        len_of_package = len(pandas.DataFrame(pandas.read_csv(f"csv_files/{i}/{j}")))
        counter += 1
        plt.scatter(len_of_package, counter, color=colors[ind])
    plt.scatter(len_of_package, counter, color=colors[ind], label=i)

plt.grid(True)
plt.gca().set(xlim=(0, 200), ylim=(0, 50),
              xlabel='Packets', ylabel='Count')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=7)


def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = 'csv_files'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig(f'plot_of_packages_and_count.png')
    os.chdir(pwd)
    plt.close()


save(name='plot_of_packages_and_count', fmt='png')
