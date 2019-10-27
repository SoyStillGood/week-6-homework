import pandas as pd
import argparse
import matplotlib.pyplot as plt
import seaborn as sns

#chose the diabetes dataset



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file", help="input data file")

    args = parser.parse_args()
    file = args.file

    diabetes = pd.read_csv(filepath_or_buffer=file, sep=' ', header=0)
    print(diabetes)

    sns.pairplot(diabetes)
    plt.show()
# at this point we have the pair of columns scattered





if __name__ == "__main__":
    main()

# this is the implementation I've made after being paired up with
# Thibault. Quite handy