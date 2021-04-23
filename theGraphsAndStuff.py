from HonorsProject import *
import matplotlib.pyplot as plt
from matplotlib import colors
import time

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

def plotAlg1Time(numberOfTimes): 
    # this is the average time it takes to get a perfect match for alg 1
    L = []
    g1 = theGame()
    for i in range(numberOfTimes):
        Start = time.time() 
        g1.algorithm1()
        End = time.time()
        L.append((Start - End))
        

    n_bins = max(L) + 1 - min(L)
    plt.figure("alg1 time")
    plt.hist(L, bins = n_bins)
    plt.title("alg 1 time taken")
    plt.xlabel("Time taken to run")
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
    
def plotAlg4Time(numberOfTimes): 
    # this is the average time it takes to get a perfect match for alg 4
    L = []
    g1 = theGame()
    for i in range(numberOfTimes):
        Start = time.time() 
        g1.algorithm4()
        End = time.time()
        L.append((Start - End))
        

    n_bins = max(L) + 1 - min(L)
    plt.figure("alg4 time")
    plt.hist(L, bins = n_bins)
    plt.title("alg 4 time taken")
    plt.xlabel("Time taken to run")
    plt.ylabel("Number of games")
    plt.show()

def plotAlg5(numberOfTimes): 
    # this is the average number of weeks it takes to get a perfect match for alg 5
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


def plotAlg5Time(numberOfTimes): 
    # this is the average time it takes to get a perfect match for alg 5
    L = []
    g1 = theGame()
    for i in range(numberOfTimes):
        Start = int(time.time())
        g1.algorithm5()
        End = int(time.time())
        L.append((Start - End))
        

    n_bins = max(L) + 1 - min(L)
    plt.figure("alg5 time")
    plt.hist(L, bins = n_bins)
    plt.title("alg 5 time taken")
    plt.xlabel("Time taken to run")
    plt.ylabel("Number of games")
    plt.show()


if __name__ == '__main__': 
    plotAlg5(1000)


