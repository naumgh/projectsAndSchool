import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np


def main():
    housing = pd.read_csv("https://raw.githubusercontent.com/thomouvic/SENG474/main/data/housing.csv")
    print(housing.head())
    print(housing.info())
    print(housing["ocean_proximity"].value_counts()) # categorical attribute
    print(housing.describe()) #summary of numerical attributes

    housing.hist(bins=50, figsize=(12, 8))
    plt.show()

    train_set, test_set = shuffle_and_split_data(housing, 0.2)
    print(len(train_set), len(test_set))

def shuffle_and_split_data(data,test_ratio):
    np.random.seed(42) # so that we generate the same random numbers always
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]



if __name__ =='__main__':
    main()