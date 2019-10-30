import pandas as pd
import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#chose the diabetes dataset


def plot_data(diabetes):
    for column1 in diabetes:
        for column2 in diabetes:
            x = diabetes[column1]
            y = diabetes[column2]

            plt.scatter(x, y)
            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.title("{0} x {1}".format(column1, column2))
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file", help="input data file")

    args = parser.parse_args()
    file = args.file

    diabetes = pd.read_csv(filepath_or_buffer=file, sep=' ', header=0)
    print(diabetes)



    pairs_plot = sns.pairplot(diabetes)
    plt.show()
    #plot_data(pairs_plot)
    #this doesn't work
    #plt.show()

    #these two (above and below) do the same thing

    # g = sns.PairGrid(diabetes)
    # g.map(plt.scatter)
    # plt.show()

    # sns.regplot(x="x", y="y", data=diabetes)
    # plt.show()





    #ax = sns.regplot(diabetes, x="age", y="sex")
    # #this doesn't work
    #plt.show()



    # coefs = np.polyfit(x, y, 1)  # we also want to do this for 2, 3
    # xs, new_line = pairs_plot(coefs, min(x), max(x))
    # plt.plot(xs, new_line)

# at this point we have the pair of columns scattered





if __name__ == "__main__":
    main()

# this is the implementation I've made after being paired up with
# Thibault. Quite handy