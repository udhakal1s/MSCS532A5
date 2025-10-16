# MSCS532A5
Quicksort and Randomized Quicksort Implementation
Umesh Dhakal
MSCS532A5
This repository contains two Python files: 
A5QS.py - This is the standard Quicksort implementation with a fixed pivot in the middle
A5RQS.py - This is a Randomized Quicksort implementation where the pivot is chosen randomly
Both of our programs measure the execution time and memory usage for four different datasets. 
For the implementation, I use Visual Studio, but you can use any tool, including a terminal.
To execute- open a terminal inside the Visual Studio Code
Run regular Quicksort- python A5QS.py  
It executes regular quicksort on all the datasets and prints the time it took to execute and the memory usage for each dataset. 
Run randomized Quicksort- python A5RQS.py
It executes regular quicksort on all the datasets and prints the time it took to execute and the memory usage for each dataset. 
From the result analysis, we can say both algorithms show efficient average performance on most datasets, other than the repeated dataset, which causes the most slowdown due to poor partitioning. For real-world applications with unpredictable input data, randomized quicksort is better as it maintains consistent O (nlogn) performance and provides greater reliability and stability.
