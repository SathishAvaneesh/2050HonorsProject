from HonorsProject import *
import matplotlib.pyplot as plt
from matplotlib import colors

def plotAlg1(numberOfTimes): 
    # this is the average number of weeks it takes to get a perfect match for alg 1
    L = []
    g1 = theGame()
    for i in range(numberOfTimes): 
        L.append(g1.algorithm1())

    n_bins = max(L) + 1 - min(L)
    plt.figure("alg1")
    plt.hist(L, bins = n_bins)
    plt.title("alg 1 number of weeks taken")
    plt.xlabel("Number of weeks")
    plt.ylabel("Number of games")
    plt.show()

def plotAlg4(numberOfTimes): 
    # this is the average number of weeks it takes to get a perfect match for alg 4
    L = []
    g1 = theGame()
    for i in range(numberOfTimes): 
        L.append(g1.algorithm4())

    n_bins = max(L) + 1 - min(L)
    plt.figure("alg4")
    plt.hist(L, bins = n_bins)
    plt.title("alg 4 number of weeks taken")
    plt.xlabel("Number of weeks")
    plt.ylabel("Number of games")
    plt.show()

def plotAlg5(numberOfTimes): 
    # this is the average number of weeks it takes to get a perfect match for alg 1
    L = []
    g1 = theGame()
    for i in range(numberOfTimes): 
        L.append(g1.algorithm5())

    n_bins = max(L) + 1 - min(L)
    plt.figure("alg5")
    plt.hist(L, bins = n_bins)
    plt.title("alg 5 number of weeks taken")
    plt.xlabel("Number of weeks")
    plt.ylabel("Number of games")
    plt.show()


if __name__ == '__main__': 
    plotAlg5(1000)


