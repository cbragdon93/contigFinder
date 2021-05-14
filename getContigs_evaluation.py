from random import sample
import time
from getContigs import getContigs

'''
This script evaluates the getContigs function I wrote up
I scale up the length of the list I get contigs from.
It's assumed that the list you pass into getContigs()
is already sorted, so no such check is currently in place
for getContigs for sorted state of the list.
'''

# unit test
myList = [1,  2,  4,  6,  8,  9, 10]
print(getContigs(myList))

# generative test
N_iter = [10, 100, 1000]
contigsDict = {str(n):{} for n in N_iter}
# for reproducibility, I'd normally place a seed here.
for n in N_iter:
    thisLineup = sorted(sample(range(1,n), round(0.7*n)))
    start = time.perf_counter()
    theseContigs = getContigs(thisLineup)
    end = time.perf_counter()
    delta = end - start
    contigsDict[str(n)] = {"time":delta, "contigs":theseContigs}
    
print([[contigsDict[k]["time"], len(contigsDict[k]["contigs"])] for k in contigsDict.keys()])
