# Umesh Dhakal 
# MSCS532A5 
# Randomized Quick Sort Implementation

import random
import time
import tracemalloc
import sys
sys.setrecursionlimit(10000)

# Function for partitioning through random pivot
def partition(arraylist, leftindex, rightindex):
    # Choosing the random pivot
    pivotpoint = random.randint(leftindex, rightindex)
    arraylist[pivotpoint], arraylist[rightindex] = arraylist[rightindex], arraylist[pivotpoint]
    pivotvalue = arraylist[rightindex]
    a = leftindex - 1
    for b in range(leftindex, rightindex):
        if arraylist[b] <= pivotvalue:
            a += 1
            arraylist[a], arraylist[b] = arraylist[b], arraylist[a]
    arraylist[a + 1], arraylist[rightindex] = arraylist[rightindex], arraylist[a + 1]
    return a + 1

# Recursive function for randomized quicksort
def quicksort(arraylist, leftindex, rightindex):
    if leftindex < rightindex:
        pivotpoint = partition(arraylist, leftindex, rightindex)
        quicksort(arraylist, leftindex, pivotpoint - 1)
        quicksort(arraylist, pivotpoint + 1, rightindex)

# Run performance test
def run(algorithm, dataset, dataset_name):
    tracemalloc.start()
    starttime = time.time()
    algorithm(dataset, 0, len(dataset) - 1)
    endtime = time.time()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    # Memory usage and time taken
    print(f"Randomized Quicksort on {dataset_name} took {endtime-starttime:.5f} seconds with {peak/1024:.2f} KB memory")

# Using different datasets like sorted, reverse data, all same repeated data, random data
test_data = 2000
datasets = {
    "Sorted Data": list(range(1, test_data + 1)),
    "Reverse Data": list(range(test_data, 0, -1)),
    "Random Data": [random.randint(1, test_data) for _ in range(test_data)],
    "Repeated Data": [5] * test_data
}

print("\nRandomized Quick Sort Performance Analysis\n")
for dataset_name, dataset in datasets.items():
    run(quicksort, dataset[:], dataset_name)
