# COP4533 Programming Assignment 2
Thurstan Ngo -   
Syed Rahman - 95234900

## Running the Program
Type `python3 main.py input_file.txt` into the terminal to run the program (python3 may not be the command setup on your machine in which case you need to use what your computer has it set to)
* Replace `input_file` with one of the three input files: `File1.txt`, `File2.txt`, `File3.txt`

## Assumptions
* The name of input file is provided as command line argument when running main.py
* The input files are txt files
## Question 1: Empirical Comparison
* In all three of our cases OPTFF had the lowest number of misses. This is expectice since this way of caching uses future knowledge of request sequence to evict the data that will be used furthest into the future.

* FIFO and LRU both performed worse that OPTFF in all of our files. However, neither policy was doing better than the other consistently. In one instance they were equivalent, in another LRU was better, and in another FIFO was better.

## Question 2: Bad Sequence for LRU or FIFO
Yes there exists a squence in which OPTFF incurs strictly fewer misses than LRU
* Sequence: 1 2 3 4 1. For this sequence LRU inccurred 5 misses and OPTFF incurred only 4.
* The reasoning for this is beccause in the case of both it will miss the very first time a new request comes in however at the end 1 is requested again after the request for 4. In the case for LRU the cache state after 4 is [2, 3, 4] then 1 is requested causing a miss since it was evicted due to being the least recently used. In the case for OPTFF the cache state after 4 is [1, 2, 4] or [1, 3, 4] and when 1 is requested it is a hit since 1 was not evicted because the algorithm looked ahed into the sequence to see that 1 will be requested again thus evicting either 2 or 3 and preventing a miss.

## Question 3: Prove OPTFF is Optimal

