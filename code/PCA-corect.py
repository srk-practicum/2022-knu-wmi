"""Apply PCA to a CSV file and plot its datapoints (one per line).
The first column should be a category (determines the color of each datapoint),
the second a label (shown alongside each datapoint)."""
import sys
import pandas
import pylab as pl
from sklearn import preprocessing
from sklearn.decomposition import PCA

